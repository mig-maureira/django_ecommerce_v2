from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ProductoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto
from django.contrib import messages


@permission_required("productos.puede_publicar_producto", raise_exception=True)
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()
            return redirect("mis_productos")
    else:
        form = ProductoForm()

    return render(request, "productos/crear_producto.html", {"form": form})


@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, vendedor=request.user)

    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()

            return redirect("mis_productos")
    else:
        form = ProductoForm(instance=producto)

    return render(request, "productos/editar_producto.html", {"form": form})


@login_required
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, vendedor=request.user)

    if request.method == "POST":
        producto.delete()
        return redirect("mis_productos")

    # Pasa el objeto producto en el contexto
    return render(request, "productos/eliminar_producto.html", {"producto": producto})


@login_required
def mis_productos(request):
    productos = Producto.objects.filter(vendedor=request.user)
    return render(request, "productos/mis_productos.html", {"productos": productos})


def obtener_carrito(request):
    return request.session.get("carrito", {})


# función para agregar al carrito
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get("carrito", {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]["cantidad"] += 1
    else:
        carrito[str(producto_id)] = {
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": float(producto.precio),
            "cantidad": 1,
            "imagen": producto.imagen.url if producto.imagen else "",
        }

    request.session["carrito"] = carrito
    request.session.modified = True
    messages.success(request, "producto agregado con exito")
    return redirect(request.META.get("HTTP_REFERER", "/"))


def restar_del_carrito(request, producto_id):
    carrito = request.session.get("carrito", {})

    if str(producto_id) in carrito:
        carrito[str(producto_id)]["cantidad"] -= 1

        if carrito[str(producto_id)]["cantidad"] <= 0:
            del carrito[str(producto_id)]

    request.session["carrito"] = carrito
    request.session.modified = True
    messages.warning(request, "Producto eliminado con exito")
    return redirect(request.META.get("HTTP_REFERER", "/"))


# Vista para ver el carrito
def ver_carrito(request):
    carrito = request.session.get("carrito", {})

    total = sum(item["precio"] * item["cantidad"] for item in carrito.values())

    return redirect(request.META.get("HTTP_REFERER", "/"))


# Eliminar producto del carrito
def eliminar_item(request, producto_id):
    carrito = request.session.get("carrito", {})

    if str(producto_id) in carrito:
        del carrito[str(producto_id)]

    request.session["carrito"] = carrito
    request.session.modified = True
    messages.warning(request, "Producto eliminado con exito")

    return redirect(request.META.get("HTTP_REFERER", "/"))


# Carrito
def carrito_context(request):
    carrito = request.session.get("carrito", {})

    total_items = sum(item["cantidad"] for item in carrito.values())
    total_precio = sum(item["precio"] * item["cantidad"] for item in carrito.values())

    return {
        "carrito": carrito,
        "total_items": total_items,
        "total_precio": total_precio,
    }


def pago(request):
    # Obtenemos los datos antes de borrar nada para asegurarnos que se vean en el agradecimiento
    carrito_data = request.session.get("carrito", {})
    total = sum(item["precio"] * item["cantidad"] for item in carrito_data.values())

    # Aquí iría tu lógica de integración con Transbank/PayPal etc.

    # 1. Renderizamos la página (mientras el carrito aún existe en la sesión o se lo pasamos)
    response = render(request, "tu_app/confirmacion.html")

    # 2. Vaciamos el carrito después de que el usuario ya vió la confirmación
    # o simplemente lo vaciamos justo antes de enviar los datos al template.
    request.session["carrito"] = {}
    request.session.modified = True

    return response


def confirmacion(request):
    messages.success(request, "¡Compra Realizada con exito!")
    return render(request, "pago.html")


def detalle_producto(request, id):
    # Busca el producto o devuelve error 404 si no existe
    producto = get_object_or_404(Producto, id=id)
    return render(request, "productos/detalle_producto.html", {"producto": producto})
