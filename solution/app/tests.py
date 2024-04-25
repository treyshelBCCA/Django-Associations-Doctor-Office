from django.test import TestCase
from app import models as m

# Create your tests here.
class AppTest(TestCase):
    def test_create_doctor(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        self.assertEqual(doc1.id, 1)
        self.assertEqual(doc5.id, 5)
        self.assertEqual(5, len(m.Doctor.objects.all()))
        self.assertIn(doc2, m.Doctor.objects.all())

    def test_create_patient(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        self.assertEqual(patient1.id, 1)
        self.assertEqual(patient5.id, 5)
        self.assertEqual(5, len(m.Patient.objects.all()))
        self.assertIn(patient2, m.Patient.objects.all())

    def test_search_patients_by_doctor(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        list = m.search_patients_by_doctor(doc2)
        self.assertEqual(len(list), 2)
        self.assertIn(patient1, list)

    def test_total_number_of_patients(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        total = m.total_number_of_patients(doc2)
        self.assertEqual(total, 2)

    def test_add_patient_to_doctor(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        doc2 = m.add_patient_to_doctor(patient5, doc2)

        total = m.total_number_of_patients(doc2)
        list = m.search_patients_by_doctor(doc2)

        self.assertEqual(3, total)
        self.assertIn(patient5, list)

    def test_add_doctor_to_patient(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        patient3 = m.add_doctor_to_patient(patient3, doc5)

        self.assertEqual(2, len(patient3.doctors.all()))
        self.assertIn(doc5, patient3.doctors.all())

    def test_search_doctors_by_patient(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        patient3 = m.add_doctor_to_patient(patient3, doc5)

        list = m.search_doctors_by_patient(patient3)

        self.assertEqual(2, len(list))
        self.assertIn(doc5, list)

    def test_recently_visited(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        patient5 = m.recently_visited(patient5)

        self.assertEqual(patient5.last_visit, m.date.today())

    def test_search_for_doctors_by_specialty(self):
        doc1 = m.create_doctor("Martin", "King", "Pediatrician")
        doc2 = m.create_doctor("Tanya", "Fitz", "Pediatrician")
        doc3 = m.create_doctor("Eric", "Henton", "ER")
        doc4 = m.create_doctor("Michael", "Morrison", "Anesthesiologist")
        doc5 = m.create_doctor("Christina", "Yang", "Cardio")

        patient1 = m.create_patient("Isabel", "Luna", "2023-02-12", "none", doc2)
        patient2 = m.create_patient("Sofia", "Luna", "2022-12-11", "antibiotics", doc2)
        patient3 = m.create_patient(
            "Silbina", "Rodriguez", "2022-12-09", "high blood pressure meds", doc3
        )
        patient4 = m.create_patient(
            "Jessica", "Cubilo", "2022-10-12", "allergy meds", doc5
        )
        patient5 = m.create_patient("Diego", "Luna", "2023-02-11", "none", doc4)

        list = m.search_for_doctors_by_specialty("Pediatrician")

        self.assertEqual(len(list), 2)
