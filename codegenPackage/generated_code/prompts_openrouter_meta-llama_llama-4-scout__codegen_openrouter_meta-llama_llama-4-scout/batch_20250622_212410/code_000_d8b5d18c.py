"""
Generated Code Metadata:
========================
Original URL: https://cliniquerobinpaul.com
Prompt: Write a Python script to manage appointment scheduling for a multidisciplinary clinic offering chiropractic care, osteopathy, and massage therapy.
Generated: DETERMINISTIC_d8b5d18c3fdb7e7e
Batch ID: 20250622_212410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

class ServiceType(Enum):
    """Enum for service types"""
    CHIROPRACTIC = "Chiropractic"
    OSTEOPATHY = "Osteopathy"
    MASSAGE_THERAPY = "Massage Therapy"

class Practitioner:
    """Class representing a practitioner"""
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.appointments = []

class Appointment:
    """Class representing an appointment"""
    def __init__(self, patient_name, service_type, practitioner, date_time):
        self.patient_name = patient_name
        self.service_type = service_type
        self.practitioner = practitioner
        self.date_time = date_time

class Clinic:
    """Class representing the clinic"""
    def __init__(self):
        self.practitioners = []

    def add_practitioner(self, practitioner):
        """Add a practitioner to the clinic"""
        self.practitioners.append(practitioner)

    def schedule_appointment(self, patient_name, service_type, practitioner_name, date_time):
        """Schedule an appointment"""
        practitioner = next((p for p in self.practitioners if p.name == practitioner_name), None)
        if practitioner is None:
            raise ValueError("Practitioner not found")

        if service_type not in [s.value for s in ServiceType]:
            raise ValueError("Invalid service type")

        if not self.is_available(practitioner, date_time):
            raise ValueError("Practitioner is not available at this time")

        appointment = Appointment(patient_name, service_type, practitioner, date_time)
        practitioner.appointments.append(appointment)
        return appointment

    def is_available(self, practitioner, date_time):
        """Check if a practitioner is available at a given time"""
        for appointment in practitioner.appointments:
            if appointment.date_time == date_time:
                return False
        return True

    def cancel_appointment(self, practitioner_name, date_time):
        """Cancel an appointment"""
        practitioner = next((p for p in self.practitioners if p.name == practitioner_name), None)
        if practitioner is None:
            raise ValueError("Practitioner not found")

        appointment = next((a for a in practitioner.appointments if a.date_time == date_time), None)
        if appointment is None:
            raise ValueError("Appointment not found")

        practitioner.appointments.remove(appointment)

    def print_schedule(self):
        """Print the schedule for all practitioners"""
        for practitioner in self.practitioners:
            print(f"Schedule for {practitioner.name} ({practitioner.specialty}):")
            for appointment in practitioner.appointments:
                print(f"  - {appointment.patient_name} ({appointment.service_type}) at {appointment.date_time}")

def main():
    clinic = Clinic()

    practitioner1 = Practitioner("John Doe", ServiceType.CHIROPRACTIC.value)
    practitioner2 = Practitioner("Jane Smith", ServiceType.OSTEOPATHY.value)

    clinic.add_practitioner(practitioner1)
    clinic.add_practitioner(practitioner2)

    try:
        appointment1 = clinic.schedule_appointment("Patient1", ServiceType.CHIROPRACTIC.value, "John Doe", datetime.now() + timedelta(days=1))
        appointment2 = clinic.schedule_appointment("Patient2", ServiceType.OSTEOPATHY.value, "Jane Smith", datetime.now() + timedelta(days=1))
        clinic.print_schedule()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
