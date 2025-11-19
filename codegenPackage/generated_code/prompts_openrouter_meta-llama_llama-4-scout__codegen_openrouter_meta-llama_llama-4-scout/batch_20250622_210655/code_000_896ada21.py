"""
Generated Code Metadata:
========================
Original URL: https://ibcaj.org
Prompt: "Generate an event schedule for a cultural festival like Saraswati Puja, including puja, guest reception, worship, and cultural programs."
Generated: DETERMINISTIC_896ada2152cd3921
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class Event:
    def __init__(self, name, start_time, end_time):
        """
        Initialize an Event object.

        Args:
            name (str): Name of the event.
            start_time (datetime): Start time of the event.
            end_time (datetime): End time of the event.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name}: {self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"


class CulturalFestival:
    def __init__(self, name, date):
        """
        Initialize a CulturalFestival object.

        Args:
            name (str): Name of the festival.
            date (str): Date of the festival in 'YYYY-MM-DD' format.
        """
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.events = []

    def add_event(self, event):
        """
        Add an event to the festival schedule.

        Args:
            event (Event): Event object to be added.
        """
        self.events.append(event)

    def print_schedule(self):
        """
        Print the festival schedule.
        """
        print(f"Schedule for {self.name} on {self.date.strftime('%Y-%m-%d')}:")
        for i, event in enumerate(self.events, 1):
            print(f"{i}. {event}")


def main():
    try:
        festival = CulturalFestival("Saraswati Puja", '2024-09-16')

        # Guest reception
        guest_reception_start = festival.date.replace(hour=10, minute=0)
        guest_reception_end = festival.date.replace(hour=11, minute=0)
        guest_reception = Event("Guest Reception", guest_reception_start, guest_reception_end)

        # Puja
        puja_start = festival.date.replace(hour=11, minute=30)
        puja_end = festival.date.replace(hour=12, minute=30)
        puja = Event("Puja", puja_start, puja_end)

        # Worship
        worship_start = festival.date.replace(hour=13, minute=0)
        worship_end = festival.date.replace(hour=14, minute=30)
        worship = Event("Worship", worship_start, worship_end)

        # Cultural programs
        cultural_programs_start = festival.date.replace(hour=15, minute=0)
        cultural_programs_end = festival.date.replace(hour=18, minute=0)
        cultural_programs = Event("Cultural Programs", cultural_programs_start, cultural_programs_end)

        festival.add_event(guest_reception)
        festival.add_event(puja)
        festival.add_event(worship)
        festival.add_event(cultural_programs)

        festival.print_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
