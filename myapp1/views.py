from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.http import Http404

# Create your views here.

class root(View):
	def get(self, request):
		return redirect('myapp1:my_index_view')

class MyIndexView(View):
	
	def get(self, request):
		
		doctors = Doctors.objects.all()

		context = {
			'doctors' : doctors
			}
		return render(request,'index.html',context)

	def post(self, request):
		if request.method == 'POST':
			docForm = DoctorForm(request.POST)
			patForm = PatientForm(request.POST) 
			
			if 'btnMakeAppointment' in request.POST:
				print ('make appointment clicked')
				if patForm.is_valid():
					print('valid')
					namee = request.POST.get("Name")
					emaill = request.POST.get("Email")
					phonee = request.POST.get("Phone")
					datee = request.POST.get("Appointment_Date")
					doctor_id = patForm.cleaned_data.get("Doctor")

					patForm = Patient(Name = namee, Email = emaill, Phone = phonee, Appointment_Date = datee, Doctor = doctor_id)
					patForm.save()
					return redirect('myapp1:after_appointment_view')
				else:
					print(patForm.errors)
					print('make appointment not valid')

			if 'btnSignUp' in request.POST:
				print ('sign up clicked')
				if docForm.is_valid():
					name = request.POST.get("Name")
					gender = request.POST.get("Gender")
					age = request.POST.get("Age")
					password = request.POST.get("Password")
					print(name)
					print(age)
					docForm = Doctors(Name = name, Gender = gender, Age = age, Password = password)
					docForm.save()
					return redirect('myapp1:my_index_view')
				else:
					print(docForm.errors)
					
		return HttpResponse('OK')
				   
	
class Dashboard(View):
	def get(self, request):
		
		doctors = Doctors.objects.all()
		patient = Patient.objects.all()
		context = {
			'doctors' : doctors, #name that we want to use
			'patient' : patient,
					
		}
		return render(request,'dashboard.html', context)

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdate' in request.POST:	
				print('update profile button clicked')
				pid = request.POST.get("patient-id")			
				name = request.POST.get("patient-name")
				appointmentdate = request.POST.get("patient-appointmentdate")
				phone = request.POST.get("patient-phone")
				doctor = request.POST.get("patient-doctor")
				print(name)
				update_patient = Patient.objects.filter(Patient_ID = pid).update(Name = name, Appointment_Date = appointmentdate, Phone = phone, Doctor = doctor)
				print(update_patient)
				print('profile updated')
			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				pid = request.POST.get("ppatient-id")
				pat = Patient.objects.filter(Patient_ID = pid).delete()
				#pers = Person.objects.filter(id = sid).delete()
				print('recorded deleted')
			elif 'btnDoctorUpdate' in request.POST:
				did = request.POST.get("doctor-id")			
				dname = request.POST.get("doctor-name")
				gender = request.POST.get("doctor-gender")
				age = request.POST.get("doctor-age")
				password = request.POST.get("doctor-password")
				update_doctor = Doctors.objects.filter(Doctor_ID = did).update(Name = dname, Gender = gender, Age = age, Password = password)
				print(update_doctor)
				print('profile updated')
			elif 'btnDoctorDelete' in request.POST:	
				print('delete button clicked')
				did = request.POST.get("ddoctor-id")
				doc = Doctors.objects.filter(Doctor_ID = did).delete()
				print('recorded deleted')
		return redirect('myapp1:dashboard')

	


class After(View):
	def get(self, request):
		return render(request,'after_appointment.html', {})        
