"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Write a Python script for managing dental patient records, including fields for patient name, contact information, and treatment history, inspired by Tiziano Testori's dental practice.
Generated: DETERMINISTIC_b13fb02b1e6839f2
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class PatientRecord:
    """Class to manage patient records for a dental practice."""

    def __init__(self, name, contact_info):
        """
        Initialize a new patient record.

        Args:
            name (str): The name of the patient.
            contact_info (dict): A dictionary containing contact information.
        """
        self.name = name
        self.contact_info = contact_info
        self.treatment_history = []

    def add_treatment(self, treatment):
        """
        Add a treatment to the patient's treatment history.

        Args:
            treatment (str): Description of the treatment performed.
        """
        self.treatment_history.append(treatment)

    def to_dict(self):
        """Convert the patient record to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'contact_info': self.contact_info,
            'treatment_history': self.treatment_history
        }

class PatientManager:
    """Class to manage a collection of patient records."""

    def __init__(self, filename='patients.json'):
        """
        Initialize the patient manager.

        Args:
            filename (str): The filename to store patient records.
        """
        self.filename = filename
        self.patients = self.load_patients()

    def load_patients(self):
        """Load patient records from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    return [PatientRecord(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading patient records: {e}")
                    return []
        return []

    def save_patients(self):
        """Save patient records to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([patient.to_dict() for patient in self.patients], file, indent=4)

    def add_patient(self, name, contact_info):
        """
        Add a new patient to the records.

        Args:
            name (str): The name of the patient.
            contact_info (dict): A dictionary containing contact information.
        """
        new_patient = PatientRecord(name, contact_info)
        self.patients.append(new_patient)
        self.save_patients()

    def find_patient(self, name):
        """
        Find a patient by name.

        Args:
            name (str): The name of the patient to find.

        Returns:
            PatientRecord or None: The patient record if found, otherwise None.
        """
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def add_treatment_to_patient(self, name, treatment):
        """
        Add a treatment to a patient's record.

        Args:
            name (str): The name of the patient.
            treatment (str): Description of the treatment performed.
        """
        patient = self.find_patient(name)
        if patient:
            patient.add_treatment(treatment)
            self.save_patients()
        else:
            print(f"Patient '{name}' not found.")

def main():
    """Main function to demonstrate the PatientManager functionality."""
    manager = PatientManager()

    # Example usage
    manager.add_patient("John Doe", {"phone": "123-456-7890", "email": "john@example.com"})
    manager.add_treatment_to_patient("John Doe", "Teeth cleaning")
    manager.add_treatment_to_patient("John Doe", "Cavity filling")

    patient = manager.find_patient("John Doe")
    if patient:
        print(f"Patient: {patient.name}, Contact: {patient.contact_info}, Treatments: {patient.treatment_history}")

if __name__ == "__main__":
    main()
```
