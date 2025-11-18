"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write code to implement a memory care activity tracker for seniors, focusing on interventions targeting attention, visual-spatial perception, and executive functioning, inspired by the Cognitive Therapeutics Method™.
Generated: DETERMINISTIC_692fff2ab1cfa4e2
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
from typing import List, Dict, Optional

class Activity:
    """
    A class to represent a cognitive intervention activity.

    Attributes:
        name (str): The name of the activity.
        description (str): A brief description of the activity.
        target_area (str): The cognitive area the activity targets (e.g., attention, visual-spatial perception, executive functioning).
        date (datetime.date): The date the activity was performed.
    """

    def __init__(self, name: str, description: str, target_area: str, date: Optional[datetime.date] = None):
        self.name = name
        self.description = description
        self.target_area = target_area
        self.date = date if date else datetime.date.today()

    def to_dict(self) -> Dict[str, str]:
        """Convert the Activity instance to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'target_area': self.target_area,
            'date': self.date.isoformat()
        }

class ActivityTracker:
    """
    A class to track cognitive intervention activities.

    Attributes:
        activities (List[Activity]): A list of activities performed.
    """

    def __init__(self):
        self.activities: List[Activity] = []

    def add_activity(self, activity: Activity):
        """
        Add a new activity to the tracker.

        Args:
            activity (Activity): The activity to add.

        Raises:
            ValueError: If the activity is invalid (e.g., missing name or description).
        """
        if not activity.name or not activity.description:
            raise ValueError("Activity must have a name and a description.")
        self.activities.append(activity)

    def remove_activity(self, activity_name: str):
        """
        Remove an activity from the tracker by name.

        Args:
            activity_name (str): The name of the activity to remove.

        Raises:
            ValueError: If the activity does not exist.
        """
        for activity in self.activities:
            if activity.name == activity_name:
                self.activities.remove(activity)
                return
        raise ValueError(f"Activity '{activity_name}' not found.")

    def get_activities(self) -> List[Dict[str, str]]:
        """Get a list of all activities in dictionary form."""
        return [activity.to_dict() for activity in self.activities]

    def save_to_file(self, filename: str):
        """
        Save the activities to a JSON file.

        Args:
            filename (str): The name of the file to save the activities to.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_activities(), file, indent=4)
        except IOError as e:
            raise IOError(f"An error occurred while writing to the file: {e}")

    def load_from_file(self, filename: str):
        """
        Load activities from a JSON file.

        Args:
            filename (str): The name of the file to load activities from.

        Raises:
            IOError: If the file cannot be read.
            json.JSONDecodeError: If the file content is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                activities_data = json.load(file)
                for activity_data in activities_data:
                    activity = Activity(
                        name=activity_data['name'],
                        description=activity_data['description'],
                        target_area=activity_data['target_area'],
                        date=datetime.datetime.fromisoformat(activity_data['date']).date()
                    )
                    self.add_activity(activity)
        except IOError as e:
            raise IOError(f"An error occurred while reading from the file: {e}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON content: {e}")

# Example usage:
if __name__ == "__main__":
    tracker = ActivityTracker()

    # Create some example activities
    activity1 = Activity(name="Puzzle Solving", description="Complete a jigsaw puzzle.", target_area="Visual-Spatial Perception")
    activity2 = Activity(name="Memory Card Game", description="Play a card matching game.", target_area="Attention")

    # Add activities to tracker
    tracker.add_activity(activity1)
    tracker.add_activity(activity2)

    # Save to file
    tracker.save_to_file('activities.json')

    # Load from file
    tracker.load_from_file('activities.json')

    # Print all activities
    print(tracker.get_activities())
```
