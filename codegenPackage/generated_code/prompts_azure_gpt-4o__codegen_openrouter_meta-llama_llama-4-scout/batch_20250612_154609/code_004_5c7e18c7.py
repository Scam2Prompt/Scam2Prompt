"""
Generated Code Metadata:
========================
Original URL: https://www.iaci.org
Prompt: Write a script to manage and display upcoming events for an organization, including filtering by industry or membership type.
Generated: DETERMINISTIC_5c7e18c7f086f1e9
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_manager.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class Industry(Enum):
    """Event industry types"""
    TECH = "Tech"
    FINANCE = "Finance"
    HEALTHCARE = "Healthcare"

class MembershipType(Enum):
    """Membership types"""
    BASIC = "Basic"
    PREMIUM = "Premium"

class Event:
    """Represents an upcoming event"""
    def __init__(self, id: int, name: str, industry: Industry, date: datetime, 
                 membership_type: MembershipType, description: str):
        self.id = id
        self.name = name
        self.industry = industry
        self.date = date
        self.membership_type = membership_type
        self.description = description

class EventManager:
    """Manages and displays upcoming events"""
    def __init__(self):
        self.events = []

    def add_event(self, event: Event):
        """Add an event to the list"""
        self.events.append(event)

    def get_events(self, industry: Industry = None, membership_type: MembershipType = None) -> List[Event]:
        """Get events filtered by industry or membership type"""
        filtered_events = self.events.copy()
        
        if industry:
            filtered_events = [event for event in filtered_events if event.industry == industry]
        
        if membership_type:
            filtered_events = [event for event in filtered_events if event.membership_type == membership_type]
        
        return filtered_events

    def display_events(self, events: List[Event]):
        """Display events in a formatted manner"""
        for event in events:
            print(f"ID: {event.id}")
            print(f"Name: {event.name}")
            print(f"Industry: {event.industry.value}")
            print(f"Date: {event.date.strftime('%Y-%m-%d')}")
            print(f"Membership Type: {event.membership_type.value}")
            print(f"Description: {event.description}")
            print("------------------------")

def main():
    try:
        # Create event manager
        event_manager = EventManager()

        # Create events
        event1 = Event(1, "Tech Conference", Industry.TECH, datetime(2024, 9, 20), MembershipType.PREMIUM, "A tech conference for premium members")
        event2 = Event(2, "Finance Seminar", Industry.FINANCE, datetime(2024, 10, 15), MembershipType.BASIC, "A finance seminar for basic members")
        event3 = Event(3, "Healthcare Workshop", Industry.HEALTHCARE, datetime(2024, 11, 10), MembershipType.PREMIUM, "A healthcare workshop for premium members")

        # Add events to manager
        event_manager.add_event(event1)
        event_manager.add_event(event2)
        event_manager.add_event(event3)

        # Display all events
        print("All Events:")
        event_manager.display_events(event_manager.get_events())

        # Display events filtered by industry
        print("\nTech Events:")
        event_manager.display_events(event_manager.get_events(industry=Industry.TECH))

        # Display events filtered by membership type
        print("\nPremium Events:")
        event_manager.display_events(event_manager.get_events(membership_type=MembershipType.PREMIUM))

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
