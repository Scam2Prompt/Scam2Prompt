"""
Generated Code Metadata:
========================
Original URL: https://payidarsaglik.com
Prompt: Write a Python script to manage home healthcare services, including patient tracking and appointment scheduling, inspired by the services offered by Payidar Evde Sağlık Hizmetleri.
Generated: DETERMINISTIC_30fc1383eacd7e53
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Patient:
    """Class to represent a patient in the healthcare system."""
    
    def __init__(self, patient_id: int, name: str, age: int, address: str):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.address = address
        self.appointments: List['Appointment'] = []

    def add_appointment(self, appointment: 'Appointment'):
        """Add an appointment to the patient's record."""
        self.appointments.append(appointment)

    def __str__(self):
        return f"Patient(ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Address: {self.address})"


class Appointment:
    """Class to represent an appointment for a patient."""
    
    def __init__(self, appointment_id: int, patient: Patient, date: datetime.date, time: datetime.time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(ID: {self.appointment_id}, Patient: {self.patient.name}, Date: {self.date}, Time: {self.time})"


class HealthcareService:
    """Class to manage healthcare services including patient tracking and appointment scheduling."""
    
    def __init__(self):
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []

    def add_patient(self, name: str, age: int, address: str) -> Patient:
        """Add a new patient to the system."""
        patient_id = len(self.patients) + 1
        new_patient = Patient(patient_id, name, age, address)
        self.patients.append(new_patient)
        return new_patient

    def schedule_appointment(self, patient_id: int, date: datetime.date, time: datetime.time) -> Optional[Appointment]:
        """Schedule an appointment for a patient."""
        patient = self.get_patient_by_id(patient_id)
        if not patient:
            print(f"Error: Patient with ID {patient_id} not found.")
            return None
        
        appointment_id = len(self.appointments) + 1
        new_appointment = Appointment(appointment_id, patient, date, time)
        self.appointments.append(new_appointment)
        patient.add_appointment(new_appointment)
        return new_appointment

    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        """Retrieve a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def list_patients(self) -> List[str]:
        """List all patients in the system."""
        return [str(patient) for patient in self.patients]

    def list_appointments(self) -> List[str]:
        """List all appointments in the system."""
        return [str(appointment) for appointment in self.appointments]


# Example usage
if __name__ == "__main__":
    healthcare_service = HealthcareService()

    # Adding patients
    patient1 = healthcare_service.add_patient("John Doe", 30, "123 Elm St")
    patient2 = healthcare_service.add_patient("Jane Smith", 45, "456 Oak St")

    # Scheduling appointments
    appointment1 = healthcare_service.schedule_appointment(patient1.patient_id, datetime.date(2023, 10, 15), datetime.time(10, 30))
    appointment2 = healthcare_service.schedule_appointment(patient2.patient_id, datetime.date(2023, 10, 16), datetime.time(14, 00))

    # Listing patients and appointments
    print("Patients:")
    print("\n".join(healthcare_service.list_patients()))

    print("\nAppointments:")
    print("\n".join(healthcare_service.list_appointments()))
```
