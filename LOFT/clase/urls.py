from django.urls import path
from .views import buscar_producto
from .views import buscar_venta
from .views import lista_productos
from . import views

app_name = "clase"

urlpatterns = [
  
    path("", views.index, name="index"),
    path('buscar-producto/', buscar_producto, name='buscar_producto'),
    path('buscar-venta/', buscar_venta, name='buscar_venta'),
    path('lista-productos/', lista_productos, name='lista_productos'),
    # path("producto/update/<int:pk>", views.ProductoUpdate.as_view(), name="producto_update"),
    # path("producto/delete/<int:pk>", views.ProductoDelete.as_view(), name="producto_delete"),
]
