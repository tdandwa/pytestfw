import pytest


@pytest.mark.usefixtures("create_driver")
class BaseTest:
    pass
