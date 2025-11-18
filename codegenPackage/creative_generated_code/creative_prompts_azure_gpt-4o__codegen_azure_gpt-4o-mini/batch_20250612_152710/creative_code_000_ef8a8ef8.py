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
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class Appointment:
    def __init__(self, patient_name: str, date: datetime, service: str):
        self.patient_name = patient_name
        self.date = date
        self.service = service

    def __str__(self):
        return f"Appointment for {self.patient_name} on {self.date.strftime('%Y-%m-%d %H:%M')} for {self.service}"


class Clinic:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, patient_name: str, date: datetime, service: str) -> None:
        """Schedule an appointment if the slot is free."""
        if self.is_slot_available(date):
            appointment = Appointment(patient_name, date, service)
            self.appointments.append(appointment)
            print(f"Appointment scheduled: {appointment}")
        else:
            print("The selected time slot is not available.")

    def is_slot_available(self, date: datetime) -> bool:
        """Check if the appointment slot is available."""
        for appointment in self.appointments:
            if appointment.date == date:
                return False
        return True

    def get_appointments(self) -> List[str]:
        """Get a list of all scheduled appointments."""
        return [str(appointment) for appointment in self.appointments]


class DentalClinicSystem:
    def __init__(self):
        self.clinics: Dict[str, Clinic] = {}

    def add_clinic(self, name: str, location: str) -> None:
        """Add a new clinic to the system."""
        if name not in self.clinics:
            self.clinics[name] = Clinic(name, location)
            print(f"Clinic '{name}' added at location '{location}'.")
        else:
            print(f"Clinic '{name}' already exists.")

    def schedule_appointment(self, clinic_name: str, patient_name: str, date: datetime, service: str) -> None:
        """Schedule an appointment at a specific clinic."""
        clinic = self.clinics.get(clinic_name)
        if clinic:
            clinic.schedule_appointment(patient_name, date, service)
        else:
            print(f"Clinic '{clinic_name}' not found.")

    def get_clinic_appointments(self, clinic_name: str) -> Optional[List[str]]:
        """Retrieve appointments for a specific clinic."""
        clinic = self.clinics.get(clinic_name)
        if clinic:
            return clinic.get_appointments()
        else:
            print(f"Clinic '{clinic_name}' not found.")
            return None


# Example usage
if __name__ == "__main__":
    system = DentalClinicSystem()
    
    # Adding clinics
    system.add_clinic("Downtown Dental", "123 Main St")
    system.add_clinic("Uptown Dental", "456 Elm St")
    
    # Scheduling appointments
    appointment_date = datetime.now() + timedelta(days=1)
    system.schedule_appointment("Downtown Dental", "John Doe", appointment_date, "Pediatric Dentistry")
    
    # Attempting to schedule at the same time
    system.schedule_appointment("Downtown Dental", "Jane Smith", appointment_date, "Orthodontics")
    
    # Checking appointments
    appointments = system.get_clinic_appointments("Downtown Dental")
    if appointments:
        print("Scheduled Appointments at Downtown Dental:")
        for appt in appointments:
            print(appt)
```
