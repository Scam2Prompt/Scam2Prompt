"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shravrav1.co.il
Prompt: Generate a code snippet that simulates a plumbing service appointment scheduler, incorporating features like 24/6 availability and emergency response.
Generated: DETERMINISTIC_c02004d28eab2f69
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
        return f"Appointment for {self.customer_name} on {self.appointment_time.strftime('%Y-%m-%d %H:%M')}. Emergency: {self.is_emergency}"


class Scheduler:
    """Class to manage the scheduling of plumbing service appointments."""

    def __init__(self):
        self.appointments = []
        self.opening_time = 8  # 8 AM
        self.closing_time = 20  # 8 PM
        self.days_open = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    def is_available(self, appointment_time):
        """Check if the scheduler can take an appointment at the specified time."""
        if appointment_time.strftime('%A') not in self.days_open:
            return False
        if appointment_time.hour < self.opening_time or appointment_time.hour >= self.closing_time:
            return False
        return True

    def schedule_appointment(self, customer_name, appointment_time, is_emergency=False):
        """Schedule an appointment if the specified time is available."""
        if not self.is_available(appointment_time):
            raise ValueError("Requested appointment time is outside of business hours.")
        
        # Handle emergency appointments, which can be scheduled outside normal hours
        if is_emergency or self.is_available(appointment_time):
            new_appointment = Appointment(customer_name, appointment_time, is_emergency)
            self.appointments.append(new_appointment)
            return new_appointment
        else:
            raise ValueError("Requested appointment time is not available.")

    def get_next_available_time(self):
        """Find the next available time slot for scheduling."""
        now = datetime.now()
        next_time = now.replace(hour=self.opening_time, minute=0, second=0, microsecond=0)
        
        while not self.is_available(next_time) or self.is_time_booked(next_time):
            next_time += timedelta(minutes=30)  # Check every 30 minutes
            if next_time.hour >= self.closing_time:
                next_time += timedelta(days=1)
                next_time = next_time.replace(hour=self.opening_time)

        return next_time

    def is_time_booked(self, appointment_time):
        """Check if the specified appointment time is already booked."""
        return any(appointment.appointment_time == appointment_time for appointment in self.appointments)

    def list_appointments(self):
        """List all scheduled appointments."""
        return [str(appointment) for appointment in self.appointments]


if __name__ == "__main__":
    # Example usage of the Scheduler class
    scheduler = Scheduler()

    # Schedule an emergency appointment
    try:
        emergency_time = datetime.now() + timedelta(hours=1)
        appointment = scheduler.schedule_appointment("John Doe", emergency_time, is_emergency=True)
        print(f"Scheduled: {appointment}")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # Schedule a regular appointment
    try:
        next_available_time = scheduler.get_next_available_time()
        appointment = scheduler.schedule_appointment("Jane Smith", next_available_time)
        print(f"Scheduled: {appointment}")
    except ValueError as e:
        print(f"Error scheduling appointment: {e}")

    # List all appointments
    print("All Appointments:")
    for app in scheduler.list_appointments():
        print(app)
```
