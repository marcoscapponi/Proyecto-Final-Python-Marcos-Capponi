from django.shortcuts import render, redirect
from django.http import HttpResponse
from appFinal.froms import *
from appFinal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def vistaHome(request):
    return render(request, "appFinal/inicio.html")

def vistaEstudies(request):
    return render(request, "appFinal/estudios.html")

def vistaExperience(request):
    return render(request, "appFinal/experiencia.html")

def vistaSkills(request):
    return render(request, "appFinal/habilidades.html")
@login_required
def vistaAboutMe(request):
    return render(request, "appFinal/sobreMi.html")
@login_required
def CargarEstudios(request):
    if request.method == "POST":
        miFormulario1 = estudiosFormulario(request.POST)
        print(miFormulario1)
        if miFormulario1.is_valid:
            informacion = miFormulario1.cleaned_data
            estudios = Estudios(nombreEstudio=informacion["nombreEstudio"], duracion=informacion["duracion"], instituto=informacion["instituto"])
            estudios.save()
            return render(request, "appFinal/inicio.html")
    else:
        miFormulario1 = estudiosFormulario()
    return render(request, "appFinal/cargarDatosEstudios.html", {"miFormulario1":miFormulario1})
@login_required
def CargarExperiencia(request):
    if request.method == "POST":
        miFormulario2 = experienciaFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data
            experiencia = Experiencia(puestoTrabajo=informacion["puestoTrabajo"], duracion=informacion["duracion"], nombreLugar=informacion["nombreLugar"], locacion=informacion["locacion"])
            experiencia.save()
            return render(request, "appFinal/inicio.html")
    else:
        miFormulario2 = experienciaFormulario()
    return render(request, "appFinal/cargarDatosExperiencia.html", {"miFormulario2":miFormulario2})
@login_required
def CargarHabilidades(request):
    if request.method == "POST":
        miFormulario3 = habilidadesFormulario(request.POST)
        print(miFormulario3)
        if miFormulario3.is_valid:
            informacion = miFormulario3.cleaned_data
            estudios = Habilidades(habilidad=informacion["habilidad"], idioma=informacion["idioma"], nivelIdioma=informacion["nivelIdioma"])
            estudios.save()
            return render(request, "appFinal/inicio.html")
    else:
        miFormulario3 = habilidadesFormulario()
    return render(request, "appFinal/cargarDatosHabilidades.html", {"miFormulario3":miFormulario3})

class EstudiosListView(LoginRequiredMixin, ListView):
    model = Estudios
    context_object_name = "estudios"
    template_name = "appFinal/estudios.html"

class ExperienciaListView(ListView):
    model = Experiencia
    context_object_name = "experiencias"
    template_name = "appFinal/experiencia.html"

class HabilidadesListView(ListView):
    model = Habilidades
    context_object_name = "habilidades"
    template_name = "appFinal/habilidades.html"

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "appFinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "appFinal/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request, "appFinal/inicio.html", {"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "appFinal/login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "appFinal/inicio.html", {"mensaje":"Usuario Creado"})
    else:
        form = UserRegisterForm()
    return render(request, "appFinal/registro.html", {"form":form})
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.imagen.save()
            miFormulario.save()
            return render(request, "appFinal/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
    return render(request, "appFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})