"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarhospital.com
Prompt: Develop a code snippet that simulates a patient care service for a specific department, such as Cardiology or Neurology, based on the multi-specialty services provided by Amar Hospital.
Generated: DETERMINISTIC_243d7349a249534c
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Patient:
    """
    Represents a patient in the hospital.
    """
    def __init__(self, name, age, condition, department):
        """
        Initializes a patient with their details.
        :param name: Name of the patient
        :param age: Age of the patient
        :param condition: Medical condition of the patient
        :param department: Department the patient is assigned to
        """
        self.name = name
        self.age = age
        self.condition = condition
        self.department = department


class Department:
    """
    Represents a department in the hospital.
    """
    def __init__(self, name):
        """
        Initializes a department with its name and patient list.
        :param name: Name of the department (e.g., Cardiology, Neurology)
        """
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        """
        Adds a patient to the department's patient list.
        :param patient: Patient object to be added
        """
        if patient.department != self.name:
            raise ValueError(f"Patient belongs to the {patient.department} department, not {self.name}.")
        self.patients.append(patient)

    def list_patients(self):
        """
        Lists all patients in the department.
        :return: List of patient details
        """
        if not self.patients:
            return f"No patients currently admitted in {self.name}."
        return [f"Name: {patient.name}, Age: {patient.age}, Condition: {patient.condition}" for patient in self.patients]


class Hospital:
    """
    Represents the hospital with multiple departments.
    """
    def __init__(self, name):
        """
        Initializes the hospital with its name and available departments.
        :param name: Name of the hospital
        """
        self.name = name
        self.departments = {}

    def add_department(self, department_name):
        """
        Adds a new department to the hospital.
        :param department_name: Name of the department to be added
        """
        if department_name in self.departments:
            raise ValueError(f"Department {department_name} already exists.")
        self.departments[department_name] = Department(department_name)

    def get_department(self, department_name):
        """
        Retrieves a department by its name.
        :param department_name: Name of the department
        :return: Department object
        """
        return self.departments.get(department_name, None)


# Simulated usage

if __name__ == "__main__":
    try:
        # Create hospital instance
        hospital = AmarHospital("Amar Hospital")
        
        # Add departments
        hospital.add_department("Cardiology")
        hospital.add_department("Neurology")
        
        # Retrieve specific department
        cardiology = hospital.get_department("Cardiology")
        neurology = hospital.get_department("Neurology")
        
        # Add patients to Cardiology
