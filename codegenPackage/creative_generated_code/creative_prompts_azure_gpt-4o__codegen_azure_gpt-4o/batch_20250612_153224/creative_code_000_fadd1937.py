"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bgalpina.com
Prompt: Write Python code to create a calendar system for scheduling hiking trips, including destinations like "Планината Фалакро" and "Остров Самотраки," with options to filter by month and year.
Generated: DETERMINISTIC_fadd1937814be4d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import calendar
from datetime import datetime
from typing import List

class HikingTrip:
    """
    A class representing a hiking trip.
    """
    def __init__(self, destination: str, date: datetime):
        self.destination = destination
        self.date = date

    def __str__(self):
        return f"{self.destination} on {self.date.strftime('%Y-%m-%d')}"

class HikingCalendar:
    """
    A class for managing hiking trips.
    """
    def __init__(self):
        self.trips = []  # List to store hiking trips

    def add_trip(self, destination: str, date: str):
        """
        Add a new hiking trip to the calendar.
        
        :param destination: Destination of the hiking trip
        :param date: Date of the hiking trip in 'YYYY-MM-DD' format
        :raises ValueError: If the date format is invalid
        """
        try:
            trip_date = datetime.strptime(date, '%Y-%m-%d')
            self.trips.append(HikingTrip(destination, trip_date))
            print(f"Trip to '{destination}' on {date} was successfully added.")
        except ValueError:
            print(f"Error: Invalid date format. Please use 'YYYY-MM-DD'.")

    def filter_trips(self, month: int, year: int) -> List[HikingTrip]:
        """
        Filter trips by month and year.
        
        :param month: Month to filter by (1-12)
        :param year: Year to filter by
        :return: List of trips happening in the specified month and year
        """
        return [trip for trip in self.trips if trip.date.month == month and trip.date.year == year]

    def display_trips(self, trips: List[HikingTrip]):
        """
        Display a list of trips.
        
        :param trips: List of HikingTrip objects
        """
        if trips:
            print("Scheduled Hiking Trips:")
            for trip in trips:
                print(f"- {trip}")
        else:
            print("No trips found for the specified month and year.")

def main():
    """
    Main function to interact with the hiking calendar system.
    """
    hiking_calendar = HikingCalendar()

    # Adding sample trips
    hiking_calendar.add_trip("Планината Фалакро", "2023-11-15")
    hiking_calendar.add_trip("Остров Самотраки", "2023-11-20")
    hiking_calendar.add_trip("Планината Фалакро", "2024-01-12")

    # Display all trips
    print("\nAll Trips:")
    hiking_calendar.display_trips(hiking_calendar.trips)

    # Filter trips by month and year
    print("\nTrips in November 2023:")
    november_trips = hiking_calendar.filter_trips(month=11, year=2023)
    hiking_calendar.display_trips(november_trips)

    print("\nTrips in January 2024:")
    january_trips = hiking_calendar.filter_trips(month=1, year=2024)
    hiking_calendar.display_trips(january_trips)

if __name__ == "__main__":
    main()
```
