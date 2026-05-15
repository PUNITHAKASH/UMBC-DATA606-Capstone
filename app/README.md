# 🚀 app/

This folder contains the **AgroIntel Pro** Streamlit web application — the front-end interface that connects all three trained ML models into a unified real-time farming intelligence dashboard.

---

## 📁 Folder Contents

| File | Description |
|---|---|
| `agro_streamlit.py` | Main Streamlit application file |
| `crop_recommender.pkl` | Trained crop recommendation model |
| `irrigation_model.pkl` | Trained irrigation classification model |
| `iot_model.pkl` | Trained IoT valve actuation model |
| `encoders.pkl` | Fitted LabelEncoders for all categorical variables |
| `metadata.pkl` | Metadata (crop list, soil types) used to populate dropdowns |

---

## ▶️ How to Run the App

### Step 1 — Clone the Repository

```bash
git clone https://github.com/PUNITHAKASH/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Navigate to the App Folder

```bash
cd app
```

### Step 4 — Launch the App

```bash
streamlit run agro_streamlit.py
```

### Step 5 — Open in Browser
