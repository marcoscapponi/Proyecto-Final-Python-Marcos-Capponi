from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class estudiosFormulario(forms.Form):
    nombreEstudio = forms.CharField()
    duracion = forms.CharField()
    instituto = forms.CharField()

class experienciaFormulario(forms.Form):
    puestoTrabajo = forms.CharField()
    duracion = forms.CharField()
    nombreLugar = forms.CharField()
    locacion = forms.CharField()

class habilidadesFormulario(forms.Form):
    habilidad = forms.CharField()
    idioma = forms.CharField()
    nivelIdioma = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email: ")
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    imagen = forms.ImageField(label="Avatar", required=False)
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']