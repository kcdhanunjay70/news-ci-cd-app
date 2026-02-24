# tests/test_app.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_spam():
    response = client.post("/predict", json={"text": "You won a free lottery"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "Spam"}

def test_predict_not_spam():
    response = client.post("/predict", json={"text": "Hello friend"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "Not Spam"}