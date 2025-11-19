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
# Import required libraries
from datetime import datetime, timedelta
from typing import List, Dict

class SafariItinerary:
    def __init__(self, days: int, location: str):
        """
        Initialize a SafariItinerary object.

        Args:
        days (int): The number of days for the safari.
        location (str): The location of the safari.
        """
        self.days = days
        self.location = location
        self.itinerary = []

    def add_day(self, date: str, activity: str, location: str, accommodation: str):
        """
        Add a day to the itinerary.

        Args:
        date (str): The date of the day (in YYYY-MM-DD format).
        activity (str): The activity for the day.
        location (str): The location of the activity.
        accommodation (str): The accommodation for the night.
        """
        self.itinerary.append({
            "date": date,
            "activity": activity,
            "location": location,
            "accommodation": accommodation
        })

    def print_itinerary(self):
        """
        Print the itinerary.
        """
        for day in self.itinerary:
            print(f"Date: {day['date']}")
            print(f"Activity: {day['activity']}")
            print(f"Location: {day['location']}")
            print(f"Accommodation: {day['accommodation']}\n")


class LuxurySafari:
    def __init__(self, name: str):
        """
        Initialize a LuxurySafari object.

        Args:
        name (str): The name of the safari.
        """
        self.name = name
        self.itinerary = SafariItinerary(9, "Amboseli and Masai Mara")

    def generate_itinerary(self):
        """
        Generate a custom itinerary for a 9-day luxury safari.
        """
        start_date = datetime.now() + timedelta(days=1)
        start_date = start_date.strftime("%Y-%m-%d")

        # Day 1: Arrival in Amboseli
        self.itinerary.add_day(start_date, "Arrive in Amboseli", "Amboseli National Park", "Sabi Sabi Earth Lodge")

        # Day 2: Game drive in Amboseli
        next_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Game drive in Amboseli", "Amboseli National Park", "Sabi Sabi Earth Lodge")

        # Day 3: Travel to Masai Mara
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Travel to Masai Mara", "Masai Mara National Reserve", "Mahali Mzuri")

        # Day 4: Game drive in Masai Mara
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Game drive in Masai Mara", "Masai Mara National Reserve", "Mahali Mzuri")

        # Day 5: Full day game drive in Masai Mara
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Full day game drive in Masai Mara", "Masai Mara National Reserve", "Mahali Mzuri")

        # Day 6: Morning game drive in Masai Mara
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Morning game drive in Masai Mara", "Masai Mara National Reserve", "Mahali Mzuri")

        # Day 7: Relaxation day at Mahali Mzuri
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Relaxation day at Mahali Mzuri", "Mahali Mzuri", "Mahali Mzuri")

        # Day 8: Game drive and depart
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Game drive and depart", "Masai Mara National Reserve", "Mahali Mzuri")

        # Day 9: Departure
        next_date = (datetime.strptime(next_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        self.itinerary.add_day(next_date, "Departure", "Nairobi", "Nairobi Hotel")

    def print_itinerary(self):
        """
        Print the itinerary.
        """
        print(f"Luxury Safari: {self.name}\n")
        self.itinerary.print_itinerary()


def main():
    try:
        safari = LuxurySafari("Amboseli and Masai Mara Luxury Safari")
        safari.generate_itinerary()
        safari.print_itinerary()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
