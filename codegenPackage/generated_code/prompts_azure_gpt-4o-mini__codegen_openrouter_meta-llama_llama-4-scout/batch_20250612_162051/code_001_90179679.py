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
# digital_support_system.py

class CulturalAccessSystem:
    """
    A digital support system for cultural access based on the initiatives of the Sophia Loisirs & Vie association.
    """

    def __init__(self):
        """
        Initialize the cultural access system.
        """
        self.users = {}
        self.cultural_events = {}

    def register_user(self, user_id, name, email):
        """
        Register a new user in the system.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): User's name.
            email (str): User's email address.

        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        self.users[user_id] = {"name": name, "email": email, "events": []}

    def create_event(self, event_id, name, date, description):
        """
        Create a new cultural event.

        Args:
            event_id (str): Unique identifier for the event.
            name (str): Event name.
            date (str): Event date.
            description (str): Event description.

        Raises:
            ValueError: If the event ID already exists.
        """
        if event_id in self.cultural_events:
            raise ValueError("Event ID already exists")
        self.cultural_events[event_id] = {"name": name, "date": date, "description": description}

    def register_user_for_event(self, user_id, event_id):
        """
        Register a user for a cultural event.

        Args:
            user_id (str): Unique identifier for the user.
            event_id (str): Unique identifier for the event.

        Raises:
            ValueError: If the user or event does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if event_id not in self.cultural_events:
            raise ValueError("Event does not exist")
        self.users[user_id]["events"].append(event_id)

    def get_user_events(self, user_id):
        """
        Get the list of events registered by a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            list: List of event IDs registered by the user.

        Raises:
            ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        return self.users[user_id]["events"]

    def get_event_details(self, event_id):
        """
        Get the details of a cultural event.

        Args:
            event_id (str): Unique identifier for the event.

        Returns:
            dict: Event details.

        Raises:
            ValueError: If the event does not exist.
        """
        if event_id not in self.cultural_events:
            raise ValueError("Event does not exist")
        return self.cultural_events[event_id]


def main():
    # Create a new cultural access system
    system = CulturalAccessSystem()

    try:
        # Register users
        system.register_user("user1", "John Doe", "john@example.com")
        system.register_user("user2", "Jane Doe", "jane@example.com")

        # Create cultural events
        system.create_event("event1", "Concert", "2024-09-17", "A live concert")
        system.create_event("event2", "Exhibition", "2024-09-20", "An art exhibition")

        # Register users for events
        system.register_user_for_event("user1", "event1")
        system.register_user_for_event("user1", "event2")
        system.register_user_for_event("user2", "event1")

        # Get user events
        print("User 1 events:", system.get_user_events("user1"))
        print("User 2 events:", system.get_user_events("user2"))

        # Get event details
        print("Event 1 details:", system.get_event_details("event1"))
        print("Event 2 details:", system.get_event_details("event2"))

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```
