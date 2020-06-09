from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')
    VIEW_BASKET = (By.LINK_TEXT, 'View basket')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    USER_NAME = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BTN = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_PRODUCT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) strong')
    MESSAGE_PRICE = (By.CSS_SELECTOR, '#messages .alert-info strong')


class BasketPageLocators:
    BASKET_TITLE = (By.CSS_SELECTOR, '.basket-title')
    EMPTY_BASKET = (By.LINK_TEXT, 'Continue shopping')
