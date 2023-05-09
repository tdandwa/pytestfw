import pytest
from tests.basetest import BaseTest


class TestLoginPage(BaseTest):

    def test_login_page_title_(self):
        assert self.get_title == "Swag Labs"

    def test_login_functionality(self):
        self.login_page.do_login()




