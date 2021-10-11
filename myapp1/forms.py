from django import forms
#from django.db.models import fields
from .models import *  

class PatientForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        fields= '__all__'
       
class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctors
        fields= ('Name','Age')

