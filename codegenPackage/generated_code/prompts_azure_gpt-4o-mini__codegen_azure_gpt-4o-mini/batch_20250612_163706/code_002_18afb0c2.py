"""
Generated Code Metadata:
========================
Original URL: https://syncconnects.com
Prompt: What are some key features to include in a membership management system for a community like Sync Connects that focuses on genuine networking?
Generated: DETERMINISTIC_18afb0c216ef8f3d
Batch ID: 20250612_163706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# membership_management.py

class Member:
    """
    A class to represent a member of the community.
    """

    def __init__(self, member_id, name, email):
        """
        Initializes a new member with the given ID, name, and email.

        :param member_id: Unique identifier for the member
        :param name: Full name of the member
        :param email: Email address of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.networking_events = []

    def add_event(self, event):
        """
        Adds a networking event to the member's list of events.

        :param event: The event to be added
        """
        self.networking_events.append(event)

    def __str__(self):
        return f"Member({self.member_id}, {self.name}, {self.email})"


class Event:
    """
    A class to represent a networking event.
    """

    def __init__(self, event_id, title, date, location):
        """
        Initializes a new event with the given ID, title, date, and location.

        :param event_id: Unique identifier for the event
        :param title: Title of the event
        :param date: Date of the event
        :param location: Location of the event
        """
        self.event_id = event_id
        self.title = title
        self.date = date
        self.location = location

    def __str__(self):
        return f"Event({self.event_id}, {self.title}, {self.date}, {self.location})"


class MembershipManagementSystem:
    """
    A class to manage members and events in the community.
    """

    def __init__(self):
        """
        Initializes the membership management system with empty member and event lists.
        """
        self.members = {}
        self.events = {}

    def add_member(self, member_id, name, email):
        """
        Adds a new member to the system.

        :param member_id: Unique identifier for the member
        :param name: Full name of the member
        :param email: Email address of the member
        :raises ValueError: If the member ID already exists
        """
        if member_id in self.members:
            raise ValueError(f"Member ID {member_id} already exists.")
        self.members[member_id] = Member(member_id, name, email)

    def add_event(self, event_id, title, date, location):
        """
        Adds a new event to the system.

        :param event_id: Unique identifier for the event
        :param title: Title of the event
        :param date: Date of the event
        :param location: Location of the event
        :raises ValueError: If the event ID already exists
        """
        if event_id in self.events:
            raise ValueError(f"Event ID {event_id} already exists.")
        self.events[event_id] = Event(event_id, title, date, location)

    def register_member_for_event(self, member_id, event_id):
        """
        Registers a member for a specific event.

        :param member_id: Unique identifier for the member
        :param event_id: Unique identifier for the event
        :raises KeyError: If the member or event does not exist
        """
        if member_id not in self.members:
            raise KeyError(f"Member ID {member_id} does not exist.")
        if event_id not in self.events:
            raise KeyError(f"Event ID {event_id} does not exist.")
        
        self.members[member_id].add_event(self.events[event_id])

    def list_members(self):
        """
        Lists all members in the system.

        :return: List of members
        """
        return list(self.members.values())

    def list_events(self):
        """
        Lists all events in the system.

        :return: List of events
        """
        return list(self.events.values())


# Example usage
if __name__ == "__main__":
    try:
        mms = MembershipManagementSystem()
        mms.add_member("001", "Alice Smith", "alice@example.com")
        mms.add_member("002", "Bob Johnson", "bob@example.com")
        mms.add_event("E001", "Networking Night", "2023-11-01", "Community Center")
        
        mms.register_member_for_event("001", "E001")
        
        print("Members:")
        for member in mms.list_members():
            print(member)
        
        print("\nEvents:")
        for event in mms.list_events():
            print(event)

    except Exception as e:
        print(f"An error occurred: {e}")
```
