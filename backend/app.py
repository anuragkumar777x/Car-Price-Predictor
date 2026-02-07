from fastapi import FastAPI
import pickle
import pandas as pd
from backend.pydantic_ import CarInput

app = FastAPI()

# Load model once
with open("backend/random_forest_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

FEATURE_ORDER = [
    "Present_Price",
    "Kms_Driven",
    "Owner",
    "no_year",
    "Fuel_Type_Diesel",
    "Fuel_Type_Petrol",
    "Seller_Type_Individual",
    "Transmission_Manual"
]
@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict_price(data: CarInput):

    input_data = {
        "Present_Price": data.present_price,
        "Kms_Driven": data.kms_driven,
        "Owner": data.owner,
        "no_year": data.no_year,
        "Fuel_Type_Diesel": 0,
        "Fuel_Type_Petrol": 0,
        "Seller_Type_Individual": 0,
        "Transmission_Manual": 0
    }

    # Fuel type encoding
    if data.fuel_type.lower() == "diesel":
        input_data["Fuel_Type_Diesel"] = 1
    elif data.fuel_type.lower() == "petrol":
        input_data["Fuel_Type_Petrol"] = 1

    # Seller type encoding
    if data.seller_type.lower() == "individual":
        input_data["Seller_Type_Individual"] = 1

    # Transmission encoding
    if data.transmission.lower() == "manual":
        input_data["Transmission_Manual"] = 1

    # Enforce feature order
    df = pd.DataFrame([[input_data[col] for col in FEATURE_ORDER]],
                      columns=FEATURE_ORDER)

    prediction = model.predict(df)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }