from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.loginPage import LoginPage
from Pages.headerMenu import HeaderMenu
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.fullscreen_window()

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        header = HeaderMenu(driver)

        driver.get("http://newtours.demoaut.com/mercurysignon.php")

        login.enter_username("mercury")
        login.enter_password("mercury")

        login.click_login()
        header.click_sign_off()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/'))
