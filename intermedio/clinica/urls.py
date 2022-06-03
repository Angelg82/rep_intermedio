from django.urls import path
from . import views

urlpatterns = [

    path("", views.inicio),
    path("especialidades" , views.especialidades , name="especialidades"),
    path("medicos" , views.medicos , name = "medicos"),
    path("enfermeras" , views.enfermeras , name = "enfermeras"),
    path("paciente" , views.paciente ,  name = "paciente"),
    path("alta_especialidades" , views.especialidades_formulario),
    path("alta_medicos" , views.medicos_formulario),
    path("alta_enfermeras" , views.enfermeras_formulario),
    path("alta_paciente" , views.paciente_formulario),
    

]