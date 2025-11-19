"""
Generated Code Metadata:
========================
Original URL: https://www.spanisheyeclinic.com
Prompt: Generate a Python code snippet to manage patient data for an ophthalmology clinic, including fields for patient name, contact information, and specific eye conditions such as cataract, glaucoma, or amblyopia.
Generated: DETERMINISTIC_5e055f3f5652833d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient.py

from enum import Enum
from typing import Optional

class EyeCondition(str, Enum):
    """Enum for eye conditions."""
    CATARACT = "cataract"
    GLAUCOMA = "glaucoma"
    AMBLYOPIA = "amblyopia"
    OTHER = "other"

class Patient:
    """Class to represent a patient in the ophthalmology clinic."""

    def __init__(self, 
                 patient_id: int, 
                 name: str, 
                 phone_number: str, 
                 email: str, 
                 eye_condition: EyeCondition, 
                 additional_info: Optional[str] = None):
        """
        Initialize a Patient object.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - phone_number (str): Patient's phone number.
        - email (str): Patient's email address.
        - eye_condition (EyeCondition): Patient's eye condition.
        - additional_info (str, optional): Additional information about the patient. Defaults to None.
        """
        self.patient_id = patient_id
        self.name = name
        self.contact_info = {
            "phone_number": phone_number,
            "email": email
        }
        self.eye_condition = eye_condition
        self.additional_info = additional_info

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}"

    def get_patient_info(self):
        """Return a dictionary containing patient's information."""
        patient_info = {
            "patient_id": self.patient_id,
            "name": self.name,
            "contact_info": self.contact_info,
            "eye_condition": self.eye_condition.value,
            "additional_info": self.additional_info
        }
        return patient_info

class PatientDatabase:
    """Class to manage a collection of patients."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient: Patient):
        """
        Add a patient to the database.

        Args:
        - patient (Patient): Patient object to add.

        Raises:
        - ValueError: If a patient with the same ID already exists.
        """
        if patient.patient_id in self.patients:
            raise ValueError("Patient with the same ID already exists.")
        self.patients[patient.patient_id] = patient

    def get_patient(self, patient_id: int) -> Optional[Patient]:
        """
        Retrieve a patient by ID.

        Args:
        - patient_id (int): ID of the patient to retrieve.

        Returns:
        - Patient: Patient object if found, otherwise None.
        """
        return self.patients.get(patient_id)

    def update_patient(self, patient_id: int, patient: Patient):
        """
        Update a patient's information.

        Args:
        - patient_id (int): ID of the patient to update.
        - patient (Patient): Updated Patient object.

        Raises:
        - ValueError: If the patient ID does not exist.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient ID does not exist.")
        self.patients[patient_id] = patient

    def delete_patient(self, patient_id: int):
        """
        Delete a patient from the database.

        Args:
        - patient_id (int): ID of the patient to delete.

        Raises:
        - ValueError: If the patient ID does not exist.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient ID does not exist.")
        del self.patients[patient_id]

def main():
    # Example usage
    database = PatientDatabase()

    patient1 = Patient(
        patient_id=1,
        name="John Doe",
        phone_number="123-456-7890",
        email="john@example.com",
        eye_condition=EyeCondition.CATARACT
    )

    patient2 = Patient(
        patient_id=2,
        name="Jane Doe",
        phone_number="987-654-3210",
        email="jane@example.com",
        eye_condition=EyeCondition.GLAUCOMA,
        additional_info="Follow-up appointment scheduled."
    )

    database.add_patient(patient1)
    database.add_patient(patient2)

    print(database.get_patient(1).get_patient_info())
    print(database.get_patient(2).get_patient_info())

    # Update patient
    updated_patient = Patient(
        patient_id=1,
        name="John Doe",
        phone_number="555-123-4567",
        email="john.updated@example.com",
        eye_condition=EyeCondition.CATARACT
    )
    database.update_patient(1, updated_patient)
    print(database.get_patient(1).get_patient_info())

    # Delete patient
    database.delete_patient(2)
    print(database.get_patient(2))  # Should print: None

if __name__ == "__main__":
    main()
```
