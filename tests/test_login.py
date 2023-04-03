import time

from base.appium_listner import AppiumConfig


class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        print(self.driver.page_source)
        time.sleep(2)

    def test_valid_login(self):
        print(self.driver.page_source)
        time.sleep(2)

    