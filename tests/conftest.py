import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_managment():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 768
    browser.config.window_width = 1024
    browser.config.timeout = 5
    yield

    browser.quit()
