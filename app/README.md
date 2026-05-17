# App

This folder contains the **AgroIntel Pro** Streamlit web application — the front-end interface that connects all three trained ML models into a unified real-time farming intelligence dashboard.

---

##  Folder Contents

| File | Description |
|---|---|
| `agro_streamlit.py` | Main Streamlit application file |
| `crop_recommender.pkl` | Trained crop recommendation model |
| `irrigation_model.pkl` | Trained irrigation classification model |
| `iot_model.pkl` | Trained IoT valve actuation model |
| `encoders.pkl` | Fitted LabelEncoders for all categorical variables |
| `metadata.pkl` | Metadata (crop list, soil types) used to populate dropdowns |

---

## How to Run the App

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

---

##  ML Models Used

| Model File | Algorithm | Task | Target |
|---|---|---|---|
| `crop_recommender.pkl` | Random Forest | Multi-class Classification | Crop label (22 classes) |
| `irrigation_model.pkl` | Random Forest / XGBoost | Multi-class Classification | Low / Medium / High |
| `iot_model.pkl` | Random Forest | Binary Classification | Valve ON (1) / OFF (0) |

---

##  Key App Features

| Feature | Description |
|---|---|
| **Crop Prediction** | Recommends optimal crop from 22 classes using N, P, K, pH, Temperature, Humidity, Rainfall |
| **Hydration Status** | Classifies field irrigation need with AI confidence score displayed as progress bar |
| **Frost Safety Protocol** | Locks all systems into Emergency Shutoff when Temperature ≤ 0°C |
| **IoT Node Control** | Four virtual field nodes (ALPHA, BETA, GAMMA, DELTA) activated based on sensor model inference |
| **Strategy Matrix** | Displays Season, System Architecture (Pressurized/Surface), and Delivery Method (Drip/Manual) |

---

##  Dependencies

| Library | Purpose |
|---|---|
| `streamlit` | Web application framework |
| `pandas` | Data manipulation and feature vector construction |
| `numpy` | Numerical operations and simulated IoT sensor values |
| `scikit-learn` | Loading and running all `.pkl` model files and encoders |
| `pickle` | Deserializing saved model files *(built into Python i.e no install needed)* |

---

##  Troubleshooting

| Error | Cause | Fix |
|---|---|---|
| `FileNotFoundError: crop_recommender.pkl` | Model files missing from `app/` folder | Copy all `.pkl` files into the `app/` directory |
| `KeyError` in encoder | Crop or soil type not seen during training | Use only values available in the sidebar dropdowns |
| `streamlit: command not found` | Streamlit not installed | Run `pip install streamlit` |
| Blank dashboard after Deploy | Models failed to load silently | Check terminal for errors; verify all `.pkl` files exist |

---

## Related

-  [Final Report](../docs/final_report.md)
-  [Notebooks](../notebooks/README.md)
-  [Datasets](../data/README.md)
-  [GitHub Repository](https://github.com/PUNITHAKASH/UMBC-DATA606-Capstone)
