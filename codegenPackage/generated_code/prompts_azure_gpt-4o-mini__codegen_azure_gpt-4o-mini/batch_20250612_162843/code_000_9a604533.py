"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Generate a custom itinerary for a 9-day luxury safari in Amboseli and Masai Mara, incorporating exclusive accommodations and top-notch safari guides.
Generated: DETERMINISTIC_9a60453339a76e2d
Batch ID: 20250612_162843
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

class SafariItinerary:
    def __init__(self, start_date, duration, accommodations, guides):
        """
        Initialize the SafariItinerary with start date, duration, accommodations, and guides.

        :param start_date: The starting date of the safari (YYYY-MM-DD).
        :param duration: The total number of days for the safari.
        :param accommodations: A list of exclusive accommodations.
        :param guides: A list of top-notch safari guides.
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration = duration
        self.accommodations = accommodations
        self.guides = guides
        self.itinerary = []

    def generate_itinerary(self):
        """
        Generate a detailed itinerary for the safari.
        """
        try:
            for day in range(self.duration):
                date = self.start_date + timedelta(days=day)
                if day < 5:  # First 5 days in Amboseli
                    location = "Amboseli National Park"
                    accommodation = self.accommodations[0]  # First accommodation
                    guide = self.guides[0]  # First guide
                else:  # Last 4 days in Masai Mara
                    location = "Masai Mara National Reserve"
                    accommodation = self.accommodations[1]  # Second accommodation
                    guide = self.guides[1]  # Second guide

                self.itinerary.append({
                    "day": day + 1,
                    "date": date.strftime("%Y-%m-%d"),
                    "location": location,
                    "accommodation": accommodation,
                    "guide": guide,
                    "activities": self.get_daily_activities(location)
                })
        except Exception as e:
            print(f"Error generating itinerary: {e}")

    def get_daily_activities(self, location):
        """
        Define daily activities based on the location.

        :param location: The location of the safari (Amboseli or Masai Mara).
        :return: A list of activities for the day.
        """
        activities = {
            "Amboseli National Park": [
                "Morning game drive",
                "Visit to a Maasai village",
                "Evening sundowner at Observation Hill"
            ],
            "Masai Mara National Reserve": [
                "Hot air balloon ride",
                "Full-day game drive with picnic lunch",
                "Visit to a local Maasai community"
            ]
        }
        return activities.get(location, [])

    def save_itinerary(self, filename):
        """
        Save the generated itinerary to a JSON file.

        :param filename: The name of the file to save the itinerary.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.itinerary, file, indent=4)
            print(f"Itinerary saved to {filename}")
        except IOError as e:
            print(f"Error saving itinerary: {e}")

# Example usage
if __name__ == "__main__":
    accommodations = [
        "Ol Tukai Lodge, Amboseli",
        "Mara Serena Safari Lodge, Masai Mara"
    ]
    guides = [
        "John Doe - Expert in wildlife photography",
        "Jane Smith - Experienced wildlife tracker"
    ]

    safari = SafariItinerary(start_date="2023-12-01", duration=9, accommodations=accommodations, guides=guides)
    safari.generate_itinerary()
    safari.save_itinerary("safari_itinerary.json")
```
