import requests

def test_index():
    response = requests.get("http://127.0.0.1:80/")
    assert response.status_code == 200
