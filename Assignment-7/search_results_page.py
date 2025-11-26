from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):

    # Use a contains-based XPath to be more resilient to surrounding whitespace or extra text
    BRAND_FILTER = (By.XPATH, "//span[contains(normalize-space(.), 'Samsung')]")
    PRICE_MIN = (By.XPATH, "//input[@placeholder='Min']")
    PRICE_MAX = (By.XPATH, "//input[@placeholder='Max']")
    PRICE_OK = (By.XPATH, "//button[@type='submit']")

    # Product links now follow the /products/...-i<id>.html pattern; select anchors that point to products
    PRODUCTS = (By.CSS_SELECTOR, "a[href*='/products/']")
    FIRST_PRODUCT = (By.CSS_SELECTOR, "a[href*='/products/']")

    def apply_brand_filter(self):
        # Try primary BRAND_FILTER locator, then fall back to some common alternatives
        try:
            print("DEBUG: attempting primary BRAND_FILTER click")
            self.click(self.BRAND_FILTER)
            return 
        except Exception:
            print("DEBUG: primary BRAND_FILTER failed, trying fallbacks")
            fallbacks = [
                (By.XPATH, "(//label[contains(., 'Samsung') or contains(., 'samsung')])[1]"),
                (By.XPATH, "(//input[@type='checkbox' and (contains(@aria-label,'Samsung') or contains(@aria-label,'samsung'))])[1]"),
                (By.XPATH, "(//a[contains(., 'Samsung') or contains(., 'samsung')])[1]"),
            ]
            for fb in fallbacks:
                try:
                    self.click(fb)
                    return
                except Exception:
                    continue
            # If none of the locators worked, raise to surface the failure
            raise

    def apply_price_filter(self):
        self.type(self.PRICE_MIN, "500")
        self.type(self.PRICE_MAX, "5000")
        self.click(self.PRICE_OK)

    def count_products(self):
        return len(self.get_elements(self.PRODUCTS))

    def open_first_product(self):
        self.click(self.FIRST_PRODUCT)
 