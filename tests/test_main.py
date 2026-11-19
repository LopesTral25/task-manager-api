
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import create_table, get_connection


@pytest.fixture
def client(tmp_path, monkeypatch):
    db_path = tmp_path / "test_tasks.db"

    create_table(str(db_path))

    monkeypatch.setattr(
        "app.routes.tasks.get_connection",
        lambda: get_connection(str(db_path))
    )

    return TestClient(app)


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Bem-vindo à Task Manager API!"
    }


def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Estudar Python",
            "description": "Praticar testes com Pytest"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Estudar Python"


def test_list_tasks(client):
    client.post(
        "/tasks/",
        json={"title": "Estudar SQL", "description": ""}
    )

    response = client.get("/tasks/")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_task(client):
    created = client.post(
        "/tasks/",
        json={"title": "Estudar FastAPI", "description": ""}
    )

    task_id = created.json()["id"]
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Estudar FastAPI"


def test_update_task(client):
    created = client.post(
        "/tasks/",
        json={"title": "Título antigo", "description": ""}
    )

    task_id = created.json()["id"]

    response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Título atualizado",
            "description": "Nova descrição",
            "completed": True
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Título atualizado"
    assert response.json()["completed"] == 1


def test_delete_task(client):
    created = client.post(
        "/tasks/",
        json={"title": "Excluir tarefa", "description": ""}
    )

    task_id = created.json()["id"]
    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200

    check = client.get(f"/tasks/{task_id}")
    assert check.status_code == 404


def test_task_not_found(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
