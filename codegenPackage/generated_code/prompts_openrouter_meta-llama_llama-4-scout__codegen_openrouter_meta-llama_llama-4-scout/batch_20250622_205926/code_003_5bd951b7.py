"""
Generated Code Metadata:
========================
Original URL: https://abilityfordisabilityfund.com
Prompt: Create a volunteer management system that tracks volunteer hours and activities for a non-profit organization supporting individuals with disabilities.
Generated: DETERMINISTIC_5bd951b7e11e2173
Batch ID: 20250622_205926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# volunteer_management_system.py

from datetime import datetime
from typing import List, Dict

class Volunteer:
    """Represents a volunteer in the system."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Volunteer object.

        Args:
            id (int): Unique identifier for the volunteer.
            name (str): Name of the volunteer.
            email (str): Email address of the volunteer.
        """
        self.id = id
        self.name = name
        self.email = email
        self.activities = []

    def add_activity(self, activity: 'Activity'):
        """Adds an activity to the volunteer's record."""
        self.activities.append(activity)


class Activity:
    """Represents a volunteer activity."""

    def __init__(self, id: int, name: str, hours: float, date: datetime):
        """
        Initializes an Activity object.

        Args:
            id (int): Unique identifier for the activity.
            name (str): Name of the activity.
            hours (float): Number of hours spent on the activity.
            date (datetime): Date the activity was performed.
        """
        self.id = id
        self.name = name
        self.hours = hours
        self.date = date


class VolunteerManagementSystem:
    """Manages volunteers and their activities."""

    def __init__(self):
        """Initializes the volunteer management system."""
        self.volunteers: Dict[int, Volunteer] = {}
        self.activities: Dict[int, Activity] = {}
        self.next_volunteer_id = 1
        self.next_activity_id = 1

    def add_volunteer(self, name: str, email: str) -> Volunteer:
        """
        Adds a new volunteer to the system.

        Args:
            name (str): Name of the volunteer.
            email (str): Email address of the volunteer.

        Returns:
            Volunteer: The newly added volunteer.
        """
        volunteer = Volunteer(self.next_volunteer_id, name, email)
        self.volunteers[self.next_volunteer_id] = volunteer
        self.next_volunteer_id += 1
        return volunteer

    def add_activity(self, volunteer_id: int, name: str, hours: float, date: datetime) -> Activity:
        """
        Adds a new activity to a volunteer's record.

        Args:
            volunteer_id (int): ID of the volunteer.
            name (str): Name of the activity.
            hours (float): Number of hours spent on the activity.
            date (datetime): Date the activity was performed.

        Returns:
            Activity: The newly added activity.

        Raises:
            ValueError: If the volunteer ID is not found.
        """
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer not found")

        activity = Activity(self.next_activity_id, name, hours, date)
        self.activities[self.next_activity_id] = activity
        self.volunteers[volunteer_id].add_activity(activity)
        self.next_activity_id += 1
        return activity

    def get_volunteer_hours(self, volunteer_id: int) -> float:
        """
        Gets the total hours volunteered by a volunteer.

        Args:
            volunteer_id (int): ID of the volunteer.

        Returns:
            float: Total hours volunteered.

        Raises:
            ValueError: If the volunteer ID is not found.
        """
        if volunteer_id not in self.volunteers:
            raise ValueError("Volunteer not found")

        return sum(activity.hours for activity in self.volunteers[volunteer_id].activities)


def main():
    # Create a volunteer management system
    vms = VolunteerManagementSystem()

    try:
        # Add volunteers
        volunteer1 = vms.add_volunteer("John Doe", "john@example.com")
        volunteer2 = vms.add_volunteer("Jane Doe", "jane@example.com")

        # Add activities
        activity1 = vms.add_activity(volunteer1.id, "Mentorship", 5.0, datetime(2022, 1, 1))
        activity2 = vms.add_activity(volunteer1.id, "Fundraising", 3.0, datetime(2022, 1, 15))
        activity3 = vms.add_activity(volunteer2.id, "Event Planning", 4.0, datetime(2022, 2, 1))

        # Get volunteer hours
        print(f"Volunteer {volunteer1.name} hours: {vms.get_volunteer_hours(volunteer1.id)}")
        print(f"Volunteer {volunteer2.name} hours: {vms.get_volunteer_hours(volunteer2.id)}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
