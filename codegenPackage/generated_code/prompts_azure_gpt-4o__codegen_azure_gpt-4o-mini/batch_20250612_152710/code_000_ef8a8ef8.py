"""
Generated Code Metadata:
========================
Original URL: https://heroesdental.com
Prompt: Write Python code to create an appointment scheduling system for a dental clinic with multiple locations, incorporating features like patient details, preferred dates, and services (e.g., pediatric dentistry, orthodontics, cosmetic dentistry).
Generated: DETERMINISTIC_ef8a8ef8906e5cc7
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Patient:
    """Class to represent a patient in the dental clinic."""
    
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def __repr__(self):
        return f"Patient(name={self.name}, contact={self.contact})"


class Appointment:
    """Class to represent an appointment in the dental clinic."""
    
    def __init__(self, patient: Patient, date: datetime.date, service: str, location: str):
        self.patient = patient
        self.date = date
        self.service = service
        self.location = location

    def __repr__(self):
        return (f"Appointment(patient={self.patient}, date={self.date}, "
                f"service={self.service}, location={self.location})")


class DentalClinic:
    """Class to manage appointments in a dental clinic."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.locations: List[str] = ["Downtown", "Uptown", "Suburb"]

    def schedule_appointment(self, patient: Patient, date: datetime.date, 
                             service: str, location: str) -> Optional[str]:
        """Schedules an appointment for a patient."""
        if location not in self.locations:
            return "Error: Invalid location."
        
        if not self.is_date_available(date, location):
            return "Error: Date is not available."

        appointment = Appointment(patient, date, service, location)
        self.appointments.append(appointment)
        return f"Appointment scheduled: {appointment}"

    def is_date_available(self, date: datetime.date, location: str) -> bool:
        """Checks if the date is available for the specified location."""
        for appointment in self.appointments:
            if appointment.date == date and appointment.location == location:
                return False
        return True

    def get_appointments(self) -> List[Appointment]:
        """Returns a list of all scheduled appointments."""
        return self.appointments


def main():
    """Main function to run the appointment scheduling system."""
    clinic = DentalClinic()

    # Example patient details
    patient1 = Patient(name="John Doe", contact="555-1234")
    patient2 = Patient(name="Jane Smith", contact="555-5678")

    # Schedule appointments
    print(clinic.schedule_appointment(patient1, datetime.date(2023, 10, 15), 
                                       "Orthodontics", "Downtown"))
    print(clinic.schedule_appointment(patient2, datetime.date(2023, 10, 15), 
                                       "Pediatric Dentistry", "Uptown"))
    print(clinic.schedule_appointment(patient1, datetime.date(2023, 10, 15), 
                                       "Cosmetic Dentistry", "Downtown"))  # Should return error

    # List all appointments
    print("All Appointments:")
    for appointment in clinic.get_appointments():
        print(appointment)


if __name__ == "__main__":
    main()
```
