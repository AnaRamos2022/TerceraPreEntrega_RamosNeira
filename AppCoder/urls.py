from django.urls import path
from AppCoder import views, forms

urlpatterns = [
   path('', views.inicio, name="Inicio"),
   path('doctores', views.doctores, name="Doctores"),
   path('pacientes', views.pacientes, name="Pacientes"),
   path('medicinas', views.medicinas, name="Medicinas"),
   path('doctorFormulario', forms.DoctorFormulario, name="DoctorFormulario"),
   path('medicinaFormulario', forms.MedicinaFormulario, name="MedicinaFormulario"),
   path('pacienteFormulario', forms.PacienteFormulario, name="PacienteFormulario"),
   #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
   path('buscar/', views.buscar),
]

