"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://heroesdental.com
Prompt: Write Python code to create an appointment scheduling system for a dental clinic with multiple locations, incorporating features like patient details, preferred dates, and services (e.g., pediatric dentistry, orthodontics, cosmetic dentistry).
Generated: DETERMINISTIC_ef8a8ef8906e5cc7
Batch ID: 20250612_152710
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


class Appointment:
    """
    Represents an individual appointment in the dental clinic.
    """
    def __init__(self, patient_name: str, patient_contact: str, location: str, 
                 service: str, preferred_date: datetime.date):
        self.patient_name = patient_name
        self.patient_contact = patient_contact
        self.location = location
        self.service = service
        self.preferred_date = preferred_date
        self.scheduled_date: Optional[datetime.date] = None
        self.status = "Pending"  # Status can be "Pending", "Confirmed", or "Completed"

    def confirm(self, scheduled_date: datetime.date):
        """
        Confirm the appointment with a specified scheduled date.
        """
        self.scheduled_date = scheduled_date
        self.status = "Confirmed"

    def complete(self):
        """
        Mark the appointment as completed.
        """
        if self.status != "Confirmed":
            raise ValueError("Appointment must be confirmed before marking as completed.")
        self.status = "Completed"


class DentalClinicScheduler:
    """
    Appointment scheduling system for a dental clinic with multiple locations and services.
    """
    def __init__(self):
        self.appointments: List[Appointment] = []

    def add_appointment(self, patient_name: str, patient_contact: str, 
                        location: str, service: str, preferred_date: datetime.date):
        """
        Add a new appointment to the system.
        """
        # Validate input
        if not patient_name or not patient_contact:
            raise ValueError("Patient name and contact information are required.")
        if location not in ["Location 1", "Location 2", "Location 3"]:
            raise ValueError("Invalid location. Choose from 'Location 1', 'Location 2', 'Location 3'.")
        if service not in ["Pediatric Dentistry", "Orthodontics", "Cosmetic Dentistry"]:
            raise ValueError("Invalid service. Choose from 'Pediatric Dentistry', 'Orthodontics', 'Cosmetic Dentistry'.")
        if preferred_date < datetime.date.today():
            raise ValueError("Preferred date cannot be in the past.")

        # Create and store the appointment
        appointment = Appointment(patient_name, patient_contact, location, service, preferred_date)
        self.appointments.append(appointment)

    def list_appointments(self):
        """
        List all appointments in the system.
        """
        if not self.appointments:
            return "No appointments scheduled."
        return [vars(app) for app in self.appointments]

    def find_appointment(self, patient_name: str) -> Optional[Appointment]:
        """
        Find an appointment by patient name.
        """
        for appointment in self.appointments:
            if appointment.patient_name == patient_name:
                return appointment
        return None

    def confirm_appointment(self, patient_name: str, scheduled_date: datetime.date):
        """
        Confirm an appointment by patient name with a scheduled date.
        """
        appointment = self.find_appointment(patient_name)
        if not appointment:
            raise ValueError("Appointment not found.")
        if scheduled_date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past.")
        appointment.confirm(scheduled_date)

    def mark_appointment_completed(self, patient_name: str):
        """
        Mark an appointment as completed by patient name.
        """
        appointment = self.find_appointment(patient_name)
        if not appointment:
            raise ValueError("Appointment not found.")
        appointment.complete()


# Example usage:
if __name__ == "__main__":
    scheduler = DentalClinicScheduler()

    # Add appointments
    try:
        scheduler.add_appointment("John Doe", "555-1234", "Location 1", "Orthodontics", datetime.date(2023, 11, 10))
        scheduler.add_appointment("Jane Smith", "555-5678", "Location 2", "Cosmetic Dentistry", datetime.date(2023, 11, 12))
    except ValueError as e:
        print(f"Error adding appointment: {e}")

    # Confirm an appointment
    try:
        scheduler.confirm_appointment("John Doe", datetime.date(2023, 11, 10))
    except ValueError as e:
        print(f"Error confirming appointment: {e}")

    # Mark an appointment as completed
    try:
        scheduler.mark_appointment_completed("John Doe")
    except ValueError as e:
        print(f"Error marking appointment completed: {e}")

    # List all appointments
    appointments = scheduler.list_appointments()
    print("Scheduled Appointments:")
    for app in appointments:
        print(app)
```
