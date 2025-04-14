from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_known_route():
    response = client.get("/search", params={"from_city": "New York", "to_city": "Washington DC"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    assert data[0]["name"] == "Knight-Swift Transport Services"

def test_search_unknown_route_returns_default():
    response = client.get("/search", params={"from_city": "Boston", "to_city": "Miami"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "UPS Inc."
