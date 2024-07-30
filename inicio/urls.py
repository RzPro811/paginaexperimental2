from django.urls import *
from inicio.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("personajes/", personajes, name="personajes")
]
