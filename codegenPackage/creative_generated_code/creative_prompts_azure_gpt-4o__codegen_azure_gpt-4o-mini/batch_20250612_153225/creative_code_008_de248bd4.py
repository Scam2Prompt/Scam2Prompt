"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Create a program to schedule health education activities and multi-diagnostic camps for rural areas, as described under MIMSR's outreach initiatives.
Generated: DETERMINISTIC_de248bd498679ed9
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Activity:
    """Class to represent a health education activity or diagnostic camp."""

    def __init__(self, name: str, date: datetime.date, location: str, description: str):
        """Initialize an Activity with a name, date, location, and description."""
        self.name = name
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        """Return a string representation of the Activity."""
        return f"{self.name} on {self.date} at {self.location}: {self.description}"


class Scheduler:
    """Class to schedule health education activities and diagnostic camps."""

    def __init__(self):
        """Initialize the Scheduler with an empty activity list."""
        self.activities: List[Activity] = []

    def add_activity(self, activity: Activity) -> None:
        """Add a new activity to the schedule.

        Args:
            activity (Activity): The activity to add.

        Raises:
            ValueError: If the activity date conflicts with an existing activity.
        """
        if self._is_date_conflict(activity.date):
            raise ValueError(f"Activity on {activity.date} conflicts with an existing activity.")
        self.activities.append(activity)

    def _is_date_conflict(self, date: datetime.date) -> bool:
        """Check if the given date conflicts with existing activities.

        Args:
            date (datetime.date): The date to check for conflicts.

        Returns:
            bool: True if there is a conflict, False otherwise.
        """
        return any(activity.date == date for activity in self.activities)

    def get_schedule(self) -> List[str]:
        """Get a list of scheduled activities.

        Returns:
            List[str]: A list of string representations of scheduled activities.
        """
        return [str(activity) for activity in self.activities]

    def remove_activity(self, activity_name: str, activity_date: datetime.date) -> bool:
        """Remove an activity from the schedule by its name and date.

        Args:
            activity_name (str): The name of the activity to remove.
            activity_date (datetime.date): The date of the activity to remove.

        Returns:
            bool: True if the activity was successfully removed, False otherwise.
        """
        for activity in self.activities:
            if activity.name == activity_name and activity.date == activity_date:
                self.activities.remove(activity)
                return True
        return False


def main():
    """Main function to demonstrate the scheduling of health education activities."""
    scheduler = Scheduler()

    # Sample activities
    activity1 = Activity("Nutrition Workshop", datetime.date(2023, 11, 15), "Village Hall", "A workshop on nutrition and healthy eating habits.")
    activity2 = Activity("Blood Donation Camp", datetime.date(2023, 11, 20), "Community Center", "A camp to encourage blood donation and health check-ups.")

    try:
        scheduler.add_activity(activity1)
        scheduler.add_activity(activity2)
    except ValueError as ve:
        print(f"Error adding activity: {ve}")

    # Display scheduled activities
    print("Scheduled Activities:")
    for activity in scheduler.get_schedule():
        print(activity)

    # Example of removing an activity
    success = scheduler.remove_activity("Nutrition Workshop", datetime.date(2023, 11, 15))
    if success:
        print("Successfully removed 'Nutrition Workshop'.")
    else:
        print("Failed to remove 'Nutrition Workshop'.")

    # Display updated schedule
    print("\nUpdated Schedule:")
    for activity in scheduler.get_schedule():
        print(activity)


if __name__ == "__main__":
    main()
```
