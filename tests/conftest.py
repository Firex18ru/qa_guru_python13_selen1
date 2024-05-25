import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_managment():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    # browser.config.timeout = 15
    yield

    browser.quit()
