from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BAR = (By.ID, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "search-box__button--1oH7")

    def search_item(self, item):
        self.type(self.SEARCH_BAR, item)
        self.click(self.SEARCH_BUTTON)
  