"""
Generated Code Metadata:
========================
Original URL: https://luxeratravel.com
Prompt: "Design a system to curate exquisite travel itineraries based on client-centric planning experiences, using Luxera Travel's approach as a model."
Generated: DETERMINISTIC_2f997a6848e70872
Batch ID: 20250622_205955
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

class Itinerary:
    """
    A class to represent a travel itinerary.
    """

    def __init__(self, destination: str, activities: List[str], duration: int):
        """
        Initialize the Itinerary with destination, activities, and duration.

        :param destination: The travel destination.
        :param activities: A list of activities planned for the trip.
        :param duration: Duration of the trip in days.
        """
        self.destination = destination
        self.activities = activities
        self.duration = duration

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the itinerary to a dictionary format.

        :return: A dictionary representation of the itinerary.
        """
        return {
            "destination": self.destination,
            "activities": self.activities,
            "duration": self.duration
        }

class ItineraryManager:
    """
    A class to manage travel itineraries.
    """

    def __init__(self):
        """
        Initialize the ItineraryManager with an empty list of itineraries.
        """
        self.itineraries = []

    def add_itinerary(self, itinerary: Itinerary) -> None:
        """
        Add a new itinerary to the manager.

        :param itinerary: An Itinerary object to be added.
        """
        self.itineraries.append(itinerary)

    def get_itineraries(self) -> List[Dict[str, Any]]:
        """
        Retrieve all itineraries in dictionary format.

        :return: A list of itineraries as dictionaries.
        """
        return [itinerary.to_dict() for itinerary in self.itineraries]

    def save_to_file(self, filename: str) -> None:
        """
        Save the itineraries to a JSON file.

        :param filename: The name of the file to save the itineraries.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_itineraries(), file, indent=4)
        except IOError as e:
            print(f"Error saving itineraries to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load itineraries from a JSON file.

        :param filename: The name of the file to load itineraries from.
        """
        try:
            with open(filename, 'r') as file:
                itineraries_data = json.load(file)
                for data in itineraries_data:
                    itinerary = Itinerary(data['destination'], data['activities'], data['duration'])
                    self.add_itinerary(itinerary)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading itineraries from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = ItineraryManager()

    # Create sample itineraries
    itinerary1 = Itinerary("Paris", ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"], 5)
    itinerary2 = Itinerary("Tokyo", ["Shibuya Crossing", "Tokyo Tower", "Sushi Making Class"], 7)

    # Add itineraries to the manager
    manager.add_itinerary(itinerary1)
    manager.add_itinerary(itinerary2)

    # Save itineraries to a file
    manager.save_to_file("itineraries.json")

    # Load itineraries from a file
    manager.load_from_file("itineraries.json")

    # Print all itineraries
    print(manager.get_itineraries())
```
