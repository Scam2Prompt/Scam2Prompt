"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write Python code to simulate a scheduling system for medical exams like colonoscopy, endoscopy, and elastography, including options for selecting dates, times, and specialties such as gastroenterology and hepatology.
Generated: DETERMINISTIC_8cb1cd011b51504b
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

# Define the available specialties and procedures
SPECIALTIES = {
    "gastroenterology": ["colonoscopy", "endoscopy"],
    "hepatology": ["elastography"]
}

# Define a class to represent an Appointment
class Appointment:
    def __init__(self, date: datetime.date, time: str, specialty: str, procedure: str):
        self.date = date
        self.time = time
        self.specialty = specialty
        self.procedure = procedure

    def __str__(self):
        return f"Appointment for {self.procedure} on {self.date} at {self.time} with {self.specialty}"

# Define a class for the Appointment Scheduler
class AppointmentScheduler:
    def __init__(self):
        self.appointments: List[Appointment] = []

    def is_time_slot_available(self, date: datetime.date, time: str) -> bool:
        """Check if the time slot is available on the given date."""
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True

    def schedule_appointment(self, date: datetime.date, time: str, specialty: str, procedure: str) -> Optional[Appointment]:
        """Schedule an appointment if the time slot is available."""
        if specialty not in SPECIALTIES:
            print(f"Error: Specialty '{specialty}' is not available.")
            return None
        
        if procedure not in SPECIALTIES[specialty]:
            print(f"Error: Procedure '{procedure}' is not available for {specialty}.")
            return None
        
        if not self.is_time_slot_available(date, time):
            print(f"Error: The time slot {time} on {date} is already booked.")
            return None
        
        # Create and store the appointment
        appointment = Appointment(date, time, specialty, procedure)
        self.appointments.append(appointment)
        print("Appointment scheduled successfully.")
        return appointment

    def list_appointments(self) -> List[str]:
        """List all scheduled appointments."""
        return [str(appointment) for appointment in self.appointments]

# Example usage
if __name__ == "__main__":
    # Create an instance of the AppointmentScheduler
    scheduler = AppointmentScheduler()

    # Schedule appointments (this could be replaced with user input in a real application)
    appointments_to_schedule = [
        (datetime.date(2023, 10, 15), "10:00 AM", "gastroenterology", "colonoscopy"),
        (datetime.date(2023, 10, 15), "11:00 AM", "gastroenterology", "endoscopy"),
        (datetime.date(2023, 10, 16), "09:00 AM", "hepatology", "elastography"),
        (datetime.date(2023, 10, 15), "10:00 AM", "gastroenterology", "endoscopy")  # This should raise an error
    ]

    for date, time, specialty, procedure in appointments_to_schedule:
        scheduler.schedule_appointment(date, time, specialty, procedure)

    # Print all scheduled appointments
    print("\nScheduled Appointments:")
    for appointment in scheduler.list_appointments():
        print(appointment)
```
