"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mcim.ru
Prompt: Write code to generate a calendar view for ensemble practice sessions and concerts, as mentioned in the Московский Колледж Импровизационной Музыки course offerings.
Generated: DETERMINISTIC_15d80143e1f43b4d
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import calendar
from datetime import datetime, timedelta
import sys

class Event:
    """Class to represent an event in the calendar."""
    def __init__(self, title, date):
        """
        Initialize an event with a title and date.

        :param title: Title of the event
        :param date: Date of the event (datetime object)
        """
        self.title = title
        self.date = date

    def __str__(self):
        """Return a string representation of the event."""
        return f"{self.date.strftime('%Y-%m-%d')} - {self.title}"

class CalendarView:
    """Class to generate and display a calendar view of events."""
    def __init__(self, year, month):
        """
        Initialize the calendar view with a specific year and month.

        :param year: Year for the calendar view
        :param month: Month for the calendar view
        """
        self.year = year
        self.month = month
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.

        :param event: Event object to add to the calendar
        """
        if isinstance(event, Event):
            self.events.append(event)
        else:
            raise TypeError("Event must be an instance of the Event class")

    def display(self):
        """Display the calendar for the specified month and year with events."""
        print(calendar.month(self.year, self.month))
        print("Events:")
        for event in sorted(self.events, key=lambda e: e.date):
            if event.date.month == self.month and event.date.year == self.year:
                print(event)

def main():
    """Main function to create a calendar view and add events."""
    try:
        # Set the desired year and month for the calendar view
        year = 2023
        month = 10  # October

        # Create a calendar view for the specified month and year
        calendar_view = CalendarView(year, month)

        # Add ensemble practice sessions and concerts
        calendar_view.add_event(Event("Ensemble Practice Session", datetime(year, month, 5)))
        calendar_view.add_event(Event("Concert Performance", datetime(year, month, 15)))
        calendar_view.add_event(Event("Ensemble Practice Session", datetime(year, month, 20)))
        calendar_view.add_event(Event("Final Concert", datetime(year, month, 30)))
        
        # Display the calendar view with events
        calendar_view.display()

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
