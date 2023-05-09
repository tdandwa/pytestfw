import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage


# def pytest_adaption(parser):
#     parser.addoption("--browser", action='store', default='chrome')


@pytest.fixture
def create_driver(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    request.cls.login_page = LoginPage(driver)
    request.cls.home_page = HomePage(driver)
    request.cls.driver = driver
    yield driver
    # driver.find_element().send_keys()


