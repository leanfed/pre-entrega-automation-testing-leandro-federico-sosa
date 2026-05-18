"""Funciones auxiliares para interactuar con saucedemo.com.

Este archivo concentra acciones reutilizables: abrir la página,
hacer login, leer productos y operar el carrito.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config import BASE_URL, DEFAULT_WAIT_TIME, VALID_PASSWORD, VALID_USERNAME


# Localizadores de Login
USERNAME_INPUT = (By.ID, "user-name")
PASSWORD_INPUT = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

# Localizadores de Inventario/Catálogo
APP_LOGO = (By.CLASS_NAME, "app_logo")
PAGE_TITLE = (By.CLASS_NAME, "title")
INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
MENU_BUTTON = (By.ID, "react-burger-menu-btn")
SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

# Localizadores de Carrito
CART_ITEM = (By.CLASS_NAME, "cart_item")
CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


def wait_until_visible(driver: WebDriver, locator: tuple, timeout: int = DEFAULT_WAIT_TIME):
    """Espera explícitamente hasta que un elemento sea visible."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))


def wait_until_clickable(driver: WebDriver, locator: tuple, timeout: int = DEFAULT_WAIT_TIME):
    """Espera explícitamente hasta que un elemento sea clickeable."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def open_login_page(driver: WebDriver) -> None:
    """Navega a la pantalla de login de SauceDemo."""
    driver.get(BASE_URL)
    wait_until_visible(driver, USERNAME_INPUT)


def login_with_valid_user(driver: WebDriver) -> None:
    """Realiza login con credenciales válidas y espera la redirección al inventario."""
    open_login_page(driver)

    wait_until_visible(driver, USERNAME_INPUT).send_keys(VALID_USERNAME)
    wait_until_visible(driver, PASSWORD_INPUT).send_keys(VALID_PASSWORD)
    wait_until_clickable(driver, LOGIN_BUTTON).click()

    WebDriverWait(driver, DEFAULT_WAIT_TIME).until(EC.url_contains("/inventory.html"))
    wait_until_visible(driver, PAGE_TITLE)


def get_page_title_text(driver: WebDriver) -> str:
    """Devuelve el título visible de la página actual."""
    return wait_until_visible(driver, PAGE_TITLE).text


def get_app_logo_text(driver: WebDriver) -> str:
    """Devuelve el texto del logo superior de la aplicación."""
    return wait_until_visible(driver, APP_LOGO).text


def get_inventory_products(driver: WebDriver):
    """Devuelve todos los productos visibles del inventario."""
    WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
        EC.presence_of_all_elements_located(INVENTORY_ITEM)
    )
    return driver.find_elements(*INVENTORY_ITEM)


def get_first_product_name_and_price(driver: WebDriver) -> tuple[str, str]:
    """Obtiene nombre y precio del primer producto visible."""
    products = get_inventory_products(driver)
    first_product = products[0]

    product_name = first_product.find_element(*INVENTORY_ITEM_NAME).text
    product_price = first_product.find_element(*INVENTORY_ITEM_PRICE).text

    return product_name, product_price


def is_main_menu_visible(driver: WebDriver) -> bool:
    """Verifica si el botón de menú principal está presente y visible."""
    return wait_until_visible(driver, MENU_BUTTON).is_displayed()


def is_sort_filter_visible(driver: WebDriver) -> bool:
    """Verifica si el filtro de ordenamiento del catálogo está presente y visible."""
    return wait_until_visible(driver, SORT_SELECT).is_displayed()


def add_first_product_to_cart(driver: WebDriver) -> str:
    """Agrega el primer producto del inventario al carrito.

    Returns:
        Nombre del producto agregado, para validarlo luego en el carrito.
    """
    product_name, _ = get_first_product_name_and_price(driver)
    add_buttons = driver.find_elements(*ADD_TO_CART_BUTTONS)
    add_buttons[0].click()
    return product_name


def get_cart_badge_text(driver: WebDriver) -> str:
    """Devuelve el contador visible del carrito."""
    return wait_until_visible(driver, CART_BADGE).text


def open_cart(driver: WebDriver) -> None:
    """Navega al carrito de compras."""
    wait_until_clickable(driver, CART_LINK).click()
    WebDriverWait(driver, DEFAULT_WAIT_TIME).until(EC.url_contains("/cart.html"))


def get_cart_product_names(driver: WebDriver) -> list[str]:
    """Obtiene los nombres de los productos presentes en el carrito."""
    WebDriverWait(driver, DEFAULT_WAIT_TIME).until(
        EC.presence_of_all_elements_located(CART_ITEM)
    )
    cart_items = driver.find_elements(*CART_ITEM)
    return [item.find_element(*CART_ITEM_NAME).text for item in cart_items]
