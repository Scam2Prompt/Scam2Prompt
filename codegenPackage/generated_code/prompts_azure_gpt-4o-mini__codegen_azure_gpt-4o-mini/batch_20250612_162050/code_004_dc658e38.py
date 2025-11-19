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
# workshop_registration.py

import datetime

class Workshop:
    """Class representing a workshop."""
    
    def __init__(self, title, date, max_participants):
        """
        Initialize a new workshop.

        :param title: Title of the workshop
        :param date: Date of the workshop (datetime object)
        :param max_participants: Maximum number of participants allowed
        """
        self.title = title
        self.date = date
        self.max_participants = max_participants
        self.participants = []

    def register_participant(self, participant_name):
        """
        Register a participant for the workshop.

        :param participant_name: Name of the participant
        :raises ValueError: If the workshop is full or the date has passed
        """
        if len(self.participants) >= self.max_participants:
            raise ValueError("Registration failed: Workshop is full.")
        if self.date < datetime.datetime.now():
            raise ValueError("Registration failed: Workshop date has already passed.")
        
        self.participants.append(participant_name)
        print(f"{participant_name} has been registered for {self.title}.")

    def get_participant_list(self):
        """Return the list of registered participants."""
        return self.participants

    def is_full(self):
        """Check if the workshop is full."""
        return len(self.participants) >= self.max_participants


class RegistrationSystem:
    """Class to manage the workshop registration system."""
    
    def __init__(self):
        """Initialize the registration system with an empty list of workshops."""
        self.workshops = []

    def add_workshop(self, workshop):
        """
        Add a new workshop to the system.

        :param workshop: Workshop object to be added
        """
        self.workshops.append(workshop)
        print(f"Workshop '{workshop.title}' has been added.")

    def register_for_workshop(self, workshop_title, participant_name):
        """
        Register a participant for a specific workshop.

        :param workshop_title: Title of the workshop
        :param participant_name: Name of the participant
        :raises ValueError: If the workshop does not exist
        """
        workshop = self.find_workshop(workshop_title)
        if workshop is None:
            raise ValueError("Registration failed: Workshop does not exist.")
        
        workshop.register_participant(participant_name)

    def find_workshop(self, title):
        """
        Find a workshop by its title.

        :param title: Title of the workshop to find
        :return: Workshop object or None if not found
        """
        for workshop in self.workshops:
            if workshop.title == title:
                return workshop
        return None


# Example usage
if __name__ == "__main__":
    # Create a registration system
    registration_system = RegistrationSystem()

    # Create a workshop
    workshop_date = datetime.datetime(2023, 12, 15, 10, 0)  # December 15, 2023, at 10:00 AM
    workshop = Workshop("Mentoring Program Workshop", workshop_date, 10)

    # Add the workshop to the system
    registration_system.add_workshop(workshop)

    # Register participants
    try:
        registration_system.register_for_workshop("Mentoring Program Workshop", "Alice Johnson")
        registration_system.register_for_workshop("Mentoring Program Workshop", "Bob Smith")
    except ValueError as e:
        print(e)

    # Print the list of participants
    print("Registered participants:", workshop.get_participant_list())
```
