import pytest
import inspect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes
from automation.config.base import APPLITOOLS_API_KEY

APP_NAME = 'automation_bookstore'
APP_UNDER_TEST = 'https://automationbookstore.dev/'

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(APP_UNDER_TEST)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def eyes():
    eyes = Eyes()
    if not APPLITOOLS_API_KEY:
        raise ValueError("Applitools API key is not set.")
    eyes.api_key = APPLITOOLS_API_KEY
    yield eyes
    try:
        eyes.close()
    finally:
        eyes.abort_if_not_closed()

def validate_window(driver, eyes, tag):
    open_eyes(driver, eyes)
    eyes.check_window(tag=tag)

def open_eyes(driver, eyes):
    eyes.open(driver, APP_NAME, test_name=get_test_name(), viewport_size={'width': 1024, 'height': 768})

def get_test_name():
    return inspect.stack()[3].function