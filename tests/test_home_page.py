from tests.basetest import BaseTest


class TestHomePage(BaseTest):

    def test_login(self):

    def test_home_page_title(self):
        assert self.get_home_page_title == 'Swag Labs'
