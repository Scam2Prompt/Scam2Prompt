"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Develop a scheduling system in Python that allows for appointment confirmations and changes, similar to ProSync's appointment scheduling feature.
Generated: DETERMINISTIC_72f99b754a873b1a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Appointment:
    """Class representing an appointment."""
    
    def __init__(self, title: str, start_time: datetime.datetime, end_time: datetime.datetime):
        """
        Initialize an appointment with a title, start time, and end time.
        
        :param title: Title of the appointment
        :param start_time: Start time of the appointment
        :param end_time: End time of the appointment
        """
        if end_time <= start_time:
            raise ValueError("End time must be after start time.")
        
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.confirmed = False

    def confirm(self):
        """Confirm the appointment."""
        self.confirmed = True

    def change_time(self, new_start_time: datetime.datetime, new_end_time: datetime.datetime):
        """
        Change the time of the appointment.
        
        :param new_start_time: New start time for the appointment
        :param new_end_time: New end time for the appointment
        """
        if new_end_time <= new_start_time:
            raise ValueError("New end time must be after new start time.")
        
        self.start_time = new_start_time
        self.end_time = new_end_time

class Scheduler:
    """Class to manage appointments."""
    
    def __init__(self):
        """Initialize the scheduler with an empty list of appointments."""
        self.appointments: List[Appointment] = []

    def add_appointment(self, appointment: Appointment):
        """
        Add a new appointment to the scheduler.
        
        :param appointment: Appointment to be added
        """
        if self.is_time_slot_taken(appointment.start_time, appointment.end_time):
            raise ValueError("Time slot is already taken.")
        
        self.appointments.append(appointment)

    def is_time_slot_taken(self, start_time: datetime.datetime, end_time: datetime.datetime) -> bool:
        """
        Check if the given time slot is already taken by another appointment.
        
        :param start_time: Start time to check
        :param end_time: End time to check
        :return: True if the time slot is taken, False otherwise
        """
        for appointment in self.appointments:
            if (start_time < appointment.end_time and end_time > appointment.start_time):
                return True
        return False

    def confirm_appointment(self, appointment: Appointment):
        """
        Confirm an existing appointment.
        
        :param appointment: Appointment to be confirmed
        """
        if appointment not in self.appointments:
            raise ValueError("Appointment not found in the scheduler.")
        
        appointment.confirm()

    def change_appointment_time(self, appointment: Appointment, new_start_time: datetime.datetime, new_end_time: datetime.datetime):
        """
        Change the time of an existing appointment.
        
        :param appointment: Appointment to change
        :param new_start_time: New start time for the appointment
        :param new_end_time: New end time for the appointment
        """
        if appointment not in self.appointments:
            raise ValueError("Appointment not found in the scheduler.")
        
        # Check if the new time slot is available
        if self.is_time_slot_taken(new_start_time, new_end_time):
            raise ValueError("New time slot is already taken.")
        
        appointment.change_time(new_start_time, new_end_time)

    def list_appointments(self) -> List[Appointment]:
        """Return a list of all appointments."""
        return self.appointments

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Create an appointment
    try:
        appointment1 = Appointment("Doctor's Appointment", datetime.datetime(2023, 10, 15, 10, 0), datetime.datetime(2023, 10, 15, 11, 0))
        scheduler.add_appointment(appointment1)
        
        # Confirm the appointment
        scheduler.confirm_appointment(appointment1)
        
        # Change the appointment time
        scheduler.change_appointment_time(appointment1, datetime.datetime(2023, 10, 15, 11, 0), datetime.datetime(2023, 10, 15, 12, 0))
        
        # List all appointments
        for appt in scheduler.list_appointments():
            print(f"Title: {appt.title}, Start: {appt.start_time}, End: {appt.end_time}, Confirmed: {appt.confirmed}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
