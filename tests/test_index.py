import requests

def test_index():
    response = requests.get("http://172.31.40.146:5000/")
    assert response.status_code == 200
