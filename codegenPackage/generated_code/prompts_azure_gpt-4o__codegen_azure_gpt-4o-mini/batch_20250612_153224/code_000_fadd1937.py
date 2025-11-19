"""
Generated Code Metadata:
========================
Original URL: https://bgalpina.com
Prompt: Write Python code to create a calendar system for scheduling hiking trips, including destinations like "Планината Фалакро" and "Остров Самотраки," with options to filter by month and year.
Generated: DETERMINISTIC_fadd1937814be4d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import calendar
from datetime import datetime
from typing import List, Dict, Optional

class HikingTrip:
    """Class to represent a hiking trip."""
    
    def __init__(self, destination: str, date: datetime):
        self.destination = destination
        self.date = date

    def __repr__(self):
        return f"HikingTrip(destination='{self.destination}', date='{self.date.strftime('%Y-%m-%d')}')"


class HikingCalendar:
    """Class to manage a calendar of hiking trips."""
    
    def __init__(self):
        self.trips: List[HikingTrip] = []

    def add_trip(self, destination: str, date: str) -> None:
        """Add a new hiking trip to the calendar.

        Args:
            destination (str): The destination of the hiking trip.
            date (str): The date of the hiking trip in 'YYYY-MM-DD' format.
        """
        try:
            trip_date = datetime.strptime(date, '%Y-%m-%d')
            new_trip = HikingTrip(destination, trip_date)
            self.trips.append(new_trip)
            print(f"Trip added: {new_trip}")
        except ValueError as e:
            print(f"Error adding trip: {e}. Please use 'YYYY-MM-DD' format.")

    def filter_trips(self, year: Optional[int] = None, month: Optional[int] = None) -> List[HikingTrip]:
        """Filter trips by year and/or month.

        Args:
            year (Optional[int]): The year to filter by.
            month (Optional[int]): The month to filter by.

        Returns:
            List[HikingTrip]: A list of trips that match the filters.
        """
        filtered_trips = self.trips
        
        if year is not None:
            filtered_trips = [trip for trip in filtered_trips if trip.date.year == year]
        
        if month is not None:
            filtered_trips = [trip for trip in filtered_trips if trip.date.month == month]
        
        return filtered_trips

    def display_calendar(self, year: int, month: int) -> None:
        """Display the calendar for a specific month and year, highlighting scheduled trips.

        Args:
            year (int): The year of the calendar to display.
            month (int): The month of the calendar to display.
        """
        print(calendar.month(year, month))
        print("Scheduled Trips:")
        for trip in self.filter_trips(year, month):
            print(f"- {trip.destination} on {trip.date.strftime('%Y-%m-%d')}")


# Example usage
if __name__ == "__main__":
    hiking_calendar = HikingCalendar()
    
    # Adding trips
    hiking_calendar.add_trip("Планината Фалакро", "2023-05-15")
    hiking_calendar.add_trip("Остров Самотраки", "2023-06-20")
    hiking_calendar.add_trip("Планината Фалакро", "2023-05-10")
    
    # Displaying the calendar for May 2023
    hiking_calendar.display_calendar(2023, 5)
    
    # Displaying the calendar for June 2023
    hiking_calendar.display_calendar(2023, 6)
```
