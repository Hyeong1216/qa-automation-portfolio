from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_first_item_to_cart(self):
        self.page.locator("[data-test^='add-to-cart']").first.click()

    def go_to_cart(self):
        self.cart_icon.click()