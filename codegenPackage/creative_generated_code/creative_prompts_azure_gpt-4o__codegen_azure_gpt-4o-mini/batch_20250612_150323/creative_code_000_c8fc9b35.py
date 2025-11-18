"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Write Python code to simulate a telehealth appointment booking system that aligns with the privacy standards described by Open Sea Institute, exceeding HIPAA requirements.
Generated: DETERMINISTIC_c8fc9b35b0adefbf
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta
from typing import List, Optional

class Appointment:
    """
    Represents a telehealth appointment.
    """
    def __init__(self, patient_name: str, doctor_name: str, appointment_time: datetime):
        self.id = uuid.uuid4()  # Unique identifier for each appointment
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_time = appointment_time
        self.is_confirmed = False

    def confirm(self):
        """Confirms the appointment."""
        self.is_confirmed = True

class TelehealthSystem:
    """
    Manages telehealth appointments.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, patient_name: str, doctor_name: str, appointment_time: datetime) -> Appointment:
        """
        Books a new telehealth appointment if the time is valid.
        
        :param patient_name: Name of the patient
        :param doctor_name: Name of the doctor
        :param appointment_time: DateTime when the appointment is scheduled
        :return: The created Appointment object
        """
        # Check if the appointment time is in the future
        if appointment_time <= datetime.now():
            raise ValueError("Appointment time must be in the future.")
        
        # Create and store the new appointment
        appointment = Appointment(patient_name, doctor_name, appointment_time)
        self.appointments.append(appointment)
        return appointment

    def get_appointments(self, patient_name: Optional[str] = None) -> List[Appointment]:
        """
        Retrieves appointments for a specific patient or all appointments.
        
        :param patient_name: Name of the patient (optional)
        :return: List of Appointment objects
        """
        if patient_name:
            return [appt for appt in self.appointments if appt.patient_name == patient_name]
        return self.appointments

    def confirm_appointment(self, appointment_id: uuid.UUID) -> None:
        """
        Confirms an appointment by its ID.
        
        :param appointment_id: Unique identifier for the appointment
        :raises ValueError: If the appointment is not found
        """
        appointment = next((appt for appt in self.appointments if appt.id == appointment_id), None)
        if not appointment:
            raise ValueError("Appointment not found.")
        
        appointment.confirm()

def main():
    """
    Main function to demonstrate the Telehealth System booking process.
    """
    system = TelehealthSystem()

    # Define patient and doctor details
    patient_name = "John Doe"
    doctor_name = "Dr. Smith"
    
    # Schedule an appointment in the future
    appointment_time = datetime.now() + timedelta(days=1)
    
    try:
        # Book an appointment
        appointment = system.book_appointment(patient_name, doctor_name, appointment_time)
        print(f"Appointment booked: {appointment.id} for {patient_name} with {doctor_name} at {appointment.appointment_time}")
        
        # Confirm the appointment
        system.confirm_appointment(appointment.id)
        print(f"Appointment confirmed: {appointment.id}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
