from django import forms 

class CursoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

    def __str__(self):

        return f"{self.nombre} --- {self.camada}"

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    profesión = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()

class AlumnoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()   
     
