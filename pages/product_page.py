from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_be_product_added_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT).text
        assert product_name == message_product, 'Product name does not match the name in basket'

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        assert product_price == message_price, 'Product price does not match the price in basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT), \
            "Success message is not disappeared"
