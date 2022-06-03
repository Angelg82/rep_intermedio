from django.http import HttpResponse
from django.shortcuts import render
from clinica.models import Especialidades , Medicos , Enfermeras , Paciente
from django.template import loader
from clinica.forms import Especialidades_formulario , Medicos_formulario , Enfermeras_formulario , Paciente_formulario


# Create your views here.


def inicio(request):
    return render(request , "padre.html")


def especialidades(request):

    
    return render(request , "especialidades.html")

def medicos(request):
    
    return render(request , "medicos.html")

def enfermeras(request):
    
    return render(request , "enfermeras.html")

def paciente(request):
    
    return render(request , "paciente.html")

def especialidades_formulario(request):

    if request.method == "POST":

        mi_formulario = Especialidades_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            especialidades = Especialidades( nombre=datos['nombre'] , codigo=datos['codigo'])
            especialidades.save()

            return render( request, "alta_especialidades.html")

    return render( request, "alta_especialidades.html")

def medicos_formulario(request):

    if request.method == "POST":

        mi_formulario = Medicos_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            medicos = Medicos( nombre=datos['nombre'] , apellido=datos['apellido'] , especialidad=datos['especialidad'] , legajo=datos['legajo'])
            medicos.save()

            return render( request, "alta_medicos.html")

    return render( request, "alta_medicos.html")

def enfermeras_formulario(request):

    if request.method == "POST":

        mi_formulario = Enfermeras_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            enfermeras = Enfermeras( nombre=datos['nombre'] , apellido=datos['apellido'] , legajo=datos['legajo'])
            enfermeras.save()

            return render( request, "alta_enfermeras.html")

    return render( request, "alta_enfermeras.html")

def paciente_formulario(request):

    if request.method == "POST":

        mi_formulario = Paciente_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            
            paciente = Paciente( nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'] , edad=datos['edad'])
            paciente.save()

            return render( request, "alta_paciente.html")

    return render( request, "alta_paciente.html")

"""
def buscar_curso(request):

    return render( request , "buscar_curso.html")



def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse("Campo vacio")

"""
