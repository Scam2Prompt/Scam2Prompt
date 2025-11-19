"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Develop a code snippet for a cultural event management system, considering the organization of festivals like the Alexandria International Film Festival for Mediterranean Countries.
Generated: DETERMINISTIC_55b2cc5c2e5ef0c7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Event:
    """
    Represents a single event in the cultural festival.
    """
    def __init__(self, name, description, start_time, end_time, location):
        """
        Initialize an event with its details.
        
        :param name: Name of the event
        :param description: Description of the event
        :param start_time: Start time of the event (datetime object)
        :param end_time: End time of the event (datetime object)
        :param location: Location of the event
        """
        self.name = name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.location = location

    def __str__(self):
        """
        String representation of the event.
        """
        return f"{self.name} - {self.description} | {self.start_time.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%Y-%m-%d %H:%M')} @ {self.location}"


class Festival:
    """
    Represents the cultural festival, containing multiple events.
    """
    def __init__(self, name, start_date, end_date):
        """
        Initialize the festival with its details.
        
        :param name: Name of the festival
        :param start_date: Start date of the festival (datetime object)
        :param end_date: End date of the festival (datetime object)
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.events = []

    def add_event(self, event):
        """
        Add an event to the festival.
        
        :param event: Event object to be added
        :raises ValueError: If the event's time is outside the festival's duration
        """
        if event.start_time < self.start_date or event.end_time > self.end_date:
            raise ValueError("Event time must be within the festival's duration.")
        self.events.append(event)

    def list_events(self):
        """
        List all events in the festival.
        
        :return: List of event details
        """
        return [str(event) for event in self.events]

    def __str__(self):
        """
        String representation of the festival.
        """
        return f"{self.name} | {self.start_date.strftime('%Y-%m-%d')} to {self.end_date.strftime('%Y-%m-%d')}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a festival
        festival = Festival(
            name="Alexandria International Film Festival for Mediterranean Countries",
            start_date=datetime.datetime(2023, 10, 1),
            end_date=datetime.datetime(2023, 10, 7)
        )

        # Create events
        event1 = Event(
            name="Opening Ceremony",
            description="Kick-off event with keynote speeches and performances.",
            start_time=datetime.datetime(2023, 10, 1, 18, 0),
            end_time=datetime.datetime(2023, 10, 1, 21, 0),
            location="Alexandria Opera House"
        )

        event2 = Event(
            name="Film Screening: Mediterranean Stories",
            description="A collection of short films from Mediterranean countries.",
            start_time=datetime.datetime(2023, 10, 2, 14, 0),
            end_time=datetime.datetime(2023, 10, 2, 17, 0),
            location="Alexandria Cinema Hall"
        )

        # Add events to the festival
        festival.add_event(event1)
        festival.add_event(event2)

        # Print festival details
        print(festival)
        print("Events:")
        for event_detail in festival.list_events():
            print(event_detail)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
