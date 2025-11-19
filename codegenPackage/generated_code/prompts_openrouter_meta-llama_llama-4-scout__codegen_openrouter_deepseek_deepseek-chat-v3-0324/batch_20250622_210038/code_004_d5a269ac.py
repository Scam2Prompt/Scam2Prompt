"""
Generated Code Metadata:
========================
Original URL: https://dee-lance.pages.dev
Prompt: "Develop a use case for integrating metaverse features into a freelancing platform like DeeLance, focusing on virtual meetings and networking events."
Generated: DETERMINISTIC_d5a269ac841b3e37
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json
from datetime import datetime
from typing import Optional, List, Dict
from uuid import uuid4
from enum import Enum

# Error handling classes
class MetaverseIntegrationError(Exception):
    """Base class for metaverse integration errors"""
    pass

class UserNotFoundError(MetaverseIntegrationError):
    """Raised when a user is not found"""
    pass

class EventConflictError(MetaverseIntegrationError):
    """Raised when there's a scheduling conflict"""
    pass

# Enums for event types and statuses
class EventType(Enum):
    MEETING = "virtual_meeting"
    NETWORKING = "networking_event"

class EventStatus(Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# Data models
class User:
    def __init__(self, user_id: str, username: str, avatar_url: Optional[str] = None):
        self.user_id = user_id
        self.username = username
        self.avatar_url = avatar_url

class VirtualEvent:
    def __init__(
        self,
        event_id: str,
        title: str,
        event_type: EventType,
        host: User,
        start_time: datetime,
        end_time: datetime,
        max_participants: Optional[int] = None,
        description: Optional[str] = None,
        virtual_space_id: Optional[str] = None
    ):
        self.event_id = event_id
        self.title = title
        self.event_type = event_type
        self.host = host
        self.start_time = start_time
        self.end_time = end_time
        self.max_participants = max_participants
        self.description = description
        self.virtual_space_id = virtual_space_id
        self.participants: List[User] = []
        self.status = EventStatus.SCHEDULED

    def add_participant(self, user: User) -> None:
        if self.max_participants and len(self.participants) >= self.max_participants:
            raise MetaverseIntegrationError("Event has reached maximum participants")
        self.participants.append(user)

    def update_status(self, new_status: EventStatus) -> None:
        self.status = new_status

    def to_dict(self) -> Dict:
        return {
            "event_id": self.event_id,
            "title": self.title,
            "event_type": self.event_type.value,
            "host": {
                "user_id": self.host.user_id,
                "username": self.host.username,
                "avatar_url": self.host.avatar_url
            },
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat(),
            "max_participants": self.max_participants,
            "description": self.description,
            "virtual_space_id": self.virtual_space_id,
            "participants": [
                {
                    "user_id": p.user_id,
                    "username": p.username,
                    "avatar_url": p.avatar_url
                } for p in self.participants
            ],
            "status": self.status.value
        }

# Main service class
class MetaverseIntegrationService:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.events: Dict[str, VirtualEvent] = {}
        self.virtual_spaces: Dict[str, Dict] = {}

    def register_user(self, user_id: str, username: str, avatar_url: Optional[str] = None) -> User:
        if user_id in self.users:
            raise MetaverseIntegrationError("User already registered")
        user = User(user_id, username, avatar_url)
        self.users[user_id] = user
        return user

    def get_user(self, user_id: str) -> User:
        if user_id not in self.users:
            raise UserNotFoundError(f"User {user_id} not found")
        return self.users[user_id]

    def create_virtual_space(self, space_name: str, space_type: str, capacity: int) -> str:
        space_id = str(uuid4())
        self.virtual_spaces[space_id] = {
            "space_id": space_id,
            "space_name": space_name,
            "space_type": space_type,
            "capacity": capacity,
            "is_available": True
        }
        return space_id

    def schedule_event(
        self,
        title: str,
        event_type: EventType,
        host_id: str,
        start_time: datetime,
        end_time: datetime,
        max_participants: Optional[int] = None,
        description: Optional[str] = None
    ) -> VirtualEvent:
        # Check for time conflicts
        for event in self.events.values():
            if event.host.user_id == host_id and (
                (start_time >= event.start_time and start_time < event.end_time) or
                (end_time > event.start_time and end_time <= event.end_time) or
                (start_time <= event.start_time and end_time >= event.end_time)
            ):
                raise EventConflictError("Host has another event scheduled during this time")

        host = self.get_user(host_id)
        event_id = str(uuid4())
        
        # Find available virtual space
        space_id = None
        for space in self.virtual_spaces.values():
            if space["is_available"] and (max_participants is None or space["capacity"] >= max_participants):
                space_id = space["space_id"]
                space["is_available"] = False
                break

        event = VirtualEvent(
            event_id=event_id,
            title=title,
            event_type=event_type,
            host=host,
            start_time=start_time,
            end_time=end_time,
            max_participants=max_participants,
            description=description,
            virtual_space_id=space_id
        )
        
        self.events[event_id] = event
        return event

    def join_event(self, event_id: str, user_id: str) -> VirtualEvent:
        if event_id not in self.events:
            raise MetaverseIntegrationError("Event not found")
        
        event = self.events[event_id]
        user = self.get_user(user_id)
        
        if event.status != EventStatus.SCHEDULED:
            raise MetaverseIntegrationError("Event is not in scheduled state")
        
        if datetime.now() > event.start_time:
            raise MetaverseIntegrationError("Event has already started")
        
        event.add_participant(user)
        return event

    def start_event(self, event_id: str, host_id: str) -> VirtualEvent:
        if event_id not in self.events:
            raise MetaverseIntegrationError("Event not found")
        
        event = self.events[event_id]
        
        if event.host.user_id != host_id:
            raise MetaverseIntegrationError("Only the host can start the event")
        
        if event.status != EventStatus.SCHEDULED:
            raise MetaverseIntegrationError("Event is not in scheduled state")
        
        if datetime.now() < event.start_time:
            raise MetaverseIntegrationError("Event cannot start before scheduled time")
        
        event.update_status(EventStatus.IN_PROGRESS)
        return event

    def end_event(self, event_id: str, host_id: str) -> VirtualEvent:
        if event_id not in self.events:
            raise MetaverseIntegrationError("Event not found")
        
        event = self.events[event_id]
        
        if event.host.user_id != host_id:
            raise MetaverseIntegrationError("Only the host can end the event")
        
        if event.status != EventStatus.IN_PROGRESS:
            raise MetaverseIntegrationError("Event is not in progress")
        
        event.update_status(EventStatus.COMPLETED)
        
        # Release virtual space
        if event.virtual_space_id:
            self.virtual_spaces[event.virtual_space_id]["is_available"] = True
        
        return event

    def cancel_event(self, event_id: str, host_id: str) -> VirtualEvent:
        if event_id not in self.events:
            raise MetaverseIntegrationError("Event not found")
        
        event = self.events[event_id]
        
        if event.host.user_id != host_id:
            raise MetaverseIntegrationError("Only the host can cancel the event")
        
        if event.status not in [EventStatus.SCHEDULED, EventStatus.IN_PROGRESS]:
            raise MetaverseIntegrationError("Event cannot be cancelled in its current state")
        
        event.update_status(EventStatus.CANCELLED)
        
        # Release virtual space
        if event.virtual_space_id:
            self.virtual_spaces[event.virtual_space_id]["is_available"] = True
        
        return event

    def get_event_details(self, event_id: str) -> Dict:
        if event_id not in self.events:
            raise MetaverseIntegrationError("Event not found")
        return self.events[event_id].to_dict()

    def list_upcoming_events(self, event_type: Optional[EventType] = None) -> List[Dict]:
        now = datetime.now
