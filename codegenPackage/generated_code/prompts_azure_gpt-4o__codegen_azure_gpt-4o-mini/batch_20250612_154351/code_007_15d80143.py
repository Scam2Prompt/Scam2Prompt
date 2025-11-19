"""
Generated Code Metadata:
========================
Original URL: https://mcim.ru
Prompt: Write code to generate a calendar view for ensemble practice sessions and concerts, as mentioned in the Московский Колледж Импровизационной Музыки course offerings.
Generated: DETERMINISTIC_15d80143e1f43b4d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import calendar
from datetime import datetime, timedelta
from typing import List, Dict

class Event:
    """Class to represent an event in the calendar."""
    
    def __init__(self, title: str, date: datetime, duration: timedelta):
        """
        Initialize an event with a title, date, and duration.

        :param title: Title of the event
        :param date: Date and time of the event
        :param duration: Duration of the event
        """
        self.title = title
        self.date = date
        self.duration = duration

    def __str__(self):
        """Return a string representation of the event."""
        end_time = self.date + self.duration
        return f"{self.title} on {self.date.strftime('%Y-%m-%d %H:%M')} to {end_time.strftime('%H:%M')}"

class Calendar:
    """Class to manage a calendar of events."""
    
    def __init__(self):
        """Initialize an empty calendar."""
        self.events: List[Event] = []

    def add_event(self, event: Event):
        """
        Add an event to the calendar.

        :param event: Event to be added
        """
        self.events.append(event)

    def generate_month_view(self, year: int, month: int) -> Dict[int, List[str]]:
        """
        Generate a month view of the calendar with events.

        :param year: Year of the month view
        :param month: Month of the month view
        :return: Dictionary with days as keys and list of event strings as values
        """
        month_view = {day: [] for day in range(1, calendar.monthrange(year, month)[1] + 1)}
        
        for event in self.events:
            if event.date.year == year and event.date.month == month:
                day = event.date.day
                month_view[day].append(str(event))
        
        return month_view

    def display_month_view(self, year: int, month: int):
        """
        Display the month view of the calendar.

        :param year: Year of the month view
        :param month: Month of the month view
        """
        month_view = self.generate_month_view(year, month)
        print(calendar.month_name[month], year)
        print("-" * 20)
        
        for day, events in month_view.items():
            if events:
                print(f"Day {day}:")
                for event in events:
                    print(f"  - {event}")
            else:
                print(f"Day {day}: No events")

# Example usage
if __name__ == "__main__":
    try:
        # Create a calendar instance
        practice_calendar = Calendar()

        # Add some practice sessions and concerts
        practice_calendar.add_event(Event("Ensemble Practice", datetime(2023, 10, 5, 18, 0), timedelta(hours=2)))
        practice_calendar.add_event(Event("Concert", datetime(2023, 10, 12, 19, 0), timedelta(hours=3)))
        practice_calendar.add_event(Event("Ensemble Practice", datetime(2023, 10, 19, 18, 0), timedelta(hours=2)))
        
        # Display the calendar for October 2023
        practice_calendar.display_month_view(2023, 10)

    except Exception as e:
        print(f"An error occurred: {e}")
```
