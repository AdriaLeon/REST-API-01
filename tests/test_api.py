from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_app_starts():
    response = client.get("/docs")
    assert response.status_code == 200

def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Task API"
    }

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok"
    }

def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn CI",
            "description": "Write GitHub Actions"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Learn CI"
    assert data["description"] == "Write GitHub Actions"
    assert data["completed"] is False

def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task():
    created = client.post(
        "/tasks",
        json={
            "title": "Task",
            "description": "Description"
        }
    ).json()

    response = client.get(f"/tasks/{created['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "Task"

def test_update_task():
    created = client.post(
        "/tasks",
        json={
            "title": "Old",
            "description": "Old description"
        }
    ).json()

    response = client.put(
        f"/tasks/{created['id']}",
        json={
            "title": "New",
            "description": "New description",
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "New"
    assert data["completed"] is True

def test_delete_task():
    created = client.post(
        "/tasks",
        json={
            "title": "Delete me",
            "description": "..."
        }
    ).json()

    response = client.delete(f"/tasks/{created['id']}")

    assert response.status_code == 204

def test_get_unknown_task():
    response = client.get("/tasks/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"