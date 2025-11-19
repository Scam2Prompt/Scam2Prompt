"""
Generated Code Metadata:
========================
Original URL: https://virasmile.it
Prompt: Generate a code snippet for a dental clinic management system that includes features for booking appointments and managing patient records, similar to the services offered by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_dcb88735f40d7b73
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# dental_clinic_management.py

from datetime import datetime, timedelta
from typing import List, Optional

class Patient:
    """Class to represent a patient in the dental clinic."""
    
    def __init__(self, patient_id: int, name: str, contact: str):
        self.patient_id = patient_id
        self.name = name
        self.contact = contact
        self.records = []  # List to store patient records

    def add_record(self, record: str):
        """Add a medical record for the patient."""
        self.records.append(record)

    def get_records(self) -> List[str]:
        """Retrieve all medical records for the patient."""
        return self.records


class Appointment:
    """Class to represent an appointment in the dental clinic."""
    
    def __init__(self, appointment_id: int, patient: Patient, date_time: datetime):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date_time = date_time

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Date & Time: {self.date_time}"


class DentalClinic:
    """Class to manage the dental clinic operations."""
    
    def __init__(self):
        self.patients: List[Patient] = []  # List to store patients
        self.appointments: List[Appointment] = []  # List to store appointments
        self.next_patient_id = 1
        self.next_appointment_id = 1

    def add_patient(self, name: str, contact: str) -> Patient:
        """Add a new patient to the clinic."""
        patient = Patient(self.next_patient_id, name, contact)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def book_appointment(self, patient_id: int, date_time: datetime) -> Optional[Appointment]:
        """Book an appointment for a patient."""
        patient = self.find_patient(patient_id)
        if not patient:
            print(f"Error: Patient with ID {patient_id} not found.")
            return None
        
        appointment = Appointment(self.next_appointment_id, patient, date_time)
        self.appointments.append(appointment)
        self.next_appointment_id += 1
        return appointment

    def find_patient(self, patient_id: int) -> Optional[Patient]:
        """Find a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

    def get_appointments(self) -> List[Appointment]:
        """Retrieve all appointments."""
        return self.appointments


# Example usage
if __name__ == "__main__":
    clinic = DentalClinic()
    
    # Adding patients
    patient1 = clinic.add_patient("John Doe", "123-456-7890")
    patient2 = clinic.add_patient("Jane Smith", "098-765-4321")
    
    # Booking appointments
    appointment1 = clinic.book_appointment(patient1.patient_id, datetime.now() + timedelta(days=1))
    appointment2 = clinic.book_appointment(patient2.patient_id, datetime.now() + timedelta(days=2))
    
    # Displaying appointments
    for appointment in clinic.get_appointments():
        print(appointment)
```
