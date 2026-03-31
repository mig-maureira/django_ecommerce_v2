# Proyecto E-commerce - Django

Este proyecto es una plataforma de comercio electrónico desarrollada con **Django**. Incluye un sistema completo de gestión de productos, un carrito de compras basado en sesiones, registro de usuarios con perfiles extendidos y un formulario de contacto dinámico.

---

## 1. Motor de Base de Datos Utilizado

El proyecto utiliza **PostgreSQL** como motor de base de datos robusto, ejecutándose a través de un contenedor **Docker**.

- **Motor (Engine):** `django.db.backends.postgresql`
- **Nombre de la Base de Datos:** `alma`
- **Usuario:** `postgres`
- **Host:** `localhost`
- **Puerto:** `5433` (Mapeado en Docker)

---

## 2. Descripción del Modelo de Datos

La arquitectura de datos está organizada en tres aplicaciones principales, utilizando el ORM de Django para todas las operaciones:

### Aplicación `productos`

- **Producto:** Gestiona el inventario de la tienda.
  - `vendedor`: Relación `ForeignKey` con el usuario.
  - `nombre`, `descripcion`, `precio` e `imagen`.
  - `disponible`: Booleano para control de stock visual.

### Aplicación `login_app`

- **Profile (Perfil):** Extensión del modelo `User` nativo mediante `OneToOneField`.
  - Almacena `imagen` de perfil, `direccion`, `ciudad` y `telefono`.

### Aplicación `contacto`

- **Contacto:** Registra los mensajes de usuarios desde la Landing Page.
  - Almacena `nombre`, `correo` y el `mensaje` enviado.

---

## 3. Rutas Principales del Módulo de Administración

El panel administrativo de Django permite una gestión integral de los datos.

- **URL de Acceso:** `http://127.0.0.1:8000/admin/`
- **Modelos Registrados:** \* `Producto` (en la app productos).
  - `Profile` (en la app login_app).
  - `User/Groups` (gestión de permisos nativa).

---

## 4. Pasos para Ejecutar el Proyecto

Siga estos pasos para configurar el entorno de desarrollo:

1.  **Levantar Base de Datos (Docker):**
    Asegúrese de que su contenedor de PostgreSQL esté activo en el puerto `5433`.

2.  **Instalar Dependencias:**

    ```bash
    pip install django pillow psycopg2-binary
    ```

3.  **Realizar Migraciones:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4.  **Crear Superusuario (Opcional para Admin):**

    ```bash
    python manage.py createsuperuser
    ```

5.  **Ejecutar Servidor:**
    ```bash
    python manage.py runserver
    ```

---
