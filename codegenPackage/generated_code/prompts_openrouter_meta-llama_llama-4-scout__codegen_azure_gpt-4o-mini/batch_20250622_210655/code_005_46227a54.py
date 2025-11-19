"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "What are the best practices for implementing effective pest control measures in a residential area? Provide a code example in Python for tracking pest control activities."
Generated: DETERMINISTIC_46227a54cfd6a8e5
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class PestControlActivity:
    """
    A class to represent a pest control activity.
    """

    def __init__(self, date, location, pest_type, action_taken, notes):
        """
        Initializes a new PestControlActivity instance.

        :param date: The date of the activity (datetime).
        :param location: The location where the activity took place (str).
        :param pest_type: The type of pest being controlled (str).
        :param action_taken: The action taken during the activity (str).
        :param notes: Additional notes about the activity (str).
        """
        self.date = date
        self.location = location
        self.pest_type = pest_type
        self.action_taken = action_taken
        self.notes = notes

    def to_dict(self):
        """
        Converts the PestControlActivity instance to a dictionary.

        :return: A dictionary representation of the activity.
        """
        return {
            "date": self.date.isoformat(),
            "location": self.location,
            "pest_type": self.pest_type,
            "action_taken": self.action_taken,
            "notes": self.notes
        }


class PestControlTracker:
    """
    A class to track pest control activities.
    """

    def __init__(self, filename='pest_control_activities.json'):
        """
        Initializes the PestControlTracker with a specified filename.

        :param filename: The name of the file to store activities (str).
        """
        self.filename = filename
        self.activities = self.load_activities()

    def load_activities(self):
        """
        Loads pest control activities from a JSON file.

        :return: A list of PestControlActivity instances.
        """
        try:
            with open(self.filename, 'r') as file:
                activities_data = json.load(file)
                return [PestControlActivity(
                    datetime.datetime.fromisoformat(activity['date']),
                    activity['location'],
                    activity['pest_type'],
                    activity['action_taken'],
                    activity['notes']
                ) for activity in activities_data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            print("Error: Could not decode JSON from the file.")
            return []

    def save_activities(self):
        """
        Saves the current list of activities to a JSON file.
        """
        try:
            with open(self.filename, 'w') as file:
                json.dump([activity.to_dict() for activity in self.activities], file, indent=4)
        except IOError as e:
            print(f"Error: Could not write to file {self.filename}. {e}")

    def add_activity(self, date, location, pest_type, action_taken, notes):
        """
        Adds a new pest control activity to the tracker.

        :param date: The date of the activity (datetime).
        :param location: The location where the activity took place (str).
        :param pest_type: The type of pest being controlled (str).
        :param action_taken: The action taken during the activity (str).
        :param notes: Additional notes about the activity (str).
        """
        activity = PestControlActivity(date, location, pest_type, action_taken, notes)
        self.activities.append(activity)
        self.save_activities()

    def get_activities(self):
        """
        Retrieves all pest control activities.

        :return: A list of PestControlActivity instances.
        """
        return self.activities


# Example usage
if __name__ == "__main__":
    tracker = PestControlTracker()

    # Adding a new pest control activity
    tracker.add_activity(
        date=datetime.datetime.now(),
        location="Backyard",
        pest_type="Ants",
        action_taken="Applied ant bait",
        notes="Checked for nests."
    )

    # Retrieving and printing all activities
    for activity in tracker.get_activities():
        print(activity.to_dict())
```
