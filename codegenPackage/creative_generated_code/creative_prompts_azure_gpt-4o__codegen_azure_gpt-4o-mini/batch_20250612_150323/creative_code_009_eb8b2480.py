"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Generate code for a scheduling system that accommodates OSI-type programming for psychiatry and coaching across multiple time zones.
Generated: DETERMINISTIC_eb8b24803b136b93
Batch ID: 20250612_150323
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
import json

class Appointment:
    """Class to represent an appointment."""
    
    def __init__(self, title, start_time, end_time, timezone):
        """
        Initialize an appointment with a title, start time, end time, and timezone.

        :param title: The title of the appointment
        :param start_time: Start time of the appointment (datetime object)
        :param end_time: End time of the appointment (datetime object)
        :param timezone: Timezone of the appointment (str)
        """
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.timezone = timezone

    def to_dict(self):
        """Convert the appointment to a dictionary."""
        return {
            'title': self.title,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'timezone': self.timezone
        }

class Scheduler:
    """Class to manage appointments across different time zones."""
    
    def __init__(self):
        """Initialize an empty scheduler."""
        self.appointments = []

    def add_appointment(self, title, start_time_str, end_time_str, timezone_str):
        """
        Add an appointment to the scheduler.

        :param title: The title of the appointment
        :param start_time_str: Start time of the appointment (str)
        :param end_time_str: End time of the appointment (str)
        :param timezone_str: Timezone of the appointment (str)
        """
        try:
            # Convert string times to datetime objects
            timezone = pytz.timezone(timezone_str)
            start_time = timezone.localize(datetime.fromisoformat(start_time_str))
            end_time = timezone.localize(datetime.fromisoformat(end_time_str))
            
            # Create and store the appointment
            appointment = Appointment(title, start_time, end_time, timezone_str)
            self.appointments.append(appointment)

        except (ValueError, pytz.UnknownTimeZoneError) as e:
            print(f"Error adding appointment: {e}")

    def list_appointments(self):
        """List all appointments in a human-readable format."""
        for appointment in self.appointments:
            print(f"{appointment.title} | {appointment.start_time} - {appointment.end_time} ({appointment.timezone})")

    def to_json(self):
        """Convert the list of appointments to JSON format."""
        return json.dumps([appt.to_dict() for appt in self.appointments], indent=4)

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Add appointments (replace with appropriate time strings and timezones)
    scheduler.add_appointment("Client Session", "2023-10-01T10:00:00", "2023-10-01T11:00:00", "America/New_York")
    scheduler.add_appointment("Group Therapy", "2023-10-01T15:00:00", "2023-10-01T16:00:00", "Europe/London")
    
    # List appointments
    scheduler.list_appointments()
    
    # Output appointments as JSON
    print(scheduler.to_json())
```
