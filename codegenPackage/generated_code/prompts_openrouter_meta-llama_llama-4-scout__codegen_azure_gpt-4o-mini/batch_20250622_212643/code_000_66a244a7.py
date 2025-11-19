"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Generate a Python script to create a customized itinerary for a 9-day Kenyan safari trip, including destinations like Amboseli, Masai Mara, Naivasha, and Nakuru."
Generated: DETERMINISTIC_66a244a7b784871c
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class Itinerary:
    def __init__(self, start_date, duration):
        """
        Initialize the itinerary with a start date and duration.
        
        :param start_date: The starting date of the trip (YYYY-MM-DD).
        :param duration: The total number of days for the trip.
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration = duration
        self.destinations = []
    
    def add_destination(self, name, days, activities):
        """
        Add a destination to the itinerary.
        
        :param name: The name of the destination.
        :param days: The number of days to spend at the destination.
        :param activities: A list of activities to do at the destination.
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than zero.")
        if sum(dest['days'] for dest in self.destinations) + days > self.duration:
            raise ValueError("Total days exceed the trip duration.")
        
        destination = {
            'name': name,
            'days': days,
            'activities': activities,
            'start_date': self.start_date + timedelta(days=sum(dest['days'] for dest in self.destinations)),
        }
        self.destinations.append(destination)

    def generate_itinerary(self):
        """
        Generate the complete itinerary as a structured dictionary.
        
        :return: A dictionary containing the itinerary details.
        """
        itinerary = {
            'trip_start_date': self.start_date.strftime("%Y-%m-%d"),
            'duration': self.duration,
            'destinations': self.destinations
        }
        return itinerary

    def save_itinerary(self, filename):
        """
        Save the itinerary to a JSON file.
        
        :param filename: The name of the file to save the itinerary.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_itinerary(), file, indent=4)
            print(f"Itinerary saved to {filename}")
        except IOError as e:
            print(f"Error saving itinerary: {e}")

def main():
    # Create a 9-day itinerary for a Kenyan safari trip
    itinerary = Itinerary(start_date="2023-10-01", duration=9)

    # Add destinations with activities
    itinerary.add_destination("Amboseli National Park", 2, [
        "Game drives to see elephants",
        "Visit Observation Hill for panoramic views"
    ])
    itinerary.add_destination("Masai Mara", 4, [
        "Wildlife safari and game drives",
        "Hot air balloon ride over the savannah",
        "Visit a Maasai village"
    ])
    itinerary.add_destination("Lake Naivasha", 1, [
        "Boat ride to see hippos and birds",
        "Visit Crescent Island"
    ])
    itinerary.add_destination("Lake Nakuru National Park", 2, [
        "Bird watching, especially flamingos",
        "Game drives to see rhinos and other wildlife"
    ])

    # Save the itinerary to a JSON file
    itinerary.save_itinerary("kenyan_safari_itinerary.json")

if __name__ == "__main__":
    main()
```
