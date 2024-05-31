from django.db import models

# Create your models here.

from django.db import models

class Platillo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class PlatilloPromocion(models.Model):
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio_promocion = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = models.URLField(null=True, blank=True)

class Comentario(models.Model):
    PUNTAJE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    descripcion = models.TextField()
    puntaje = models.IntegerField(choices=PUNTAJE_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion

class Entrada(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = models.URLField(null=True, blank=True)

class Bebida(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nombre