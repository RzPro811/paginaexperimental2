from django.db import models

class Personaje(models.Model):
    nombre      = models.CharField(max_length=50)
    imagen      = models.ImageField(upload_to= "oc", default= "oc/defaul.png")
    descripcion = models.CharField(max_length=500)
    fuerza      = models.FloatField()
    agilidad    = models.FloatField()
    crackilidad = models.FloatField()
    class Meta:
        verbose_name = "Personaje"
        verbose_name_plural = "Personajes"