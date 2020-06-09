from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(f'{email}')
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(f'{password}')
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD).send_keys(f'{password}')
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'The browser is not located on the login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USER_NAME), 'Email address for login is not present'
        assert self.is_element_present(*LoginPageLocators.PASSWORD), 'Password for login is not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), 'Email address for registration' \
                                                                               ' is not present'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Password for registration' \
                                                                                  ' is not present'
        assert self.is_element_present(*LoginPageLocators.REPEAT_PASSWORD), 'Repeat password for registration' \
                                                                            ' is not present'
