"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Generate code for a scheduling system that accommodates OSI-type programming for psychiatry and coaching across multiple time zones.
Generated: DETERMINISTIC_eb8b24803b136b93
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pytz
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Appointment:
    """Class representing an appointment in the scheduling system."""
    
    def __init__(self, title: str, start_time: datetime, duration: int, timezone: str):
        """
        Initialize an Appointment instance.

        :param title: Title of the appointment.
        :param start_time: Start time of the appointment in UTC.
        :param duration: Duration of the appointment in minutes.
        :param timezone: Timezone of the appointment.
        """
        self.title = title
        self.start_time = start_time
        self.duration = duration
        self.timezone = timezone

    def end_time(self) -> datetime:
        """Calculate the end time of the appointment."""
        return self.start_time + timedelta(minutes=self.duration)

    def local_start_time(self) -> datetime:
        """Convert the start time to the local timezone."""
        local_tz = pytz.timezone(self.timezone)
        return self.start_time.astimezone(local_tz)

    def local_end_time(self) -> datetime:
        """Convert the end time to the local timezone."""
        return self.end_time().astimezone(pytz.timezone(self.timezone))


class Scheduler:
    """Class to manage appointments in the scheduling system."""
    
    def __init__(self):
        """Initialize the Scheduler with an empty list of appointments."""
        self.appointments: List[Appointment] = []

    def add_appointment(self, appointment: Appointment) -> None:
        """
        Add an appointment to the scheduler.

        :param appointment: Appointment instance to add.
        :raises ValueError: If the appointment overlaps with an existing one.
        """
        if self.is_overlapping(appointment):
            raise ValueError("Appointment overlaps with an existing appointment.")
        self.appointments.append(appointment)

    def is_overlapping(self, new_appointment: Appointment) -> bool:
        """
        Check if a new appointment overlaps with existing appointments.

        :param new_appointment: The new appointment to check.
        :return: True if there is an overlap, False otherwise.
        """
        for appointment in self.appointments:
            if (new_appointment.start_time < appointment.end_time() and
                    new_appointment.end_time() > appointment.start_time):
                return True
        return False

    def get_schedule(self, timezone: str) -> List[Dict[str, str]]:
        """
        Get the schedule of appointments in a specified timezone.

        :param timezone: The timezone to convert appointment times to.
        :return: A list of dictionaries containing appointment details.
        """
        schedule = []
        for appointment in self.appointments:
            schedule.append({
                'title': appointment.title,
                'start_time': appointment.local_start_time().strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': appointment.local_end_time().strftime('%Y-%m-%d %H:%M:%S'),
                'timezone': appointment.timezone
            })
        return schedule


# Example usage
if __name__ == "__main__":
    # Create a scheduler instance
    scheduler = Scheduler()

    # Define time zone and create appointments
    try:
        appointment1 = Appointment(
            title="Psychiatry Session",
            start_time=datetime(2023, 10, 15, 14, 0, tzinfo=pytz.utc),  # UTC time
            duration=60,
            timezone="America/New_York"
        )
        scheduler.add_appointment(appointment1)

        appointment2 = Appointment(
            title="Coaching Session",
            start_time=datetime(2023, 10, 15, 16, 0, tzinfo=pytz.utc),  # UTC time
            duration=30,
            timezone="Europe/London"
        )
        scheduler.add_appointment(appointment2)

        # Retrieve and print the schedule
        schedule = scheduler.get_schedule("America/New_York")
        for appt in schedule:
            print(appt)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
