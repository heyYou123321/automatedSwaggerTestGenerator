# tests/conftest.py
import pytest

@pytest.fixture
def get_data():
    return {
        "id": 1,
        "userId": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }

@pytest.fixture
def get_data_status_code():
    return {
         "expected_status_code": 200
    }

@pytest.fixture
def get_all_data():
    return {
        "expected_response": {
            "id": 1,
            "userId": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        "expected_status_code": 200    
    }

@pytest.fixture
def post_data():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

@pytest.fixture
def post_data_status_code():
    return {
         "expected_status_code": 201
    }