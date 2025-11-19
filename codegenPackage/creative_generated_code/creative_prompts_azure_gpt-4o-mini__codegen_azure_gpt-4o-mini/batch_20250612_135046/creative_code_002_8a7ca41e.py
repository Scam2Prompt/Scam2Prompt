"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: How can I implement a scheduling system for executive coaching appointments that prioritizes privacy and flexibility for high-level clients?
Generated: DETERMINISTIC_8a7ca41e8a0fb00f
Batch ID: 20250612_135046
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

class Appointment:
    """Class to represent an appointment for executive coaching."""
    
    def __init__(self, client_name: str, appointment_time: datetime.datetime):
        self.client_name = client_name
        self.appointment_time = appointment_time

    def __repr__(self) -> str:
        return f"Appointment(client_name={self.client_name}, appointment_time={self.appointment_time})"

class Scheduler:
    """Class to manage scheduling of coaching appointments."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def add_appointment(self, client_name: str, appointment_time: datetime.datetime) -> None:
        """Add a new appointment if it does not conflict with existing ones."""
        if self.is_time_conflicted(appointment_time):
            raise ValueError("Appointment time is already booked.")
        self.appointments.append(Appointment(client_name, appointment_time))

    def is_time_conflicted(self, appointment_time: datetime.datetime) -> bool:
        """Check if the given appointment time conflicts with existing appointments."""
        return any(appt.appointment_time == appointment_time for appt in self.appointments)

    def get_appointments(self, client_name: Optional[str] = None) -> List[Dict[str, datetime.datetime]]:
        """Retrieve all appointments, optionally filtered by client name."""
        if client_name:
            return [{"client_name": appt.client_name, "appointment_time": appt.appointment_time} 
                    for appt in self.appointments if appt.client_name == client_name]
        return [{"client_name": appt.client_name, "appointment_time": appt.appointment_time} 
                for appt in self.appointments]

    def cancel_appointment(self, client_name: str, appointment_time: datetime.datetime) -> None:
        """Cancel an existing appointment."""
        appointment_to_cancel = next((appt for appt in self.appointments 
                                        if appt.client_name == client_name 
                                        and appt.appointment_time == appointment_time), None)
        if appointment_to_cancel:
            self.appointments.remove(appointment_to_cancel)
        else:
            raise ValueError("Appointment not found.")

# Example usage of the Scheduler class
if __name__ == "__main__":
    scheduler = Scheduler()
    
    try:
        # Adding appointments
        scheduler.add_appointment("Alice Johnson", datetime.datetime(2023, 10, 24, 10, 0))
        scheduler.add_appointment("Bob Smith", datetime.datetime(2023, 10, 24, 11, 0))

        # Retrieve all appointments
        print(scheduler.get_appointments())

        # Cancel an appointment
        scheduler.cancel_appointment("Alice Johnson", datetime.datetime(2023, 10, 24, 10, 0))

        # Retrieve appointments for a specific client
        print(scheduler.get_appointments("Bob Smith"))

    except ValueError as e:
        print(f"Error: {e}")
```
