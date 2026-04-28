from pages.login_page import LoginPage
from utils import config

def test_invalid_login(setup):
    driver = setup
    driver.get(config.BASE_URL)

    login = LoginPage(driver)
    login.login(config.INVALID_USERNAME, config.INVALID_PASSWORD)

    error = login.get_error()
    assert "Epic sadface" in error