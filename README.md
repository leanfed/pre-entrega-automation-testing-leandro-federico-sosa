# Pre-entrega Automation Testing - SauceDemo

Proyecto de automatización web realizado como pre-entrega del curso de Testing QA.  
El objetivo es automatizar flujos básicos de navegación, login, validación de catálogo y carrito utilizando **Python**, **Pytest** y **Selenium WebDriver** sobre el sitio [SauceDemo](https://www.saucedemo.com/).

---

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Pytest HTML
- Git y GitHub
- Google Chrome

---

## Estructura del proyecto

```text
pre-entrega-automation-testing-federico-sosa/
│
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   ├── driver_factory.py
│   └── saucedemo_actions.py
│
├── datos/
│   └── .gitkeep
│
├── reports/
│   ├── screenshots/
│   │   └── .gitkeep
│   └── .gitkeep
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Casos automatizados

### 1. Login exitoso

Valida que el usuario pueda iniciar sesión correctamente con las credenciales:

- Usuario: `standard_user`
- Contraseña: `secret_sauce`

Validaciones realizadas:

- Redirección a `/inventory.html`
- Título visible `Products`
- Logo superior `Swag Labs`

---

### 2. Navegación y verificación del catálogo

Validaciones realizadas:

- Título del navegador `Swag Labs`
- Título visible de la página `Products`
- Existencia de productos visibles
- Obtención del nombre y precio del primer producto
- Presencia del menú principal
- Presencia del filtro de ordenamiento

---

### 3. Interacción con productos y carrito

Validaciones realizadas:

- Agregado del primer producto al carrito
- Incremento del contador del carrito a `1`
- Navegación a `/cart.html`
- Confirmación de que el producto agregado aparece en el carrito

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd pre-entrega-automation-testing-federico-sosa
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

En Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

En Windows CMD:

```bash
venv\Scripts\activate.bat
```

En Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de pruebas

Ejecutar todos los tests:

```bash
pytest -v
```

Ejecutar generando reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

También se puede generar un reporte autocontenido:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

---

## Evidencias

El proyecto incluye captura automática de pantalla cuando un test falla.

Las capturas se guardan en:

```text
reports/screenshots/
```

El reporte HTML se genera en:

```text
reports/reporte.html
```

---

## Buenas prácticas aplicadas

- Tests independientes entre sí.
- Uso de fixtures de Pytest para crear y cerrar el navegador.
- Uso de esperas explícitas con Selenium WebDriver.
- Código separado entre tests y funciones auxiliares.
- Nombres descriptivos para funciones, variables y tests.
- Comentarios explicativos en archivos principales.
- Capturas automáticas ante fallos.
- Configuración centralizada en `utils/config.py`.

---

## Comandos sugeridos de Git

```bash
git init
git add .
git commit -m "Inicializa estructura del proyecto de automatización"

git add tests/test_saucedemo.py utils/
git commit -m "Agrega tests de login catalogo y carrito"

git add README.md requirements.txt pytest.ini
git commit -m "Documenta instalacion ejecucion y dependencias"

git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```

---

## Autor

Leandro Federico Sosa
