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
    """Represents a hiking trip with destination, date, and details."""
    
    def __init__(self, destination: str, date: datetime, details: str = ""):
        self.destination = destination
        self.date = date
        self.details = details
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')}: {self.destination} - {self.details}"

class HikingCalendar:
    """A calendar system for managing and filtering hiking trips."""
    
    def __init__(self):
        self.trips: List[HikingTrip] = []
    
    def add_trip(self, destination: str, year: int, month: int, day: int, details: str = "") -> None:
        """Add a new hiking trip to the calendar.
        
        Args:
            destination: Name of the hiking destination.
            year: Year of the trip.
            month: Month of the trip (1-12).
            day: Day of the trip.
            details: Additional details about the trip.
            
        Raises:
            ValueError: If the date is invalid.
        """
        try:
            date = datetime(year, month, day)
            self.trips.append(HikingTrip(destination, date, details))
        except ValueError as e:
            raise ValueError(f"Invalid date: {e}")
    
    def get_trips_by_month(self, year: int, month: int) -> List[HikingTrip]:
        """Get all trips scheduled for a specific month and year.
        
        Args:
            year: Year to filter by.
            month: Month to filter by (1-12).
            
        Returns:
            List of HikingTrip objects for the specified month and year.
        """
        return [trip for trip in self.trips 
                if trip.date.year == year and trip.date.month == month]
    
    def get_trips_by_destination(self, destination: str) -> List[HikingTrip]:
        """Get all trips to a specific destination.
        
        Args:
            destination: Destination name to filter by.
            
        Returns:
            List of HikingTrip objects for the specified destination.
        """
        return [trip for trip in self.trips if trip.destination == destination]
    
    def display_monthly_calendar(self, year: int, month: int) -> None:
        """Display a calendar for a month with scheduled trips marked.
        
        Args:
            year: Year of the calendar.
            month: Month of the calendar (1-12).
        """
        cal = calendar.TextCalendar()
        month_str = cal.formatmonth(year, month)
        trips = self.get_trips_by_month(year, month)
        
        trip_days = [trip.date.day for trip in trips]
        
        print(f"\nHiking Trips in {calendar.month_name[month]} {year}:")
        print(month_str)
        
        if trip_days:
            print("Scheduled trips on days:", ", ".join(map(str, trip_days)))
            for trip in trips:
                print(f"  {trip}")
        else:
            print("No trips scheduled this month.")

# Example usage
if __name__ == "__main__":
    hiking_calendar = HikingCalendar()
    
    # Add some sample trips
    hiking_calendar.add_trip("Планината Фалакро", 2023, 6, 15, "Weekend hike")
    hiking_calendar.add_trip("Остров Самотраки", 2023, 7, 22, "Summer expedition")
    hiking_calendar.add_trip("Планината Фалакро", 2023, 8, 5, "Advanced trail")
    
    # Display June 2023 calendar
    hiking_calendar.display_monthly_calendar(2023, 6)
    
    # Get all trips to Планината Фалакро
    print("\nAll trips to Планината Фалакро:")
    for trip in hiking_calendar.get_trips_by_destination("Планината Фалакро"):
        print(trip)
```
