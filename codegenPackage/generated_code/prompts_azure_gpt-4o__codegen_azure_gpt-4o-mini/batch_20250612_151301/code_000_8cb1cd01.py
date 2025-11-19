"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write Python code to simulate a scheduling system for medical exams like colonoscopy, endoscopy, and elastography, including options for selecting dates, times, and specialties such as gastroenterology and hepatology.
Generated: DETERMINISTIC_8cb1cd011b51504b
Batch ID: 20250612_151301
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

class Appointment:
    """Class to represent a medical exam appointment."""
    
    def __init__(self, specialty: str, date: datetime.date, time: datetime.time):
        self.specialty = specialty
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.specialty} appointment on {self.date} at {self.time}"

class Scheduler:
    """Class to manage scheduling of medical exams."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.specialties: List[str] = ["Gastroenterology", "Hepatology"]
        self.available_times: List[datetime.time] = [
            datetime.time(hour=9, minute=0),
            datetime.time(hour=10, minute=0),
            datetime.time(hour=11, minute=0),
            datetime.time(hour=14, minute=0),
            datetime.time(hour=15, minute=0),
        ]

    def is_time_available(self, date: datetime.date, time: datetime.time) -> bool:
        """Check if the requested time is available on the given date."""
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                return False
        return True

    def schedule_appointment(self, specialty: str, date: datetime.date, time: datetime.time) -> Optional[Appointment]:
        """Schedule an appointment if the time is available."""
        if specialty not in self.specialties:
            raise ValueError(f"Specialty '{specialty}' is not available.")
        
        if not self.is_time_available(date, time):
            raise ValueError(f"Time {time} on {date} is already booked.")
        
        appointment = Appointment(specialty, date, time)
        self.appointments.append(appointment)
        return appointment

    def list_appointments(self) -> List[str]:
        """List all scheduled appointments."""
        return [str(appointment) for appointment in self.appointments]

def main():
    """Main function to run the scheduling system."""
    scheduler = Scheduler()
    
    # Example usage
    try:
        # Schedule a colonoscopy
        appointment1 = scheduler.schedule_appointment("Gastroenterology", datetime.date(2023, 10, 15), datetime.time(9, 0))
        print(f"Scheduled: {appointment1}")

        # Schedule an endoscopy
        appointment2 = scheduler.schedule_appointment("Hepatology", datetime.date(2023, 10, 15), datetime.time(10, 0))
        print(f"Scheduled: {appointment2}")

        # Attempt to schedule a conflicting appointment
        appointment3 = scheduler.schedule_appointment("Gastroenterology", datetime.date(2023, 10, 15), datetime.time(9, 0))
        print(f"Scheduled: {appointment3}")

    except ValueError as e:
        print(f"Error: {e}")

    # List all appointments
    print("\nAll Scheduled Appointments:")
    for appointment in scheduler.list_appointments():
        print(appointment)

if __name__ == "__main__":
    main()
```
