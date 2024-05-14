from django.shortcuts import render, redirect
from .models import NuevoVendedor, NuevoCliente, NuevoProducto, Ventas

def agregar_vendedor(request):
    if request.method == 'POST':
        form = NuevoVendedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Crear:agregar_vendedor') 
    else:
        form = NuevoVendedor()
    return render(request, 'Crear/agregar_vendedor.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = NuevoCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Crear:agregar_cliente')
    else:
        form = NuevoCliente()
    return render(request, 'Crear/agregar_cliente.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = NuevoProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Crear:agregar_producto')
    else:
        form = NuevoProducto()
    return render(request, 'Crear/agregar_producto.html', {'form': form})

def agregar_venta(request):
    if request.method == 'POST':
        form = Ventas(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Crear:agregar_venta')
    else:
        form = Ventas()
    return render(request, 'Crear/agregar_venta.html', {'form': form})

