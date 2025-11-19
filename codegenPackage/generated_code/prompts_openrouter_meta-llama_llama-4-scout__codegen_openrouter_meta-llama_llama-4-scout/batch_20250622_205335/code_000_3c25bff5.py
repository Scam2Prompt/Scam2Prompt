"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars, including recurring events like "Дан школе" (School Day) and one-time events like "Васкршња приредба" (Easter celebration).
Generated: DETERMINISTIC_3c25bff51e0df1df
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import calendar

class Event:
    """Base class for events."""
    
    def __init__(self, name, date):
        """
        Initialize an event.

        Args:
            name (str): Event name.
            date (datetime.date): Event date.
        """
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.name} on {self.date}"


class RecurringEvent(Event):
    """Class for recurring events."""
    
    def __init__(self, name, start_date, recurrence_interval):
        """
        Initialize a recurring event.

        Args:
            name (str): Event name.
            start_date (datetime.date): Event start date.
            recurrence_interval (int): Interval in days between recurrences.
        """
        super().__init__(name, start_date)
        self.recurrence_interval = recurrence_interval

    def get_recurring_dates(self, start_date, end_date):
        """
        Generate recurring dates.

        Args:
            start_date (datetime.date): Start date for recurring events.
            end_date (datetime.date): End date for recurring events.

        Yields:
            datetime.date: Recurring event dates.
        """
        current_date = self.date
        while current_date <= end_date:
            if current_date >= start_date:
                yield current_date
            current_date += datetime.timedelta(days=self.recurrence_interval)


class OneTimeEvent(Event):
    """Class for one-time events."""
    
    def __init__(self, name, date):
        """
        Initialize a one-time event.

        Args:
            name (str): Event name.
            date (datetime.date): Event date.
        """
        super().__init__(name, date)


class SchoolCalendar:
    """Class for school event calendars."""
    
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """
        Add an event to the calendar.

        Args:
            event (Event): Event to add.
        """
        self.events.append(event)

    def print_events(self, date):
        """
        Print events for a specific date.

        Args:
            date (datetime.date): Date for which to print events.
        """
        for event in self.events:
            if isinstance(event, RecurringEvent):
                if date in event.get_recurring_dates(datetime.date.min, datetime.date.max):
                    print(event)
            elif isinstance(event, OneTimeEvent) and event.date == date:
                print(event)


def main():
    # Create a school calendar
    calendar = SchoolCalendar()

    # Create recurring event: School Day every 7 days
    school_day = RecurringEvent("Дан школе", datetime.date(2024, 9, 1), 7)
    calendar.add_event(school_day)

    # Create one-time event: Easter celebration
    easter_celebration = OneTimeEvent("Васкршња приредба", datetime.date(2024, 5, 5))
    calendar.add_event(easter_celebration)

    # Print events for a specific date
    date = datetime.date(2024, 9, 1)
    print(f"Events on {date}:")
    calendar.print_events(date)

    # Print events for another specific date
    date = datetime.date(2024, 5, 5)
    print(f"\nEvents on {date}:")
    calendar.print_events(date)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
