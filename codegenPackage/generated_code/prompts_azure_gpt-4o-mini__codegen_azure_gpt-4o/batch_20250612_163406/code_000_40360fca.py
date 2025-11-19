"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Generate a code snippet for a booking system that allows users to schedule appointments at an art makeup salon in Ginza, Tokyo, similar to M luce's reservation system.
Generated: DETERMINISTIC_40360fca1cc83a8e
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BookingSystem:
    def __init__(self):
        # Initialize the booking system with an empty schedule
        self.schedule = {}

    def add_appointment(self, customer_name, appointment_date, appointment_time):
        """
        Adds a new appointment to the schedule.

        Args:
            customer_name (str): Name of the customer.
            appointment_date (str): Date of the appointment in 'YYYY-MM-DD' format.
            appointment_time (str): Time of the appointment in 'HH:MM' format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate date and time format
            appointment_datetime = datetime.datetime.strptime(
                f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M"
            )

            # Check if the appointment slot is already booked
            if appointment_datetime in self.schedule:
                return "Error: Appointment slot is already booked."

            # Add the appointment to the schedule
            self.schedule[appointment_datetime] = customer_name
            return f"Appointment successfully booked for {customer_name} on {appointment_date} at {appointment_time}."
        except ValueError:
            return "Error: Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time."

    def view_schedule(self):
        """
        Returns the current schedule of appointments.

        Returns:
            str: A formatted string of all appointments.
        """
        if not self.schedule:
            return "No appointments scheduled."
        
        # Sort appointments by date and time
        sorted_schedule = sorted(self.schedule.items())
        schedule_str = "Current Appointments:\n"
        for appointment_datetime, customer_name in sorted_schedule:
            schedule_str += f"{appointment_datetime.strftime('%Y-%m-%d %H:%M')} - {customer_name}\n"
        return schedule_str

    def cancel_appointment(self, appointment_date, appointment_time):
        """
        Cancels an existing appointment.

        Args:
            appointment_date (str): Date of the appointment in 'YYYY-MM-DD' format.
            appointment_time (str): Time of the appointment in 'HH:MM' format.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            # Validate date and time format
            appointment_datetime = datetime.datetime.strptime(
                f"{appointment_date} {appointment_time}", "%Y-%m-%d %H:%M"
            )

            # Check if the appointment exists
            if appointment_datetime not in self.schedule:
                return "Error: No appointment found at the specified date and time."

            # Remove the appointment from the schedule
            del self.schedule[appointment_datetime]
            return f"Appointment on {appointment_date} at {appointment_time} has been successfully canceled."
        except ValueError:
            return "Error: Invalid date or time format. Please use 'YYYY-MM-DD' for date and 'HH:MM' for time."


# Example usage
if __name__ == "__main__":
    salon_booking = BookingSystem()

    # Add appointments
    print(salon_booking.add_appointment("Alice", "2023-10-15", "14:00"))
    print(salon_booking.add_appointment("Bob", "2023-10-15", "15:00"))

    # View schedule
    print(salon_booking.view_schedule())

    # Cancel an appointment
    print(salon_booking.cancel_appointment("2023-10-15", "14:00"))

    # View schedule after cancellation
    print(salon_booking.view_schedule())
```
