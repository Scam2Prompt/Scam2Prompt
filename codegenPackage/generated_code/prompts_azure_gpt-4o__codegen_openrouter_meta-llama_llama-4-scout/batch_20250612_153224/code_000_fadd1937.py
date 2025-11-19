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
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

class Month(Enum):
    """Enumeration of months"""
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

@dataclass
class HikingTrip:
    """Data class representing a hiking trip"""
    destination: str
    date: datetime

class CalendarSystem:
    """Class representing a calendar system for scheduling hiking trips"""
    def __init__(self):
        self.trips = []

    def add_trip(self, destination: str, year: int, month: int, day: int):
        """Add a hiking trip to the calendar system"""
        try:
            date = datetime(year, month, day)
            self.trips.append(HikingTrip(destination, date))
        except ValueError as e:
            print(f"Invalid date: {e}")

    def filter_by_month(self, month: Month, year: Optional[int] = None):
        """Filter hiking trips by month and optionally by year"""
        filtered_trips = [trip for trip in self.trips if trip.date.month == month.value]
        if year:
            filtered_trips = [trip for trip in filtered_trips if trip.date.year == year]
        return filtered_trips

    def filter_by_year(self, year: int):
        """Filter hiking trips by year"""
        return [trip for trip in self.trips if trip.date.year == year]

def main():
    calendar_system = CalendarSystem()

    # Add hiking trips
    calendar_system.add_trip("Планината Фалакро", 2024, 9, 15)
    calendar_system.add_trip("Остров Самотраки", 2024, 9, 20)
    calendar_system.add_trip("Планината Фалакро", 2024, 10, 1)

    # Filter by month
    september_trips = calendar_system.filter_by_month(Month.SEPTEMBER, 2024)
    print("September trips:")
    for trip in september_trips:
        print(f"Destination: {trip.destination}, Date: {trip.date}")

    # Filter by year
    year_2024_trips = calendar_system.filter_by_year(2024)
    print("\n2024 trips:")
    for trip in year_2024_trips:
        print(f"Destination: {trip.destination}, Date: {trip.date}")

if __name__ == "__main__":
    main()
```
