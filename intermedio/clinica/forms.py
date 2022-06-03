from django import forms

class Especialidades_formulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()

class Medicos_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    legajo = forms.IntegerField()


class Enfermeras_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    legajo = forms.IntegerField()


class Paciente_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField()