"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Outline a project management tool that helps organize event logistics, including venue selection and staff management, based on Pozy Media's event planning approach.
Generated: DETERMINISTIC_98916f9bc2e4c018
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Event Management Tool for Pozy Media

This tool helps organize event logistics, including venue selection and staff management.
It provides functionalities to manage events, venues, staff, and tasks.
"""

from datetime import datetime
from typing import List, Dict, Optional
import json
import os

class Event:
    """Represents an event with all its details."""
    
    def __init__(self, event_id: str, name: str, start_date: datetime, end_date: datetime,
                 venue_id: str, staff_ids: List[str], tasks: List[str]):
        self.event_id = event_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.venue_id = venue_id
        self.staff_ids = staff_ids
        self.tasks = tasks

    def to_dict(self) -> Dict:
        """Convert Event object to dictionary for serialization."""
        return {
            'event_id': self.event_id,
            'name': self.name,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'venue_id': self.venue_id,
            'staff_ids': self.staff_ids,
            'tasks': self.tasks
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Event':
        """Create Event object from dictionary."""
        return cls(
            event_id=data['event_id'],
            name=data['name'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date']),
            venue_id=data['venue_id'],
            staff_ids=data['staff_ids'],
            tasks=data['tasks']
        )

class Venue:
    """Represents a venue where events can be held."""
    
    def __init__(self, venue_id: str, name: str, address: str, capacity: int, facilities: List[str]):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.capacity = capacity
        self.facilities = facilities

    def to_dict(self) -> Dict:
        """Convert Venue object to dictionary for serialization."""
        return {
            'venue_id': self.venue_id,
            'name': self.name,
            'address': self.address,
            'capacity': self.capacity,
            'facilities': self.facilities
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Venue':
        """Create Venue object from dictionary."""
        return cls(
            venue_id=data['venue_id'],
            name=data['name'],
            address=data['address'],
            capacity=data['capacity'],
            facilities=data['facilities']
        )

class Staff:
    """Represents a staff member who can be assigned to events."""
    
    def __init__(self, staff_id: str, name: str, role: str, contact: str, availability: List[datetime]):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.contact = contact
        self.availability = availability

    def to_dict(self) -> Dict:
        """Convert Staff object to dictionary for serialization."""
        return {
            'staff_id': self.staff_id,
            'name': self.name,
            'role': self.role,
            'contact': self.contact,
            'availability': [dt.isoformat() for dt in self.availability]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Staff':
        """Create Staff object from dictionary."""
        return cls(
            staff_id=data['staff_id'],
            name=data['name'],
            role=data['role'],
            contact=data['contact'],
            availability=[datetime.fromisoformat(dt) for dt in data['availability']]
        )

class EventManager:
    """Main class to manage events, venues, and staff."""
    
    def __init__(self, data_dir: str = 'data'):
        self.data_dir = data_dir
        self.events: Dict[str, Event] = {}
        self.venues: Dict[str, Venue] = {}
        self.staff: Dict[str, Staff] = {}
        self._ensure_data_dir()
        self._load_data()

    def _ensure_data_dir(self) -> None:
        """Ensure data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)

    def _load_data(self) -> None:
        """Load data from JSON files."""
        try:
            # Load events
            events_path = os.path.join(self.data_dir, 'events.json')
            if os.path.exists(events_path):
                with open(events_path, 'r') as f:
                    events_data = json.load(f)
                    self.events = {e['event_id']: Event.from_dict(e) for e in events_data}

            # Load venues
            venues_path = os.path.join(self.data_dir, 'venues.json')
            if os.path.exists(venues_path):
                with open(venues_path, 'r') as f:
                    venues_data = json.load(f)
                    self.venues = {v['venue_id']: Venue.from_dict(v) for v in venues_data}

            # Load staff
            staff_path = os.path.join(self.data_dir, 'staff.json')
            if os.path.exists(staff_path):
                with open(staff_path, 'r') as f:
                    staff_data = json.load(f)
                    self.staff = {s['staff_id']: Staff.from_dict(s) for s in staff_data}
        except Exception as e:
            print(f"Error loading data: {e}")

    def _save_data(self) -> None:
        """Save data to JSON files."""
        try:
            # Save events
            with open(os.path.join(self.data_dir, 'events.json'), 'w') as f:
                json.dump([e.to_dict() for e in self.events.values()], f, indent=2)

            # Save venues
            with open(os.path.join(self.data_dir, 'venues.json'), 'w') as f:
                json.dump([v.to_dict() for v in self.venues.values()], f, indent=2)

            # Save staff
            with open(os.path.join(self.data_dir, 'staff.json'), 'w') as f:
                json.dump([s.to_dict() for s in self.staff.values()], f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_event(self, event: Event) -> None:
        """Add a new event."""
        if event.event_id in self.events:
            raise ValueError(f"Event with ID {event.event_id} already exists")
        self.events[event.event_id] = event
        self._save_data()

    def get_event(self, event_id: str) -> Optional[Event]:
        """Get an event by ID."""
        return self.events.get(event_id)

    def add_venue(self, venue: Venue) -> None:
        """Add a new venue."""
        if venue.venue_id in self.venues:
            raise ValueError(f"Venue with ID {venue.venue_id} already exists")
        self.venues[venue.venue_id] = venue
        self._save_data()

    def get_venue(self, venue_id: str) -> Optional[Venue]:
        """Get a venue by ID."""
        return self.venues.get(venue_id)

    def add_staff(self, staff: Staff) -> None:
        """Add a new staff member."""
        if staff.staff_id in self.staff:
            raise ValueError(f"Staff with ID {staff.staff_id} already exists")
        self.staff[staff.staff_id] = staff
        self._save_data()

    def get_staff(self, staff_id: str) -> Optional[Staff]:
        """Get a staff member by ID."""
        return self.staff.get(staff_id)

    def assign_staff_to_event(self, event_id: str, staff_id: str) -> None:
        """Assign a staff member to an event."""
        if event_id not in self.events:
            raise ValueError(f"Event with ID {event_id} not found")
        if staff_id not in self.staff:
            raise ValueError(f"Staff with ID {staff_id} not found")
        
        if staff_id not in self.events[event_id].staff_ids:
            self.events[event_id].staff_ids.append(staff_id)
            self._save_data()

    def get_available_venues(self, start_date: datetime, end_date: datetime, capacity: int) -> List[Venue]:
        """Get venues available during the specified time period with sufficient capacity."""
        available_venues = []
        
        for venue in self.venues.values():
            # Check capacity
            if venue.capacity < capacity:
                continue
                
            # Check if venue is already booked for any overlapping events
            is_available = True
            for event in self.events.values():
                if event.venue_id == venue.venue_id:
                    if (start_date < event.end_date) and (end_date > event.start_date):
                        is_available = False
                        break
            
            if is_available:
                available_venues.append(venue)
                
        return available_venues

    def get_available_staff(self, start_date: datetime, end_date: datetime,
