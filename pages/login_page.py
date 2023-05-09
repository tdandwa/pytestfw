"""Class contains the actions for the given page"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# locators of elements on login page
user_name_id = (By.ID, 'user-name')
password_id = (By.ID, 'password')
login_btn_id = (By.ID, 'login-button')


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def do_login(self):
        self.enter_text(user_name_id, "standard_user")
        self.enter_text(password_id, "secret_sauce")
        self.click_element(login_btn_id)

    def get_title(self):
        return self.get_title()


