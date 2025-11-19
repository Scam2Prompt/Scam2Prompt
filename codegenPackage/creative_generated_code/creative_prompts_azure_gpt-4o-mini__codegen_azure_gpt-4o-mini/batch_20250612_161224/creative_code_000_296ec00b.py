"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherealspamassagetherapist.com
Prompt: Generate a code snippet for a booking system that allows clients to schedule appointments for Swedish massage therapy at Ethereal Spa.
Generated: DETERMINISTIC_296ec00b6fa1df25
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import pytz

class Appointment:
    def __init__(self, client_name, appointment_time):
        self.client_name = client_name
        self.appointment_time = appointment_time

    def __repr__(self):
        return f"Appointment(client_name='{self.client_name}', appointment_time='{self.appointment_time}')"


class SpaBookingSystem:
    def __init__(self):
        self.appointments = []
        self.timezone = pytz.timezone("America/New_York")  # Set timezone for the appointments

    def book_appointment(self, client_name: str, appointment_time: str):
        """
        Books an appointment if the time is available.

        Args:
            client_name (str): Name of the client.
            appointment_time (str): Appointment time in 'YYYY-MM-DD HH:MM' format.

        Raises:
            ValueError: If the appointment time is invalid or already booked.
        """
        # Parse and localize the appointment time
        try:
            appointment_time = self.timezone.localize(datetime.strptime(appointment_time, "%Y-%m-%d %H:%M"))
        except ValueError as e:
            raise ValueError("Invalid appointment time format. Please use 'YYYY-MM-DD HH:MM' format.") from e

        # Check if the appointment is already booked
        if any(appointment.appointment_time == appointment_time for appointment in self.appointments):
            raise ValueError("This appointment time is already booked. Please choose another time.")

        # Add the new appointment
        new_appointment = Appointment(client_name, appointment_time)
        self.appointments.append(new_appointment)
        print(f"Appointment booked successfully: {new_appointment}")

    def list_appointments(self):
        """Prints all scheduled appointments."""
        if not self.appointments:
            print("No appointments scheduled.")
            return
        print("Scheduled Appointments:")
        for appointment in self.appointments:
            print(appointment)

# Example usage:
if __name__ == "__main__":
    spa_booking_system = SpaBookingSystem()

    try:
        spa_booking_system.book_appointment("John Doe", "2023-10-15 14:00")
        spa_booking_system.book_appointment("Jane Smith", "2023-10-15 15:00")
        spa_booking_system.list_appointments()
    except ValueError as e:
        print(f"Error: {e}")
```
