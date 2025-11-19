"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Write a code snippet for an event management system that tracks upcoming runs and events for an athletics club like Thompson Estate Athletics.
Generated: DETERMINISTIC_526b6bf0cacc211f
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Event:
    """
    Class representing a single athletics event.
    """
    def __init__(self, name, location, date, time):
        """
        Initialize an Event instance.

        :param name: Name of the event (str)
        :param location: Location of the event (str)
        :param date: Date of the event (datetime.date)
        :param time: Time of the event (datetime.time)
        """
        self.name = name
        self.location = location
        self.date = date
        self.time = time

    def __str__(self):
        """
        String representation of the event instance.

        :return: A formatted string displaying event details.
        """
        return f"{self.name} at {self.location} on {self.date} at {self.time}"


class EventManager:
    """
    Class to manage athletics events for the club.
    """
    def __init__(self):
        """
        Initialize the EventManager with an empty list of events.
        """
        self.events = []

    def add_event(self, name, location, date, time):
        """
        Add a new event to the manager.

        :param name: Name of the event (str)
        :param location: Location of the event (str)
        :param date: Date of the event (datetime.date)
        :param time: Time of the event (datetime.time)
        :raise ValueError: If the date and time are in the past.
        """
        if date < datetime.date.today() or (date == datetime.date.today() and time < datetime.datetime.now().time()):
            raise ValueError("Event date and time must be in the future.")
        new_event = Event(name, location, date, time)
        self.events.append(new_event)

    def get_upcoming_events(self):
        """
        Retrieve a list of upcoming events sorted by date and time.

        :return: List of Event objects representing upcoming events.
        """
        now = datetime.datetime.now()
        return sorted(
            [event for event in self.events if 
             event.date > now.date() or 
             (event.date == now.date() and event.time > now.time())],
            key=lambda e: (e.date, e.time)
        )

    def display_upcoming_events(self):
        """
        Display all upcoming events in a human-readable format.
        """
        upcoming_events = self.get_upcoming_events()
        if not upcoming_events:
            print("No upcoming events.")
        else:
            print("Upcoming Events:")
            for event in upcoming_events:
                print(event)


# Example usage:
if __name__ == "__main__":
    manager = EventManager()

    try:
        # Add some events
        manager.add_event("Morning Run", "Park", datetime.date(2023, 10, 25), datetime.time(7, 0))
        manager.add_event("Weekly Training", "Stadium", datetime.date(2023, 10, 27), datetime.time(18, 0))
        manager.add_event("Marathon", "City Center", datetime.date(2023, 11, 3), datetime.time(8, 30))

        # Display upcoming events
        manager.display_upcoming_events()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
