"""
Generated Code Metadata:
========================
Original URL: https://drcelsolemos.com.br
Prompt: Write a Python script to manage dental clinic appointments, including scheduling and payment processing, inspired by Dr. Celso Lemos' clinic.
Generated: DETERMINISTIC_4e3cafdfa22faed7
Batch ID: 20250622_210655
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

class Appointment:
    """Class to represent a dental appointment."""
    
    def __init__(self, patient_name: str, appointment_time: datetime.datetime, treatment: str):
        self.patient_name = patient_name
        self.appointment_time = appointment_time
        self.treatment = treatment
        self.paid = False

    def mark_as_paid(self):
        """Mark the appointment as paid."""
        self.paid = True

    def __str__(self):
        return f"Appointment for {self.patient_name} on {self.appointment_time} for {self.treatment}. Paid: {self.paid}"


class Clinic:
    """Class to manage dental clinic appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, appointment_time: datetime.datetime, treatment: str) -> None:
        """Schedule a new appointment."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(patient_name, appointment_time, treatment)
            self.appointments.append(new_appointment)
            print(f"Appointment scheduled: {new_appointment}")
        else:
            print(f"Error: Time slot {appointment_time} is already booked.")

    def is_time_slot_available(self, appointment_time: datetime.datetime) -> bool:
        """Check if the given time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def process_payment(self, patient_name: str, appointment_time: datetime.datetime) -> None:
        """Process payment for a specific appointment."""
        appointment = self.find_appointment(patient_name, appointment_time)
        if appointment:
            appointment.mark_as_paid()
            print(f"Payment processed for {patient_name} on {appointment_time}.")
        else:
            print(f"Error: No appointment found for {patient_name} on {appointment_time}.")

    def find_appointment(self, patient_name: str, appointment_time: datetime.datetime) -> Optional[Appointment]:
        """Find an appointment by patient name and time."""
        for appointment in self.appointments:
            if appointment.patient_name == patient_name and appointment.appointment_time == appointment_time:
                return appointment
        return None

    def list_appointments(self) -> None:
        """List all scheduled appointments."""
        if not self.appointments:
            print("No appointments scheduled.")
        for appointment in self.appointments:
            print(appointment)


# Example usage
if __name__ == "__main__":
    clinic = Clinic()
    
    # Schedule appointments
    clinic.schedule_appointment("John Doe", datetime.datetime(2023, 10, 15, 10, 0), "Teeth Cleaning")
    clinic.schedule_appointment("Jane Smith", datetime.datetime(2023, 10, 15, 11, 0), "Cavity Filling")
    
    # List appointments
    clinic.list_appointments()
    
    # Process payment
    clinic.process_payment("John Doe", datetime.datetime(2023, 10, 15, 10, 0))
    
    # List appointments again to see payment status
    clinic.list_appointments()
```
