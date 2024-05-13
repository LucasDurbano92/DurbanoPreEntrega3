from django.shortcuts import render
from .models import Producto
from .models import Venta

from . import models


def index(request):
    ventas_de_perifericos = models.Venta.objects.all()
    contexto = {"ventas": ventas_de_perifericos}
    return render(request, "clase/index.html", contexto)


def buscar_venta(request):
    if request.method == 'GET' and 'q' in request.GET:
        busqueda = request.GET.get('q', '')
        productos = Venta.objects.filter(Nro_Venta__icontains=busqueda)
    else:
        productos = Venta.objects.all()

    return render(request, 'clase/buscar_venta.html', {'ventas': productos})


def buscar_producto(request):
    if request.method == 'GET' and 'q' in request.GET:
        busqueda = request.GET.get('q', '')
        productos = Producto.objects.filter(nombre__icontains=busqueda)
    else:
        productos = Producto.objects.all()

    return render(request, 'clase/buscar_producto.html', {'productos': productos})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'clase/lista_productos.html', {'productos': productos})