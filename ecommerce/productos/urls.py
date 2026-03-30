from django.urls import path
from . import views

urlpatterns = [
    path("crear/", views.crear_producto, name="crear_producto"),
    path("mis-productos/", views.mis_productos, name="mis_productos"),
    path("editar/<int:pk>/", views.editar_producto, name="editar_producto"),
    path("eliminar/<int:pk>/", views.eliminar_producto, name="eliminar_producto"),
    # carrito de compras
    path("carrito/", views.ver_carrito, name="ver_carrito"), 
    path("carrito/agregar/<int:idProducto>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("carrito/restar/<int:producto_id>/", views.restar_del_carrito, name="restar_del_carrito"),
    path("carrito/eliminar/<int:producto_id>/", views.eliminar_item, name="eliminar_item"),
]