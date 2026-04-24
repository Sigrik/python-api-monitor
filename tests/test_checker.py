from app.checker import check_url

def test_check_url():
    result = check_url("https://google.com")
    assert "status" in result or "error" in result