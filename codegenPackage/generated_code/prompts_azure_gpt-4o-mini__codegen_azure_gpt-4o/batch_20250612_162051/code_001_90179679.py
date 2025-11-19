"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate a code snippet that demonstrates how to implement a digital support system for cultural access based on the initiatives of the Sophia Loisirs & Vie association.
Generated: DETERMINISTIC_9017967927e0cfaa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Support System for Cultural Access
Based on the initiatives of the Sophia Loisirs & Vie association.
This script provides a basic implementation of a system to manage cultural events, 
user registrations, and access support.
"""

import json
from datetime import datetime


class CulturalEvent:
    """
    Represents a cultural event.
    """
    def __init__(self, event_id, name, date, location, max_participants):
        self.event_id = event_id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.location = location
        self.max_participants = max_participants
        self.participants = []

    def register_user(self, user):
        """
        Registers a user for the event if slots are available.
        """
        if len(self.participants) >= self.max_participants:
            raise ValueError("Event is fully booked.")
        if user.user_id in [u.user_id for u in self.participants]:
            raise ValueError("User is already registered for this event.")
        self.participants.append(user)

    def to_dict(self):
        """
        Converts the event details to a dictionary for serialization.
        """
        return {
            "event_id": self.event_id,
            "name": self.name,
            "date": self.date.strftime("%Y-%m-%d"),
            "location": self.location,
            "max_participants": self.max_participants,
            "participants": [user.to_dict() for user in self.participants],
        }


class User:
    """
    Represents a user in the system.
    """
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        """
        Converts the user details to a dictionary for serialization.
        """
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
        }


class CulturalAccessSystem:
    """
    Main system to manage cultural events and user registrations.
    """
    def __init__(self):
        self.events = {}
        self.users = {}

    def add_event(self, event):
        """
        Adds a new cultural event to the system.
        """
        if event.event_id in self.events:
            raise ValueError("Event with this ID already exists.")
        self.events[event.event_id] = event

    def add_user(self, user):
        """
        Adds a new user to the system.
        """
        if user.user_id in self.users:
            raise ValueError("User with this ID already exists.")
        self.users[user.user_id] = user

    def register_user_to_event(self, user_id, event_id):
        """
        Registers a user to a specific event.
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        if event_id not in self.events:
            raise ValueError("Event not found.")
        user = self.users[user_id]
        event = self.events[event_id]
        event.register_user(user)

    def save_data(self, file_path):
        """
        Saves the system data to a JSON file.
        """
        data = {
            "events": {event_id: event.to_dict() for event_id, event in self.events.items()},
            "users": {user_id: user.to_dict() for user_id, user in self.users.items()},
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self, file_path):
        """
        Loads system data from a JSON file.
        """
        with open(file_path, "r") as file:
            data = json.load(file)
        self.events = {
            event_id: CulturalEvent(
                event_id=event_id,
                name=event_data["name"],
                date=event_data["date"],
                location=event_data["location"],
                max_participants=event_data["max_participants"],
            )
            for event_id, event_data in data["events"].items()
        }
        self.users = {
            user_id: User(
                user_id=user_id,
                name=user_data["name"],
                email=user_data["email"],
            )
            for user_id, user_data in data["users"].items()
        }
        # Re-register participants to events
        for event_id, event_data in data["events"].items():
            for participant_data in event_data["participants"]:
                user = self.users[participant_data["user_id"]]
                self.events[event_id].participants.append(user)


# Example usage
if __name__ == "__main__":
    system = CulturalAccessSystem()

    # Create users
    user1 = User(user_id="U001", name="Alice", email="alice@example.com")
    user2 = User(user_id="U002", name="Bob", email="bob@example.com")

    # Add users to the system
    system.add_user(user1)
    system.add_user(user2)

    # Create an event
    event = CulturalEvent(
        event_id="E001",
        name="Art Exhibition",
        date="2023-12-01",
        location="Sophia Cultural Center",
        max_participants=2,
    )

    # Add event to the system
    system.add_event(event)

    # Register users to the event
    system.register_user_to_event(user_id="U001", event_id="E001")
    system.register_user_to_event(user_id="U002", event_id="E001")

    # Save system data to a file
    system.save_data("cultural_access_data.json")

    # Load system data from a file
    new_system = CulturalAccessSystem()
    new_system.load_data("cultural_access_data.json")
    print("Data loaded successfully.")
```
