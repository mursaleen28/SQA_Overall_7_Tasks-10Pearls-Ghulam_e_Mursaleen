from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    FREE_SHIPPING = (By.XPATH, "//div[contains(text(),'Free Shipping')]")

    def is_free_shipping_available(self):
        try:
            self.get_element(self.FREE_SHIPPING)
            return True
        except:
            return False
 