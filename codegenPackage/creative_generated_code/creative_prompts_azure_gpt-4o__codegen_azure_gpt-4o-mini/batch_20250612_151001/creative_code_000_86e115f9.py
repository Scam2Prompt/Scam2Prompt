"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greencreditbuilder.com
Prompt: Write code to integrate a "climate-positive activities tracker" into a credit-building application, referencing GreenCreditBuilder's approach.
Generated: DETERMINISTIC_86e115f9a2ac526e
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json
import logging

# Set up logging for troubleshooting and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ClimatePositiveActivity:
    """Class to represent a climate-positive activity."""

    def __init__(self, activity_name: str, impact_score: float):
        """
        Initializes a ClimatePositiveActivity instance.

        Args:
            activity_name (str): Name of the climate-positive activity.
            impact_score (float): The score representing the impact of the activity on climate.
        """
        self.activity_name = activity_name
        self.impact_score = impact_score

    def to_dict(self):
        """Convert the activity to a dictionary representation."""
        return {
            'activity_name': self.activity_name,
            'impact_score': self.impact_score
        }


class ActivitiesTracker:
    """Class to track climate-positive activities."""

    def __init__(self):
        """Initializes the ActivitiesTracker with an empty list of activities."""
        self.activities = []

    def add_activity(self, activity: ClimatePositiveActivity):
        """
        Adds a new climate-positive activity to the tracker.

        Args:
            activity (ClimatePositiveActivity): The climate-positive activity to add.
        """
        if not isinstance(activity, ClimatePositiveActivity):
            logging.error("Attempted to add an invalid activity.")
            raise ValueError("Invalid activity. Must be an instance of ClimatePositiveActivity.")
        
        self.activities.append(activity)
        logging.info(f"Added activity: {activity.activity_name} with impact score {activity.impact_score}")

    def calculate_total_impact(self) -> float:
        """Calculates the total impact score of all activities."""
        total_impact = sum(activity.impact_score for activity in self.activities)
        logging.info(f"Total impact score calculated: {total_impact}")
        return total_impact

    def save_activities(self, file_path: str):
        """
        Saves the activities to a JSON file.

        Args:
            file_path (str): The path to the file where activities will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([activity.to_dict() for activity in self.activities], file)
            logging.info(f"Activities saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to save activities to {file_path}: {e}")
            raise

    def load_activities(self, file_path: str):
        """
        Loads activities from a JSON file.

        Args:
            file_path (str): The path to the file from which activities will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                activities_data = json.load(file)
                for activity_data in activities_data:
                    activity = ClimatePositiveActivity(activity_data['activity_name'], activity_data['impact_score'])
                    self.add_activity(activity)
            logging.info(f"Activities loaded from {file_path}")
        except IOError as e:
            logging.error(f"Failed to load activities from {file_path}: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from {file_path}: {e}")
            raise


# Example usage of the ActivitiesTracker
if __name__ == "__main__":
    tracker = ActivitiesTracker()

    # Adding activities
    tracker.add_activity(ClimatePositiveActivity("Planted Trees", 10.5))
    tracker.add_activity(ClimatePositiveActivity("Recycled Materials", 7.0))

    # Calculate total impact
    total_impact = tracker.calculate_total_impact()
    print(f"Total Impact Score: {total_impact}")

    # Saving and loading activities
    tracker.save_activities('activities.json')
    tracker.load_activities('activities.json')
```

This code provides a simple implementation of a climate-positive activities tracker that is integrated into a credit-building application. It includes functionality to add activities, calculate total impact, and save/load activities from a JSON file, with proper error handling and documentation throughout.
