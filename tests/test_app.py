import json
import pytest
from app import app, APP_VERSION


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestHomeRoute:
    def test_status_code(self, client):
        assert client.get("/").status_code == 200

    def test_content(self, client):
        assert b"DevOps Portfolio Launchpad" in client.get("/").data


class TestHealthRoute:
    def test_status_code(self, client):
        assert client.get("/health").status_code == 200

    def test_returns_json(self, client):
        response = client.get("/health")
        assert response.content_type == "application/json"

    def test_payload(self, client):
        data = json.loads(client.get("/health").data)
        assert data["status"] == "healthy"
        assert data["service"] == "devops-launchpad"


class TestInfoRoute:
    def test_status_code(self, client):
        assert client.get("/info").status_code == 200

    def test_returns_json(self, client):
        response = client.get("/info")
        assert response.content_type == "application/json"

    def test_version(self, client):
        data = json.loads(client.get("/info").data)
        assert data["version"] == APP_VERSION

    def test_environment_key_present(self, client):
        data = json.loads(client.get("/info").data)
        assert "environment" in data

    def test_python_path_key_present(self, client):
        data = json.loads(client.get("/info").data)
        assert "python_path" in data


class TestNotFound:
    def test_unknown_route_returns_404(self, client):
        assert client.get("/does-not-exist").status_code == 404
