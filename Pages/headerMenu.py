class HeaderMenu:

    def __init__(self, driver):
        self.driver = driver
        self.__sign_off_link_text = "SIGN-OFF"

    def click_sign_off(self):
        self.driver.find_element_by_link_text(self.__sign_off_link_text).click()

