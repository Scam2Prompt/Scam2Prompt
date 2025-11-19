"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Generate a code snippet for a dental appointment booking system that includes fields for patient name, contact information, and preferred appointment date, inspired by Buford Dental's online booking process.
Generated: DETERMINISTIC_854da5ff404e84ed
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Optional

class Appointment:
    """Class to represent a dental appointment."""
    
    def __init__(self, patient_name: str, contact_info: str, appointment_date: str):
        self.patient_name = patient_name
        self.contact_info = contact_info
        self.appointment_date = self.validate_date(appointment_date)

    @staticmethod
    def validate_date(date_str: str) -> datetime:
        """Validate and convert the appointment date from string to datetime object."""
        try:
            appointment_date = datetime.strptime(date_str, '%Y-%m-%d')
            if appointment_date < datetime.now():
                raise ValueError("Appointment date cannot be in the past.")
            return appointment_date
        except ValueError as e:
            raise ValueError(f"Invalid date format or value: {e}")

class AppointmentBookingSystem:
    """Class to manage the appointment booking system."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, patient_name: str, contact_info: str, appointment_date: str) -> None:
        """Book a new appointment and add it to the system."""
        try:
            new_appointment = Appointment(patient_name, contact_info, appointment_date)
            self.appointments.append(new_appointment)
            print(f"Appointment booked successfully for {patient_name} on {new_appointment.appointment_date.strftime('%Y-%m-%d')}.")
        except ValueError as e:
            print(f"Error booking appointment: {e}")

    def list_appointments(self) -> None:
        """List all booked appointments."""
        if not self.appointments:
            print("No appointments booked.")
            return
        
        print("Booked Appointments:")
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient_name}, Contact: {appointment.contact_info}, Date: {appointment.appointment_date.strftime('%Y-%m-%d')}")

# Example usage
if __name__ == "__main__":
    booking_system = AppointmentBookingSystem()
    
    # Booking appointments
    booking_system.book_appointment("John Doe", "john.doe@example.com", "2023-12-01")
    booking_system.book_appointment("Jane Smith", "jane.smith@example.com", "2023-11-15")
    
    # Listing all appointments
    booking_system.list_appointments()
```
