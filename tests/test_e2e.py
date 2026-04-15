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

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_full_checkout_flow(page: Page):
    # 로그인
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    # 상품 추가
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    # 장바구니 이동
    inventory.go_to_cart()
    cart = CartPage(page)
    assert cart.get_item_count() == 1

    # 체크아웃 정보 입력
    cart.proceed_to_checkout()
    checkout = CheckoutPage(page)
    checkout.fill_info("Hyeong", "Suk", "98011")
    checkout.continue_checkout()

    # 주문 완료
    checkout.finish()
    assert checkout.is_complete()

def test_checkout_without_info(page: Page):
    # 로그인
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    # 상품 추가 후 체크아웃으로 이동
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    # 정보 없이 continue 클릭
    checkout = CheckoutPage(page)
    checkout.continue_checkout()
    assert checkout.error_message.is_visible()

def test_cart_item_count_after_add(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(page)
    assert cart.get_item_count() == 1