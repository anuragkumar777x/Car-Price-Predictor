# 🚗 Car Price Prediction System

## 📌 Overview
This project predicts the **selling price of a used car** based on important features such as present price, kilometers driven, fuel type, ownership history, and car age.  
It is an **end-to-end Machine Learning project** with a **FastAPI backend** and a **Streamlit frontend**.

---

## 🎯 Problem Statement
Estimating the resale value of a used car is difficult due to multiple influencing factors and non-linear relationships.  
This project aims to:
- Predict used car prices accurately
- Handle invalid and unrealistic inputs safely
- Provide a clean and interactive UI
- Demonstrate full ML deployment workflow

---

## 🧠 Solution Approach
1. Performed Exploratory Data Analysis (EDA)
2. Engineered features such as car age and encoded categorical variables
3. Trained a **Random Forest Regressor**
4. Built a **FastAPI backend** for inference
5. Built a **Streamlit frontend** with soft warnings

---

## 📊 Exploratory Data Analysis (EDA)
Key insights:
- `Present_Price` has the strongest impact on selling price
- More owners lead to lower resale value
- Fuel type, seller type, and transmission affect pricing
- Data shows non-linear relationships → Random Forest chosen

---

## 🧪 Model Details
- **Algorithm:** Random Forest Regressor
- **Why Random Forest?**
  - Handles non-linearity well
  - Robust to outliers
  - No feature scaling required

---

## 🧩 Input Features

| Feature | Description |
|------|------------|
| Present_Price | Current showroom price (₹ in lakhs) |
| Kms_Driven | Total kilometers driven |
| Owner | Number of previous owners |
| no_year | Age of the car (years) |
| Fuel_Type | Petrol / Diesel |
| Seller_Type | Individual / Dealer |
| Transmission | Manual / Automatic |

---

## ⚙️ Backend (FastAPI)
- Loads ML model once at startup
- Uses **Pydantic** for validation
- Handles:
  - Range validation
  - Logical consistency checks
  - Case-insensitive categorical inputs
- Exposes a `/predict` endpoint

### Sample API Request
```json
{
  "present_price": 10,
  "kms_driven": 50000,
  "owner": 1,
  "no_year": 5,
  "fuel_type": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual"
}
```

### Sample API Response
```json
{
  "predicted_price": 4.25
}
```

---

## 🎨 Frontend (Streamlit)
- Clean and interactive UI
- Soft warnings for unrealistic inputs
- Dropdowns and sliders for easy input
- Displays predicted price in ₹ lakhs

---

## ⚠️ Input Validation Strategy
- **Backend:** Hard validation (impossible inputs rejected)
- **Frontend:** Soft warnings (prediction allowed with caution)

---

## 🚫 Model Limitations
- Trained on limited historical data
- Cannot extrapolate for very high-priced cars (e.g., ₹1 crore)
- Predictions are approximate and market-dependent

---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Streamlit
- Requests

---

## ▶️ How to Run the Project

### 1️⃣ Start Backend
```bash
uvicorn backend.app:app --reload
```

### 2️⃣ Start Frontend
```bash
streamlit run frontend/streamlit.py
```

---

## 📌 Future Improvements
- Add prediction confidence score
- Add feature importance visualization
- Deploy backend and frontend
- Support more car categories

---

## 🧑‍💻 Author
**Anurag**  
B.Tech (Cyber Security)  
Machine Learning & Backend Development

---

## 💡 Note
This project is intended for **learning, demonstration, and interview purposes**.
