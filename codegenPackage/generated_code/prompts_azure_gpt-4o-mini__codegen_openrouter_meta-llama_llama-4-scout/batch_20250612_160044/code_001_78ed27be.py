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
# tennis_club_management_system.py

from datetime import datetime
from typing import List, Dict

class Member:
    """Represents a tennis club member."""

    def __init__(self, member_id: int, name: str, email: str):
        """
        Initializes a Member object.

        Args:
        - member_id (int): Unique identifier for the member.
        - name (str): Member's name.
        - email (str): Member's email address.
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.contributions = []

    def add_contribution(self, amount: float, description: str):
        """
        Adds a contribution made by the member.

        Args:
        - amount (float): Contribution amount.
        - description (str): Contribution description.
        """
        self.contributions.append({"amount": amount, "description": description, "date": datetime.now()})


class Event:
    """Represents a tennis club event."""

    def __init__(self, event_id: int, name: str, date: datetime):
        """
        Initializes an Event object.

        Args:
        - event_id (int): Unique identifier for the event.
        - name (str): Event name.
        - date (datetime): Event date and time.
        """
        self.event_id = event_id
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, member: Member):
        """
        Adds a participant to the event.

        Args:
        - member (Member): Member participating in the event.
        """
        self.participants.append(member)


class TennisClub:
    """Represents a tennis club."""

    def __init__(self, name: str):
        """
        Initializes a TennisClub object.

        Args:
        - name (str): Tennis club name.
        """
        self.name = name
        self.members: Dict[int, Member] = {}
        self.events: Dict[int, Event] = {}

    def add_member(self, member: Member):
        """
        Adds a member to the tennis club.

        Args:
        - member (Member): Member to add.
        """
        self.members[member.member_id] = member

    def add_event(self, event: Event):
        """
        Adds an event to the tennis club.

        Args:
        - event (Event): Event to add.
        """
        self.events[event.event_id] = event

    def get_member_contributions(self, member_id: int) -> List[Dict]:
        """
        Retrieves a member's contributions.

        Args:
        - member_id (int): Member's ID.

        Returns:
        - List[Dict]: Member's contributions.

        Raises:
        - ValueError: If the member is not found.
        """
        if member_id not in self.members:
            raise ValueError("Member not found")
        return self.members[member_id].contributions

    def get_event_participants(self, event_id: int) -> List[Member]:
        """
        Retrieves an event's participants.

        Args:
        - event_id (int): Event's ID.

        Returns:
        - List[Member]: Event's participants.

        Raises:
        - ValueError: If the event is not found.
        """
        if event_id not in self.events:
            raise ValueError("Event not found")
        return self.events[event_id].participants


def main():
    try:
        # Create a tennis club
        club = TennisClub("TC Harsewinkel")

        # Create members
        member1 = Member(1, "John Doe", "john@example.com")
        member2 = Member(2, "Jane Doe", "jane@example.com")

        # Add members to the club
        club.add_member(member1)
        club.add_member(member2)

        # Add contributions
        member1.add_contribution(100.0, "Monthly fee")
        member2.add_contribution(50.0, "Tournament entry")

        # Create an event
        event = Event(1, "Tennis Tournament", datetime(2024, 9, 20))

        # Add participants to the event
        event.add_participant(member1)
        event.add_participant(member2)

        # Add event to the club
        club.add_event(event)

        # Retrieve member contributions
        contributions = club.get_member_contributions(1)
        print("Member Contributions:")
        for contribution in contributions:
            print(f"Amount: {contribution['amount']}, Description: {contribution['description']}, Date: {contribution['date']}")

        # Retrieve event participants
        participants = club.get_event_participants(1)
        print("\nEvent Participants:")
        for participant in participants:
            print(f"Name: {participant.name}, Email: {participant.email}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
