"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Write a code snippet for a tennis club management system that tracks member contributions and organizes events, similar to the functionalities described on TC Harsewinkel's website.
Generated: DETERMINISTIC_78ed27bea27b773b
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Member:
    """Class representing a member of the tennis club."""
    
    def __init__(self, member_id: int, name: str, contributions: float = 0.0):
        self.member_id = member_id
        self.name = name
        self.contributions = contributions
        
    def update_contributions(self, amount: float) -> None:
        """Update the member's contributions by the given amount."""
        if amount < 0:
            raise ValueError("Contribution amount must be non-negative")
        self.contributions += amount

class Event:
    """Class representing an event organized by the tennis club."""
    
    def __init__(self, event_id: int, name: str, date: datetime.date, participants: List[Member] = None):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.participants = participants if participants is not None else []
        
    def add_participant(self, member: Member) -> None:
        """Add a member as a participant in the event."""
        if member in self.participants:
            raise ValueError("Member is already a participant in this event")
        self.participants.append(member)

class TennisClub:
    """Class representing the tennis club management system."""
    
    def __init__(self):
        self.members: Dict[int, Member] = {}
        self.events: Dict[int, Event] = {}
        
    def add_member(self, member_id: int, name: str) -> None:
        """Add a new member to the club."""
        if member_id in self.members:
            raise ValueError(f"Member with ID {member_id} already exists")
        self.members[member_id] = Member(member_id, name)

    def record_contribution(self, member_id: int, amount: float) -> None:
        """Record a contribution made by a member."""
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}")
        self.members[member_id].update_contributions(amount)
    
    def create_event(self, event_id: int, name: str, date: datetime.date) -> None:
        """Create a new event."""
        if event_id in self.events:
            raise ValueError(f"Event with ID {event_id} already exists")
        self.events[event_id] = Event(event_id, name, date)

    def register_member_for_event(self, event_id: int, member_id: int) -> None:
        """Register a member for a specific event."""
        if event_id not in self.events:
            raise ValueError(f"No event found with ID {event_id}")
        if member_id not in self.members:
            raise ValueError(f"No member found with ID {member_id}")
        self.events[event_id].add_participant(self.members[member_id])

# Example usage
if __name__ == "__main__":
    club = TennisClub()
    try:
        club.add_member(1, "John Doe")
        club.record_contribution(1, 100.0)
        club.create_event(101, "Tennis Tournament", datetime.date(2023, 6, 15))
        club.register_member_for_event(101, 1)
        
        print(f"Member Contributions: {club.members[1].contributions}")
        print(f"Event Participants: {len(club.events[101].participants)}")

    except ValueError as e:
        print(f"Error: {e}")
```
