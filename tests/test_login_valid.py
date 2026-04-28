from pages.login_page import LoginPage
from utils import config

def test_valid_login(setup):
    driver = setup
    driver.get(config.BASE_URL)

    login = LoginPage(driver)
    login.login(config.VALID_USERNAME, config.VALID_PASSWORD)

    assert "inventory" in driver.current_url