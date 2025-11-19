"""
Generated Code Metadata:
========================
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write code to implement a memory care activity tracker for seniors, focusing on interventions targeting attention, visual-spatial perception, and executive functioning, inspired by the Cognitive Therapeutics Method™.
Generated: DETERMINISTIC_692fff2ab1cfa4e2
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Activity:
    """Class to represent an activity for memory care."""
    
    def __init__(self, name: str, description: str, category: str):
        self.name = name
        self.description = description
        self.category = category
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the activity to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "timestamp": self.timestamp.isoformat()
        }

class ActivityTracker:
    """Class to track activities for memory care interventions."""
    
    def __init__(self):
        self.activities: List[Activity] = []

    def add_activity(self, name: str, description: str, category: str) -> None:
        """Add a new activity to the tracker."""
        if not name or not description or not category:
            raise ValueError("Activity name, description, and category must not be empty.")
        
        activity = Activity(name, description, category)
        self.activities.append(activity)

    def get_activities(self) -> List[Dict[str, Any]]:
        """Retrieve all activities as a list of dictionaries."""
        return [activity.to_dict() for activity in self.activities]

    def save_to_file(self, filename: str) -> None:
        """Save activities to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_activities(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load activities from a JSON file."""
        try:
            with open(filename, 'r') as file:
                activities_data = json.load(file)
                for activity_data in activities_data:
                    activity = Activity(
                        name=activity_data['name'],
                        description=activity_data['description'],
                        category=activity_data['category']
                    )
                    activity.timestamp = datetime.fromisoformat(activity_data['timestamp'])
                    self.activities.append(activity)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    tracker = ActivityTracker()
    
    # Adding activities
    try:
        tracker.add_activity("Puzzle Solving", "Engage in a jigsaw puzzle.", "Visual-Spatial")
        tracker.add_activity("Memory Game", "Play a card matching game.", "Attention")
        tracker.add_activity("Planning a Meal", "Plan a week's meals.", "Executive Functioning")
    except ValueError as e:
        print(f"Error adding activity: {e}")

    # Saving activities to a file
    tracker.save_to_file("activities.json")

    # Loading activities from a file
    tracker.load_from_file("activities.json")

    # Displaying all activities
    print(tracker.get_activities())
```
