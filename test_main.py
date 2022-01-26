from fastapi.testclient import TestClient

from .main import app
from .main import fizzbuzz


client = TestClient(app)


def test_respond_fizzbuzz():
    """basic test module"""
    checklist = list(range(1, 11)) + [15]
    for number in checklist:
        response = client.get("/fizzbuzz/" + str(number))
        fizzbuzz_str = fizzbuzz(number)
        assert response.status_code == 200
        content = response.json()
        assert content == {
            "number": number,
            "fizzbuzz": fizzbuzz_str,
            "placeholder_post": {
                "title": content["placeholder_post"]["title"],
                "body": content["placeholder_post"]["body"],
            },
        }
