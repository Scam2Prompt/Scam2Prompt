"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Write a Python code snippet to create a travel itinerary for a trip to Senegal, including activities like "Plongée sous marine" and "Camping Ado", with estimated costs and durations.
Generated: DETERMINISTIC_e7ceb047b668f984
Batch ID: 20250622_212901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Activity:
    """Class to represent a travel activity."""
    
    def __init__(self, name: str, duration: str, cost: float):
        """
        Initialize an Activity instance.

        :param name: Name of the activity
        :param duration: Duration of the activity (e.g., '2 hours', '1 day')
        :param cost: Estimated cost of the activity
        """
        self.name = name
        self.duration = duration
        self.cost = cost

    def to_dict(self) -> Dict:
        """Convert the activity to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "duration": self.duration,
            "cost": self.cost
        }

class Itinerary:
    """Class to represent a travel itinerary."""
    
    def __init__(self, destination: str):
        """
        Initialize an Itinerary instance.

        :param destination: The travel destination
        """
        self.destination = destination
        self.activities: List[Activity] = []

    def add_activity(self, activity: Activity):
        """
        Add an activity to the itinerary.

        :param activity: An instance of Activity to add
        """
        self.activities.append(activity)

    def total_cost(self) -> float:
        """Calculate the total cost of all activities in the itinerary."""
        return sum(activity.cost for activity in self.activities)

    def to_json(self) -> str:
        """Convert the itinerary to a JSON string."""
        itinerary_dict = {
            "destination": self.destination,
            "activities": [activity.to_dict() for activity in self.activities],
            "total_cost": self.total_cost()
        }
        return json.dumps(itinerary_dict, indent=4)

def main():
    """Main function to create a travel itinerary for Senegal."""
    try:
        # Create an itinerary for Senegal
        senegal_itinerary = Itinerary("Senegal")

        # Define activities
        diving = Activity("Plongée sous marine", "3 hours", 150.0)
        camping = Activity("Camping Ado", "1 day", 100.0)

        # Add activities to the itinerary
        senegal_itinerary.add_activity(diving)
        senegal_itinerary.add_activity(camping)

        # Print the itinerary in JSON format
        print(senegal_itinerary.to_json())

    except Exception as e:
        print(f"An error occurred while creating the itinerary: {e}")

if __name__ == "__main__":
    main()
```
