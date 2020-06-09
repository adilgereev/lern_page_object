from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), 'There are products in the basket'

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), 'Basket is not empty'
