"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebenezerbandeira.com.br
Prompt: How can I implement the practical aspects of the APS CUT course in a healthcare application?
Generated: DETERMINISTIC_c8576db6d5865901
Batch ID: 20250612_162854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

# Define a class to represent a patient
class Patient:
    def __init__(self, patient_id: int, name: str, age: int, health_conditions: List[str]):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.health_conditions = health_conditions

    def __repr__(self):
        return f"Patient({self.patient_id}, {self.name}, {self.age}, {self.health_conditions})"

# Define a class to handle patient records and healthcare operations
class HealthcareSystem:
    def __init__(self):
        self.patients: Dict[int, Patient] = {}

    def add_patient(self, name: str, age: int, health_conditions: List[str]) -> Patient:
        """Add a new patient to the healthcare system."""
        patient_id = self._generate_patient_id()
        new_patient = Patient(patient_id, name, age, health_conditions)
        self.patients[patient_id] = new_patient
        return new_patient

    def _generate_patient_id(self) -> int:
        """Generate a unique patient ID."""
        while True:
            patient_id = random.randint(1000, 9999)
            if patient_id not in self.patients:
                return patient_id

    def get_patient(self, patient_id: int) -> Patient:
        """Retrieve a patient's record by their ID."""
        patient = self.patients.get(patient_id)
        if not patient:
            raise ValueError(f"Patient with ID {patient_id} not found.")
        return patient

    def update_patient_health_conditions(self, patient_id: int, health_conditions: List[str]) -> None:
        """Update a patient's health conditions."""
        patient = self.get_patient(patient_id)
        patient.health_conditions = health_conditions

    def list_patients(self) -> List[Patient]:
        """List all patients in the system."""
        return list(self.patients.values())

# Example usage
if __name__ == "__main__":
    healthcare_system = HealthcareSystem()

    # Adding patients
    try:
        patient1 = healthcare_system.add_patient("Alice Smith", 30, ["Diabetes"])
        patient2 = healthcare_system.add_patient("Bob Johnson", 45, ["Hypertension", "Asthma"])

        print("Patients added:")
        print(healthcare_system.list_patients())

        # Retrieving a patient
        retrieved_patient = healthcare_system.get_patient(patient1.patient_id)
        print(f"Retrieved patient: {retrieved_patient}")

        # Updating health conditions
        healthcare_system.update_patient_health_conditions(patient1.patient_id, ["Diabetes", "High Cholesterol"])
        print(f"Updated patient: {healthcare_system.get_patient(patient1.patient_id)}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
