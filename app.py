from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CI/CD Render Demo")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "CI/CD Pipeline Working on Render 🚀"}

@app.post("/predict")
def predict(data: TextInput):
    if "spam" in data.text.lower():
        return {"prediction": "Spam"}
    return {"prediction": "Not Spam"}
