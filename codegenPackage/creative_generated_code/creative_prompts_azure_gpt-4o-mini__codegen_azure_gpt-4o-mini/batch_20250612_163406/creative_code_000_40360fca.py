"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Generate a code snippet for a booking system that allows users to schedule appointments at an art makeup salon in Ginza, Tokyo, similar to M luce's reservation system.
Generated: DETERMINISTIC_40360fca1cc83a8e
Batch ID: 20250612_163406
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
    """Class to represent a single appointment."""

    def __init__(self, customer_name: str, appointment_time: datetime):
        self.customer_name = customer_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment({self.customer_name}, {self.appointment_time})"


class Salon:
    """Class to manage the booking system for an art makeup salon."""

    def __init__(self):
        self.appointments: List[Appointment] = []

    def book_appointment(self, customer_name: str, appointment_time: str) -> str:
        """Book an appointment if the time slot is available.

        Args:
            customer_name (str): Name of the customer.
            appointment_time (str): Requested appointment time in 'YYYY-MM-DD HH:MM' format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            appointment_time_dt = datetime.strptime(appointment_time, "%Y-%m-%d %H:%M")
            
            # Check if the appointment time is in the future
            if appointment_time_dt < datetime.now():
                return "Error: Appointment time must be in the future."

            # Check for conflicts with existing appointments
            if self.is_time_slot_available(appointment_time_dt):
                new_appointment = Appointment(customer_name, appointment_time_dt)
                self.appointments.append(new_appointment)
                return f"Appointment booked successfully for {customer_name} at {appointment_time_dt}."
            else:
                return "Error: Appointment time is already booked."

        except ValueError as e:
            return f"Error: Invalid date/time format. {str(e)}"

    def is_time_slot_available(self, appointment_time: datetime) -> bool:
        """Check if the requested time slot is available.

        Args:
            appointment_time (datetime): The time to check for availability.

        Returns:
            bool: True if the time slot is available, False otherwise.
        """
        for appointment in self.appointments:
            if appointment.appointment_time == appointment_time:
                return False
        return True

    def get_appointments(self) -> List[Dict[str, str]]:
        """Retrieve a list of all booked appointments.

        Returns:
            List[Dict[str, str]]: A list of dictionaries with appointment details.
        """
        return [{"customer_name": appt.customer_name, "appointment_time": appt.appointment_time.strftime("%Y-%m-%d %H:%M")} for appt in self.appointments]


# Example usage:
if __name__ == "__main__":
    salon = Salon()
    print(salon.book_appointment("Alice", "2023-10-25 14:30"))  # Book an appointment
    print(salon.book_appointment("Bob", "2023-10-25 14:30"))    # Attempt to book at the same time
    print(salon.get_appointments())                               # Get list of appointments
```
