"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dalilamedeiros.com
Prompt: How can I implement a workshop registration system for a mentoring program like the one offered by Dalila Medeiros?
Generated: DETERMINISTIC_dc658e3837253c19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Workshop:
    """Class to represent a workshop."""
    
    def __init__(self, title, date, capacity):
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d")  # Expecting date in 'YYYY-MM-DD' format
        self.capacity = capacity
        self.registered = []

    def register_participant(self, participant):
        """Registers a participant for the workshop if there is capacity."""
        if len(self.registered) < self.capacity:
            self.registered.append(participant)
            return True
        else:
            raise ValueError("Registration failed: Workshop is full.")

    def __str__(self):
        return f"{self.title} on {self.date.strftime('%Y-%m-%d')} - {len(self.registered)}/{self.capacity} registered"

class Participant:
    """Class to represent a participant in the workshop."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"

class RegistrationSystem:
    """Class to handle the registration system for workshops."""
    
    def __init__(self):
        self.workshops = []

    def add_workshop(self, title, date, capacity):
        """Adds a new workshop to the system."""
        workshop = Workshop(title, date, capacity)
        self.workshops.append(workshop)

    def register_participant(self, workshop_title, participant):
        """Registers the participant to the specified workshop."""
        for workshop in self.workshops:
            if workshop.title == workshop_title:
                try:
                    workshop.register_participant(participant)
                    print(f"Successfully registered {participant} to {workshop.title}")
                except ValueError as e:
                    print(e)
                return
        print(f"Workshop {workshop_title} not found.")

    def save_to_file(self, filename):
        """Saves all workshop registrations to a JSON file."""
        data = {
            "workshops": [
                {
                    "title": workshop.title,
                    "date": workshop.date.strftime('%Y-%m-%d'),
                    "capacity": workshop.capacity,
                    "registered": [{"name": p.name, "email": p.email} for p in workshop.registered]
                } for workshop in self.workshops
            ]
        }
        try:
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data saved to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")

# Example usage:
if __name__ == "__main__":
    system = RegistrationSystem()
    
    # Adding workshops
    system.add_workshop("Introduction to Python", "2023-10-15", 30)
    system.add_workshop("Data Science Basics", "2023-10-22", 20)

    # Registering participants
    participant1 = Participant("Alice Smith", "alice@example.com")
    participant2 = Participant("Bob Johnson", "bob@example.com")

    system.register_participant("Introduction to Python", participant1)
    system.register_participant("Data Science Basics", participant2)

    # Save to file
    system.save_to_file("workshop_registrations.json")
```
