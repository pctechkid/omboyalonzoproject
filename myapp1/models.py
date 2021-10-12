from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Doctors(models.Model):
	Doctor_ID = models.AutoField(primary_key=True)
	Name = models.CharField(max_length = 50)
	Age = models.IntegerField()
	Gender = models.CharField(max_length = 10)
	Password = models.CharField(max_length = 20)

	

class Patient(models.Model):
	Patient_ID = models.AutoField(primary_key=True)
	Name = models.CharField(max_length = 50)
	Email = models.CharField(max_length = 50)
	Appointment_Date = models.DateField()
	Phone = models.CharField(max_length = 50)
	Doctor = models.ForeignKey(Doctors, on_delete = models.CASCADE)

	
	

