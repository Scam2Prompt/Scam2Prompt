"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Write a script to automate the creation of travel itineraries for destinations like Petra in Jordan or the Pyramids in Egypt, based on the tour descriptions provided by Skyline International Agent.
Generated: DETERMINISTIC_723cf865895637b0
Batch ID: 20250612_153224
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
from typing import List, Dict

class Itinerary:
    """
    A class to represent a travel itinerary.
    """

    def __init__(self, destination: str, activities: List[str], travel_dates: Dict[str, str]):
        """
        Initializes the Itinerary class with destination, activities, and travel dates.

        :param destination: The travel destination (e.g., Petra, Pyramids).
        :param activities: List of activities planned for the destination.
        :param travel_dates: Dictionary containing start and end date of travel.
        """
        self.destination = destination
        self.activities = activities
        self.travel_dates = travel_dates

    def to_dict(self) -> Dict[str, any]:
        """
        Converts the Itinerary instance to a dictionary format for easy serialization.

        :return: A dictionary representation of the itinerary.
        """
        return {
            'destination': self.destination,
            'activities': self.activities,
            'travel_dates': self.travel_dates,
        }

    def display_itinerary(self) -> None:
        """
        Displays the itinerary in a user-friendly format.
        """
        print(f"Itinerary for {self.destination}:")
        print(f"Travel Dates: {self.travel_dates['start']} to {self.travel_dates['end']}")
        print("Activities:")
        for activity in self.activities:
            print(f"- {activity}")


def create_itinerary(destination: str, activities: List[str], start_date: str, end_date: str) -> Itinerary:
    """
    Creates an itinerary for a specified destination.

    :param destination: The travel destination.
    :param activities: List of planned activities.
    :param start_date: The start date of the travel (YYYY-MM-DD).
    :param end_date: The end date of the travel (YYYY-MM-DD).
    :return: An Itinerary object.
    """
    try:
        # Validate date formats
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')

        # Generate travel dates dictionary
        travel_dates = {'start': start_date, 'end': end_date}
        
        # Create an Itinerary object
        itinerary = Itinerary(destination, activities, travel_dates)
        return itinerary
    except ValueError as e:
        print(f"Error in date format: {e}")
        raise


def save_itinerary_to_file(itinerary: Itinerary, filename: str) -> None:
    """
    Saves the itinerary to a JSON file.

    :param itinerary: The Itinerary object to save.
    :param filename: The filename where the itinerary will be saved.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(itinerary.to_dict(), file, indent=4)
        print(f"Itinerary saved to {filename}")
    except IOError as e:
        print(f"Error saving itinerary to file: {e}")
        raise


# Example usage
if __name__ == '__main__':
    destination = "Petra, Jordan"
    activities = [
        "Visit the Treasury",
        "Explore the Monastery",
        "Hike the Al-Siq",
        "Sunset at the Royal Tombs"
    ]
    start_date = "2023-12-01"
    end_date = "2023-12-07"

    try:
        # Create an itinerary
        itinerary = create_itinerary(destination, activities, start_date, end_date)

        # Display the created itinerary
        itinerary.display_itinerary()

        # Save the itinerary to a file
        save_itinerary_to_file(itinerary, 'itinerary_petrapyramids.json')
        
    except Exception as e:
        print(f"An error occurred while creating the itinerary: {e}")
```
