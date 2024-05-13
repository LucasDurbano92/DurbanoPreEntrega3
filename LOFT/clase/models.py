from django.db import models

class Vendedor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
        
    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nombre

class Precio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Venta(models.Model):
    Nro_Venta = models.PositiveIntegerField(unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    producto = models.ManyToManyField(Producto)