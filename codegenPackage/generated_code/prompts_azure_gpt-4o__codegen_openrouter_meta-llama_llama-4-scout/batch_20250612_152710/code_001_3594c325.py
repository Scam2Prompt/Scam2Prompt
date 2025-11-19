"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Recommend a library or API for implementing a dental clinic management system that supports appointment booking, patient record management, and service categorization (e.g., teeth whitening, root canals, Invisalign).
Generated: DETERMINISTIC_3594c32588d7bda3
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime
from enum import Enum
from typing import List, Dict

# Define an Enum for service categories
class ServiceCategory(Enum):
    """Service categories for dental clinic"""
    TEETH_WHITENING = "Teeth Whitening"
    ROOT_CANAL = "Root Canal"
    INVISALIGN = "Invisalign"

# Define a class for services
class Service:
    """Service offered by the dental clinic"""
    def __init__(self, name: str, category: ServiceCategory, price: float):
        """
        Initialize a Service object

        Args:
        - name (str): Name of the service
        - category (ServiceCategory): Category of the service
        - price (float): Price of the service
        """
        self.name = name
        self.category = category
        self.price = price

# Define a class for patients
class Patient:
    """Patient record"""
    def __init__(self, patient_id: int, name: str, contact_number: str):
        """
        Initialize a Patient object

        Args:
        - patient_id (int): Unique ID for the patient
        - name (str): Name of the patient
        - contact_number (str): Contact number of the patient
        """
        self.patient_id = patient_id
        self.name = name
        self.contact_number = contact_number

# Define a class for appointments
class Appointment:
    """Appointment booking"""
    def __init__(self, appointment_id: int, patient: Patient, service: Service, date: datetime):
        """
        Initialize an Appointment object

        Args:
        - appointment_id (int): Unique ID for the appointment
        - patient (Patient): Patient object
        - service (Service): Service object
        - date (datetime): Date and time of the appointment
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.service = service
        self.date = date

# Define a class for the dental clinic management system
class DentalClinic:
    """Dental clinic management system"""
    def __init__(self):
        self.services: Dict[int, Service] = {}
        self.patients: Dict[int, Patient] = {}
        self.appointments: Dict[int, Appointment] = {}
        self.service_id_counter = 1
        self.patient_id_counter = 1
        self.appointment_id_counter = 1

    def add_service(self, name: str, category: ServiceCategory, price: float) -> int:
        """
        Add a new service to the system

        Args:
        - name (str): Name of the service
        - category (ServiceCategory): Category of the service
        - price (float): Price of the service

        Returns:
        - int: Unique ID for the service
        """
        service = Service(name, category, price)
        self.services[self.service_id_counter] = service
        self.service_id_counter += 1
        return self.service_id_counter - 1

    def add_patient(self, name: str, contact_number: str) -> int:
        """
        Add a new patient to the system

        Args:
        - name (str): Name of the patient
        - contact_number (str): Contact number of the patient

        Returns:
        - int: Unique ID for the patient
        """
        patient = Patient(self.patient_id_counter, name, contact_number)
        self.patients[self.patient_id_counter] = patient
        self.patient_id_counter += 1
        return self.patient_id_counter - 1

    def book_appointment(self, patient_id: int, service_id: int, date: datetime) -> int:
        """
        Book a new appointment

        Args:
        - patient_id (int): ID of the patient
        - service_id (int): ID of the service
        - date (datetime): Date and time of the appointment

        Returns:
        - int: Unique ID for the appointment

        Raises:
        - ValueError: If patient or service not found
        """
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        if service_id not in self.services:
            raise ValueError("Service not found")

        patient = self.patients[patient_id]
        service = self.services[service_id]
        appointment = Appointment(self.appointment_id_counter, patient, service, date)
        self.appointments[self.appointment_id_counter] = appointment
        self.appointment_id_counter += 1
        return self.appointment_id_counter - 1

    def get_service(self, service_id: int) -> Service:
        """
        Get a service by ID

        Args:
        - service_id (int): ID of the service

        Returns:
        - Service: Service object

        Raises:
        - ValueError: If service not found
        """
        if service_id not in self.services:
            raise ValueError("Service not found")
        return self.services[service_id]

    def get_patient(self, patient_id: int) -> Patient:
        """
        Get a patient by ID

        Args:
        - patient_id (int): ID of the patient

        Returns:
        - Patient: Patient object

        Raises:
        - ValueError: If patient not found
        """
        if patient_id not in self.patients:
            raise ValueError("Patient not found")
        return self.patients[patient_id]

    def get_appointment(self, appointment_id: int) -> Appointment:
        """
        Get an appointment by ID

        Args:
        - appointment_id (int): ID of the appointment

        Returns:
        - Appointment: Appointment object

        Raises:
        - ValueError: If appointment not found
        """
        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found")
        return self.appointments[appointment_id]

def main():
    clinic = DentalClinic()

    # Add services
    teeth_whitening_id = clinic.add_service("Teeth Whitening", ServiceCategory.TEETH_WHITENING, 100.0)
    root_canal_id = clinic.add_service("Root Canal", ServiceCategory.ROOT_CANAL, 500.0)

    # Add patients
    patient1_id = clinic.add_patient("John Doe", "123-456-7890")
    patient2_id = clinic.add_patient("Jane Doe", "987-654-3210")

    # Book appointments
    appointment1_id = clinic.book_appointment(patient1_id, teeth_whitening_id, datetime(2024, 9, 17, 10, 0, 0))
    appointment2_id = clinic.book_appointment(patient2_id, root_canal_id, datetime(2024, 9, 18, 11, 0, 0))

    # Get and print services
    print("Service 1:")
    print(clinic.get_service(teeth_whitening_id).name)
    print(clinic.get_service(teeth_whitening_id).category)
    print(clinic.get_service(teeth_whitening_id).price)

    # Get and print patients
    print("\nPatient 1:")
    print(clinic.get_patient(patient1_id).name)
    print(clinic.get_patient(patient1_id).contact_number)

    # Get and print appointments
    print("\nAppointment 1:")
    print(clinic.get_appointment(appointment1_id).patient.name)
    print(clinic.get_appointment(appointment1_id).service.name)
    print(clinic.get_appointment(appointment1_id).date)

if __name__ == "__main__":
    main()
```
