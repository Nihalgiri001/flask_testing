from app import app 

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

def test_health_check():
    response = app.test_client().get('/health')
    assert response.status_code == 200