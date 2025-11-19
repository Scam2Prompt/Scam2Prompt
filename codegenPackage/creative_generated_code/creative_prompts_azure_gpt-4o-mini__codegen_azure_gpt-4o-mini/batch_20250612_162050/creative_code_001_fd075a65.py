"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Write a Python script that lists activities and seminars for a wine festival, similar to those offered at FestiVin Caraquet.
Generated: DETERMINISTIC_fd075a65a7e0c46f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class WineFestival:
    def __init__(self, festival_name: str):
        """
        Initialize the WineFestival class with a festival name.

        :param festival_name: Name of the wine festival.
        """
        self.festival_name = festival_name
        self.activities: List[Dict[str, Any]] = []

    def add_activity(self, name: str, description: str, date: str, time: str):
        """
        Add an activity to the wine festival.

        :param name: Name of the activity.
        :param description: Description of the activity.
        :param date: Date of the activity.
        :param time: Time of the activity.
        """
        activity = {
            'name': name,
            'description': description,
            'date': date,
            'time': time
        }
        self.activities.append(activity)

    def list_activities(self) -> None:
        """
        List all activities in the festival.
        """
        if not self.activities:
            print("No activities available.")
            return

        print(f"Activities for {self.festival_name}:")
        for activity in self.activities:
            print(f"{activity['name']} - {activity['description']} on {activity['date']} at {activity['time']}")

    def save_activities(self, filepath: str) -> None:
        """
        Save the list of activities to a JSON file.

        :param filepath: Path to the JSON file where activities will be saved.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.activities, file, indent=4)
            print(f"Activities saved to {filepath}.")
        except IOError as e:
            print(f"Error saving activities to file: {e}")

    def load_activities(self, filepath: str) -> None:
        """
        Load activities from a JSON file.

        :param filepath: Path to the JSON file to load activities from.
        """
        try:
            with open(filepath, 'r') as file:
                self.activities = json.load(file)
            print(f"Activities loaded from {filepath}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading activities from file: {e}")

if __name__ == "__main__":
    festival = WineFestival("FestiVin Caraquet")

    # Adding sample activities
    festival.add_activity("Wine Tasting", "Experience a variety of wines from local vineyards.", "2023-09-15", "14:00")
    festival.add_activity("Grape Stomping", "Join us for some fun stomping grapes!", "2023-09-16", "10:00")
    festival.add_activity("Cooking with Wine", "Learn to cook delicious meals using wine.", "2023-09-17", "12:00")

    # List all activities
    festival.list_activities()

    # Save activities to a file
    festival.save_activities("activities.json")

    # Load activities from a file (for demonstration)
    festival.load_activities("activities.json")
```
