from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyecto
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    lista_proyectos= Proyecto.objects.all()

    data = {
        "Nombre": Proyecto.nombre,
        "Estudiante": Proyecto.estudiante,
        "Tipo": Proyecto.tipo,
        "Profesor": Proyecto.profesor, 
        "lista_proyectos": lista_proyectos,   
    }
    return render(request, 'core/index.html', data)


def nuevo_proyecto(request):
    if(request.POST):
        nombre=request.POST['NombreProyecto']
        estudiante=request.POST['NombreEstudiante']
        tema=request.POST['TemaProyecto']

        proyecto = Proyecto()

        proyecto.nombre = nombre
        proyecto.estudiante =  estudiante
        proyecto.tipo = tema

        proyecto.save()

    return render(request,"core/index.html")

        


