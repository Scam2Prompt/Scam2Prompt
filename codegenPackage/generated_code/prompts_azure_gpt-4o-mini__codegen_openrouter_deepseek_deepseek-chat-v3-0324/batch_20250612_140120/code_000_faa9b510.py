"""
Generated Code Metadata:
========================
Original URL: https://jamuae.com
Prompt: Generate a code snippet for an event management system that includes features for wedding planning, corporate events, and festival organization as described on the Jam UAE website.
Generated: DETERMINISTIC_faa9b510958faf2d
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
import uuid

class EventType(Enum):
    WEDDING = "Wedding"
    CORPORATE = "Corporate"
    FESTIVAL = "Festival"

class EventStatus(Enum):
    PLANNING = "Planning"
    CONFIRMED = "Confirmed"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Vendor:
    def __init__(self, name: str, service_type: str, contact: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.service_type = service_type
        self.contact = contact

class Guest:
    def __init__(self, name: str, email: str, rsvp_status: bool = False):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.rsvp_status = rsvp_status

class Task:
    def __init__(self, description: str, due_date: datetime, assigned_to: str):
        self.id = str(uuid.uuid4())
        self.description = description
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.completed = False

class Event:
    def __init__(
        self,
        name: str,
        event_type: EventType,
        start_date: datetime,
        end_date: datetime,
        location: str,
        organizer: str
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.event_type = event_type
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.organizer = organizer
        self.status = EventStatus.PLANNING
        self.guests: List[Guest] = []
        self.vendors: List[Vendor] = []
        self.tasks: List[Task] = []
        self.budget: float = 0.0
        self.notes: str = ""

    def add_guest(self, guest: Guest) -> None:
        self.guests.append(guest)

    def add_vendor(self, vendor: Vendor) -> None:
        self.vendors.append(vendor)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def update_status(self, status: EventStatus) -> None:
        self.status = status

    def set_budget(self, amount: float) -> None:
        if amount >= 0:
            self.budget = amount
        else:
            raise ValueError("Budget cannot be negative")

    def add_note(self, note: str) -> None:
        self.notes += f"\n{datetime.now().strftime('%Y-%m-%d %H:%M')}: {note}"

class EventManager:
    def __init__(self):
        self.events: Dict[str, Event] = {}

    def create_event(
        self,
        name: str,
        event_type: EventType,
        start_date: datetime,
        end_date: datetime,
        location: str,
        organizer: str
    ) -> Event:
        if start_date > end_date:
            raise ValueError("End date must be after start date")
        
        event = Event(name, event_type, start_date, end_date, location, organizer)
        self.events[event.id] = event
        return event

    def get_event(self, event_id: str) -> Optional[Event]:
        return self.events.get(event_id)

    def get_events_by_type(self, event_type: EventType) -> List[Event]:
        return [event for event in self.events.values() if event.event_type == event_type]

    def cancel_event(self, event_id: str) -> None:
        event = self.events.get(event_id)
        if event:
            event.update_status(EventStatus.CANCELLED)
        else:
            raise ValueError("Event not found")

    def get_upcoming_events(self) -> List[Event]:
        now = datetime.now()
        return [
            event for event in self.events.values()
            if event.start_date > now and event.status != EventStatus.CANCELLED
        ]

    def get_event_guests(self, event_id: str) -> List[Guest]:
        event = self.events.get(event_id)
        if event:
            return event.guests
        raise ValueError("Event not found")

    def get_event_vendors(self, event_id: str) -> List[Vendor]:
        event = self.events.get(event_id)
        if event:
            return event.vendors
        raise ValueError("Event not found")

    def get_event_tasks(self, event_id: str) -> List[Task]:
        event = self.events.get(event_id)
        if event:
            return event.tasks
        raise ValueError("Event not found")

# Example usage
if __name__ == "__main__":
    manager = EventManager()
    
    # Create a wedding event
    wedding = manager.create_event(
        "Smith-Johnson Wedding",
        EventType.WEDDING,
        datetime(2023, 12, 15),
        datetime(2023, 12, 15),
        "Grand Ballroom, Dubai",
        "Jam UAE"
    )
    
    # Add guests
    wedding.add_guest(Guest("Alice Johnson", "alice@example.com", True))
    wedding.add_guest(Guest("Bob Smith", "bob@example.com"))
    
    # Add vendors
    wedding.add_vendor(Vendor("Dubai Catering", "Catering", "contact@dubaicatering.com"))
    wedding.add_vendor(Vendor("Luxury Flowers", "Florist", "info@luxuryflowers.ae"))
    
    # Add tasks
    wedding.add_task(Task("Finalize menu", datetime(2023, 11, 1), "Catering Team"))
    wedding.add_task(Task("Send invitations", datetime(2023, 10, 15), "Planning Team"))
    
    # Update budget and status
    wedding.set_budget(50000.0)
    wedding.update_status(EventStatus.CONFIRMED)
    
    # Get upcoming events
    upcoming = manager.get_upcoming_events()
    print(f"Upcoming events: {[e.name for e in upcoming]}")
```
