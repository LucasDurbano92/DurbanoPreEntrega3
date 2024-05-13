from django.shortcuts import render


from . import models


def index(request):
    ventas_de_perifericos = models.Venta.objects.all()
    contexto = {"ventas": ventas_de_perifericos}
    return render(request, "clase/index.html", contexto)