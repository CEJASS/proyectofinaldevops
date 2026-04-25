import pytest
from app import app


@pytest.fixture
def client():
      app.config["TESTING"] = True
      with app.test_client() as client:
                yield client


def test_hola_mundo_status_code(client):
      response = client.get("/")
      assert response.status_code == 200


def test_hola_mundo_contenido(client):
      response = client.get("/")
      assert "Hola Mundo" in response.data.decode("utf-8")


def test_health_check_status(client):
      response = client.get("/health")
      assert response.status_code == 200


def test_health_check_json(client):
      response = client.get("/health")
      data = response.get_json()
      assert data["status"] == "ok"
