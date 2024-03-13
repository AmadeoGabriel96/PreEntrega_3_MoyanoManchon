from django.db import models

# Create your models here.

class Curso(models.Model): 

    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.camada}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    profesión = models.CharField(max_length=30)

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

class Alumno(models.Model): 

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()   

    def __str__(self):

        return f"{self.nombre} --- {self.apellido}"

    