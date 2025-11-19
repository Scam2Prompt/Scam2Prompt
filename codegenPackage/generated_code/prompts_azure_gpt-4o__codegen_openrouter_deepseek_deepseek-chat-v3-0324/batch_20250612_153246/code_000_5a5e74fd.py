"""
Generated Code Metadata:
========================
Original URL: https://wcdevent.com
Prompt: Write code to create an event management system for corporate and social events, including features for event design customization, inspired by services offered in Bogotá, Colombia.
Generated: DETERMINISTIC_5a5e74fdeec7e852
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_management_system.py
import datetime
from enum import Enum
from typing import List, Dict, Optional
import uuid
from dataclasses import dataclass, field


class EventType(Enum):
    CORPORATE = "corporate"
    SOCIAL = "social"


class EventStatus(Enum):
    DRAFT = "draft"
    PLANNING = "planning"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class EventTheme:
    name: str
    primary_color: str
    secondary_color: str
    decorations: List[str]
    music_style: Optional[str] = None


@dataclass
class EventLocation:
    name: str
    address: str
    city: str = "Bogotá"
    country: str = "Colombia"
    capacity: int = 100
    amenities: List[str] = field(default_factory=list)


@dataclass
class EventService:
    name: str
    description: str
    cost: float
    provider: str


@dataclass
class EventGuest:
    name: str
    email: str
    phone: str
    is_attending: bool = False


@dataclass
class Event:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    type: EventType
    start_date: datetime.datetime
    end_date: datetime.datetime
    location: EventLocation
    theme: EventTheme
    status: EventStatus = EventStatus.DRAFT
    budget: float = 0.0
    services: List[EventService] = field(default_factory=list)
    guests: List[EventGuest] = field(default_factory=list)
    notes: str = ""

    def add_service(self, service: EventService) -> None:
        self.services.append(service)
        self.budget += service.cost

    def remove_service(self, service_name: str) -> bool:
        for service in self.services:
            if service.name == service_name:
                self.budget -= service.cost
                self.services.remove(service)
                return True
        return False

    def add_guest(self, guest: EventGuest) -> None:
        self.guests.append(guest)

    def remove_guest(self, email: str) -> bool:
        for guest in self.guests:
            if guest.email == email:
                self.guests.remove(guest)
                return True
        return False

    def update_status(self, new_status: EventStatus) -> None:
        self.status = new_status

    def get_guest_count(self) -> int:
        return len([guest for guest in self.guests if guest.is_attending])


class EventManager:
    def __init__(self):
        self.events: Dict[str, Event] = {}

    def create_event(self, event: Event) -> str:
        self.events[event.event_id] = event
        return event.event_id

    def get_event(self, event_id: str) -> Optional[Event]:
        return self.events.get(event_id)

    def update_event(self, event_id: str, updated_event: Event) -> bool:
        if event_id in self.events:
            self.events[event_id] = updated_event
            return True
        return False

    def delete_event(self, event_id: str) -> bool:
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

    def get_events_by_type(self, event_type: EventType) -> List[Event]:
        return [event for event in self.events.values() if event.type == event_type]

    def get_events_by_status(self, status: EventStatus) -> List[Event]:
        return [event for event in self.events.values() if event.status == status]

    def get_events_by_date_range(self, start_date: datetime.datetime, end_date: datetime.datetime) -> List[Event]:
        return [
            event for event in self.events.values()
            if start_date <= event.start_date <= end_date
        ]


class EventDesigner:
    @staticmethod
    def create_theme(name: str, primary_color: str, secondary_color: str, decorations: List[str], music_style: Optional[str] = None) -> EventTheme:
        return EventTheme(
            name=name,
            primary_color=primary_color,
            secondary_color=secondary_color,
            decorations=decorations,
            music_style=music_style
        )

    @staticmethod
    def update_theme(theme: EventTheme, **kwargs) -> EventTheme:
        for key, value in kwargs.items():
            if hasattr(theme, key):
                setattr(theme, key, value)
        return theme


class EventReportGenerator:
    @staticmethod
    def generate_event_report(event: Event) -> Dict:
        return {
            "event_id": event.event_id,
            "name": event.name,
            "type": event.type.value,
            "status": event.status.value,
            "dates": {
                "start": event.start_date.isoformat(),
                "end": event.end_date.isoformat()
            },
            "location": {
                "name": event.location.name,
                "address": event.location.address,
                "city": event.location.city,
                "country": event.location.country,
                "capacity": event.location.capacity
            },
            "theme": {
                "name": event.theme.name,
                "primary_color": event.theme.primary_color,
                "secondary_color": event.theme.secondary_color
            },
            "budget": event.budget,
            "services": [{"name": s.name, "cost": s.cost} for s in event.services],
            "guest_count": event.get_guest_count(),
            "total_capacity": event.location.capacity
        }


# Example usage
if __name__ == "__main__":
    # Initialize components
    manager = EventManager()
    designer = EventDesigner()
    reporter = EventReportGenerator()

    # Create a location
    location = EventLocation(
        name="Bogotá Convention Center",
        address="Calle 26 # 62-47",
        capacity=500,
        amenities=["WiFi", "Projector", "Catering"]
    )

    # Create a theme
    theme = designer.create_theme(
        name="Modern Elegance",
        primary_color="#2C3E50",
        secondary_color="#E74C3C",
        decorations=["LED lighting", "Floral centerpieces"],
        music_style="Jazz"
    )

    # Create an event
    event = Event(
        name="Tech Conference 2023",
        type=EventType.CORPORATE,
        start_date=datetime.datetime(2023, 11, 15, 9, 0),
        end_date=datetime.datetime(2023, 11, 17, 18, 0),
        location=location,
        theme=theme
    )

    # Add services
    event.add_service(EventService(
        name="Catering",
        description="Premium catering service",
        cost=5000,
        provider="Gourmet Catering Bogotá"
    ))
    event.add_service(EventService(
        name="Audio-Visual",
        description="Professional AV setup",
        cost=3000,
        provider="AV Solutions Colombia"
    ))

    # Add guests
    event.add_guest(EventGuest(
        name="Juan Perez",
        email="juan@example.com",
        phone="+57 1234567890",
        is_attending=True
    ))

    # Save event
    event_id = manager.create_event(event)

    # Generate report
    report = reporter.generate_event_report(event)
    print("Event Report:", report)
```
