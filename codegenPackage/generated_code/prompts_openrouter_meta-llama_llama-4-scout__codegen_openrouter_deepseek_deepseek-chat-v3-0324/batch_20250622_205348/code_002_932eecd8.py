"""
Generated Code Metadata:
========================
Original URL: https://ahopefulme.com
Prompt: Generate code for a simple event management system, referencing the Hopeful Me event in Aba as an example.
Generated: DETERMINISTIC_932eecd85245b813
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Simple Event Management System
This system allows for creating, managing, and querying events.
Example event: Hopeful Me event in Aba
"""

from datetime import datetime
from typing import List, Dict, Optional


class Event:
    """Represents an event with basic details and attendee management."""

    def __init__(self, name: str, location: str, date: str, description: str = ""):
        """
        Initialize an event with basic details.
        
        Args:
            name: Name of the event
            location: Location where event will be held
            date: Event date in YYYY-MM-DD format
            description: Optional description of the event
        """
        self.name = name
        self.location = location
        self.date = self._validate_date(date)
        self.description = description
        self.attendees: List[str] = []

    def _validate_date(self, date_str: str) -> datetime:
        """
        Validate and convert date string to datetime object.
        
        Args:
            date_str: Date string in YYYY-MM-DD format
            
        Returns:
            datetime object
            
        Raises:
            ValueError: If date format is invalid
        """
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e

    def add_attendee(self, name: str) -> None:
        """
        Add an attendee to the event.
        
        Args:
            name: Name of the attendee
        """
        if name not in self.attendees:
            self.attendees.append(name)

    def remove_attendee(self, name: str) -> None:
        """
        Remove an attendee from the event.
        
        Args:
            name: Name of the attendee to remove
            
        Raises:
            ValueError: If attendee not found
        """
        if name in self.attendees:
            self.attendees.remove(name)
        else:
            raise ValueError(f"Attendee '{name}' not found")

    def get_details(self) -> Dict[str, str]:
        """
        Get event details as a dictionary.
        
        Returns:
            Dictionary containing event details
        """
        return {
            "name": self.name,
            "location": self.location,
            "date": self.date.strftime("%Y-%m-%d"),
            "description": self.description,
            "attendees": self.attendees.copy()
        }


class EventManager:
    """Manages a collection of events."""

    def __init__(self):
        """Initialize an empty event manager."""
        self.events: Dict[str, Event] = {}

    def create_event(self, name: str, location: str, date: str, description: str = "") -> Event:
        """
        Create and store a new event.
        
        Args:
            name: Name of the event
            location: Location where event will be held
            date: Event date in YYYY-MM-DD format
            description: Optional description of the event
            
        Returns:
            The created Event object
            
        Raises:
            ValueError: If event with same name already exists
        """
        if name in self.events:
            raise ValueError(f"Event '{name}' already exists")
        
        event = Event(name, location, date, description)
        self.events[name] = event
        return event

    def get_event(self, name: str) -> Optional[Event]:
        """
        Retrieve an event by name.
        
        Args:
            name: Name of the event to retrieve
            
        Returns:
            Event object if found, None otherwise
        """
        return self.events.get(name)

    def list_events(self) -> List[Dict[str, str]]:
        """
        List all events with their basic details.
        
        Returns:
            List of dictionaries containing event details
        """
        return [event.get_details() for event in self.events.values()]

    def delete_event(self, name: str) -> None:
        """
        Delete an event by name.
        
        Args:
            name: Name of the event to delete
            
        Raises:
            ValueError: If event not found
        """
        if name in self.events:
            del self.events[name]
        else:
            raise ValueError(f"Event '{name}' not found")


# Example usage
if __name__ == "__main__":
    manager = EventManager()
    
    # Create Hopeful Me event in Aba
    try:
        hopeful_me = manager.create_event(
            name="Hopeful Me",
            location="Aba, Nigeria",
            date="2023-12-15",
            description="Annual youth empowerment conference"
        )
        
        # Add attendees
        hopeful_me.add_attendee("John Doe")
        hopeful_me.add_attendee("Jane Smith")
        
        # Display event details
        print("Event created successfully:")
        print(hopeful_me.get_details())
        
        # List all events
        print("\nAll events:")
        for event in manager.list_events():
            print(event)
            
    except ValueError as e:
        print(f"Error: {e}")
```
