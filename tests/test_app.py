# tests/test_app.py
from fastapi.testclient import TestClient
from app import app  # your FastAPI app file

client = TestClient(app)

def test_prediction_spam():
    # Example input that should be classified as Spam
    data = {"message": "Congratulations! You won a free lottery ticket!"}
    response = client.post("/predict", json=data)
    
    # Check status code
    assert response.status_code == 200
    
    # Check prediction output
    assert response.json()["prediction"] == "Spam"

def test_prediction_ham():
    # Example input that should be classified as Ham (non-spam)
    data = {"message": "Hey, are we meeting tomorrow for lunch?"}
    response = client.post("/predict", json=data)
    
    # Check status code
    assert response.status_code == 200
    
    # Check prediction output
    assert response.json()["prediction"] == "Ham"