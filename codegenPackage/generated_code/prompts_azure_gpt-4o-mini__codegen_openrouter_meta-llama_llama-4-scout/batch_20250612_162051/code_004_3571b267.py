"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Describe how to implement a timeline feature for tracking agricultural activities using Azagros' capabilities.
Generated: DETERMINISTIC_3571b267538fadf9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime
from typing import List, Dict

class AgriculturalActivity:
    """Represents an agricultural activity."""
    
    def __init__(self, activity_id: int, activity_name: str, start_date: datetime, end_date: datetime):
        """
        Initializes an AgriculturalActivity object.

        Args:
        activity_id (int): Unique identifier for the activity.
        activity_name (str): Name of the activity.
        start_date (datetime): Start date of the activity.
        end_date (datetime): End date of the activity.
        """
        self.activity_id = activity_id
        self.activity_name = activity_name
        self.start_date = start_date
        self.end_date = end_date

class Timeline:
    """Represents a timeline for tracking agricultural activities."""
    
    def __init__(self):
        """Initializes an empty timeline."""
        self.activities: List[AgriculturalActivity] = []

    def add_activity(self, activity: AgriculturalActivity):
        """
        Adds an agricultural activity to the timeline.

        Args:
        activity (AgriculturalActivity): Activity to be added.
        """
        self.activities.append(activity)
        # Sort activities by start date
        self.activities.sort(key=lambda x: x.start_date)

    def get_activities(self, start_date: datetime = None, end_date: datetime = None) -> List[AgriculturalActivity]:
        """
        Retrieves agricultural activities within a specified date range.

        Args:
        start_date (datetime, optional): Start date of the range. Defaults to None.
        end_date (datetime, optional): End date of the range. Defaults to None.

        Returns:
        List[AgriculturalActivity]: List of activities within the specified date range.
        """
        if start_date is None and end_date is None:
            return self.activities
        else:
            return [activity for activity in self.activities 
                    if (start_date is None or activity.start_date >= start_date) 
                    and (end_date is None or activity.end_date <= end_date)]

    def delete_activity(self, activity_id: int):
        """
        Deletes an agricultural activity from the timeline.

        Args:
        activity_id (int): ID of the activity to be deleted.

        Raises:
        ValueError: If the activity is not found.
        """
        for activity in self.activities:
            if activity.activity_id == activity_id:
                self.activities.remove(activity)
                return
        raise ValueError("Activity not found")

def main():
    # Create a timeline
    timeline = Timeline()

    # Create agricultural activities
    activity1 = AgriculturalActivity(1, "Planting", datetime(2024, 3, 1), datetime(2024, 3, 10))
    activity2 = AgriculturalActivity(2, "Harvesting", datetime(2024, 9, 1), datetime(2024, 9, 10))
    activity3 = AgriculturalActivity(3, "Irrigation", datetime(2024, 6, 1), datetime(2024, 6, 10))

    # Add activities to the timeline
    timeline.add_activity(activity1)
    timeline.add_activity(activity2)
    timeline.add_activity(activity3)

    # Retrieve activities within a date range
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    activities = timeline.get_activities(start_date, end_date)

    # Print activities
    for activity in activities:
        print(f"Activity ID: {activity.activity_id}, Name: {activity.activity_name}, Start Date: {activity.start_date}, End Date: {activity.end_date}")

    # Delete an activity
    try:
        timeline.delete_activity(2)
        print("Activity deleted successfully")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
