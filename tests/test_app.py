# tests/test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_prediction_spam():
    data = {"text": "Congratulations! You won a free lottery ticket!"}
    response = client.post("/predict", json=data)
    
    assert response.status_code == 200
    assert response.json()["prediction"] == "Spam"

def test_prediction_ham():
    data = {"text": "Hey, are we meeting tomorrow for lunch?"}
    response = client.post("/predict", json=data)
    
    assert response.status_code == 200
    assert response.json()["prediction"] == "Not Spam"