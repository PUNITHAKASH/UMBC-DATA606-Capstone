import streamlit as st  # <-- This line fixes the NameError
import pandas as pd
import numpy as np
import pickle

# --- 1. ARCHITECTURAL CONFIGURATION ---
st.set_page_config(page_title="AgroIntel Pro | Enterprise Intelligence", layout="wide")

# --- 2. FINAL UX CSS (High-Contrast & Visibility Fix) ---
st.markdown("""
    <style>
    .stApp { background-color: #f1f5f9; }
    [data-testid="stSidebar"] { background-color: #0f172a; border-right: 2px solid #1e293b; }
    [data-testid="stSidebar"] * { color: #f1f5f9 !important; }
    
    /* Force Metric Labels Visibility */
    [data-testid="stMetricLabel"] div {
        color: #1e293b !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
    }
    
    /* High-Contrast Values */
    div[data-testid="stMetricValue"] > div {
        color: #0f172a !important;
        font-weight: 900 !important;
    }

    /* FIX: Force Confidence Text Visibility */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 0.9rem !important;
        opacity: 1.0 !important;
        display: block !important;
    }

    /* FIX: Force Header Visibility for Matrix */
    h1, h2, h3, h4 {
        color: #0f172a !important;
        font-weight: 800 !important;
        margin-top: 1.5rem !important;
    }

    /* Card Styling */
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        padding: 24px !important;
        border-radius: 12px !important;
    }
    
    .node-card {
        background: #ffffff;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
    }
    .node-active { border-color: #10b981; background: #ecfdf5; }
    .node-offline { border-color: #fca5a5; background: #fef2f2; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ENGINE INITIALIZATION ---
@st.cache_resource
def initialize_engine():
    try:
        crop_m = pickle.load(open('crop_recommender.pkl', 'rb'))
        irr_m = pickle.load(open('irrigation_model.pkl', 'rb'))
        iot_m = pickle.load(open('iot_model.pkl', 'rb'))
        enc = pickle.load(open('encoders.pkl', 'rb'))
        meta = pickle.load(open('metadata.pkl', 'rb'))
        return crop_m, irr_m, iot_m, enc, meta
    except:
        return None, None, None, None, None

crop_model, irr_model, iot_model, encoders, metadata = initialize_engine()

# --- 4. ADMIN CONSOLE (SIDEBAR) ---
with st.sidebar:
    st.header("Admin Console")
    st.markdown("---")
    n = st.number_input("Nitrogen (N)", value=90)
    p = st.number_input("Phosphorus (P)", value=40)
    k = st.number_input("Potassium (K)", value=40)
    temp = st.slider("Temperature (°C)", -10.0, 50.0, 31.79)
    hum = st.slider("Humidity (%)", 10.0, 100.0, 37.0)
    ph = st.number_input("Soil pH", 0.0, 14.0, 5.5)
    rain = st.number_input("Rainfall (mm)", value=35.0)
    
    st.markdown("---")
    season_choice = st.selectbox("Operating Season", ["Summer", "Winter", "Monsoon"])
    soil_type = st.selectbox("Site Geotype", metadata['soils'] if metadata else ["Clayey"])
    crop_choice = st.selectbox("Inference Mode", ["AI Prediction"] + (metadata['crops'] if metadata else []))
    
    hw_link = st.checkbox("Bridge IoT Handshake", value=False)
    deploy = st.button("Deploy Analytics", type="primary", use_container_width=True)

# --- 5. DASHBOARD ---
st.title("AgroIntel Pro | Enterprise Intelligence")
st.caption("Operational Resource Planning & Predictive Irrigation Logic")

if deploy and crop_model:
    c_feat = [[n, p, k, temp, hum, ph, rain]]
    pred_crop = crop_model.predict(c_feat)[0]
    final_crop = pred_crop if "AI" in crop_choice else crop_choice
    
    # Frost Protection & Strategy Logic
    if temp <= 0:
        it, im, status, timer, confidence = 'LOCKED', 'EMERGENCY SHUTOFF', "FROST RISK", 0, 100.0
    else:
        high_thirst = ['rice', 'papaya', 'coconut', 'jute', 'coffee']
        it = 'Pressurized' if (final_crop.lower() in high_thirst or temp > 30) else 'Surface'
        im = 'Drip' if (final_crop.lower() in high_thirst or temp > 30) else 'Manual'

        try:
            feat_vector = [[
                encoders['Soil_Type'].transform([soil_type])[0],
                encoders['Crop_Type'].transform([final_crop])[0],
                temp, hum, rain,
                encoders['Season'].transform([season_choice])[0],
                encoders['Irr_Type'].transform([it])[0],
                encoders['Irr_Method'].transform([im])[0]
            ]]
            irr_idx = irr_model.predict(feat_vector)[0]
            status = encoders['Irrigation_Need'].inverse_transform([irr_idx])[0]
            
            probs = irr_model.predict_proba(feat_vector)[0]
            confidence = max(probs) * 100
            timer = 45 if status == "High" else (25 if status == "Medium" else 10)
        except:
            status, timer, confidence = "MODERATE", 20, 0.0

    # Display Metrics
    st.markdown("---")
    k1, k2, k3 = st.columns(3)
    k1.metric("Predicted Crop", final_crop.capitalize())
    with k2:
        st.metric("Hydration Status", status)
        st.progress(confidence / 100)
        # Force the text below the bar to be visible
        st.markdown(f"<p style='color:#0f172a; font-weight:800; font-size:0.9rem;'>AI Confidence: {confidence:.1f}%</p>", unsafe_allow_html=True)
    k3.metric("System Timer", f"{timer} Mins")

    st.markdown("### Operational Strategy Matrix")
    c1, c2, c3 = st.columns(3)
    def info_box(title, val):
        return f'<div style="background:white; padding:20px; border-radius:12px; border-left:6px solid #3b82f6; box-shadow: 0 2px 4px rgba(0,0,0,0.05);"><small style="color:#64748b; font-weight:800; text-transform:uppercase;">{title}</small><br><b style="font-size:1.1rem; color:#1e293b;">{val}</b></div>'
    c1.markdown(info_box("Cycle Season", season_choice), unsafe_allow_html=True)
    c2.markdown(info_box("System Architecture", it), unsafe_allow_html=True)
    c3.markdown(info_box("Delivery Method", im), unsafe_allow_html=True)

    st.markdown("### IoT Actuation Array")
    if hw_link:
        if temp <= 0:
            st.warning("Hardware Locked: Frost Protection Protocol Active.")
            valves = [0, 0, 0, 0]
        else:
            st.success("Hardware Bridge Active.")
            valves = iot_model.predict([[np.random.uniform(2, 18) for _ in range(20)]])[0]
    else:
        st.error("Hardware Bridge Offline: Handshake Required.")
        valves = [0, 0, 0, 0]

    n_cols = st.columns(4)
    nodes = ["ALPHA", "BETA", "GAMMA", "DELTA"]
    for i, name in enumerate(nodes):
        if not hw_link:
            stat, cls, col = "OFFLINE", "node-offline", "#ef4444"
        else:
            is_act = (valves[i] == 1 and temp > 0)
            stat, cls, col = ("ACTIVE", "node-active", "#10b981") if is_act else ("STDBY", "", "#94a3b8")
        n_cols[i].markdown(f'<div class="node-card {cls}"><small style="color:#64748b; font-weight:800;">NODE {name}</small><br><span style="color:{col}; font-weight:800;">{stat}</span></div>', unsafe_allow_html=True)
else:
    st.info("Awaiting telemetry input from the Admin Console.")
