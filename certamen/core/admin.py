from django.contrib import admin
from .models import Profesor, Proyecto, Estudiante

# Register your models here.

admin.site.register(Proyecto)
admin.site.register(Profesor)
admin.site.register(Estudiante)