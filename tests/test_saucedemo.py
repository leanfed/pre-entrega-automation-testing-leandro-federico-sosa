"""Tests automatizados para la pre-entrega de SauceDemo."""

import pytest

from utils.saucedemo_actions import (
    add_first_product_to_cart,
    get_app_logo_text,
    get_cart_badge_text,
    get_cart_product_names,
    get_first_product_name_and_price,
    get_inventory_products,
    get_page_title_text,
    is_main_menu_visible,
    is_sort_filter_visible,
    login_with_valid_user,
    open_cart,
)


@pytest.mark.smoke
@pytest.mark.login
def test_login_exitoso_redirige_a_inventario(driver):
    """Valida login exitoso con usuario estándar."""
    login_with_valid_user(driver)

    assert "/inventory.html" in driver.current_url, "El usuario no fue redirigido al inventario."
    assert get_page_title_text(driver) == "Products", "El título visible del inventario no es correcto."
    assert get_app_logo_text(driver) == "Swag Labs", "El logo de la aplicación no coincide."


@pytest.mark.catalogo
def test_catalogo_muestra_titulo_productos_menu_y_filtro(driver):
    """Valida elementos principales del catálogo de productos."""
    login_with_valid_user(driver)

    products = get_inventory_products(driver)
    first_product_name, first_product_price = get_first_product_name_and_price(driver)

    print(f"Primer producto listado: {first_product_name} - {first_product_price}")

    assert driver.title == "Swag Labs", "El título del navegador no es correcto."
    assert get_page_title_text(driver) == "Products", "El título visible del catálogo no es correcto."
    assert len(products) > 0, "No se encontraron productos visibles en el inventario."
    assert first_product_name != "", "El primer producto no tiene nombre visible."
    assert first_product_price.startswith("$"), "El precio del primer producto no tiene formato esperado."
    assert is_main_menu_visible(driver), "El menú principal no está visible."
    assert is_sort_filter_visible(driver), "El filtro de ordenamiento no está visible."


@pytest.mark.carrito
def test_agregar_primer_producto_al_carrito(driver):
    """Agrega el primer producto al carrito y valida que aparezca correctamente."""
    login_with_valid_user(driver)

    added_product_name = add_first_product_to_cart(driver)

    assert get_cart_badge_text(driver) == "1", "El contador del carrito no se incrementó a 1."

    open_cart(driver)
    cart_product_names = get_cart_product_names(driver)

    assert "/cart.html" in driver.current_url, "No se navegó correctamente al carrito."
    assert added_product_name in cart_product_names, "El producto agregado no aparece en el carrito."
