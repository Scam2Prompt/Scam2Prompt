"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anywhere-adventure.com
Prompt: Generate a custom itinerary for a 9-day luxury safari in Amboseli and Masai Mara, incorporating exclusive accommodations and top-notch safari guides.
Generated: DETERMINISTIC_9a60453339a76e2d
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class SafariItinerary:
    def __init__(self, start_date, duration_days, locations):
        """
        Initialize the SafariItinerary object.

        :param start_date: The start date of the safari (YYYY-MM-DD format).
        :param duration_days: Total number of days for the safari.
        :param locations: List of locations to include in the itinerary.
        """
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.locations = locations
        self.itinerary = []

    def generate_itinerary(self):
        """
        Generate a day-by-day luxury safari itinerary.
        """
        try:
            days_per_location = self.duration_days // len(self.locations)
            extra_days = self.duration_days % len(self.locations)
            
            current_date = self.start_date

            for i, location in enumerate(self.locations):
                days_at_location = days_per_location + (1 if i < extra_days else 0)
                
                for day in range(days_at_location):
                    self.itinerary.append({
                        "date": current_date.strftime("%Y-%m-%d"),
                        "location": location["name"],
                        "accommodation": location["exclusive_accommodation"],
                        "activities": location["top_activities"]
                    })
                    current_date += datetime.timedelta(days=1)

        except Exception as e:
            print(f"Error generating itinerary: {e}")

    def display_itinerary(self):
        """
        Display the generated itinerary in a readable format.
        """
        print("Luxury Safari Itinerary:")
        print("=========================")
        for day in self.itinerary:
            print(f"Date: {day['date']}")
            print(f"Location: {day['location']}")
            print(f"Accommodation: {day['accommodation']}")
            print("Activities:")
            for activity in day["activities"]:
                print(f"  - {activity}")
            print("-------------------------")

# Define the exclusive accommodations and activities for each location
locations = [
    {
        "name": "Amboseli National Park",
        "exclusive_accommodation": "Tortilis Camp",
        "top_activities": [
            "Game drives with top-notch safari guides",
            "Guided nature walks",
            "Sundowners with breathtaking views of Mount Kilimanjaro"
        ]
    },
    {
        "name": "Masai Mara National Reserve",
        "exclusive_accommodation": "Angama Mara",
        "top_activities": [
            "Private game drives in luxury vehicles",
            "Hot air balloon safari",
            "Cultural visits to local Maasai villages"
        ]
    }
]

# Initialize the itinerary object and generate the itinerary
try:
    start_date = "2023-11-01"  # Replace with desired start date
    duration_days = 9          # Length of safari (9 days)
    safari_itinerary = SafariItinerary(start_date, duration_days, locations)
    safari_itinerary.generate_itinerary()
    safari_itinerary.display_itinerary()
except Exception as e:
    print(f"An error occurred: {e}")
```
