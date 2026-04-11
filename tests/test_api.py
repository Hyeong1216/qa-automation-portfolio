import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="module")
def post_response():
    return requests.get(f"{BASE_URL}/posts/1")

def test_get_post_status_code(post_response):
    assert post_response.status_code == 200

def test_get_post_has_correct_id(post_response):
    data = post_response.json()
    assert data["id"] == 1

def test_get_post_has_required_fields(post_response):
    data = post_response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
#----------------------
def test_create_post():
    new_post = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "test title"
    assert "id" in data

def test_update_post():
    updated_post = {
        "title": "updated title",
        "body": "updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updated title"

def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

#------------------------------------------------------------------------------------------------------------------------------------
def test_create_post_missing_title():
    # title 없이 보내면?
    incomplete_post = {
        "body": "test body",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=incomplete_post)
    # jsonplaceholder는 관대하게 201 반환하지만
    # 실무 API였으면 400이어야 함 — 여기선 구조 확인
    assert response.status_code == 201

def test_create_post_empty_body():
    # 아무것도 안 보내면?
    response = requests.post(f"{BASE_URL}/posts", json={})
    assert response.status_code == 201

def test_get_post_invalid_id_string():
    # 숫자 대신 문자열 id로 요청하면?
    response = requests.get(f"{BASE_URL}/posts/abc")
    assert response.status_code == 404

def test_get_posts_returns_list():
    # 전체 목록 조회 — 리스트인지, 비어있지 않은지
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_posts_list_item_has_required_fields():
    # 목록의 각 아이템이 올바른 구조인지
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    first_item = data[0]
    assert "id" in first_item
    assert "title" in first_item
    assert "userId" in first_item
