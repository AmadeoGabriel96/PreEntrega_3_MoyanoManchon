from django.urls import path
from AppCoderPE3.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", curso), 
    path("profesores/", profesores), 
    path("alumnos/", alumnos), 

    path("crear_curso/", crear_curso, name="Cursos"),
    path("crear_profesor/", crear_profesor, name="Profesores"),
    path("crear_alumno/", crear_alumno, name="Alumnos"),

    path("buscar_curso/", buscar_curso),

    path("busqueda/", busqueda, name="Busqueda"),
    path("resultados/", resultados),
]