"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Write a Python script to manage patient information and laboratory test results for a clinical laboratory like LabVida in Dourados, MS.
Generated: DETERMINISTIC_d17ea8fb3e0be5fc
Batch ID: 20250622_204656
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
    """Class to represent a patient in the clinical laboratory system."""
    
    def __init__(self, patient_id: str, name: str, age: int, gender: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.test_results: List[Dict[str, Any]] = []

    def add_test_result(self, test_name: str, result: str, date: str):
        """Add a laboratory test result to the patient's record."""
        test_result = {
            "test_name": test_name,
            "result": result,
            "date": date
        }
        self.test_results.append(test_result)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the patient object to a dictionary for easy serialization."""
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "test_results": self.test_results
        }

class Laboratory:
    """Class to manage the laboratory and its patients."""
    
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.patients: Dict[str, Patient] = {}
        self.load_data()

    def load_data(self):
        """Load patient data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for patient_data in data:
                    patient = Patient(**patient_data)
                    self.patients[patient.patient_id] = patient

    def save_data(self):
        """Save patient data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump([patient.to_dict() for patient in self.patients.values()], file, indent=4)

    def add_patient(self, patient_id: str, name: str, age: int, gender: str):
        """Add a new patient to the laboratory."""
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID {patient_id} already exists.")
        self.patients[patient_id] = Patient(patient_id, name, age, gender)
        self.save_data()

    def add_test_result(self, patient_id: str, test_name: str, result: str, date: str):
        """Add a test result for a specific patient."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        self.patients[patient_id].add_test_result(test_name, result, date)
        self.save_data()

    def get_patient_info(self, patient_id: str) -> Dict[str, Any]:
        """Retrieve patient information including test results."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID {patient_id} does not exist.")
        return self.patients[patient_id].to_dict()

def main():
    """Main function to demonstrate the laboratory management system."""
    lab = Laboratory('patients_data.json')

    # Example usage
    try:
        lab.add_patient('001', 'John Doe', 30, 'Male')
        lab.add_test_result('001', 'Blood Test', 'Normal', '2023-10-01')
        patient_info = lab.get_patient_info('001')
        print(json.dumps(patient_info, indent=4))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
