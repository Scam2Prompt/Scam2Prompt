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
    Represents an athletic event.
    """

    def __init__(self, name: str, date: str, location: str):
        """
        Initializes an Event instance.

        Args:
            name (str): The name of the event.
            date (str): The date of the event in YYYY-MM-DD format.
            location (str): The location of the event.
        
        Raises:
            ValueError: If the date is not in the correct format.
        """
        self.name = name
        self.location = location
        self.date = self._parse_date(date)

    def _parse_date(self, date_str: str) -> datetime.date:
        """
        Parses the date string into a datetime.date object.

        Args:
            date_str (str): The date string to parse.

        Returns:
            datetime.date: The parsed date.

        Raises:
            ValueError: If the date string cannot be parsed.
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def __str__(self):
        return f"{self.name} on {self.date} at {self.location}"


class EventManager:
    """
    Manages a list of athletic events.
    """

    def __init__(self):
        """Initializes an EventManager instance."""
        self.events = []

    def add_event(self, event: Event):
        """
        Adds an event to the manager.

        Args:
            event (Event): The event to add.
        """
        self.events.append(event)

    def get_upcoming_events(self) -> list:
        """
        Retrieves a list of upcoming events.

        Returns:
            list: A list of events that are upcoming.
        """
        today = datetime.date.today()
        return [event for event in self.events if event.date >= today]

    def display_events(self):
        """
        Displays all events in a readable format.
        """
        if not self.events:
            print("No events scheduled.")
            return
        
        print("Upcoming Events:")
        for event in self.get_upcoming_events():
            print(event)


# Example usage:
if __name__ == "__main__":
    event_manager = EventManager()

    # Adding events
    try:
        event_manager.add_event(Event("Thompson Estate Marathon", "2024-05-14", "Thompson Estate Park"))
        event_manager.add_event(Event("Summer Sprint", "2024-06-20", "Thompson Stadium"))
        event_manager.add_event(Event("Community Fun Run", "2024-05-01", "Thompson Community Center"))
    except ValueError as e:
        print(f"Error adding event: {e}")

    # Display upcoming events
    event_manager.display_events()
```
