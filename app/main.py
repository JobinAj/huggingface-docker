from fastapi import FastAPI
from app.model import model

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hugging Face Model API is running"}

@app.post("/predict/")
def predict(text: str):
    prediction = model.predict(text)
    return {"prediction": prediction}
