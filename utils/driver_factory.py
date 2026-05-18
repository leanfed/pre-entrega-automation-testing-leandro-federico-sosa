"""Fábrica de WebDriver.

Centralizar la creación del navegador permite reutilizar configuración
sin repetir código en cada test.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(headless: bool = False) -> webdriver.Chrome:
    """Crea y configura una instancia de Chrome WebDriver.

    Args:
        headless: si es True, ejecuta el navegador sin interfaz gráfica.

    Returns:
        Instancia configurada de Chrome WebDriver.
    """
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)  # Se priorizan esperas explícitas.
    return driver
