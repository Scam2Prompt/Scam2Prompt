"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Design a workflow in Python for scheduling field technical assistance for machinery repairs, incorporating Track Diesel Peru's focus on on-site and workshop services.
Generated: DETERMINISTIC_3ecd2e8b18f31aa2
Batch ID: 20250612_151610
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

class Technician:
    """Represents a technician who provides field technical assistance."""

    def __init__(self, name: str, available_slots: List[datetime.datetime]):
        self.name = name
        self.available_slots = available_slots  # List of available datetime slots

    def is_available(self, appointment_time: datetime.datetime) -> bool:
        """Check if the technician is available at the specified time."""
        return appointment_time in self.available_slots


class Appointment:
    """Represents an appointment for machinery repair assistance."""

    def __init__(self, technician: Technician, time: datetime.datetime):
        self.technician = technician
        self.time = time

    def __str__(self):
        return f"Appointment with {self.technician.name} at {self.time}"


class Scheduler:
    """Scheduler for managing field technical assistance appointments."""

    def __init__(self):
        self.appointments: List[Appointment] = []

    def schedule_appointment(self, technician: Technician, appointment_time: datetime.datetime) -> Optional[Appointment]:
        """Schedule an appointment if the technician is available."""
        if technician.is_available(appointment_time):
            appointment = Appointment(technician, appointment_time)
            self.appointments.append(appointment)
            technician.available_slots.remove(appointment_time)  # Remove the slot from availability
            return appointment
        else:
            raise ValueError(f"Technician {technician.name} is not available at {appointment_time}")


def main():
    """Main function to demonstrate scheduling workflow."""
    # Define available time slots for the technician
    technician_slots = [datetime.datetime(2023, 10, 5, hour) for hour in range(9, 17)]  # 9 AM to 5 PM
    technician = Technician(name="John Doe", available_slots=technician_slots)

    # Create a scheduler
    scheduler = Scheduler()

    # Example appointment time
    try:
        appointment_time = datetime.datetime(2023, 10, 5, 10)  # 10 AM on October 5th
        appointment = scheduler.schedule_appointment(technician, appointment_time)
        print(appointment)
        
        # Attempt to schedule another appointment at the same time to test error handling
        another_appointment = scheduler.schedule_appointment(technician, appointment_time)
    
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
