import joblib
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from schema import Passenger


app = FastAPI(
    title="Titanic Survival Prediction API",
    description="Predicts passenger survival from a preprocessing + logistic regression pipeline",
    version="1.0.0"
)

model = joblib.load("model/titanic_pipeline.joblib") #load the whole pipeline

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/health")
def health():
    return {"status":"okk"}

@app.post("/predict")
def  predict(passenger:Passenger):
    data = pd.DataFrame([passenger.model_dump()])
    prediction = int(model.predict(data)[0])
    confidence = float(model.predict_proba(data)[0][prediction])
    label = "Survived" if prediction == 1 else "Did not survive"
    return{"prediction": prediction,"label":label,"confidence":round(confidence,3)}