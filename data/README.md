# 📊 data/

This folder contains all raw datasets used in the **AgroIntel** capstone project.

---

## 📁 Dataset Overview

| File | Layer | Rows | Columns | Size |
|---|---|---|---|---|
| `Crop_recommendation.csv` | Strategic | 2,200 | 8 | ~146 KB |
| `irrigation_prediction.csv` | Tactical | 10,000 | 19 | ~1.17 MB |
| `irrigation_machine.csv` | Operational | 2,000 | 23 | ~177 KB |

---

## 🌾 1. Crop_recommendation.csv

**Purpose:** Trains the crop recommendation model.
**Each row:** One soil sample observation.

| Column | Type | Definition | Range |
|---|---|---|---|
| `N` | Numerical | Nitrogen content (kg/ha) | 0 – 140 |
| `P` | Numerical | Phosphorus content (kg/ha) | 5 – 145 |
| `K` | Numerical | Potassium content (kg/ha) | 5 – 205 |
| `temperature` | Numerical | Ambient temperature (°C) | 8 – 44 |
| `humidity` | Numerical | Relative humidity (%) | 14 – 100 |
| `ph` | Numerical | Soil pH level | 3.5 – 9.9 |
| `rainfall` | Numerical | Annual rainfall (mm) | 20 – 298 |
| `label` | Categorical | **Target** — recommended crop | 22 crop classes |

---

## 💧 2. irrigation_prediction.csv

**Purpose:** Trains the irrigation need classifier.
**Each row:** One field irrigation decision snapshot.

| Column | Type | Definition | Values |
|---|---|---|---|
| `Soil_Type` | Categorical | Geotype of the field | Clayey, Sandy, Loamy, Alluvial, etc. |
| `Crop_Type` | Categorical | Crop being grown | rice, wheat, maize, etc. |
| `Temperature` | Numerical | Ambient temperature (°C) | -10 – 50 |
| `Humidity` | Numerical | Relative humidity (%) | 10 – 100 |
| `Rainfall` | Numerical | Rainfall received (mm) | 0 – 300 |
| `Season` | Categorical | Agricultural season | Summer, Winter, Monsoon |
| `Irr_Type` | Categorical | Irrigation system type | Pressurized, Surface |
| `Irr_Method` | Categorical | Delivery method | Drip, Manual |
| `Irrigation_Need` | Categorical | **Target** — irrigation level | Low, Medium, High |

---

## 🤖 3. irrigation_machine.csv

**Purpose:** Trains the IoT valve actuation model.
**Each row:** One IoT sensor grid reading from a field node.

| Column | Type | Definition | Range |
|---|---|---|---|
| `sensor_1` … `sensor_20` | Numerical | Raw IoT sensor readings | 2 – 18 |
| `valve_state` | Binary | **Target** — valve decision | 0 = OFF, 1 = ON |

---

## ⚠️ Notes

- All datasets are used read-only — no raw files are modified.
- Categorical columns are label-encoded at training time; encoders saved to `encoders.pkl`.
- IoT sensor data is simulated in the web app via `numpy.random.uniform()`.

---

## 🔗 Sources

| Dataset | Link |
|---|---|
| Crop Recommendation | [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) |
| Irrigation Prediction | Kaggle *(add exact link)* |
| IoT Sensor Data | Kaggle *(add exact link)* |

---

## 🔗 Related

- 📘 [Final Report](../docs/final_report.md)
- 📓 [Notebooks](../notebooks/README.md)
- 🐙 [GitHub Repository](https://github.com/PUNITHAKASH/UMBC-DATA606-Capstone)
