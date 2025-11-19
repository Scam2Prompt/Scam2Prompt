"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Create a program to track upcoming conferences, workshops, and seminars, based on the event structure outlined by ORIC at Kinnaird College.
Generated: DETERMINISTIC_2b0b405193fc4a2c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Event:
    """
    A class to represent an event such as a conference, workshop, or seminar.
    """

    def __init__(self, title: str, date: datetime.date, location: str, description: str):
        """
        Initializes an Event instance.

        :param title: Title of the event
        :param date: Date of the event
        :param location: Location of the event
        :param description: Description of the event
        """
        self.title = title
        self.date = date
        self.location = location
        self.description = description

    def __str__(self):
        return f"{self.title} on {self.date} at {self.location}: {self.description}"


class EventTracker:
    """
    A class to track a list of events.
    """

    def __init__(self):
        """
        Initializes the EventTracker with an empty list of events.
        """
        self.events: List[Event] = []

    def add_event(self, event: Event) -> None:
        """
        Adds an event to the tracker.

        :param event: An instance of Event to be added
        """
        if not isinstance(event, Event):
            raise ValueError("Only Event instances can be added.")
        self.events.append(event)

    def get_upcoming_events(self) -> List[Event]:
        """
        Retrieves a list of upcoming events.

        :return: A list of upcoming Event instances
        """
        today = datetime.date.today()
        return [event for event in self.events if event.date >= today]

    def display_events(self) -> None:
        """
        Displays all upcoming events in a formatted manner.
        """
        upcoming_events = self.get_upcoming_events()
        if not upcoming_events:
            print("No upcoming events.")
            return
        
        print("Upcoming Events:")
        for event in upcoming_events:
            print(event)


def main():
    """
    Main function to run the event tracking program.
    """
    tracker = EventTracker()

    # Sample events
    try:
        tracker.add_event(Event("Tech Conference 2023", datetime.date(2023, 11, 15), "Kinnaird College", "A conference on the latest in technology."))
        tracker.add_event(Event("Workshop on AI", datetime.date(2023, 10, 20), "Kinnaird College", "An interactive workshop on Artificial Intelligence."))
        tracker.add_event(Event("Seminar on Data Science", datetime.date(2023, 12, 5), "Kinnaird College", "A seminar discussing the future of Data Science."))
    except ValueError as e:
        print(f"Error adding event: {e}")

    # Display upcoming events
    tracker.display_events()


if __name__ == "__main__":
    main()
```
