from appFinal.views import *
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', vistaHome, name="home"),
    path('estudies', EstudiosListView.as_view(), name="estudies"),
    path('experience', ExperienciaListView.as_view(), name="experience"),
    path('skills', HabilidadesListView.as_view(), name="skills"),
    path('aboutme', vistaAboutMe, name="aboutme"),
    path('cargarestudio', CargarEstudios, name="cargarestudio"),
    path('cargarexperiencia', CargarExperiencia, name="cargarexperiencia"),
    path('cargarhabilidad', CargarHabilidades, name="cargarhabilidad"),
    path('login', login_request, name="login"),
    path('register', register, name="register"),
    path('logout', LogoutView.as_view(template_name= "appFinal/inicio.html"), name="logout"),
    path('editarPerfil', editarPerfil, name="editarPerfil"),
    # path('editarEstudio/<estudios_nombre>/', editarEstudios, name="editarEstudios"),
    ]