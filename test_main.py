from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task():
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 201
    assert response.json() == {"title": "Write tests", "done": False}


def test_get_tasks_grows():
    response = client.post("/tasks", json={"title": "Buy groceries"})
    assert response.status_code == 201

    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert {"title": "Buy groceries", "done": False} in tasks


def test_create_task_empty_title_fails():
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Title cannot be empty"
