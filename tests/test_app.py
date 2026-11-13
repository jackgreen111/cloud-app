from app import app, TITLE


def test_addition():
    assert 2 + 2 == 4


def test_index_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert TITLE in response.get_data(as_text=True)


def test_api_status():
    response = app.test_client().get("/api/status")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "ok"
    assert data["title"] == TITLE


def test_health():
    response = app.test_client().get("/health")
    assert response.get_json() == {"status": "ok"}
