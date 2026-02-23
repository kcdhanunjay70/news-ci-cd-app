from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
def test_home():
    response = client.get("/")
    assert response.status_code == 200
def test_prediction():
    response = client.post("/predict", json={"text": "spam message"})
    assert response.json()["prediction"] == "Spam"