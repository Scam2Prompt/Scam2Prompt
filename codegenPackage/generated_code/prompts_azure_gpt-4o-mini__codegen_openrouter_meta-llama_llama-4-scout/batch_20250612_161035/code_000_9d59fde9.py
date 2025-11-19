"""
Generated Code Metadata:
========================
Original URL: https://sus.weebly.com
Prompt: Explain how to implement a health monitoring system using the principles of the Sistema Único de Saúde (SUS) for community health management.
Generated: DETERMINISTIC_9d59fde9fc028ec4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_monitoring_system.py

from datetime import datetime
from typing import Dict, List

class Patient:
    """Represents a patient in the health monitoring system."""

    def __init__(self, patient_id: int, name: str, age: int, address: str):
        """
        Initializes a Patient object.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - age (int): Patient's age.
        - address (str): Patient's address.
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.address = address
        self.health_data = []

    def add_health_data(self, data: Dict):
        """Adds health data for the patient."""
        self.health_data.append(data)


class HealthMonitoringSystem:
    """Manages patient data and provides health monitoring functionality."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient: Patient):
        """Adds a patient to the system."""
        self.patients[patient.patient_id] = patient

    def get_patient(self, patient_id: int) -> Patient:
        """
        Retrieves a patient by their ID.

        Args:
        - patient_id (int): Unique identifier for the patient.

        Returns:
        - Patient: The patient object if found, otherwise None.
        """
        return self.patients.get(patient_id)

    def update_patient_health_data(self, patient_id: int, data: Dict):
        """
        Updates a patient's health data.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - data (Dict): Health data to be added.

        Raises:
        - ValueError: If the patient is not found.
        """
        patient = self.get_patient(patient_id)
        if patient:
            patient.add_health_data(data)
        else:
            raise ValueError("Patient not found")

    def get_patient_health_data(self, patient_id: int) -> List[Dict]:
        """
        Retrieves a patient's health data.

        Args:
        - patient_id (int): Unique identifier for the patient.

        Returns:
        - List[Dict]: A list of health data dictionaries.

        Raises:
        - ValueError: If the patient is not found.
        """
        patient = self.get_patient(patient_id)
        if patient:
            return patient.health_data
        else:
            raise ValueError("Patient not found")


class SUSHealthMonitoringSystem(HealthMonitoringSystem):
    """Implements the SUS health monitoring system."""

    def __init__(self):
        super().__init__()
        self.health_units = {}

    def add_health_unit(self, unit_id: int, name: str, address: str):
        """
        Adds a health unit to the system.

        Args:
        - unit_id (int): Unique identifier for the health unit.
        - name (str): Health unit's name.
        - address (str): Health unit's address.
        """
        self.health_units[unit_id] = {"name": name, "address": address}

    def get_health_unit(self, unit_id: int) -> Dict:
        """
        Retrieves a health unit by its ID.

        Args:
        - unit_id (int): Unique identifier for the health unit.

        Returns:
        - Dict: The health unit data if found, otherwise None.
        """
        return self.health_units.get(unit_id)


def main():
    # Create a SUS health monitoring system
    sus_system = SUSHealthMonitoringSystem()

    # Add health units
    sus_system.add_health_unit(1, "Health Unit 1", "Rua Exemplo, 123")
    sus_system.add_health_unit(2, "Health Unit 2", "Avenida Exemplo, 456")

    # Create patients
    patient1 = Patient(1, "John Doe", 30, "Rua Exemplo, 123")
    patient2 = Patient(2, "Jane Doe", 25, "Avenida Exemplo, 456")

    # Add patients to the system
    sus_system.add_patient(patient1)
    sus_system.add_patient(patient2)

    # Add health data for patients
    patient1_data = {"date": datetime.now().strftime("%Y-%m-%d"), "blood_pressure": 120, "heart_rate": 80}
    patient2_data = {"date": datetime.now().strftime("%Y-%m-%d"), "blood_pressure": 110, "heart_rate": 90}

    sus_system.update_patient_health_data(1, patient1_data)
    sus_system.update_patient_health_data(2, patient2_data)

    # Retrieve patient health data
    patient1_health_data = sus_system.get_patient_health_data(1)
    patient2_health_data = sus_system.get_patient_health_data(2)

    print("Patient 1 Health Data:")
    for data in patient1_health_data:
        print(data)

    print("\nPatient 2 Health Data:")
    for data in patient2_health_data:
        print(data)


if __name__ == "__main__":
    main()
```
