from django.db import models
from datetime import date

# Create your models here.
class Doctor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    specialty = models.TextField()


class Patient(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    last_visit = models.DateField()
    prescription = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name="patients")


def create_doctor(first_name, last_name, specialty):
    doctor = Doctor(first_name=first_name, last_name=last_name, specialty=specialty)
    doctor.save()
    return doctor


def create_patient(first_name, last_name, last_visit, prescription, doctor):
    patient = Patient(
        first_name=first_name,
        last_name=last_name,
        last_visit=last_visit,
        prescription=prescription,
    )
    patient.save()
    patient.doctors.add(doctor)
    return patient


def search_patients_by_doctor(doctor):
    patients = doctor.patients.all()
    return patients


def search_doctors_by_patient(patient):
    doctors = patient.doctors.all()
    return doctors


def total_number_of_patients(doctor):
    return len(doctor.patients.all())


def add_patient_to_doctor(patient, doctor):
    doctor.patients.add(patient)
    return doctor


def add_doctor_to_patient(patient, doctor):
    patient.doctors.add(doctor)
    return patient


def recently_visited(patient):
    patient.last_visit = date.today()
    patient.save()
    return patient


def search_for_doctors_by_specialty(specialty):
    list = Doctor.objects.filter(specialty=specialty)
    return list
