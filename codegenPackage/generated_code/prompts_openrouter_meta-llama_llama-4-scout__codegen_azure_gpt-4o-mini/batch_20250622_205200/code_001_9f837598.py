"""
Generated Code Metadata:
========================
Original URL: https://ogma.ca
Prompt: Write a Python script to manage membership information for an organization like OGMA, including member names, contact details, and event registrations.
Generated: DETERMINISTIC_9f837598bd499204
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class Member:
    """Class to represent a member of the organization."""
    
    def __init__(self, name, contact_details):
        self.name = name
        self.contact_details = contact_details
        self.events_registered = []

    def register_event(self, event_name):
        """Register the member for an event."""
        if event_name not in self.events_registered:
            self.events_registered.append(event_name)
        else:
            raise ValueError(f"{self.name} is already registered for {event_name}.")

    def __repr__(self):
        return f"Member(name={self.name}, contact_details={self.contact_details}, events_registered={self.events_registered})"


class MembershipManager:
    """Class to manage membership information."""
    
    def __init__(self, data_file='members.json'):
        self.data_file = data_file
        self.members = self.load_members()

    def load_members(self):
        """Load members from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                try:
                    members_data = json.load(file)
                    return {name: Member(name, details) for name, details in members_data.items()}
                except json.JSONDecodeError as e:
                    print(f"Error loading members: {e}")
                    return {}
        return {}

    def save_members(self):
        """Save members to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump({name: member.contact_details for name, member in self.members.items()}, file)

    def add_member(self, name, contact_details):
        """Add a new member to the organization."""
        if name in self.members:
            raise ValueError(f"Member {name} already exists.")
        self.members[name] = Member(name, contact_details)
        self.save_members()

    def register_member_for_event(self, name, event_name):
        """Register a member for an event."""
        if name not in self.members:
            raise ValueError(f"Member {name} does not exist.")
        self.members[name].register_event(event_name)
        self.save_members()

    def get_member_info(self, name):
        """Retrieve information about a member."""
        if name not in self.members:
            raise ValueError(f"Member {name} does not exist.")
        return self.members[name]

    def __repr__(self):
        return f"MembershipManager(members={self.members})"


if __name__ == "__main__":
    # Example usage of the MembershipManager
    manager = MembershipManager()

    # Adding members
    try:
        manager.add_member("Alice Smith", {"email": "alice@example.com", "phone": "123-456-7890"})
        manager.add_member("Bob Johnson", {"email": "bob@example.com", "phone": "098-765-4321"})
    except ValueError as e:
        print(e)

    # Registering a member for an event
    try:
        manager.register_member_for_event("Alice Smith", "Annual Gala")
    except ValueError as e:
        print(e)

    # Retrieving member information
    try:
        member_info = manager.get_member_info("Alice Smith")
        print(member_info)
    except ValueError as e:
        print(e)
```
