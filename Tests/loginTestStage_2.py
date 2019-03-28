from selenium import webdriver
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.fullscreen_window()

    def test_login(self):
        self.driver.get("http://newtours.demoaut.com/mercurysignon.php")
        self.driver.find_element_by_name("userName").send_keys("mercury")
        self.driver.find_element_by_name("password").send_keys("mercury")
        self.driver.find_element_by_name("login").click()
        self.driver.find_element_by_link_text("SIGN-OFF").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
