from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    payload1 = {
        "sepal_length": 2.2,
        "sepal_width": 4.2,
        "petal_length": 0.2,
        "petal_width": 1.4,
    }
    payload2 = {
        "sepal_length": 0.2,
        "sepal_width": 0.9,
        "petal_length": 1.2,
        "petal_width": 0.4,
    }

    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload2)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}
