import requests

def test_index():
    response = requests.get("http://13.229.200.22:5000/")
    assert response.status_code == 200
