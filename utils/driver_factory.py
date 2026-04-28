import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()

    # CI mode (GitHub Actions)
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(options=options)