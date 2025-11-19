"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a code snippet for a tennis club management system that tracks member contributions and organizes events, similar to the functionalities described on TC Harsewinkel's website.
Generated: DETERMINISTIC_78ed27bea27b773b
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Member:
    """Class to represent a member of the tennis club."""
    
    def __init__(self, member_id: int, name: str, contributions: float = 0.0):
        self.member_id = member_id
        self.name = name
        self.contributions = contributions

    def add_contribution(self, amount: float):
        """Add a contribution to the member's account."""
        if amount < 0:
            raise ValueError("Contribution amount must be positive.")
        self.contributions += amount

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Contributions: {self.contributions:.2f}"


class Event:
    """Class to represent an event organized by the tennis club."""
    
    def __init__(self, event_id: int, name: str, date: datetime.date):
        self.event_id = event_id
        self.name = name
        self.date = date

    def __str__(self):
        return f"Event ID: {self.event_id}, Name: {self.name}, Date: {self.date}"


class TennisClub:
    """Class to manage members and events in the tennis club."""
    
    def __init__(self):
        self.members: List[Member] = []
        self.events: List[Event] = []

    def add_member(self, member: Member):
        """Add a new member to the club."""
        if any(m.member_id == member.member_id for m in self.members):
            raise ValueError("Member with this ID already exists.")
        self.members.append(member)

    def add_event(self, event: Event):
        """Add a new event to the club."""
        if any(e.event_id == event.event_id for e in self.events):
            raise ValueError("Event with this ID already exists.")
        self.events.append(event)

    def get_member(self, member_id: int) -> Optional[Member]:
        """Retrieve a member by their ID."""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def get_event(self, event_id: int) -> Optional[Event]:
        """Retrieve an event by its ID."""
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

    def list_members(self) -> List[str]:
        """List all members in the club."""
        return [str(member) for member in self.members]

    def list_events(self) -> List[str]:
        """List all events organized by the club."""
        return [str(event) for event in self.events]


# Example usage
if __name__ == "__main__":
    club = TennisClub()

    # Adding members
    try:
        member1 = Member(member_id=1, name="Alice")
        club.add_member(member1)
        member1.add_contribution(100.0)

        member2 = Member(member_id=2, name="Bob")
        club.add_member(member2)
        member2.add_contribution(150.0)

        # Listing members
        print("Members:")
        print("\n".join(club.list_members()))

        # Adding events
        event1 = Event(event_id=1, name="Summer Tournament", date=datetime.date(2023, 7, 15))
        club.add_event(event1)

        # Listing events
        print("\nEvents:")
        print("\n".join(club.list_events()))

    except ValueError as e:
        print(f"Error: {e}")
```
