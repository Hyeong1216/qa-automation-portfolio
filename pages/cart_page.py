from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("[data-test='checkout']")
        self.cart_items = page.locator(".cart_item")
        self.remove_button = page.locator("[data-test^='remove']")

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def get_item_count(self):
        return self.cart_items.count()