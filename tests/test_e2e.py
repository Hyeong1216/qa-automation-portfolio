import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_login_success(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_login_wrong_password(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "wrong_password")
    assert login.error_message.is_visible()

def test_login_empty_fields(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("", "")
    assert login.error_message.is_visible()

from pages.inventory_page import InventoryPage

def test_add_to_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    assert inventory.cart_badge.text_content() == "1"

def test_go_to_cart(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()
    assert page.url == "https://www.saucedemo.com/cart.html"