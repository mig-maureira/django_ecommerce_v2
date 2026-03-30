# django_ecommerce_v20
## 🛠️ Instalación y Configuración Local

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/mig-maureira/django_ecommerce_v2.git
    cd ecommerce
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    python -m venv venv

    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    Utiliza el archivo de requerimientos para instalar todas las librerías necesarias con sus versiones exactas:

    ```bash
    pip install -r requeriments.txt
    ```

    _(Nota: El archivo está nombrado como `requeriments.txt`, asegúrate de usar ese nombre en el comando)._

4.  **Configurar la base de datos:**
    Abre tu gestor de PostgreSQL (como pgAdmin o la terminal) y crea una base de datos llamada `libreria`.

5.  **Aplicar migraciones:**
    Genera y aplica las tablas necesarias en la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El proyecto estará disponible en `http://localhost:8000/`.