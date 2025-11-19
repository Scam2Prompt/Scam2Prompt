"""
Generated Code Metadata:
========================
Original URL: https://wordoflifenw.com
Prompt: Generate a code snippet for a church management system that includes features for tracking ministries and events similar to those at Word of Life Northwest.
Generated: DETERMINISTIC_9fffb89e2a7e3d93
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# church_management_system.py
import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto


class MinistryType(Enum):
    """Enum representing different types of ministries in the church."""
    WORSHIP = auto()
    YOUTH = auto()
    CHILDREN = auto()
    OUTREACH = auto()
    PRAYER = auto()
    ADMINISTRATION = auto()


@dataclass
class Member:
    """Class representing a church member."""
    id: int
    name: str
    email: str
    phone: str
    join_date: datetime.date


@dataclass
class Ministry:
    """Class representing a church ministry."""
    id: int
    name: str
    ministry_type: MinistryType
    leader: Member
    members: List[Member]
    description: str
    meeting_schedule: str

    def add_member(self, member: Member) -> None:
        """Add a member to this ministry."""
        if member not in self.members:
            self.members.append(member)

    def remove_member(self, member: Member) -> None:
        """Remove a member from this ministry."""
        if member in self.members:
            self.members.remove(member)


@dataclass
class Event:
    """Class representing a church event."""
    id: int
    name: str
    description: str
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    location: str
    responsible_ministry: Ministry
    attendees: List[Member]
    is_recurring: bool = False
    recurrence_pattern: Optional[str] = None

    def add_attendee(self, member: Member) -> None:
        """Add an attendee to this event."""
        if member not in self.attendees:
            self.attendees.append(member)

    def remove_attendee(self, member: Member) -> None:
        """Remove an attendee from this event."""
        if member in self.attendees:
            self.attendees.remove(member)


class ChurchManagementSystem:
    """Main class for the church management system."""
    
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.ministries: Dict[int, Ministry] = {}
        self.events: Dict[int, Event] = {}
        self.next_member_id = 1
        self.next_ministry_id = 1
        self.next_event_id = 1

    def add_member(self, name: str, email: str, phone: str, join_date: datetime.date) -> Member:
        """Add a new member to the system."""
        member = Member(
            id=self.next_member_id,
            name=name,
            email=email,
            phone=phone,
            join_date=join_date
        )
        self.members[self.next_member_id] = member
        self.next_member_id += 1
        return member

    def add_ministry(
        self,
        name: str,
        ministry_type: MinistryType,
        leader: Member,
        description: str,
        meeting_schedule: str
    ) -> Ministry:
        """Add a new ministry to the system."""
        if leader.id not in self.members:
            raise ValueError("Leader must be a registered member")
            
        ministry = Ministry(
            id=self.next_ministry_id,
            name=name,
            ministry_type=ministry_type,
            leader=leader,
            members=[leader],
            description=description,
            meeting_schedule=meeting_schedule
        )
        self.ministries[self.next_ministry_id] = ministry
        self.next_ministry_id += 1
        return ministry

    def add_event(
        self,
        name: str,
        description: str,
        start_datetime: datetime.datetime,
        end_datetime: datetime.datetime,
        location: str,
        responsible_ministry: Ministry,
        is_recurring: bool = False,
        recurrence_pattern: Optional[str] = None
    ) -> Event:
        """Add a new event to the system."""
        if responsible_ministry.id not in self.ministries:
            raise ValueError("Responsible ministry must be registered")
            
        if end_datetime <= start_datetime:
            raise ValueError("End datetime must be after start datetime")
            
        event = Event(
            id=self.next_event_id,
            name=name,
            description=description,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            location=location,
            responsible_ministry=responsible_ministry,
            attendees=[],
            is_recurring=is_recurring,
            recurrence_pattern=recurrence_pattern
        )
        self.events[self.next_event_id] = event
        self.next_event_id += 1
        return event

    def get_upcoming_events(self, days_ahead: int = 30) -> List[Event]:
        """Get events happening within the next specified days."""
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days_ahead)
        return [
            event for event in self.events.values()
            if now <= event.start_datetime <= end_date
        ]

    def get_ministry_members(self, ministry_id: int) -> List[Member]:
        """Get all members of a specific ministry."""
        if ministry_id not in self.ministries:
            raise ValueError("Ministry not found")
        return self.ministries[ministry_id].members

    def get_member_ministries(self, member_id: int) -> List[Ministry]:
        """Get all ministries a member belongs to."""
        if member_id not in self.members:
            raise ValueError("Member not found")
        return [
            ministry for ministry in self.ministries.values()
            if self.members[member_id] in ministry.members
        ]


# Example usage
if __name__ == "__main__":
    cms = ChurchManagementSystem()
    
    # Add some members
    pastor = cms.add_member(
        name="John Smith",
        email="john@example.com",
        phone="555-1234",
        join_date=datetime.date(2010, 5, 15)
    )
    
    worship_leader = cms.add_member(
        name="Sarah Johnson",
        email="sarah@example.com",
        phone="555-5678",
        join_date=datetime.date(2015, 3, 22)
    )
    
    # Add a ministry
    worship_ministry = cms.add_ministry(
        name="Worship Team",
        ministry_type=MinistryType.WORSHIP,
        leader=worship_leader,
        description="Leads the congregation in worship during services",
        meeting_schedule="Every Wednesday at 7:00 PM"
    )
    
    # Add an event
    sunday_service = cms.add_event(
        name="Sunday Worship Service",
        description="Weekly Sunday worship service",
        start_datetime=datetime.datetime.now() + datetime.timedelta(days=2, hours=10),
        end_datetime=datetime.datetime.now() + datetime.timedelta(days=2, hours=12),
        location="Main Sanctuary",
        responsible_ministry=worship_ministry,
        is_recurring=True,
        recurrence_pattern="Weekly on Sundays"
    )
```
