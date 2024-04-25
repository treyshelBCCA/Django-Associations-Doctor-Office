# Purpose

You will be creating an organization system for a doctor's office.

Create two models that are connected to one another.

`Doctor` should have the following fields:

- [ ] first_name
- [ ] last_name
- [ ] specialty
- [ ] and it should be connected to the Patient class in some way with a relational field. (either here or with Patient)

`Patient` should have the following fields:

- [ ] first_name
- [ ] last_name
- [ ] last_visit is a date_field that shows the date of the patient's last visit.
- [ ] prescription
- [ ] and it should be connected to the Doctor class in some way with a relational field (either here or with Doctor)

## Functions

- [x] Create Doctor function that is thoroughly tested.
- [x] Create Patient function that is thoroughly tested.
- [ ] Search for Patient(s) by Doctor, which allows you to search for any patient that is attached to specific doctor. It should return a queryset/list of patients of that doctor.
- [ ] Search for Doctor(s) by patient, which allows you to search for any doctor that is attached to a specific patient. It should return a queryset/list of doctors of that patient.
- [ ] Total number of patients should return the total amount of patients a specific doctor has.
- [ ] Add a patient to a doctor. It should allow you to add a patient to a doctor given the patient and the doctor.
- [ ] Recently visited, it should allow you to change the last_visit date of the Patient to the current date.
- [ ] Add a doctor to a patient. It should allow you to add a doctor to a patient given the patient and doctor.
- [ ] Search for doctors by specialty, it should filter through all doctors given a certain specialty.
