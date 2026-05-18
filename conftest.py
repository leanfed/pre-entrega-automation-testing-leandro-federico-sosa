"""Configuración compartida para Pytest.

Incluye:
- Fixture del navegador.
- Captura automática de pantalla cuando falla un test.
"""

import os
from datetime import datetime

import pytest

from utils.config import SCREENSHOTS_DIR
from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    """Inicializa y cierra el navegador en cada test.

    Al crear un navegador nuevo por cada prueba, los tests quedan más
    independientes entre sí, tal como pide la consigna.
    """
    browser = create_driver(headless=False)
    yield browser
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda una captura automática si falla la etapa principal del test."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")
        if browser is None:
            return

        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{item.name}_{timestamp}.png")
        browser.save_screenshot(screenshot_path)

        # Si pytest-html está instalado, se intenta adjuntar la evidencia al reporte.
        try:
            from pytest_html import extras

            extra = getattr(report, "extra", [])
            extra.append(extras.image(screenshot_path))
            report.extra = extra
        except Exception:
            # Si el plugin no está disponible, la captura igual queda guardada en reports/screenshots.
            pass
