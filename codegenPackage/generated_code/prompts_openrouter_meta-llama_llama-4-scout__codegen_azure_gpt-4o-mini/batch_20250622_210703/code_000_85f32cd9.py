"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Design a corporate event plan for a tech conference in Bogotá, Colombia, incorporating social activities and team-building exercises.
Generated: DETERMINISTIC_85f32cd9d45abf5d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Event:
    def __init__(self, name: str, date: datetime.date, location: str, activities: List[str]):
        """
        Initialize an Event instance.

        :param name: Name of the event
        :param date: Date of the event
        :param location: Location of the event
        :param activities: List of activities planned for the event
        """
        self.name = name
        self.date = date
        self.location = location
        self.activities = activities

    def add_activity(self, activity: str):
        """
        Add an activity to the event.

        :param activity: Activity to be added
        """
        self.activities.append(activity)

    def get_event_details(self) -> Dict[str, str]:
        """
        Get the details of the event.

        :return: Dictionary containing event details
        """
        return {
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "location": self.location,
            "activities": self.activities
        }

def create_event_plan() -> Event:
    """
    Create a corporate event plan for a tech conference in Bogotá, Colombia.

    :return: An Event instance with planned activities
    """
    try:
        event_name = "Tech Conference 2023"
        event_date = datetime.date(2023, 11, 15)  # Example date
        event_location = "Bogotá, Colombia"
        
        # List of planned activities
        activities = [
            "Keynote Speech by Industry Leader",
            "Networking Lunch",
            "Panel Discussion on Emerging Technologies",
            "Team-building Exercise: Escape Room Challenge",
            "Evening Social: Tech Trivia Night",
            "Workshops on Latest Tech Trends"
        ]

        # Create the event
        tech_conference = Event(event_name, event_date, event_location, activities)
        return tech_conference

    except Exception as e:
        print(f"Error creating event plan: {e}")
        return None

def main():
    """
    Main function to execute the event planning.
    """
    event = create_event_plan()
    if event:
        event_details = event.get_event_details()
        print("Event Plan Created Successfully:")
        for key, value in event_details.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
```
