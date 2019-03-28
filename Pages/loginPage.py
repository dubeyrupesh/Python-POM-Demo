class LoginPage:

    def __init__(self, driver):
        self.__driver = driver

        # Locators - Private members
        self.__userName_textbox_name = "userName"
        self.__password_textbox_name = "password"
        self.__login_button_name = "login"

    def enter_username(self, username):
        self.__driver.find_element_by_name(self.__userName_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element_by_name(self.__password_textbox_name).send_keys(password)

    def click_login(self):
        self.__driver.find_element_by_name(self.__login_button_name).click()

