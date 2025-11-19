"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orthopedicsurgerysandiego.com
Prompt: Suggest a library for building a scheduling system that accommodates the working hours of Orthopedic Surgery San Diego, which is open Monday to Friday.
Generated: DETERMINISTIC_b11f3c5cd221de25
Batch ID: 20250612_140024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime, timedelta
import pytz  # For timezone handling
from typing import List, Optional, Tuple


class SchedulingSystem:
    """
    A scheduling system for managing appointments for Orthopedic Surgery San Diego.
    The clinic is open Monday to Friday from 8:00 AM to 5:00 PM.
    """

    # Define constants for scheduling
    WORKING_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    START_TIME = 8  # Clinic opens at 8 AM
    END_TIME = 17  # Clinic closes at 5 PM
    TIMEZONE = 'America/Los_Angeles'  # Specify the timezone

    def __init__(self):
        self.appointments: List[Tuple[datetime, datetime]] = []  # List to store scheduled appointments

    def is_within_working_hours(self, start: datetime, end: datetime) -> bool:
        """
        Check if the given time range falls within the clinic's working hours.

        :param start: Start time of the appointment.
        :param end: End time of the appointment.
        :return: True if within working hours, False otherwise.
        """
        # Check if both start and end are on a working day
        if start.strftime('%A') not in self.WORKING_DAYS or end.strftime('%A') not in self.WORKING_DAYS:
            return False
        
        # Check if the appointment times are within working hours
        if (start.hour < self.START_TIME or end.hour > self.END_TIME or 
                start >= end):
            return False
        
        return True

    def schedule_appointment(self, start: datetime, end: datetime) -> str:
        """
        Schedule an appointment if it falls within working hours.

        :param start: Start time of the appointment.
        :param end: End time of the appointment.
        :return: Confirmation message or error message.
        """
        # Ensure the times are in the correct timezone
        local_tz = pytz.timezone(self.TIMEZONE)
        start = local_tz.localize(start)
        end = local_tz.localize(end)

        # Validate working hours
        if not self.is_within_working_hours(start, end):
            return "Error: Appointment must be scheduled within working hours (Mon-Fri, 8 AM - 5 PM)."

        # Check for overlapping appointments
        for appointment in self.appointments:
            if (start < appointment[1] and end > appointment[0]):
                return "Error: Appointment overlaps with an existing appointment."

        # Schedule the appointment
        self.appointments.append((start, end))
        return f"Appointment scheduled from {start} to {end}."

    def get_schedule(self) -> List[Tuple[datetime, datetime]]:
        """
        Get the list of scheduled appointments.

        :return: List of scheduled appointments.
        """
        return self.appointments


# Example usage
if __name__ == "__main__":
    scheduler = SchedulingSystem()
    
    # Define appointment times
    start_time = datetime(2023, 10, 30, 9, 0)  # October 30, 2023, 9:00 AM
    end_time = datetime(2023, 10, 30, 10, 0)    # October 30, 2023, 10:00 AM

    # Schedule an appointment
    print(scheduler.schedule_appointment(start_time, end_time))

    # Output the current schedule
    print("Current Schedule:", scheduler.get_schedule())
```
