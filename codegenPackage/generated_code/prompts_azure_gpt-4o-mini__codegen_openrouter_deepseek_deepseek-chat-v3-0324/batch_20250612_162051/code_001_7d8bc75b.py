"""
Generated Code Metadata:
========================
Original URL: https://vipmoov.com
Prompt: Write a Python function that utilizes an event planning library to manage events globally, inspired by the services provided by VIP MOOV.
Generated: DETERMINISTIC_7d8bc75b541973ef
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
from typing import List, Dict, Optional
from enum import Enum
import uuid

class EventStatus(Enum):
    """Enum representing the status of an event."""
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"

class EventType(Enum):
    """Enum representing the type of an event."""
    CONFERENCE = "CONFERENCE"
    CONCERT = "CONCERT"
    FESTIVAL = "FESTIVAL"
    SPORTS = "SPORTS"
    OTHER = "OTHER"

class Event:
    """Class representing an event in the event planning system."""
    
    def __init__(
        self,
        name: str,
        event_type: EventType,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        location: str,
        description: str = "",
        status: EventStatus = EventStatus.DRAFT,
    ):
        """Initialize an Event instance.
        
        Args:
            name: Name of the event.
            event_type: Type of the event (from EventType enum).
            start_time: Start time of the event.
            end_time: End time of the event.
            location: Location of the event.
            description: Description of the event (optional).
            status: Status of the event (from EventStatus enum, defaults to DRAFT).
        """
        self.event_id = str(uuid.uuid4())
        self.name = name
        self.event_type = event_type
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def update_status(self, new_status: EventStatus) -> None:
        """Update the status of the event.
        
        Args:
            new_status: New status to set (from EventStatus enum).
        """
        self.status = new_status
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert the event to a dictionary for serialization.
        
        Returns:
            Dictionary representation of the event.
        """
        return {
            "event_id": self.event_id,
            "name": self.name,
            "event_type": self.event_type.value,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "location": self.location,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

class EventManager:
    """Class to manage events globally."""
    
    def __init__(self):
        """Initialize the EventManager with an empty list of events."""
        self.events: Dict[str, Event] = {}
    
    def create_event(
        self,
        name: str,
        event_type: EventType,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        location: str,
        description: str = "",
        status: EventStatus = EventStatus.DRAFT,
    ) -> Event:
        """Create a new event and add it to the manager.
        
        Args:
            name: Name of the event.
            event_type: Type of the event (from EventType enum).
            start_time: Start time of the event.
            end_time: End time of the event.
            location: Location of the event.
            description: Description of the event (optional).
            status: Status of the event (from EventStatus enum, defaults to DRAFT).
            
        Returns:
            The created Event instance.
            
        Raises:
            ValueError: If start_time is after end_time.
        """
        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")
        
        event = Event(
            name=name,
            event_type=event_type,
            start_time=start_time,
            end_time=end_time,
            location=location,
            description=description,
            status=status,
        )
        self.events[event.event_id] = event
        return event
    
    def get_event(self, event_id: str) -> Optional[Event]:
        """Retrieve an event by its ID.
        
        Args:
            event_id: ID of the event to retrieve.
            
        Returns:
            The Event instance if found, None otherwise.
        """
        return self.events.get(event_id)
    
    def update_event_status(self, event_id: str, new_status: EventStatus) -> bool:
        """Update the status of an event.
        
        Args:
            event_id: ID of the event to update.
            new_status: New status to set (from EventStatus enum).
            
        Returns:
            True if the event was found and updated, False otherwise.
        """
        event = self.get_event(event_id)
        if event:
            event.update_status(new_status)
            return True
        return False
    
    def delete_event(self, event_id: str) -> bool:
        """Delete an event by its ID.
        
        Args:
            event_id: ID of the event to delete.
            
        Returns:
            True if the event was found and deleted, False otherwise.
        """
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False
    
    def list_events(
        self,
        status: Optional[EventStatus] = None,
        event_type: Optional[EventType] = None,
    ) -> List[Event]:
        """List events filtered by status and/or type.
        
        Args:
            status: Filter events by status (optional).
            event_type: Filter events by type (optional).
            
        Returns:
            List of Event instances matching the filters.
        """
        events = list(self.events.values())
        if status:
            events = [e for e in events if e.status == status]
        if event_type:
            events = [e for e in events if e.event_type == event_type]
        return events
    
    def get_upcoming_events(self, days: int = 30) -> List[Event]:
        """Get events happening within the next specified days.
        
        Args:
            days: Number of days to look ahead (defaults to 30).
            
        Returns:
            List of upcoming Event instances.
        """
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days)
        return [
            e for e in self.events.values()
            if e.status == EventStatus.PUBLISHED
            and now <= e.start_time <= end_date
        ]
```
