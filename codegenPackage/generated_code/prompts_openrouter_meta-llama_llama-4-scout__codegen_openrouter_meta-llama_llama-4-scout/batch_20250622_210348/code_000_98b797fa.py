"""
Generated Code Metadata:
========================
Original URL: https://munakalati.org
Prompt: Write a Python script to develop a capacity development program for children's book professionals in Africa, incorporating the features and goals of Muna Kalati's programs.
Generated: DETERMINISTIC_98b797fa70b2fd9b
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# capacity_development_program.py

"""
Capacity Development Program for Children's Book Professionals in Africa
====================================================================

This script provides a basic implementation of a capacity development program 
for children's book professionals in Africa, incorporating the features and 
goals of Muna Kalati's programs.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Participant:
    """Represents a participant in the capacity development program."""

    def __init__(self, name, email, country):
        """
        Initializes a Participant object.

        Args:
            name (str): Participant's name.
            email (str): Participant's email address.
            country (str): Participant's country of origin.
        """
        self.name = name
        self.email = email
        self.country = country
        self.training_modules = []

    def add_training_module(self, module):
        """
        Adds a training module to the participant's record.

        Args:
            module (str): Training module name.
        """
        self.training_modules.append(module)

class TrainingModule:
    """Represents a training module in the capacity development program."""

    def __init__(self, name, description, duration):
        """
        Initializes a TrainingModule object.

        Args:
            name (str): Training module name.
            description (str): Training module description.
            duration (int): Training module duration in days.
        """
        self.name = name
        self.description = description
        self.duration = duration

class CapacityDevelopmentProgram:
    """Represents the capacity development program."""

    def __init__(self):
        """
        Initializes a CapacityDevelopmentProgram object.
        """
        self.participants = []
        self.training_modules = []

    def add_participant(self, participant):
        """
        Adds a participant to the program.

        Args:
            participant (Participant): Participant object.
        """
        self.participants.append(participant)

    def add_training_module(self, module):
        """
        Adds a training module to the program.

        Args:
            module (TrainingModule): TrainingModule object.
        """
        self.training_modules.append(module)

    def assign_training_module(self, participant_name, module_name):
        """
        Assigns a training module to a participant.

        Args:
            participant_name (str): Participant's name.
            module_name (str): Training module name.

        Returns:
            bool: True if assignment is successful, False otherwise.
        """
        participant = next((p for p in self.participants if p.name == participant_name), None)
        module = next((m for m in self.training_modules if m.name == module_name), None)

        if participant and module:
            participant.add_training_module(module_name)
            logging.info(f"Assigned {module_name} to {participant_name}")
            return True
        else:
            logging.error(f"Assignment failed: participant or module not found")
            return False

def main():
    # Create a capacity development program
    program = CapacityDevelopmentProgram()

    # Create training modules
    module1 = TrainingModule("Children's Book Development", "Develop children's book content", 5)
    module2 = TrainingModule("Illustration and Design", "Learn illustration and design techniques", 3)

    # Add training modules to the program
    program.add_training_module(module1)
    program.add_training_module(module2)

    # Create participants
    participant1 = Participant("John Doe", "john.doe@example.com", "Kenya")
    participant2 = Participant("Jane Smith", "jane.smith@example.com", "South Africa")

    # Add participants to the program
    program.add_participant(participant1)
    program.add_participant(participant2)

    # Assign training modules to participants
    program.assign_training_module("John Doe", "Children's Book Development")
    program.assign_training_module("Jane Smith", "Illustration and Design")

    # Print program summary
    print("Capacity Development Program Summary:")
    print("----------------------------------------")
    for participant in program.participants:
        print(f"Participant: {participant.name} ({participant.country})")
        print(f"Email: {participant.email}")
        print("Training Modules:")
        for module in participant.training_modules:
            print(f"- {module}")
        print()

if __name__ == "__main__":
    main()
```
