"""This class contains methods to be inherited in other pages of this application"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, locator, text):
        self.driver.WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, locator):
        self.driver.WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def get_title(self):
        return self.driver.title()


