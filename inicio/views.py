from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
meses = {
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:"Julio",
    8:"Agosto",
    9:"Septiembre",
    10:"Octubre",
    11:"Noviembre",
    12:"Diciembre"
}

def inicio(request):
    global meses
    hoy = datetime.now()
    contexto = {"hoy": hoy, "mes":meses[hoy.month]}
    return render(request, "paginas/inicio.html",contexto)

def personajes(request):
    personajes = Personaje.objects.all()
    return render(request, "paginas/personajes.html", {"personaje":personajes})

