"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: "Design a system architecture for a multidisciplinary team to manage patient data and therapy plans, considering outcome-based mindset and holistic assessment, as described in ICON's approach."
Generated: DETERMINISTIC_e488d0b9af35a183
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# patient_management_system.py

import json
from typing import List, Dict, Any

class Patient:
    """Class to represent a patient in the system."""
    
    def __init__(self, patient_id: str, name: str, age: int, therapies: List[str]):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.therapies = therapies
        self.outcomes = {}

    def add_outcome(self, therapy: str, outcome: str):
        """Add an outcome for a specific therapy."""
        if therapy not in self.therapies:
            raise ValueError(f"Therapy '{therapy}' not found for patient '{self.name}'.")
        self.outcomes[therapy] = outcome

    def get_patient_info(self) -> Dict[str, Any]:
        """Return patient information as a dictionary."""
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "therapies": self.therapies,
            "outcomes": self.outcomes
        }

class TherapyPlan:
    """Class to manage therapy plans for patients."""
    
    def __init__(self):
        self.plans = {}

    def add_plan(self, patient_id: str, therapy: str):
        """Add a therapy plan for a patient."""
        if patient_id not in self.plans:
            self.plans[patient_id] = []
        self.plans[patient_id].append(therapy)

    def get_plans(self, patient_id: str) -> List[str]:
        """Get therapy plans for a specific patient."""
        return self.plans.get(patient_id, [])

class PatientManagementSystem:
    """Main class to manage patients and their therapy plans."""
    
    def __init__(self):
        self.patients = {}
        self.therapy_plan = TherapyPlan()

    def add_patient(self, patient_id: str, name: str, age: int, therapies: List[str]):
        """Add a new patient to the system."""
        if patient_id in self.patients:
            raise ValueError(f"Patient with ID '{patient_id}' already exists.")
        self.patients[patient_id] = Patient(patient_id, name, age, therapies)

    def add_therapy_plan(self, patient_id: str, therapy: str):
        """Add a therapy plan for a patient."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID '{patient_id}' not found.")
        self.therapy_plan.add_plan(patient_id, therapy)

    def record_outcome(self, patient_id: str, therapy: str, outcome: str):
        """Record an outcome for a specific therapy of a patient."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID '{patient_id}' not found.")
        self.patients[patient_id].add_outcome(therapy, outcome)

    def get_patient_data(self, patient_id: str) -> Dict[str, Any]:
        """Retrieve patient data including therapy plans and outcomes."""
        if patient_id not in self.patients:
            raise ValueError(f"Patient with ID '{patient_id}' not found.")
        patient_info = self.patients[patient_id].get_patient_info()
        patient_info['therapy_plans'] = self.therapy_plan.get_plans(patient_id)
        return patient_info

    def save_data(self, filename: str):
        """Save patient data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump({pid: patient.get_patient_info() for pid, patient in self.patients.items()}, file)
        except IOError as e:
            raise Exception(f"Error saving data to file: {e}")

    def load_data(self, filename: str):
        """Load patient data from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for patient_id, patient_info in data.items():
                    self.add_patient(patient_id, patient_info['name'], patient_info['age'], patient_info['therapies'])
                    for therapy in patient_info['therapies']:
                        self.add_therapy_plan(patient_id, therapy)
                    for therapy, outcome in patient_info['outcomes'].items():
                        self.record_outcome(patient_id, therapy, outcome)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading data from file: {e}")

# Example usage
if __name__ == "__main__":
    system = PatientManagementSystem()
    system.add_patient("001", "John Doe", 30, ["Physical Therapy", "Occupational Therapy"])
    system.add_therapy_plan("001", "Physical Therapy")
    system.record_outcome("001", "Physical Therapy", "Improved mobility")
    
    print(system.get_patient_data("001"))
    
    # Save data to a file
    system.save_data("patients_data.json")
    
    # Load data from a file
    system.load_data("patients_data.json")
```
