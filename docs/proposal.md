# AgroIntel: A Multi-Model AI Framework for Optimized Crop Selection and Precision Irrigation

**Author:** Punith Akash Balachandran  
**Project Title:** AgroIntel: A Multi-Model AI Framework for Optimized Crop Selection and Precision Irrigation  
**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  

---

## 🔗 Project Links
* **GitHub Repository:** [https://github.com/PUNITHAKASH/UMBC-DATA606-Capstone]
* **LinkedIn Profile:** [Punith Akash Balachandran](https://www.linkedin.com/in/punith-akash-a145a024a/)
* **PowerPoint Presentation:** *To be added*
* **YouTube Video:** *To be added*

---

## 📖 Background

### What is it about?
AgroIntel is an **Intelligent Agricultural Decision Support System** designed to bridge the gap between raw environmental data and actionable farming insights. The framework operates across three distinct layers:

* **Strategic (Crop Selection):** Matches soil nutrients (N-P-K) to the best-suited crop types to maximize yield.
* **Tactical (Irrigation Forecasting):** Utilizes weather data (temperature/humidity) to predict and schedule precise water requirements.
* **Operational (IoT Automation):** Connects simulated hardware and sensors to automate field actions in real-time.

### Why does it matter?
Modern agriculture faces the dual challenge of rising food demand and dwindling water resources. This project advocates for **Precision Agriculture** to address:

* **Global Food Security:** Meeting demand despite resource scarcity.
* **Data-Driven Accuracy:** Replacing anecdotal evidence and manual scheduling with real-time analytics.
* **Waste Reduction:** Eliminating over-irrigation to lower the environmental footprint.
* **Economic Efficiency:** Maximizing yields while reducing the cost of operations.

### Research Questions
1.  Can ensemble learning models accurately forecast field irrigation requirements based on real-time environmental conditions?
2.  To what extent can soil pH and climatic conditions be used to prescribe biologically adapted crops for specific land parcels?
3.  How can multiple machine learning models be integrated into a single, user-friendly application for end-to-end farming advice?

---

## 📊 Data Sources

### 1. Agricultural Planning & Prediction
* **File:** `irrigation_prediction.csv`
* **Role:** Primary driver for Tactical Irrigation and Regional Crop Selection.
* **Size/Shape:** 1.17 MB | 10,000 rows × 20 columns.
* **Target:** `Irrigation_Need` (Low, Medium, High).
* **Key Features:** Soil_Type, Soil_pH, Temperature_C, Humidity, Rainfall_mm, Crop_Type, Season.

### 2. Soil Nutrient Analysis
* **File:** `Crop_recommendation.csv`
* **Role:** Specialized for high-precision Nutrient-Based Crop Recommendation.
* **Size/Shape:** 146.5 KB | 2,200 rows × 8 columns.
* **Target:** `label` (Recommended crop name).
* **Key Features:** N (Nitrogen), P (Phosphorus), K (Potassium), pH, Rainfall.

### 3. IoT Sensor Network
* **File:** `irrigation_machine.csv`
* **Role:** Hardware Simulation layer monitoring real-time moisture across land parcels.
* **Size/Shape:** 177 KB | 2,000 rows × 24 columns.
* **Target:** `parcel_0`, `parcel_1`, `parcel_2` (Binary activation status).
* **Key Features:** Sensor_0 through Sensor_19.

### 4. Expert-Knowledge Augmented Dataset (Booster Set)
* **File:** Synthetic (Generated in-memory).
* **Role:** Resolves low-correlation issues by teaching the AI "Ground Truths" (e.g., Rice requires high rainfall).
* **Size/Shape:** ~150 KB | 1,000 rows × 20 columns.
* **Target:** `Crop_Type`.
* **Key Features:** Soil_pH, Rainfall_mm, Temperature_C, Season.
