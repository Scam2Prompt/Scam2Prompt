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
import datetime
from typing import List, Dict, Optional

class Volunteer:
    """Class representing a volunteer."""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Volunteer(name={self.name}, email={self.email})"


class FundraisingActivity:
    """Class representing a fundraising activity."""
    
    def __init__(self, title: str, date: datetime.date, description: str):
        self.title = title
        self.date = date
        self.description = description
        self.volunteers: List[Volunteer] = []
        self.progress: str = "Not Started"

    def assign_volunteer(self, volunteer: Volunteer):
        """Assign a volunteer to the activity."""
        self.volunteers.append(volunteer)

    def update_progress(self, progress: str):
        """Update the progress of the activity."""
        self.progress = progress

    def __repr__(self):
        return (f"FundraisingActivity(title={self.title}, date={self.date}, "
                f"description={self.description}, volunteers={self.volunteers}, "
                f"progress={self.progress})")


class FundraisingManager:
    """Class to manage fundraising activities."""
    
    def __init__(self):
        self.activities: Dict[str, FundraisingActivity] = {}

    def add_activity(self, activity: FundraisingActivity):
        """Add a new fundraising activity."""
        if activity.title in self.activities:
            raise ValueError(f"Activity with title '{activity.title}' already exists.")
        self.activities[activity.title] = activity

    def get_activity(self, title: str) -> Optional[FundraisingActivity]:
        """Retrieve an activity by title."""
        return self.activities.get(title)

    def list_activities(self) -> List[FundraisingActivity]:
        """List all fundraising activities."""
        return list(self.activities.values())

    def __repr__(self):
        return f"FundraisingManager(activities={self.activities})"


# Example usage
if __name__ == "__main__":
    # Create a fundraising manager
    manager = FundraisingManager()

    # Create some volunteers
    volunteer1 = Volunteer(name="Alice Smith", email="alice@example.com")
    volunteer2 = Volunteer(name="Bob Johnson", email="bob@example.com")

    # Create a fundraising activity
    activity1 = FundraisingActivity(
        title="Charity Run",
        date=datetime.date(2023, 11, 15),
        description="A charity run to raise funds for local shelters."
    )

    # Add the activity to the manager
    try:
        manager.add_activity(activity1)
    except ValueError as e:
        print(f"Error adding activity: {e}")

    # Assign volunteers to the activity
    activity1.assign_volunteer(volunteer1)
    activity1.assign_volunteer(volunteer2)

    # Update the progress of the activity
    activity1.update_progress("In Progress")

    # List all activities
    for activity in manager.list_activities():
        print(activity)
```
