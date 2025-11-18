"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Create a program to track upcoming conferences, workshops, and seminars, based on the event structure outlined by ORIC at Kinnaird College.
Generated: DETERMINISTIC_2b0b405193fc4a2c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the requested program written in Python. It uses a simple structure to track conferences, workshops, and seminars.

```python
import datetime

class Event:
    """
    Represents an event with relevant details.
    """
    def __init__(self, title, event_type, date, location, organizer):
        """
        Initialize an Event object.

        :param title: Title of the event.
        :param event_type: Type of the event (e.g., Conference, Workshop, Seminar).
        :param date: Date of the event (YYYY-MM-DD format).
        :param location: Location where the event will take place.
        :param organizer: Name of the organizer or organizing body.
        """
        try:
            self.title = title
            self.event_type = event_type
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
            self.location = location
            self.organizer = organizer
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

    def __str__(self):
        """
        Provide a readable string representation for the event.

        :return: String describing the event.
        """
        return (f"[{self.event_type}] {self.title}\nDate: {self.date.strftime('%Y-%m-%d')}\n"
                f"Location: {self.location}\nOrganizer: {self.organizer}")


class EventManager:
    """
    Manages a collection of events.
    """
    def __init__(self):
        """
        Initialize an empty list to store events.
        """
        self.events = []

    def add_event(self, event):
        """
        Add an event to the manager.

        :param event: Event object to be added.
        """
        if not isinstance(event, Event):
            raise TypeError("Only Event objects can be added.")
        self.events.append(event)

    def upcoming_events(self):
        """
        Retrieve a list of upcoming events.

        :return: List of events sorted by date that are in the future.
        """
        today = datetime.datetime.today()
        return sorted([event for event in self.events if event.date > today], key=lambda x: x.date)

    def display_events(self, events):
        """
        Display a list of events in a readable format.

        :param events: List of Event objects to display.
        """
        if not events:
            print("No upcoming events.")
        for event in events:
            print(event)
            print("-" * 40)


def main():
    """
    Main function to demonstrate the program functionality.
    """
    # Initialize the event manager
    manager = EventManager()

    try:
        # Add some sample events
        manager.add_event(Event("AI and Machine Learning Seminar", "Seminar", "2023-12-10", "Kinnaird College Auditorium", "ORIC"))
        manager.add_event(Event("International Conference on Science", "Conference", "2024-01-15", "Main Hall", "ORIC"))
        manager.add_event(Event("Workshop on Python Programming", "Workshop", "2023-11-25", "Lab 3", "Computer Science Department"))

        # Fetch and display upcoming events
        print("Upcoming Events:")
        upcoming = manager.upcoming_events()
        manager.display_events(upcoming)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

Let me know if further modifications are needed!
