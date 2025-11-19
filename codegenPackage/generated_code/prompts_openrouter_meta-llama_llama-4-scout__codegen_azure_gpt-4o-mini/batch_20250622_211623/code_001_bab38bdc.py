"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Generate a code snippet for a simple booking system for a psychology clinic like Back On Track Psychology that offers services in multiple languages.
Generated: DETERMINISTIC_bab38bdc907af176
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Appointment:
    """Class representing a single appointment."""
    
    def __init__(self, client_name: str, appointment_time: datetime, language: str):
        self.client_name = client_name
        self.appointment_time = appointment_time
        self.language = language

    def __repr__(self):
        return f"Appointment(client_name={self.client_name}, appointment_time={self.appointment_time}, language={self.language})"


class BookingSystem:
    """Class to manage the booking system for the psychology clinic."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, client_name: str, appointment_time: datetime, language: str) -> str:
        """Books an appointment if the time slot is available."""
        if self.is_time_slot_available(appointment_time):
            new_appointment = Appointment(client_name, appointment_time, language)
            self.appointments.append(new_appointment)
            return f"Appointment booked for {client_name} on {appointment_time} in {language}."
        else:
            return "Error: Time slot is not available."

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Checks if the requested time slot is available."""
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def list_appointments(self) -> List[Dict[str, str]]:
        """Returns a list of all booked appointments."""
        return [{"client_name": appt.client_name, "appointment_time": appt.appointment_time.strftime("%Y-%m-%d %H:%M"), "language": appt.language} for appt in self.appointments]

    def cancel_appointment(self, client_name: str, appointment_time: datetime) -> str:
        """Cancels an existing appointment."""
        for appointment in self.appointments:
            if appointment.client_name == client_name and appointment.appointment_time == appointment_time:
                self.appointments.remove(appointment)
                return f"Appointment for {client_name} on {appointment_time} has been canceled."
        return "Error: Appointment not found."


# Example usage
if __name__ == "__main__":
    booking_system = BookingSystem()
    
    # Book an appointment
    print(booking_system.book_appointment("John Doe", datetime(2023, 10, 15, 10, 0), "English"))
    
    # List appointments
    print(booking_system.list_appointments())
    
    # Cancel an appointment
    print(booking_system.cancel_appointment("John Doe", datetime(2023, 10, 15, 10, 0)))
    
    # Attempt to cancel a non-existing appointment
    print(booking_system.cancel_appointment("John Doe", datetime(2023, 10, 15, 11, 0)))
```
