from django.shortcuts import render
from django.http import HttpResponse
from AppCoderPE3.forms import *
from AppCoderPE3.models import * 

# Create your views here.

def inicio(request):

    return render(request,"AppCoderPE3/inicio.html")

def curso(request):

    return render(request,"AppCoderPE3/cursos.html")  

def profesores(request):

    return render(request,"AppCoderPE3/profesores.html")

def alumnos(request):

    return render(request,"AppCoderPE3/alumnos.html") 

def crear_curso(request):

    if request.method =="POST":

        curso_nuevo = Curso(
            nombre=request.POST["nombre"],
            camada=request.POST["camada"])

        curso_nuevo.save()

        return render(request,"AppCoderPE3/inicio.html")

    return render(request, "AppCoderPE3/crear_curso.html")  

def crear_profesor(request):

    if request.method == "POST":

        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            profesor_nuevo = Profesor(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                edad=info_dic["edad"],
                email=info_dic["email"],
                profesión=info_dic["profesión"],
            )

            profesor_nuevo.save()

            return render(request, "AppCoderPE3/crear_profesor.html")

    else: 

        formulario = ProfesorFormulario()

    return render(request, "AppCoderPE3/crear_profesor.html", {"form":formulario})    

def crear_alumno(request):

    if request.method == "POST":

        formulario = AlumnoFormulario(request.POST)

        if formulario.is_valid():

            info_dic = formulario.cleaned_data

            alumno_nuevo = Alumno(
                nombre=info_dic["nombre"],
                apellido=info_dic["apellido"],
                edad=info_dic["edad"],
                email=info_dic["email"],
            )

            alumno_nuevo.save()

            return render(request, "AppCoderPE3/crear_alumno.html")

    else: 

        formulario = AlumnoFormulario()

    return render(request, "AppCoderPE3/crear_alumno.html", {"form":formulario})

def buscar_curso(request):

    if request.GET:

        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains=nombre)

        mensaje = f"Estás buscando el curso: {nombre}"
   
        return render(request, "AppCoderPE3/buscar_curso.html", {"resultados":cursos})

    
    return render(request, "AppCoderPE3/buscar_curso.html")

def busqueda(request):

    return render(request, "AppCoderPE3/busqueda.html")    

def resultados(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "AppCoderPE3/resultados.html", {"cursos":cursos, "camada":camada})

    else: 

        respuesta = "No enviaste datos."    

    return HttpResponse(respuesta)


    
  









 