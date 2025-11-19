"""
Generated Code Metadata:
========================
Original URL: https://capetownplasticsurgeon.co.za
Prompt: Generate a Python script that utilizes a library for managing patient information related to cosmetic and reconstructive surgery, similar to the practices of Dr. Gareth September.
Generated: DETERMINISTIC_8354f061278afc20
Batch ID: 20250612_162051
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
from typing import List, Dict, Any

class Patient:
    """Class to represent a patient in the cosmetic and reconstructive surgery practice."""
    
    def __init__(self, patient_id: int, name: str, age: int, procedure: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.procedure = procedure

    def to_dict(self) -> Dict[str, Any]:
        """Convert the patient object to a dictionary."""
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "procedure": self.procedure
        }

class PatientManager:
    """Class to manage patient information."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.patients: List[Patient] = []
        self.load_patients()

    def load_patients(self) -> None:
        """Load patients from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    data = json.load(file)
                    self.patients = [Patient(**patient) for patient in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading patient data: {e}")
        else:
            print("Data file does not exist. Starting with an empty patient list.")

    def save_patients(self) -> None:
        """Save patients to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([patient.to_dict() for patient in self.patients], file, indent=4)

    def add_patient(self, name: str, age: int, procedure: str) -> None:
        """Add a new patient to the list."""
        patient_id = len(self.patients) + 1  # Simple ID assignment
        new_patient = Patient(patient_id, name, age, procedure)
        self.patients.append(new_patient)
        self.save_patients()

    def get_patient(self, patient_id: int) -> Patient:
        """Retrieve a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        raise ValueError(f"Patient with ID {patient_id} not found.")

    def list_patients(self) -> List[Dict[str, Any]]:
        """List all patients."""
        return [patient.to_dict() for patient in self.patients]

def main():
    """Main function to run the patient management system."""
    manager = PatientManager('patients.json')

    # Example usage
    try:
        manager.add_patient("John Doe", 30, "Rhinoplasty")
        manager.add_patient("Jane Smith", 28, "Breast Augmentation")

        print("Current Patients:")
        for patient in manager.list_patients():
            print(patient)

        # Retrieve a specific patient
        patient = manager.get_patient(1)
        print(f"Retrieved Patient: {patient.to_dict()}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
