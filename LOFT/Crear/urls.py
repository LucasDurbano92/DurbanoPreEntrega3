from django.urls import path
from . import views

app_name = "Crear"

urlpatterns = [
  
    path('agregar_vendedor/', views.agregar_vendedor, name='agregar_vendedor'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_venta/', views.agregar_venta, name='agregar_venta'),
  ]
