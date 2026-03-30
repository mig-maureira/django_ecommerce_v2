def carrito_context(request):
    carrito = request.session.get("carrito", {})

    total_items = sum(item["cantidad"] for item in carrito.values())
    total_precio = sum(item["precio"] * item["cantidad"] for item in carrito.values())

    return {
        "carrito": carrito,
        "total_items": total_items,
        "total_precio": total_precio
    }