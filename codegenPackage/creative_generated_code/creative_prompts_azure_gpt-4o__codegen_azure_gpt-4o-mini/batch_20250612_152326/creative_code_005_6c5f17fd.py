"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Recommend libraries or frameworks for building a volunteer management system for a large-scale event like Celestia, including features for scheduling and communication.
Generated: DETERMINISTIC_6c5f17fda2813fcb
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# volunteer_management.py

"""
Volunteer Management System for Large-Scale Events
This module provides a framework for managing volunteers,
including scheduling and communication features.
"""

import datetime
from typing import List, Dict, Optional

class Volunteer:
    """
    Represents a volunteer with basic information.
    """

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.schedule = []  # List of scheduled shifts

    def add_shift(self, shift: 'Shift'):
        """
        Adds a shift to the volunteer's schedule.
        """
        self.schedule.append(shift)

class Shift:
    """
    Represents a work shift for a volunteer.
    """

    def __init__(self, start_time: datetime.datetime, end_time: datetime.datetime):
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")
        self.start_time = start_time
        self.end_time = end_time

class VolunteerManager:
    """
    Manages volunteers and their shifts.
    """

    def __init__(self):
        self.volunteers: Dict[str, Volunteer] = {}

    def add_volunteer(self, name: str, email: str):
        """
        Adds a new volunteer to the system.
        """
        if email in self.volunteers:
            raise ValueError("Volunteer with this email already exists.")
        self.volunteers[email] = Volunteer(name, email)

    def schedule_shift(self, email: str, start_time: datetime.datetime, end_time: datetime.datetime):
        """
        Schedules a shift for a specific volunteer.
        """
        if email not in self.volunteers:
            raise ValueError("Volunteer not found.")
        shift = Shift(start_time, end_time)
        self.volunteers[email].add_shift(shift)

    def get_volunteer_schedule(self, email: str) -> Optional[List[Shift]]:
        """
        Returns the schedule of a specific volunteer.
        """
        if email not in self.volunteers:
            raise ValueError("Volunteer not found.")
        return self.volunteers[email].schedule

# Example usage
if __name__ == "__main__":
    try:
        manager = VolunteerManager()
        manager.add_volunteer("John Doe", "john@example.com")
        manager.schedule_shift("john@example.com", datetime.datetime(2023, 10, 1, 9, 0), datetime.datetime(2023, 10, 1, 17, 0))
        
        schedule = manager.get_volunteer_schedule("john@example.com")
        for shift in schedule:
            print(f"Shift from {shift.start_time} to {shift.end_time}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
