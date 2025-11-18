"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Write Python code to simulate scheduling appointments for mobile mammography services, ensuring the system checks patient eligibility based on age and absence of breast issues.
Generated: DETERMINISTIC_80f66a1aaaa9017e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import re

class Patient:
    def __init__(self, name: str, age: int, has_breast_issues: bool):
        self.name = name
        self.age = age
        self.has_breast_issues = has_breast_issues

    def is_eligible(self) -> bool:
        """Check if the patient is eligible for a mammography appointment."""
        return self.age >= 40 and not self.has_breast_issues


class Appointment:
    def __init__(self, patient: Patient, date: datetime):
        self.patient = patient
        self.date = date

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.date.strftime('%Y-%m-%d %H:%M')}"


class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, patient: Patient, date: datetime) -> str:
        """Schedule an appointment if the patient is eligible."""
        try:
            if not patient.is_eligible():
                return f"Patient {patient.name} is not eligible for a mammography appointment."

            if self.is_time_slot_filled(date):
                return f"Time slot on {date.strftime('%Y-%m-%d %H:%M')} is already filled."

            appointment = Appointment(patient, date)
            self.appointments.append(appointment)
            return str(appointment)

        except Exception as e:
            return f"An error occurred while scheduling: {str(e)}"

    def is_time_slot_filled(self, date: datetime) -> bool:
        """Check if the requested time slot is already filled."""
        return any(appointment.date == date for appointment in self.appointments)

    def list_appointments(self) -> str:
        """List all scheduled appointments."""
        if not self.appointments:
            return "No appointments scheduled."

        return "\n".join(str(appointment) for appointment in self.appointments)


def main():
    # Sample patient data
    patients = [
        Patient("Alice", 45, False),
        Patient("Bob", 38, False),
        Patient("Carol", 50, True),
        Patient("Dave", 42, False),
    ]
    
    # Instantiate the scheduler
    scheduler = AppointmentScheduler()

    # Schedule appointments
    for patient in patients:
        appointment_date = datetime.now() + timedelta(days=len(scheduler.appointments))  # Staggered scheduling
        result = scheduler.schedule_appointment(patient, appointment_date)
        print(result)

    # List all scheduled appointments
    print("\nScheduled Appointments:")
    print(scheduler.list_appointments())


if __name__ == "__main__":
    main()
```
