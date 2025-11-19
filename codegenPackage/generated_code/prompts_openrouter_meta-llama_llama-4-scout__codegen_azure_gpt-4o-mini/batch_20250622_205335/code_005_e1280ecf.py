"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Write a Python script to manage school event calendars for events like "Дан школе" and "Васкршња приредба".
Generated: DETERMINISTIC_e1280ecf30dd9a31
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """Class to represent a school event."""
    
    def __init__(self, name: str, date: str, description: Optional[str] = None):
        """
        Initialize an event with a name, date, and optional description.

        :param name: Name of the event
        :param date: Date of the event in 'YYYY-MM-DD' format
        :param description: Optional description of the event
        """
        self.name = name
        self.date = self._validate_date(date)
        self.description = description

    @staticmethod
    def _validate_date(date_str: str) -> str:
        """Validate the date format and return the date string."""
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def to_dict(self) -> Dict:
        """Convert the event to a dictionary."""
        return {
            'name': self.name,
            'date': self.date,
            'description': self.description
        }

class EventCalendar:
    """Class to manage a calendar of school events."""
    
    def __init__(self, filename: str):
        """
        Initialize the event calendar with a filename for data storage.

        :param filename: The filename where events will be stored
        """
        self.filename = filename
        self.events: List[Event] = self.load_events()

    def load_events(self) -> List[Event]:
        """Load events from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                events_data = json.load(file)
                return [Event(**event) for event in events_data]
        except FileNotFoundError:
            return []  # Return an empty list if the file does not exist
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the events file.")

    def save_events(self) -> None:
        """Save the current events to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([event.to_dict() for event in self.events], file, indent=4)

    def add_event(self, name: str, date: str, description: Optional[str] = None) -> None:
        """Add a new event to the calendar."""
        new_event = Event(name, date, description)
        self.events.append(new_event)
        self.save_events()

    def get_events(self) -> List[Event]:
        """Get a list of all events."""
        return self.events

    def find_event(self, name: str) -> Optional[Event]:
        """Find an event by name."""
        for event in self.events:
            if event.name == name:
                return event
        return None

def main():
    """Main function to demonstrate the EventCalendar functionality."""
    calendar = EventCalendar('events.json')

    # Example usage
    try:
        calendar.add_event("Дан школе", "2023-05-15", "Annual school day celebration.")
        calendar.add_event("Васкршња приредба", "2023-04-10", "Easter performance by students.")
        
        print("Current Events:")
        for event in calendar.get_events():
            print(f"{event.name} on {event.date}: {event.description}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
