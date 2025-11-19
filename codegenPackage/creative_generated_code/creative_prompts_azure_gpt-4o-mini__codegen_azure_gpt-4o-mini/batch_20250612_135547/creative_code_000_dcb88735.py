"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virasmile.it
Prompt: Generate a code snippet for a dental clinic management system that includes features for booking appointments and managing patient records, similar to the services offered by Studio Dentistico dott.ssa Vira Palazzo.
Generated: DETERMINISTIC_dcb88735f40d7b73
Batch ID: 20250612_135547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Patient:
    """Class to represent a patient."""
    
    def __init__(self, patient_id: int, name: str, email: str, phone: str):
        self.patient_id = patient_id
        self.name = name
        self.email = email
        self.phone = phone

class Appointment:
    """Class to represent a dental appointment."""
    
    def __init__(self, appointment_id: int, patient: Patient, date: datetime.datetime, notes: Optional[str] = None):
        self.appointment_id = appointment_id
        self.patient = patient
        self.date = date
        self.notes = notes

class DentalClinic:
    """Class to manage a dental clinic's operations, focusing on patient records and appointments."""
    
    def __init__(self):
        self.patients: List[Patient] = []
        self.appointments: List[Appointment] = []
    
    def add_patient(self, name: str, email: str, phone: str) -> Patient:
        """Add a new patient to the clinic."""
        new_patient_id = len(self.patients) + 1
        new_patient = Patient(new_patient_id, name, email, phone)
        self.patients.append(new_patient)
        return new_patient
    
    def book_appointment(self, patient_id: int, appointment_date: str, notes: Optional[str] = None) -> Optional[Appointment]:
        """Book a new appointment for a patient."""
        # Convert string date to datetime object
        try:
            appointment_date_time = datetime.datetime.strptime(appointment_date, "%Y-%m-%d %H:%M")
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None
        
        patient = self.get_patient_by_id(patient_id)
        if not patient:
            print(f"Patient with ID {patient_id} not found.")
            return None

        new_appointment_id = len(self.appointments) + 1
        new_appointment = Appointment(new_appointment_id, patient, appointment_date_time, notes)
        self.appointments.append(new_appointment)
        return new_appointment

    def get_patient_by_id(self, patient_id: int) -> Optional[Patient]:
        """Retrieve a patient by their ID."""
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None
    
    def list_appointments(self) -> List[Appointment]:
        """List all scheduled appointments."""
        return self.appointments

# Example usage
if __name__ == "__main__":
    clinic = DentalClinic()
    # Adding a patient
    patient = clinic.add_patient("John Doe", "john@example.com", "1234567890")
    
    # Booking an appointment
    appointment = clinic.book_appointment(patient.patient_id, "2023-10-15 14:30", "Routine checkup")
    
    # Listing all appointments
    appointments = clinic.list_appointments()
    for appt in appointments:
        print(f"Appointment ID: {appt.appointment_id}, Patient: {appt.patient.name}, Date: {appt.date}, Notes: {appt.notes}")
```
