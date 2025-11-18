"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Implement a feature to manage school events and cultural activities, inspired by the Event Planning module in Him Saral's school management system.
Generated: DETERMINISTIC_e45b2aad45e57ffc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
from datetime import datetime

class Event:
    """Class representing a school event."""
    
    def __init__(self, title: str, date: datetime, description: str, location: str):
        """
        Initializes a new event.
        
        Args:
            title (str): The title of the event.
            date (datetime): The date and time of the event.
            description (str): A brief description of the event.
            location (str): The location where the event will be held.
        """
        self.title = title
        self.date = date
        self.description = description
        self.location = location

    def __repr__(self):
        return f"Event(title='{self.title}', date='{self.date}', location='{self.location}')"


class EventManager:
    """Class to manage a list of school events."""
    
    def __init__(self):
        """Initializes the EventManager with an empty event list."""
        self.events: List[Event] = []

    def add_event(self, title: str, date: datetime, description: str, location: str) -> None:
        """
        Adds a new event to the event manager.
        
        Args:
            title (str): The title of the event.
            date (datetime): The date and time of the event.
            description (str): A brief description of the event.
            location (str): The location of the event.
        
        Raises:
            ValueError: If the event date is in the past.
        """
        if date < datetime.now():
            raise ValueError("Event date cannot be in the past.")
        
        new_event = Event(title, date, description, location)
        self.events.append(new_event)

    def remove_event(self, title: str) -> Optional[Event]:
        """
        Removes an event from the event manager by title.
        
        Args:
            title (str): The title of the event to be removed.
        
        Returns:
            Optional[Event]: The removed event if found, None otherwise.
        """
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                return event
        return None

    def list_events(self) -> List[Dict[str, str]]:
        """
        Lists all events in a human-readable format.
        
        Returns:
            List[Dict[str, str]]: A list of events with relevant details.
        """
        return [{"title": event.title, "date": event.date.strftime("%Y-%m-%d %H:%M"), 
                 "description": event.description, "location": event.location} for event in self.events]

    def find_event(self, title: str) -> Optional[Event]:
        """
        Finds an event by title.
        
        Args:
            title (str): The title of the event to find.
        
        Returns:
            Optional[Event]: The event if found, None otherwise.
        """
        for event in self.events:
            if event.title == title:
                return event
        return None

# Example Usage
if __name__ == "__main__":
    manager = EventManager()
    
    try:
        manager.add_event("Science Fair", datetime(2023, 11, 15, 10, 0), 
                          "Annual science exhibition and competition.", "School Auditorium")
        manager.add_event("Cultural Fest", datetime(2023, 12, 20, 18, 0), 
                          "A celebration of culture with performances.", "Main Hall")
        
        print("Current Events:")
        print(manager.list_events())

        removed_event = manager.remove_event("Science Fair")
        print(f"Removed Event: {removed_event}")

        print("Updated Events:")
        print(manager.list_events())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
