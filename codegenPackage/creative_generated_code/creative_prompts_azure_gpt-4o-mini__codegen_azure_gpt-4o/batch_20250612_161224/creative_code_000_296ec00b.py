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
import datetime

class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass

class BookingSystem:
    def __init__(self):
        """Initialize an empty schedule for appointments."""
        self.appointments = {}

    def is_available(self, date_time):
        """
        Check if a specific date and time is available for booking.
        :param date_time: datetime object representing the desired appointment time.
        :return: True if available, False otherwise.
        """
        return date_time not in self.appointments

    def book_appointment(self, client_name, date_time):
        """
        Book an appointment for Swedish massage therapy.
        :param client_name: Name of the client.
        :param date_time: Desired date and time as a datetime object.
        :raises BookingError: If the desired time slot is already booked.
        """
        if not isinstance(date_time, datetime.datetime):
            raise ValueError("date_time must be a datetime object.")

        if self.is_available(date_time):
            self.appointments[date_time] = client_name
            print(f"Appointment successfully booked for {client_name} on {date_time}.")
        else:
            raise BookingError(f"The time slot {date_time} is already booked.")

    def cancel_appointment(self, client_name, date_time):
        """
        Cancel an existing appointment.
        :param client_name: Name of the client.
        :param date_time: Date and time of the appointment to cancel.
        :raises BookingError: If no matching appointment is found.
        """
        if self.appointments.get(date_time) == client_name:
            del self.appointments[date_time]
            print(f"Appointment for {client_name} on {date_time} has been cancelled.")
        else:
            raise BookingError(f"No appointment found for {client_name} at {date_time}.")

    def view_schedule(self):
        """
        View all scheduled appointments.
        :return: Dictionary with datetime keys and client name values.
        """
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            print("Scheduled Appointments:")
            for date_time, client_name in sorted(self.appointments.items()):
                print(f"{date_time}: {client_name}")

# Example Usage
if __name__ == "__main__":
    spa_booking_system = BookingSystem()

    try:
        # Client attempts to book an appointment.
        appointment_time = datetime.datetime(2023, 12, 15, 14, 0)  # December 15, 2023 at 2:00 PM
        spa_booking_system.book_appointment("John Doe", appointment_time)

        # View all scheduled appointments.
        spa_booking_system.view_schedule()

        # Attempt to double-book the same time slot (raises an exception).
        spa_booking_system.book_appointment("Jane Smith", appointment_time)

    except BookingError as e:
        print(f"Booking Error: {e}")

    try:
        # Cancel John's appointment.
        spa_booking_system.cancel_appointment("John Doe", appointment_time)
        spa_booking_system.view_schedule()
    except BookingError as e:
        print(f"Booking Error: {e}")
```

This code snippet provides a fully functional booking system for scheduling appointments at Ethereal Spa. Meeting all requested criteria, it includes error handling, comments, and adheres to Python best practices. You can execute this code to test and use it immediately.
