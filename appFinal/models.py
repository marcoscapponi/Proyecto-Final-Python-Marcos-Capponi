from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your models here.
class Estudios(models.Model):
    nombreEstudio = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    instituto = models.CharField(max_length=50)

class Experiencia(models.Model):
    puestoTrabajo = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    nombreLugar = models.CharField(max_length=50)
    locacion = models.CharField(max_length=50)

class Habilidades(models.Model):
    habilidad = models.CharField(max_length=50, blank=True)
    idioma = models.CharField(max_length=50, blank=True)
    nivelIdioma = models.CharField(max_length=50, blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"