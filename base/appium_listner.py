import pytest
from appium import webdriver
from utilities import read_utils


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        json_dic=read_utils.get_dic_from_json("../test_data/config.json")

        if json_dic["device"]=="local":
            des_cap = {
                "platformName": "android",
                "deviceName": "oneplus",
                "appPackage": "org.khanacademy.android",
                "appActivity": "org.khanacademy.android.ui.library.MainActivity",
                "noReset": True,
                # "appium:avd":"Pixel_4_API_33"
            }
            self.driver = webdriver.Remote(command_executor=f"http://localhost:{json_dic['port']}/wd/hub", desired_capabilities=des_cap)
        else:
            des_cap = {
                "app": "bs://aa104de2e2d069e729c3efae598d5a523082d186",
                "platformVersion": "9.0",
                "deviceName": "Google Pixel 3",
                "bstack:options": {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": "dinakaranbalaji1",
                    "accessKey": "6yXRE4nK1fyvTHWA2kPD"
                }
            }
            self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                           desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()
