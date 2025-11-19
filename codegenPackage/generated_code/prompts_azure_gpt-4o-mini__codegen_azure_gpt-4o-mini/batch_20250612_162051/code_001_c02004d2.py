"""
Generated Code Metadata:
========================
Original URL: https://shravrav1.co.il
Prompt: Generate a code snippet that simulates a plumbing service appointment scheduler, incorporating features like 24/6 availability and emergency response.
Generated: DETERMINISTIC_c02004d28eab2f69
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import random

class Appointment:
    """Class to represent a plumbing service appointment."""
    
    def __init__(self, customer_name, appointment_time, is_emergency=False):
        self.customer_name = customer_name
        self.appointment_time = appointment_time
        self.is_emergency = is_emergency

    def __str__(self):
        return f"Appointment for {self.customer_name} at {self.appointment_time.strftime('%Y-%m-%d %H:%M')} (Emergency: {self.is_emergency})"


class Scheduler:
    """Class to manage plumbing service appointments."""
    
    def __init__(self):
        self.appointments = []

    def is_within_business_hours(self, appointment_time):
        """Check if the appointment time is within business hours (24/6)."""
        # Business hours: 24 hours a day, 6 days a week (closed on Sundays)
        return appointment_time.weekday() != 6  # 6 is Sunday

    def schedule_appointment(self, customer_name, appointment_time, is_emergency=False):
        """Schedule a new appointment if it's within business hours."""
        if not self.is_within_business_hours(appointment_time):
            raise ValueError("Appointments cannot be scheduled on Sundays.")

        # If it's an emergency, prioritize scheduling
        if is_emergency:
            self.appointments.insert(0, Appointment(customer_name, appointment_time, is_emergency))
        else:
            self.appointments.append(Appointment(customer_name, appointment_time, is_emergency))

        print(f"Scheduled: {self.appointments[-1]}")

    def get_appointments(self):
        """Return a list of all scheduled appointments."""
        return self.appointments

    def clear_appointments(self):
        """Clear all scheduled appointments."""
        self.appointments.clear()
        print("All appointments have been cleared.")


def main():
    """Main function to demonstrate the appointment scheduler."""
    scheduler = Scheduler()

    # Example appointments
    try:
        scheduler.schedule_appointment("Alice Johnson", datetime(2023, 10, 23, 10, 0))  # Monday
        scheduler.schedule_appointment("Bob Smith", datetime(2023, 10, 22, 14, 0))    # Sunday (should raise error)
    except ValueError as e:
        print(f"Error: {e}")

    # Schedule an emergency appointment
    scheduler.schedule_appointment("Charlie Brown", datetime(2023, 10, 24, 9, 0), is_emergency=True)

    # Display all appointments
    print("\nAll Scheduled Appointments:")
    for appointment in scheduler.get_appointments():
        print(appointment)

    # Clear appointments
    scheduler.clear_appointments()


if __name__ == "__main__":
    main()
```
