from django import forms


class DoctorFormulario(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=30)
    email= forms.EmailField()
    
class PacienteFormulario(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()   
    
class MedicinaFormulario(forms.Form):
    codigo=forms.IntegerField()
    nombre=forms.CharField(max_length=30)
    stock= forms.IntegerField()
    
