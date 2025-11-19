"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Develop a simple algorithm for a school event management system, prioritizing events like the Copa Montessori and Feria de Robótica, as seen on the Del Sol Montessori website."
Generated: DETERMINISTIC_4d94940490852a4d
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum, auto
from typing import List, Dict, Optional

class EventPriority(Enum):
    """Priority levels for events."""
    HIGH = auto()
    MEDIUM = auto()
    LOW = auto()

class Event:
    """Represents a school event with priority, date, and details."""
    
    def __init__(self, name: str, date: datetime.date, priority: EventPriority, description: str = ""):
        self.name = name
        self.date = date
        self.priority = priority
        self.description = description
    
    def __str__(self) -> str:
        return f"{self.name} ({self.date.strftime('%Y-%m-%d')}) - Priority: {self.priority.name}"
    
    def __lt__(self, other) -> bool:
        """Compare events by priority and date."""
        if self.priority == other.priority:
            return self.date < other.date
        return self.priority.value < other.priority.value

class EventManager:
    """Manages and prioritizes school events."""
    
    def __init__(self):
        self.events: List[Event] = []
    
    def add_event(self, event: Event) -> None:
        """Add an event to the manager."""
        if not isinstance(event, Event):
            raise ValueError("Only Event objects can be added")
        self.events.append(event)
    
    def get_prioritized_events(self) -> List[Event]:
        """Return events sorted by priority and date."""
        return sorted(self.events)
    
    def get_upcoming_events(self, days: int = 30) -> List[Event]:
        """Return upcoming events within the specified number of days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days)
        upcoming = [e for e in self.events if today <= e.date <= end_date]
        return sorted(upcoming)
    
    def get_events_by_priority(self, priority: EventPriority) -> List[Event]:
        """Return events filtered by priority."""
        return sorted([e for e in self.events if e.priority == priority])

def initialize_events() -> EventManager:
    """Initialize with sample events from Del Sol Montessori."""
    manager = EventManager()
    
    # High priority events
    manager.add_event(Event(
        "Copa Montessori",
        datetime.date(2023, 11, 15),
        EventPriority.HIGH,
        "Annual sports competition"
    ))
    
    manager.add_event(Event(
        "Feria de Robótica",
        datetime.date(2023, 12, 5),
        EventPriority.HIGH,
        "Robotics fair showcasing student projects"
    ))
    
    # Medium priority events
    manager.add_event(Event(
        "Parent-Teacher Conference",
        datetime.date(2023, 10, 20),
        EventPriority.MEDIUM
    ))
    
    # Low priority events
    manager.add_event(Event(
        "Book Fair",
        datetime.date(2023, 10, 10),
        EventPriority.LOW
    ))
    
    return manager

def main():
    """Demonstrate the event management system."""
    try:
        manager = initialize_events()
        
        print("All Events:")
        for event in manager.get_prioritized_events():
            print(f"- {event}")
        
        print("\nUpcoming Events (next 30 days):")
        for event in manager.get_upcoming_events():
            print(f"- {event}")
        
        print("\nHigh Priority Events:")
        for event in manager.get_events_by_priority(EventPriority.HIGH):
            print(f"- {event}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
