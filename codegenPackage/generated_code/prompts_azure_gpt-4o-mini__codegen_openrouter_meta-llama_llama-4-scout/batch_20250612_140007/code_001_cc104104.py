"""
Generated Code Metadata:
========================
Original URL: https://idetgroup.com
Prompt: Write a code snippet that integrates a health management system with a medical service provider, focusing on features like home healthcare and occupational medicine as described by IDET.
Generated: DETERMINISTIC_cc104104970881a5
Batch ID: 20250612_140007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_management_system.py

from datetime import datetime
from typing import Dict, List

class Patient:
    """Represents a patient in the health management system."""

    def __init__(self, patient_id: int, name: str, date_of_birth: str):
        """
        Initializes a Patient object.

        Args:
        - patient_id (int): Unique identifier for the patient.
        - name (str): Patient's name.
        - date_of_birth (str): Patient's date of birth in YYYY-MM-DD format.
        """
        self.patient_id = patient_id
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def __str__(self):
        return f"Patient {self.patient_id}: {self.name}, born {self.date_of_birth.date()}"


class MedicalServiceProvider:
    """Represents a medical service provider."""

    def __init__(self, provider_id: int, name: str):
        """
        Initializes a MedicalServiceProvider object.

        Args:
        - provider_id (int): Unique identifier for the provider.
        - name (str): Provider's name.
        """
        self.provider_id = provider_id
        self.name = name
        self.services = []

    def add_service(self, service: str):
        """Adds a service offered by the provider."""
        self.services.append(service)

    def __str__(self):
        return f"Provider {self.provider_id}: {self.name}"


class HealthManagementSystem:
    """Represents a health management system."""

    def __init__(self):
        self.patients: Dict[int, Patient] = {}
        self.providers: Dict[int, MedicalServiceProvider] = {}

    def add_patient(self, patient: Patient):
        """Adds a patient to the system."""
        self.patients[patient.patient_id] = patient

    def add_provider(self, provider: MedicalServiceProvider):
        """Adds a provider to the system."""
        self.providers[provider.provider_id] = provider

    def assign_service(self, patient_id: int, provider_id: int, service: str):
        """
        Assigns a service to a patient from a provider.

        Args:
        - patient_id (int): ID of the patient.
        - provider_id (int): ID of the provider.
        - service (str): Service to be assigned.

        Raises:
        - ValueError: If patient or provider not found.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if provider_id not in self.providers:
            raise ValueError("Provider not found")

        self.providers[provider_id].add_service(service)

    def __str__(self):
        patients_str = "\n".join([str(patient) for patient in self.patients.values()])
        providers_str = "\n".join([str(provider) for provider in self.providers.values()])
        return f"Patients:\n{patients_str}\n\nProviders:\n{providers_str}"


class HomeHealthcare:
    """Represents home healthcare services."""

    def __init__(self, patient: Patient, provider: MedicalServiceProvider):
        self.patient = patient
        self.provider = provider

    def provide_care(self):
        """Provides home healthcare services."""
        print(f"Providing home healthcare to {self.patient.name} by {self.provider.name}")


class OccupationalMedicine:
    """Represents occupational medicine services."""

    def __init__(self, patient: Patient, provider: MedicalServiceProvider):
        self.patient = patient
        self.provider = provider

    def provide_service(self):
        """Provides occupational medicine services."""
        print(f"Providing occupational medicine to {self.patient.name} by {self.provider.name}")


def main():
    # Create a health management system
    hms = HealthManagementSystem()

    # Create patients
    patient1 = Patient(1, "John Doe", "1990-01-01")
    patient2 = Patient(2, "Jane Doe", "1995-06-01")

    # Add patients to the system
    hms.add_patient(patient1)
    hms.add_patient(patient2)

    # Create providers
    provider1 = MedicalServiceProvider(1, "Provider1")
    provider2 = MedicalServiceProvider(2, "Provider2")

    # Add providers to the system
    hms.add_provider(provider1)
    hms.add_provider(provider2)

    # Assign services
    hms.assign_service(1, 1, "Home Healthcare")
    hms.assign_service(2, 2, "Occupational Medicine")

    # Create home healthcare and occupational medicine services
    home_healthcare = HomeHealthcare(patient1, provider1)
    occupational_medicine = OccupationalMedicine(patient2, provider2)

    # Provide services
    home_healthcare.provide_care()
    occupational_medicine.provide_service()

    # Print health management system information
    print("\nHealth Management System:")
    print(hms)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
