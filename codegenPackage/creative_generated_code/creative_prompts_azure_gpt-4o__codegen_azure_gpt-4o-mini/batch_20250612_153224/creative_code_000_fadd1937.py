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
from typing import List, Dict, Optional

class HikingTrip:
    """
    Class representing a hiking trip with a destination and date.
    """
    def __init__(self, destination: str, trip_date: datetime):
        self.destination = destination
        self.trip_date = trip_date

    def __repr__(self):
        return f"HikingTrip(destination={self.destination}, trip_date={self.trip_date})"


class HikingCalendar:
    """
    Class for managing a calendar of hiking trips.
    """
    def __init__(self):
        self.trips: List[HikingTrip] = []

    def add_trip(self, destination: str, trip_date: datetime) -> None:
        """
        Add a new hiking trip to the calendar.
        
        :param destination: The destination of the hiking trip.
        :param trip_date: The date of the hiking trip.
        """
        trip = HikingTrip(destination, trip_date)
        self.trips.append(trip)
        print(f"Trip added: {trip}")

    def filter_trips(self, month: Optional[int] = None, year: Optional[int] = None) -> List[HikingTrip]:
        """
        Filter trips by month and/or year.
        
        :param month: The month to filter by (1-12).
        :param year: The year to filter by (e.g., 2023).
        :return: A list of trips that match the specified month and year.
        """
        filtered_trips = []
        for trip in self.trips:
            if (month is None or trip.trip_date.month == month) and \
               (year is None or trip.trip_date.year == year):
                filtered_trips.append(trip)
        return filtered_trips

    def display_calendar(self, month: int, year: int) -> None:
        """
        Display the calendar for a specific month and year, along with the scheduled trips.
        
        :param month: The month for the calendar (1-12).
        :param year: The year for the calendar.
        """
        try:
            print(calendar.month(year, month))
            print("Scheduled trips:")
            trips_in_month = self.filter_trips(month=month, year=year)
            if not trips_in_month:
                print("No trips scheduled for this month.")
            else:
                for trip in trips_in_month:
                    print(f"- {trip.destination} on {trip.trip_date.strftime('%Y-%m-%d')}")
        except ValueError as e:
            print(f"Error displaying calendar: {e}")


def main():
    """
    Main function to demonstrate the hiking calendar system.
    """
    hiking_calendar = HikingCalendar()
    
    # Sample trips
    hiking_calendar.add_trip("Планината Фалакро", datetime(2023, 10, 15))
    hiking_calendar.add_trip("Остров Самотраки", datetime(2023, 10, 22))
    hiking_calendar.add_trip("Планината Фалакро", datetime(2023, 11, 5))

    # Display calendar for October 2023
    hiking_calendar.display_calendar(10, 2023)

    # Display calendar for November 2023
    hiking_calendar.display_calendar(11, 2023)

if __name__ == "__main__":
    main()
```
