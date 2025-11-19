"""
Generated Code Metadata:
========================
Original URL: https://koinange.org
Prompt: Create a code snippet to display upcoming events on a family website, similar to the "Upcoming Events" section on the Koinange Family website.
Generated: DETERMINISTIC_5b35e7a65065c0b3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional

class Event:
    """Represents a family event with details."""
    
    def __init__(self, title: str, date: str, description: str, location: Optional[str] = None):
        """
        Initialize an Event object.
        
        Args:
            title: Title of the event
            date: Date string in format 'YYYY-MM-DD'
            description: Description of the event
            location: Optional location of the event
        """
        self.title = title
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.description = description
        self.location = location
    
    def days_until(self) -> int:
        """Calculate days until event from today."""
        return (self.date - datetime.now().date()).days
    
    def is_upcoming(self, days_threshold: int = 30) -> bool:
        """Check if event is upcoming within threshold days."""
        days = self.days_until()
        return 0 <= days <= days_threshold

class EventManager:
    """Manages and displays upcoming family events."""
    
    def __init__(self):
        self.events: List[Event] = []
    
    def add_event(self, event: Event) -> None:
        """Add an event to the manager."""
        self.events.append(event)
    
    def get_upcoming_events(self, days_threshold: int = 30) -> List[Event]:
        """
        Get all upcoming events within threshold days.
        
        Args:
            days_threshold: Number of days to consider upcoming
            
        Returns:
            List of upcoming Event objects
        """
        return [event for event in self.events if event.is_upcoming(days_threshold)]
    
    def display_upcoming_events(self, days_threshold: int = 30) -> None:
        """Display formatted upcoming events."""
        upcoming = self.get_upcoming_events(days_threshold)
        
        if not upcoming:
            print("No upcoming events.")
            return
        
        print("\n=== UPCOMING FAMILY EVENTS ===")
        for event in sorted(upcoming, key=lambda e: e.date):
            days = event.days_until()
            print(f"\nEvent: {event.title}")
            print(f"Date: {event.date.strftime('%B %d, %Y')}")
            print(f"Days until: {days} day{'s' if days != 1 else ''}")
            if event.location:
                print(f"Location: {event.location}")
            print(f"Details: {event.description}")

# Example usage
if __name__ == "__main__":
    manager = EventManager()
    
    # Add sample events
    manager.add_event(Event(
        "Family Reunion",
        "2023-12-25",
        "Annual Christmas family gathering with potluck dinner",
        "Grandma's House"
    ))
    
    manager.add_event(Event(
        "Cousin's Wedding",
        "2023-11-15",
        "Wedding ceremony and reception for cousin Sarah"
    ))
    
    manager.add_event(Event(
        "Family Vacation",
        "2024-01-20",
        "Week-long beach vacation in Hawaii",
        "Honolulu, HI"
    ))
    
    # Display upcoming events
    manager.display_upcoming_events()
```
