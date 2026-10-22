from fastapi.testclient import TestClient

from kyc_api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_check_returns_synthetic_review_status() -> None:
    response = client.post(
        "/v1/kyc/check",
        json={"application_id": "DEMO-001", "country_code": "IN"},
    )
    assert response.status_code == 200
    assert response.json()["status"] == "review_required"
    assert "no identity verification" in response.json()["message"]


def test_check_rejects_invalid_application_id() -> None:
    response = client.post(
        "/v1/kyc/check",
        json={"application_id": "real customer name", "country_code": "IN"},
    )
    assert response.status_code == 422
