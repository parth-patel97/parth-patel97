from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_openai_request():
    response = client.post("/openai_request",
                           params={"query":'thai restaurant in California'},)
    assert response.status_code == 200
    