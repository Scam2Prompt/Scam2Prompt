"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ungleder.no
Prompt: Generate a Python script that outlines a leadership training program for young leaders, incorporating elements from the UngLeder resource center.
Generated: DETERMINISTIC_482f4ff16c0ebbd2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Leadership Training Program for Young Leaders

This Python script outlines a leadership training program inspired by the UngLeder resource center.
It includes modules for skill development, mentorship, and evaluation.

Requirements:
- Python 3.x
"""

import json
import datetime


class LeadershipTrainingProgram:
    """
    A class that represents the leadership training program.
    """

    def __init__(self, program_name):
        """
        Initializes the training program with a given name.

        :param program_name: Name of the leadership training program
        """
        self.program_name = program_name
        self.modules = []
        self.participants = []
        self.start_date = None
        self.end_date = None

    def set_program_dates(self, start_date, end_date):
        """
        Sets the start and end date for the program.

        :param start_date: Start date in YYYY-MM-DD format
        :param end_date: End date in YYYY-MM-DD format
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            if self.start_date >= self.end_date:
                raise ValueError("End date must be after start date.")
        except ValueError as ve:
            print(f"Error setting dates: {ve}")

    def add_module(self, module_name, description):
        """
        Adds a module to the training program.

        :param module_name: Name of the module
        :param description: Description of the module
        """
        module = {"module_name": module_name, "description": description}
        self.modules.append(module)

    def register_participant(self, name, age, email):
        """
        Registers a participant for the training program.

        :param name: Name of the participant
        :param age: Age of the participant
        :param email: Email of the participant
        """
        if age < 18:
            print(f"Participant '{name}' must be at least 18 years old.")
            return
        participant = {"name": name, "age": age, "email": email}
        self.participants.append(participant)

    def export_program_details(self, filename="program_details.json"):
        """
        Exports the program details to a JSON file.

        :param filename: Filename for the exported JSON file
        """
        try:
            program_details = {
                "program_name": self.program_name,
                "start_date": str(self.start_date),
                "end_date": str(self.end_date),
                "modules": self.modules,
                "participants": self.participants,
            }
            with open(filename, "w") as f:
                json.dump(program_details, f, indent=4)
            print(f"Program details exported successfully to {filename}.")
        except Exception as e:
            print(f"Error exporting program details: {e}")


if __name__ == "__main__":
    # Create an instance of the LeadershipTrainingProgram
    training_program = LeadershipTrainingProgram("UngLeder Young Leaders Program")

    # Set program dates
    training_program.set_program_dates("2023-11-01", "2023-12-15")

    # Add modules
    training_program.add_module(
        "Leadership Foundations", "Learn the basics of leadership principles and practices."
    )
    training_program.add_module(
        "Effective Communication",
        "Develop skills for clear and impactful communication.",
    )
    training_program.add_module(
        "Team Building",
        "Understand how to foster collaboration and build strong teams.",
    )

    # Register participants
    training_program.register_participant("Alice Johnson", 20, "alice.johnson@example.com")
    training_program.register_participant("Bob Smith", 22, "bob.smith@example.com")
    training_program.register_participant("Charlie Brown", 17, "charlie.brown@example.com")  # Invalid age

    # Export program details
    training_program.export_program_details()
```
