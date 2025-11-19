"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Generate a Python code snippet to create a simple itinerary planner for a travel agency like Rehiletes that offers customized trips to various destinations in Mexico."
Generated: DETERMINISTIC_db76e4df4d45559e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class ItineraryPlanner:
    def __init__(self):
        """Initialize the itinerary planner with an empty itinerary."""
        self.itinerary = []

    def add_destination(self, destination: str, activities: List[str], duration: int) -> None:
        """
        Add a destination to the itinerary.

        Args:
            destination (str): The name of the destination.
            activities (List[str]): A list of activities planned at the destination.
            duration (int): The duration of stay in days at the destination.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        self.itinerary.append({
            "destination": destination,
            "activities": activities,
            "duration": duration
        })

    def remove_destination(self, destination: str) -> None:
        """
        Remove a destination from the itinerary.

        Args:
            destination (str): The name of the destination to remove.
        """
        self.itinerary = [item for item in self.itinerary if item["destination"] != destination]

    def get_itinerary(self) -> List[Dict[str, Any]]:
        """Return the current itinerary."""
        return self.itinerary

    def save_itinerary(self, filename: str) -> None:
        """
        Save the itinerary to a JSON file.

        Args:
            filename (str): The name of the file to save the itinerary.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.itinerary, file, indent=4)
        except IOError as e:
            print(f"Error saving itinerary to file: {e}")

    def load_itinerary(self, filename: str) -> None:
        """
        Load an itinerary from a JSON file.

        Args:
            filename (str): The name of the file to load the itinerary from.
        """
        try:
            with open(filename, 'r') as file:
                self.itinerary = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading itinerary from file: {e}")

# Example usage
if __name__ == "__main__":
    planner = ItineraryPlanner()
    planner.add_destination("Cancun", ["Beach", "Snorkeling"], 5)
    planner.add_destination("Mexico City", ["Museums", "Food Tour"], 3)
    
    print("Current Itinerary:")
    print(planner.get_itinerary())
    
    planner.save_itinerary("itinerary.json")
    planner.remove_destination("Cancun")
    
    print("Updated Itinerary:")
    print(planner.get_itinerary())
    
    planner.load_itinerary("itinerary.json")
    print("Loaded Itinerary:")
    print(planner.get_itinerary())
```
