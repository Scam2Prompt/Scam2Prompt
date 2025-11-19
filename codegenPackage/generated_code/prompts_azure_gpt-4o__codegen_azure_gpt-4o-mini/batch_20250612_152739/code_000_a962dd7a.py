"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Write a Python script to create a booking system for integrative dental clinics like Jané Clinic, allowing patients to schedule personalized consultations based on availability.
Generated: DETERMINISTIC_a962dd7a163854aa
Batch ID: 20250612_152739
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
    """Class representing a dental appointment."""
    
    def __init__(self, patient_name: str, appointment_time: datetime.datetime):
        self.patient_name = patient_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(patient_name='{self.patient_name}', appointment_time='{self.appointment_time}')"


class DentalClinic:
    """Class representing a dental clinic with a booking system."""
    
    def __init__(self, name: str):
        self.name = name
        self.appointments: List[Appointment] = []
        self.schedule: List[datetime.datetime] = self.generate_schedule()

    def generate_schedule(self) -> List[datetime.datetime]:
        """Generate a schedule for the clinic for the next 30 days."""
        schedule = []
        today = datetime.datetime.now()
        for i in range(30):
            date = today + datetime.timedelta(days=i)
            for hour in range(9, 17):  # Clinic hours from 9 AM to 5 PM
                schedule.append(datetime.datetime(date.year, date.month, date.day, hour, 0))
        return schedule

    def book_appointment(self, patient_name: str, appointment_time: datetime.datetime) -> Optional[str]:
        """Book an appointment for a patient if the time is available."""
        if appointment_time not in self.schedule:
            return "Selected time is not available."
        
        if any(appointment.appointment_time == appointment_time for appointment in self.appointments):
            return "This time slot is already booked."

        self.appointments.append(Appointment(patient_name, appointment_time))
        return "Appointment booked successfully."

    def view_appointments(self) -> List[Appointment]:
        """Return a list of all booked appointments."""
        return self.appointments

    def cancel_appointment(self, patient_name: str, appointment_time: datetime.datetime) -> Optional[str]:
        """Cancel an existing appointment."""
        for appointment in self.appointments:
            if appointment.patient_name == patient_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return "Appointment canceled successfully."
        return "No matching appointment found."


def main():
    """Main function to run the booking system."""
    clinic = DentalClinic("Jané Clinic")
    
    # Example usage
    print(clinic.book_appointment("John Doe", datetime.datetime(2023, 10, 15, 10, 0)))  # Book an appointment
    print(clinic.view_appointments())  # View all appointments
    print(clinic.cancel_appointment("John Doe", datetime.datetime(2023, 10, 15, 10, 0)))  # Cancel the appointment
    print(clinic.view_appointments())  # View all appointments after cancellation


if __name__ == "__main__":
    main()
```
