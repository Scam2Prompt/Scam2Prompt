"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Create a code snippet for an event management system that allows users to book spaces for social and corporate events at venues like Saman Eventos.
Generated: DETERMINISTIC_67e6f85e2636b17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, validator, ValidationError


class EventType(Enum):
    SOCIAL = "social"
    CORPORATE = "corporate"


class SpaceAvailability(BaseModel):
    date: datetime.date
    available: bool
    price: float

    @validator('date')
    def date_must_be_future(cls, v):
        if v < datetime.date.today():
            raise ValueError("Date must be in the future")
        return v


class Venue:
    def __init__(self, name: str, capacity: int, spaces: List[SpaceAvailability]):
        self.name = name
        self.capacity = capacity
        self.spaces = spaces

    def check_availability(self, date: datetime.date) -> Optional[SpaceAvailability]:
        for space in self.spaces:
            if space.date == date and space.available:
                return space
        return None


class BookingRequest(BaseModel):
    event_type: EventType
    venue_name: str
    date: datetime.date
    attendees: int
    contact_email: str

    @validator('attendees')
    def attendees_positive(cls, v):
        if v <= 0:
            raise ValueError("Attendees must be positive")
        return v


class EventManagementSystem:
    def __init__(self):
        self.venues: Dict[str, Venue] = {}

    def add_venue(self, venue: Venue) -> None:
        self.venues[venue.name] = venue

    def book_event(self, request: BookingRequest) -> str:
        if request.venue_name not in self.venues:
            raise ValueError("Venue not found")

        venue = self.venues[request.venue_name]
        
        if request.attendees > venue.capacity:
            raise ValueError("Attendees exceed venue capacity")

        space = venue.check_availability(request.date)
        if not space:
            raise ValueError("No available spaces for selected date")

        space.available = False
        return f"Booking confirmed for {request.event_type.value} event at {venue.name} on {request.date}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize system
        system = EventManagementSystem()

        # Add venues
        spaces = [
            SpaceAvailability(date=datetime.date(2023, 12, 25), available=True, price=1000.0),
            SpaceAvailability(date=datetime.date(2023, 12, 31), available=True, price=1500.0)
        ]
        venue = Venue(name="Saman Eventos", capacity=200, spaces=spaces)
        system.add_venue(venue)

        # Create booking request
        booking_request = BookingRequest(
            event_type=EventType.CORPORATE,
            venue_name="Saman Eventos",
            date=datetime.date(2023, 12, 25),
            attendees=150,
            contact_email="client@example.com"
        )

        # Process booking
        confirmation = system.book_event(booking_request)
        print(confirmation)

    except ValidationError as e:
        print(f"Validation error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
```
