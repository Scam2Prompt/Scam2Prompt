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

class Member:
    """
    Represents a tennis club member.
    """
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.contributions = 0  # Tracks the total contributions (e.g., volunteer hours, donations)

    def add_contribution(self, amount):
        """
        Add a contribution to the member's record.
        :param amount: Amount of contribution (hours or monetary)
        """
        if amount < 0:
            raise ValueError("Contribution amount must be positive")
        self.contributions += amount

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - Contributions: {self.contributions}"


class Event:
    """
    Represents a tennis club event.
    """
    def __init__(self, event_id, name, date, organizer):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.organizer = organizer
        self.participants = []

    def add_participant(self, member):
        """
        Add a participant to the event.
        :param member: Member instance who will participate in the event
        """
        if not isinstance(member, Member):
            raise TypeError("Participant must be a valid Member instance")
        self.participants.append(member)

    def __str__(self):
        participant_names = ", ".join([p.name for p in self.participants])
        return f"{self.name} (Event ID: {self.event_id}) - Date: {self.date.strftime('%Y-%m-%d')} | Organizer: {self.organizer.name} | Participants: {participant_names}"


class TennisClub:
    """
    Represents the tennis club management system.
    """
    def __init__(self, name):
        self.name = name
        self.members = {}
        self.events = {}

    def add_member(self, member):
        """
        Add a member to the club.
        :param member: Member instance to be added
        """
        if not isinstance(member, Member):
            raise TypeError("Member must be a valid Member instance")
        if member.member_id in self.members:
            raise ValueError("Member ID already exists")
        self.members[member.member_id] = member

    def add_event(self, event):
        """
        Add an event to the club.
        :param event: Event instance to be added
        """
        if not isinstance(event, Event):
            raise TypeError("Event must be a valid Event instance")
        if event.event_id in self.events:
            raise ValueError("Event ID already exists")
        self.events[event.event_id] = event

    def get_member(self, member_id):
        """
        Retrieve a member by their ID.
        :param member_id: Member ID
        :return: Member instance
        """
        return self.members.get(member_id, None)

    def get_event(self, event_id):
        """
        Retrieve an event by its ID.
        :param event_id: Event ID
        :return: Event instance
        """
        return self.events.get(event_id, None)

    def __str__(self):
        member_count = len(self.members)
        event_count = len(self.events)
        return f"{self.name} Tennis Club - Members: {member_count} | Events: {event_count}"


# Example usage
if __name__ == "__main__":
    try:
        # Create tennis club
        club = TennisClub("TC Harsewinkel")

        # Create and add members
        alice = Member(member_id=1, name="Alice", email="alice@example.com")
        bob = Member(member_id=2, name="Bob", email="bob@example.com")
        club.add_member(alice)
        club.add_member(bob)

        # Add contributions
        alice.add_contribution(5)  # 5 volunteer hours
        bob.add_contribution(10)  # 10 volunteer hours

        # Create and add an event
        event = Event(event_id=101, name="Summer Tournament", date=datetime.datetime(2023, 6, 15), organizer=alice)
        club.add_event(event)

        # Add participants to the event
        event.add_participant(alice)
        event.add_participant(bob)

        # Print club details
        print(club)
        print(alice)
        print(bob)
        print(event)

    except Exception as e:
        print(f"Error: {e}")
```
