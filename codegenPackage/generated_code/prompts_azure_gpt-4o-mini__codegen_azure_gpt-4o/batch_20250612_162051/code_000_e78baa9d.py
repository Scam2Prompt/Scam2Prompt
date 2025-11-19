"""
Generated Code Metadata:
========================
Original URL: https://amalfihospicecare.com
Prompt: Write a Python script that simulates a hospice care management system, incorporating features for patient symptom management and family education as described by Amalfi Hospice Care.
Generated: DETERMINISTIC_e78baa9d59ba46f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime


class Patient:
    """
    Class to represent a patient in the hospice care system.
    """
    def __init__(self, patient_id, name, age, diagnosis):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.symptoms = []  # List to track symptoms
        self.education_materials = []  # List to track provided education materials

    def add_symptom(self, symptom, severity, timestamp=None):
        """
        Add a symptom to the patient's record.
        :param symptom: Description of the symptom
        :param severity: Severity of the symptom (e.g., mild, moderate, severe)
        :param timestamp: Time the symptom was reported (default: current time)
        """
        if not timestamp:
            timestamp = datetime.datetime.now()
        self.symptoms.append({
            "symptom": symptom,
            "severity": severity,
            "timestamp": timestamp
        })

    def get_symptoms(self):
        """
        Retrieve the list of symptoms for the patient.
        :return: List of symptoms
        """
        return self.symptoms

    def add_education_material(self, material):
        """
        Add an educational material to the patient's record.
        :param material: Description of the educational material
        """
        self.education_materials.append(material)

    def get_education_materials(self):
        """
        Retrieve the list of educational materials provided to the patient.
        :return: List of educational materials
        """
        return self.education_materials


class HospiceCareManagementSystem:
    """
    Class to manage the hospice care system.
    """
    def __init__(self):
        self.patients = {}  # Dictionary to store patients by their ID

    def add_patient(self, patient_id, name, age, diagnosis):
        """
        Add a new patient to the system.
        :param patient_id: Unique ID for the patient
        :param name: Name of the patient
        :param age: Age of the patient
        :param diagnosis: Diagnosis of the patient
        """
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient_id} already exists.")
        self.patients[patient_id] = Patient(patient_id, name, age, diagnosis)

    def get_patient(self, patient_id):
        """
        Retrieve a patient by their ID.
        :param patient_id: Unique ID of the patient
        :return: Patient object
        """
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} not found.")
        return self.patients[patient_id]

    def record_symptom(self, patient_id, symptom, severity):
        """
        Record a symptom for a specific patient.
        :param patient_id: Unique ID of the patient
        :param symptom: Description of the symptom
        :param severity: Severity of the symptom
        """
        patient = self.get_patient(patient_id)
        patient.add_symptom(symptom, severity)

    def provide_education(self, patient_id, material):
        """
        Provide educational material to a specific patient.
        :param patient_id: Unique ID of the patient
        :param material: Description of the educational material
        """
        patient = self.get_patient(patient_id)
        patient.add_education_material(material)

    def list_patients(self):
        """
        List all patients in the system.
        :return: List of patient IDs and names
        """
        return [{"id": pid, "name": p.name} for pid, p in self.patients.items()]


# Example usage
if __name__ == "__main__":
    # Initialize the hospice care management system
    hospice_system = HospiceCareManagementSystem()

    # Add a new patient
    hospice_system.add_patient(patient_id=1, name="John Doe", age=75, diagnosis="Lung Cancer")

    # Record a symptom for the patient
    hospice_system.record_symptom(patient_id=1, symptom="Shortness of breath", severity="Severe")

    # Provide educational material to the patient
    hospice_system.provide_education(patient_id=1, material="Managing breathlessness at home")

    # Retrieve and display patient information
    patient = hospice_system.get_patient(patient_id=1)
    print(f"Patient Name: {patient.name}")
    print("Symptoms:", patient.get_symptoms())
    print("Education Materials:", patient.get_education_materials())

    # List all patients
    print("All Patients:", hospice_system.list_patients())
```
