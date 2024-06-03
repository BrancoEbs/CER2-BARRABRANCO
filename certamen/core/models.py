from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30, verbose_name= "Nombre Estudiante", primary_key=True)
    correo = models.EmailField(max_length=100, verbose_name= "Correo Estudiante")

    def __str__(self) -> str:
        return f"{self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre Profesor", primary_key=True)
    correo = models.EmailField(max_length=50, verbose_name="Correo Profesor")

    def __str__(self) -> str:
        return f"{self.nombre}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=25)
    estudiante = models.CharField(max_length=25)
    tipo = models.CharField(max_length=30)
    profesor = models.CharField(max_length=25,default="Sin Seleccionar")

    def __str__(self) -> str:
        return self.nombre



