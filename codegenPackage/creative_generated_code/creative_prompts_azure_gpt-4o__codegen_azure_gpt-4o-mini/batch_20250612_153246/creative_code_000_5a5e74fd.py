"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wcdevent.com
Prompt: Write code to create an event management system for corporate and social events, including features for event design customization, inspired by services offered in Bogotá, Colombia.
Generated: DETERMINISTIC_5a5e74fdeec7e852
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# event_management_system.py

from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """
    A class to represent an event.
    
    Attributes:
        name (str): The name of the event.
        date (datetime): The date and time of the event.
        location (str): The location of the event.
        custom_design (Dict): A dictionary containing design customizations for the event.
    """
    
    def __init__(self, name: str, date: datetime, location: str, custom_design: Optional[Dict] = None):
        self.name = name
        self.date = date
        self.location = location
        self.custom_design = custom_design if custom_design else {}

    def update_design(self, customization: Dict):
        """
        Updates the event's design customizations.
        
        Args:
            customization (Dict): A dictionary containing new design customizations.
        """
        self.custom_design.update(customization)

    def __str__(self):
        return f"Event(Name: {self.name}, Date: {self.date}, Location: {self.location}, Design: {self.custom_design})"


class EventManager:
    """
    A class to manage events.
    
    Attributes:
        events (List[Event]): A list of events managed by the EventManager.
    """
    
    def __init__(self):
        self.events = []

    def create_event(self, name: str, date: datetime, location: str, custom_design: Optional[Dict] = None) -> Event:
        """
        Creates a new event and adds it to the event list.
        
        Args:
            name (str): The name of the event.
            date (datetime): The date and time of the event.
            location (str): The location of the event.
            custom_design (Optional[Dict]): Design customizations for the event.
        
        Returns:
            Event: The created event.
        """
        event = Event(name, date, location, custom_design)
        self.events.append(event)
        return event

    def get_events(self) -> List[Event]:
        """
        Returns the list of events.
        
        Returns:
            List[Event]: A list of events.
        """
        return self.events

    def find_event(self, name: str) -> Optional[Event]:
        """
        Finds an event by its name.
        
        Args:
            name (str): The name of the event to find.
        
        Returns:
            Optional[Event]: The found event or None if not found.
        """
        for event in self.events:
            if event.name == name:
                return event
        return None

    def remove_event(self, name: str) -> bool:
        """
        Removes an event by its name.
        
        Args:
            name (str): The name of the event to remove.
        
        Returns:
            bool: True if the event was removed, False if not found.
        """
        event_to_remove = self.find_event(name)
        if event_to_remove:
            self.events.remove(event_to_remove)
            return True
        return False


if __name__ == "__main__":
    # Example usage
    event_manager = EventManager()
    
    # Create an event
    event1 = event_manager.create_event("Corporate Retreat", datetime(2023, 11, 20, 9, 0), "Hotel Bogotá", {"theme": "Business", "colors": ["Blue", "Silver"]})
    
    # Create another event
    event2 = event_manager.create_event("Wedding Reception", datetime(2023, 12, 15, 18, 0), "Botanical Gardens", {"theme": "Romantic", "colors": ["Pink", "Gold"]})
    
    # Fetch all events
    all_events = event_manager.get_events()
    for event in all_events:
        print(event)

    # Update design for an event
    event1.update_design({"lighting": "Soft", "decor": "Minimalist"})
    
    # Find and remove an event
    if event_manager.remove_event("Wedding Reception"):
        print("Wedding Reception removed successfully.")
    else:
        print("Event not found.")
```

This code provides a basic event management system for creating, managing, and customizing events, with proper documentation and error handling in place.
