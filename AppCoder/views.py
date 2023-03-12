from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Doctor, Medicina, Paciente
from django.http.request import QueryDict
from AppCoder.forms import DoctorFormulario, MedicinaFormulario, PacienteFormulario

# Create your views here.
def inicio(request):
    return render(request, "AppCoder/inicio.html")
  
def doctores(request):
    if request.method == 'POST':
        miFormulario = DoctorFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data
            doctor = Doctor (codigo=informacion['codigo'],nombre=informacion['nombre'], apellido=informacion['apellido'],especialidad=informacion['especialidad'],email=informacion['email']) 
            doctor.save()
            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
    else:
        miFormulario= DoctorFormulario() 
    return render(request, "AppCoder/doctores.html", {"miFormulario":miFormulario})

def medicinas(request):
    if request.method == 'POST':
        miFormulario = MedicinaFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data
            medicina = Medicina (codigo=informacion['codigo'],nombre=informacion['nombre'], stock=informacion['stock']) 
            medicina.save()
            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
    else:
        miFormulario= MedicinaFormulario() 
    return render(request, "AppCoder/medicinas.html", {"miFormulario":miFormulario})

def pacientes(request):
    if request.method == 'POST':
        miFormulario = PacienteFormulario(request.POST) 
        print(miFormulario)
        if miFormulario.is_valid:  
            informacion = miFormulario.cleaned_data
            paciente = Paciente (codigo=informacion['codigo'],nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email']) 
            paciente.save()
            return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
    else:
        miFormulario= PacienteFormulario() 
    return render(request, "AppCoder/pacientes.html", {"miFormulario":miFormulario})

def buscar(request):
    if  request.GET["codigo"]:
        codigo = request.GET['codigo'] 
        doctores = Doctor.objects.filter(codigo__icontains=codigo)
        return render(request, "AppCoder/inicio.html", {"doctores":doctores, "codigo":codigo})
    else:
        respuesta = "No ingresaste datos"
    return HttpResponse(respuesta)
