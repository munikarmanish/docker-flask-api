import pytest

from web.app.main import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    response = client.get('/')
    assert response.data == b'hello'


def test_square(client):
    response = client.get('/square/2')
    assert response.data == b'4.0'


def test_invalid(client):
    response = client.get('/square/a')
    assert response.status_code == 500
