from django.db import models
from django import forms
from clase.models import Vendedor, Cliente, Producto, Venta

class NuevoVendedor(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre']

class NuevoCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre']

class NuevoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre']

class Ventas(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['Nro_Venta', 'cliente', 'vendedor', 'producto']
    producto = forms.ModelMultipleChoiceField(queryset=Producto.objects.all(), widget=forms.CheckboxSelectMultiple)