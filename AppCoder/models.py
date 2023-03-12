from django.db import models

   
class Doctor(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)
    email=models.EmailField()

class Paciente(models.Model):
    codigo=models.IntegerField()
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Medicina(models.Model):
    codigo= models.IntegerField()
    nombre=models.CharField(max_length=50)
    stock = models.IntegerField()