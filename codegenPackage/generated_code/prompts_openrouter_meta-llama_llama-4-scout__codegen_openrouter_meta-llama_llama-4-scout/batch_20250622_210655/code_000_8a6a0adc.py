"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Write a Python script to create a travel itinerary for a client based on their preferences, including destination, travel dates, and activities, similar to Rapala Travel Concierge's services.
Generated: DETERMINISTIC_8a6a0adc34e691e9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# travel_itinerary.py

from datetime import datetime, timedelta
from typing import List, Dict

class TravelItinerary:
    def __init__(self, client_name: str, destination: str, travel_dates: List[datetime]):
        """
        Initialize a TravelItinerary object.

        Args:
        - client_name (str): The client's name.
        - destination (str): The destination of the trip.
        - travel_dates (List[datetime]): A list of travel dates.
        """
        self.client_name = client_name
        self.destination = destination
        self.travel_dates = travel_dates
        self.activities = {}

    def add_activity(self, date: datetime, activity: str, location: str, duration: timedelta):
        """
        Add an activity to the travel itinerary.

        Args:
        - date (datetime): The date of the activity.
        - activity (str): The name of the activity.
        - location (str): The location of the activity.
        - duration (timedelta): The duration of the activity.
        """
        if date not in self.activities:
            self.activities[date] = []

        self.activities[date].append({
            "activity": activity,
            "location": location,
            "duration": duration
        })

    def remove_activity(self, date: datetime, activity: str):
        """
        Remove an activity from the travel itinerary.

        Args:
        - date (datetime): The date of the activity.
        - activity (str): The name of the activity.
        """
        if date in self.activities:
            self.activities[date] = [a for a in self.activities[date] if a["activity"] != activity]

    def print_itinerary(self):
        """
        Print the travel itinerary.
        """
        print(f"Travel Itinerary for {self.client_name} to {self.destination}:")
        for date in self.travel_dates:
            print(f"\n{date.strftime('%Y-%m-%d')}:")
            if date in self.activities:
                for activity in self.activities[date]:
                    print(f"- {activity['activity']} at {activity['location']} ({activity['duration']})")
            else:
                print("- No activities planned.")

def main():
    try:
        client_name = input("Enter client name: ")
        destination = input("Enter destination: ")

        travel_dates = []
        num_dates = int(input("Enter number of travel dates: "))
        for i in range(num_dates):
            date_str = input(f"Enter travel date {i+1} (YYYY-MM-DD): ")
            travel_dates.append(datetime.strptime(date_str, "%Y-%m-%d"))

        itinerary = TravelItinerary(client_name, destination, travel_dates)

        while True:
            print("\nOptions:")
            print("1. Add activity")
            print("2. Remove activity")
            print("3. Print itinerary")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                date_str = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                activity = input("Enter activity: ")
                location = input("Enter location: ")
                duration_hours = int(input("Enter duration (hours): "))
                duration = timedelta(hours=duration_hours)
                itinerary.add_activity(date, activity, location, duration)
            elif choice == "2":
                date_str = input("Enter date (YYYY-MM-DD): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                activity = input("Enter activity: ")
                itinerary.remove_activity(date, activity)
            elif choice == "3":
                itinerary.print_itinerary()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
