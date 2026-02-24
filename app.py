# app.py
from fastapi import FastAPI
from pydantic import BaseModel

# ✅ FastAPI app instance
app = FastAPI()

# ✅ Data model for POST requests
class Message(BaseModel):
    text: str

# ✅ Simple spam detection logic
def is_spam(text: str) -> bool:
    spam_keywords = ["free", "win", "lottery", "congratulations"]
    return any(word.lower() in text.lower() for word in spam_keywords)

# ✅ POST route for /predict
@app.post("/predict")
def predict(message: Message):
    if is_spam(message.text):
        return {"prediction": "Spam"}
    else:
        return {"prediction": "Not Spam"}

# ✅ GET route for root ("/") to test in browser or CI logs
# app.py
@app.get("/")
def read_root():
    return "CI/CD Pipeline Working on Render 🚀"

# ✅ Optional: print for CI console + local run
if __name__ == "__main__":
    print("Hello K.C.Dhanunjay Infosys")
    import uvicorn
    # Run FastAPI server locally
    uvicorn.run(app, host="0.0.0.0", port=8000)