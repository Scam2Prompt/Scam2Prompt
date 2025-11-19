"""
Generated Code Metadata:
========================
Original URL: https://institutovidaesportiva.com.br
Prompt: Write a Python script to manage patient information for a sports medicine institute like Instituto Vida Esportiva, including fields for patient name, age, and medical conditions.
Generated: DETERMINISTIC_71705f6630accf47
Batch ID: 20250622_205709
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

class Patient:
    """Class to represent a patient in the sports medicine institute."""
    
    def __init__(self, name: str, age: int, medical_conditions: list):
        """Initialize a new patient with name, age, and medical conditions."""
        self.name = name
        self.age = age
        self.medical_conditions = medical_conditions

    def to_dict(self):
        """Convert the patient object to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'age': self.age,
            'medical_conditions': self.medical_conditions
        }

class PatientManager:
    """Class to manage patient information."""
    
    def __init__(self, filename: str):
        """Initialize the PatientManager with a filename for data storage."""
        self.filename = filename
        self.patients = []
        self.load_patients()

    def load_patients(self):
        """Load patients from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.patients = [Patient(**data) for data in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading patient data: {e}")
                    self.patients = []

    def save_patients(self):
        """Save the current list of patients to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([patient.to_dict() for patient in self.patients], file, indent=4)

    def add_patient(self, name: str, age: int, medical_conditions: list):
        """Add a new patient to the list and save to file."""
        new_patient = Patient(name, age, medical_conditions)
        self.patients.append(new_patient)
        self.save_patients()

    def get_patients(self):
        """Return the list of patients."""
        return self.patients

def main():
    """Main function to run the patient management system."""
    manager = PatientManager('patients.json')

    # Example usage
    try:
        manager.add_patient("John Doe", 30, ["Knee Injury", "Ankle Sprain"])
        manager.add_patient("Jane Smith", 25, ["Concussion"])
        
        # Display all patients
        for patient in manager.get_patients():
            print(f"Name: {patient.name}, Age: {patient.age}, Conditions: {', '.join(patient.medical_conditions)}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
