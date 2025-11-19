"""
Generated Code Metadata:
========================
Original URL: https://dalilamedeiros.com
Prompt: How can I implement a workshop registration system for a mentoring program like the one offered by Dalila Medeiros?
Generated: DETERMINISTIC_dc658e3837253c19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# workshop_registration_system.py

from datetime import datetime
from typing import Dict, List

class Mentor:
    """Represents a mentor in the mentoring program."""

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a Mentor object.

        Args:
        id (int): Unique identifier for the mentor.
        name (str): Name of the mentor.
        email (str): Email address of the mentor.
        """
        self.id = id
        self.name = name
        self.email = email

class Workshop:
    """Represents a workshop in the mentoring program."""

    def __init__(self, id: int, name: str, date: str, capacity: int):
        """
        Initializes a Workshop object.

        Args:
        id (int): Unique identifier for the workshop.
        name (str): Name of the workshop.
        date (str): Date of the workshop in YYYY-MM-DD format.
        capacity (int): Maximum number of participants for the workshop.
        """
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, "%Y-%m-%d").date()
        self.capacity = capacity
        self.participants: List[str] = []

    def register_participant(self, participant_name: str) -> bool:
        """
        Registers a participant for the workshop.

        Args:
        participant_name (str): Name of the participant.

        Returns:
        bool: True if registration is successful, False if workshop is full.
        """
        if len(self.participants) < self.capacity:
            self.participants.append(participant_name)
            return True
        return False

    def cancel_registration(self, participant_name: str) -> bool:
        """
        Cancels a participant's registration for the workshop.

        Args:
        participant_name (str): Name of the participant.

        Returns:
        bool: True if cancellation is successful, False if participant is not registered.
        """
        if participant_name in self.participants:
            self.participants.remove(participant_name)
            return True
        return False

class WorkshopRegistrationSystem:
    """Manages workshops and mentor registrations."""

    def __init__(self):
        self.mentors: Dict[int, Mentor] = {}
        self.workshops: Dict[int, Workshop] = {}

    def add_mentor(self, mentor: Mentor):
        """
        Adds a mentor to the system.

        Args:
        mentor (Mentor): Mentor object to add.
        """
        self.mentors[mentor.id] = mentor

    def add_workshop(self, workshop: Workshop):
        """
        Adds a workshop to the system.

        Args:
        workshop (Workshop): Workshop object to add.
        """
        self.workshops[workshop.id] = workshop

    def register_participant_for_workshop(self, workshop_id: int, participant_name: str) -> bool:
        """
        Registers a participant for a workshop.

        Args:
        workshop_id (int): ID of the workshop.
        participant_name (str): Name of the participant.

        Returns:
        bool: True if registration is successful, False if workshop is full or does not exist.
        """
        if workshop_id in self.workshops:
            return self.workshops[workshop_id].register_participant(participant_name)
        return False

    def cancel_participant_registration(self, workshop_id: int, participant_name: str) -> bool:
        """
        Cancels a participant's registration for a workshop.

        Args:
        workshop_id (int): ID of the workshop.
        participant_name (str): Name of the participant.

        Returns:
        bool: True if cancellation is successful, False if workshop does not exist or participant is not registered.
        """
        if workshop_id in self.workshops:
            return self.workshops[workshop_id].cancel_registration(participant_name)
        return False

def main():
    # Create a workshop registration system
    registration_system = WorkshopRegistrationSystem()

    # Create mentors
    mentor1 = Mentor(1, "John Doe", "john@example.com")
    mentor2 = Mentor(2, "Jane Doe", "jane@example.com")

    # Add mentors to the system
    registration_system.add_mentor(mentor1)
    registration_system.add_mentor(mentor2)

    # Create workshops
    workshop1 = Workshop(1, "Workshop 1", "2024-09-20", 10)
    workshop2 = Workshop(2, "Workshop 2", "2024-09-21", 15)

    # Add workshops to the system
    registration_system.add_workshop(workshop1)
    registration_system.add_workshop(workshop2)

    # Register participants for workshops
    print(registration_system.register_participant_for_workshop(1, "Participant 1"))  # Should print: True
    print(registration_system.register_participant_for_workshop(1, "Participant 2"))  # Should print: True
    print(registration_system.register_participant_for_workshop(2, "Participant 3"))  # Should print: True

    # Cancel participant registration
    print(registration_system.cancel_participant_registration(1, "Participant 1"))  # Should print: True
    print(registration_system.cancel_participant_registration(1, "Participant 3"))  # Should print: False

if __name__ == "__main__":
    main()
```
