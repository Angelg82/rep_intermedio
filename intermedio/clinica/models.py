from django.db import models

# Create your models here.

class Especialidades(models.Model):

    nombre=models.CharField(max_length=40)
    codigo = models.IntegerField()

class Medicos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)
    legajo = models.IntegerField()

class Enfermeras(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    legajo = models.IntegerField()

class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    edad= models.IntegerField()

