# app.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

def is_spam(text: str) -> bool:
    spam_keywords = ["free", "win", "lottery", "congratulations"]
    return any(word.lower() in text.lower() for word in spam_keywords)

@app.post("/predict")
def predict(message: Message):
    if is_spam(message.text):
        return {"prediction": "Spam"}
    else:
        return {"prediction": "Not Spam"}