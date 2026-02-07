import streamlit as st
import requests

API_URL = 'https://car-price-predictor-vfgc.onrender.com'

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.write("Enter car details to estimate the selling price (in lakhs ₹)")

# --- Inputs ---
present_price = st.number_input("Present Price (₹ in lakhs)", min_value=1.0, max_value=50.0, value=5.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=300000, value=30000)
owner = st.selectbox("Owner Count", [0, 1, 2, 3])
no_year = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
seller_type = st.selectbox("Seller Type", ["Individual", "Dealer"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# --- Warnings (soft rules) ---
warnings = []

if present_price > 30:
    warnings.append("⚠️ Price is outside training range (prediction may be less accurate).")

if no_year == 0 and kms_driven > 20000:
    warnings.append("⚠️ High mileage for a new car may reduce accuracy.")

if owner > 1 and no_year < 2:
    warnings.append("⚠️ Multiple owners for a relatively new car.")

for w in warnings:
    st.warning(w)

# --- Predict button ---
if st.button("Predict Price 🚀"):
    payload = {
        "present_price": present_price,
        "kms_driven": kms_driven,
        "owner": owner,
        "no_year": no_year,
        "fuel_type": fuel_type,
        "seller_type": seller_type,
        "transmission": transmission
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            price = result["predicted_price"]

            st.success(f"💰 Estimated Selling Price: ₹ {price} lakhs")
        else:
            st.error("❌ Prediction failed. Please check inputs.")

    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running. Start FastAPI first.")