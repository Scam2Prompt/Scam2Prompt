"""
Generated Code Metadata:
========================
Original URL: https://fondation.app
Prompt: Write a script to schedule and manage fundraising activities, including assigning volunteers and tracking progress, inspired by CRM.f's activity planning tools.
Generated: DETERMINISTIC_5728e84d86fb2fd2
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fundraising_activity_manager.py

import datetime
from typing import List, Dict

class Volunteer:
    """Represents a volunteer assigned to a fundraising activity."""

    def __init__(self, name: str, email: str):
        """
        Initializes a Volunteer instance.

        Args:
        - name (str): The volunteer's name.
        - email (str): The volunteer's email address.
        """
        self.name = name
        self.email = email

class FundraisingActivity:
    """Represents a fundraising activity with assigned volunteers and progress tracking."""

    def __init__(self, title: str, date: datetime.date, goal: float):
        """
        Initializes a FundraisingActivity instance.

        Args:
        - title (str): The activity's title.
        - date (datetime.date): The activity's scheduled date.
        - goal (float): The activity's fundraising goal.
        """
        self.title = title
        self.date = date
        self.goal = goal
        self.volunteers: List[Volunteer] = []
        self.progress: float = 0.0

    def assign_volunteer(self, volunteer: Volunteer):
        """Assigns a volunteer to the activity."""
        self.volunteers.append(volunteer)

    def update_progress(self, amount: float):
        """
        Updates the activity's progress.

        Args:
        - amount (float): The amount raised.

        Raises:
        - ValueError: If the amount is negative or exceeds the goal.
        """
        if amount < 0 or self.progress + amount > self.goal:
            raise ValueError("Invalid amount")
        self.progress += amount

class FundraisingActivityManager:
    """Manages a collection of fundraising activities."""

    def __init__(self):
        self.activities: Dict[str, FundraisingActivity] = {}

    def create_activity(self, title: str, date: datetime.date, goal: float):
        """
        Creates a new fundraising activity.

        Args:
        - title (str): The activity's title.
        - date (datetime.date): The activity's scheduled date.
        - goal (float): The activity's fundraising goal.

        Returns:
        - FundraisingActivity: The created activity.
        """
        activity = FundraisingActivity(title, date, goal)
        self.activities[title] = activity
        return activity

    def get_activity(self, title: str) -> FundraisingActivity:
        """
        Retrieves a fundraising activity by title.

        Args:
        - title (str): The activity's title.

        Returns:
        - FundraisingActivity: The activity instance, or None if not found.
        """
        return self.activities.get(title)

def main():
    # Example usage:
    manager = FundraisingActivityManager()

    # Create a fundraising activity
    activity = manager.create_activity(
        "Charity Run",
        datetime.date(2024, 9, 20),
        10000.0
    )

    # Assign volunteers
    volunteer1 = Volunteer("John Doe", "john@example.com")
    volunteer2 = Volunteer("Jane Smith", "jane@example.com")
    activity.assign_volunteer(volunteer1)
    activity.assign_volunteer(volunteer2)

    # Update progress
    activity.update_progress(5000.0)

    # Print activity details
    print(f"Activity: {activity.title}")
    print(f"Date: {activity.date}")
    print(f"Goal: ${activity.goal:.2f}")
    print(f"Progress: ${activity.progress:.2f}")
    print("Volunteers:")
    for volunteer in activity.volunteers:
        print(f"- {volunteer.name} ({volunteer.email})")

if __name__ == "__main__":
    main()
```
