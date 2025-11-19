"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Generate a code snippet for an NDIS provider management system that includes features for personalized care plans and community participation activities as described by Shareth Homecare Services.
Generated: DETERMINISTIC_d47652be60924473
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NDIS Provider Management System
This script provides a system for managing personalized care plans and community participation activities
for NDIS participants as described by Shareth Homecare Services.

Author: Expert Programmer
"""

import json


class Participant:
    """
    Class to represent an NDIS Participant.
    """

    def __init__(self, participant_id, name, age):
        """
        Initialize a participant object.
        :param participant_id: Unique ID for the participant.
        :param name: Name of the participant.
        :param age: Age of the participant.
        """
        self.participant_id = participant_id
        self.name = name
        self.age = age
        self.care_plan = {}
        self.activities = []

    def add_care_plan(self, goal, strategies):
        """
        Add a personalized care plan to the participant's record.
        :param goal: The goal of the care plan.
        :param strategies: Strategies to achieve the goal.
        """
        self.care_plan = {"goal": goal, "strategies": strategies}

    def add_activity(self, activity_name, description):
        """
        Add a community participation activity.
        :param activity_name: Name of the activity.
        :param description: Brief description of the activity.
        """
        self.activities.append({"activity_name": activity_name, "description": description})

    def to_dict(self):
        """
        Convert the participant object to a dictionary.
        :return: Dictionary representation of the participant object.
        """
        return {
            "participant_id": self.participant_id,
            "name": self.name,
            "age": self.age,
            "care_plan": self.care_plan,
            "activities": self.activities,
        }


class NDISManagementSystem:
    """
    Class to manage NDIS participants and their personalized care plans and activities.
    """

    def __init__(self):
        """
        Initialize the NDIS management system.
        """
        self.participants = {}

    def add_participant(self, participant_id, name, age):
        """
        Add a new NDIS participant.
        :param participant_id: Unique ID for the participant.
        :param name: Name of the participant.
        :param age: Age of the participant.
        """
        if participant_id in self.participants:
            raise ValueError(f"Participant with ID {participant_id} already exists.")
        self.participants[participant_id] = Participant(participant_id, name, age)

    def get_participant(self, participant_id):
        """
        Retrieve a participant's information.
        :param participant_id: Unique ID for the participant.
        :return: Participant object.
        """
        if participant_id not in self.participants:
            raise ValueError(f"Participant with ID {participant_id} not found.")
        return self.participants[participant_id]

    def save_to_file(self, filepath):
        """
        Save participant data to a JSON file.
        :param filepath: Path of the file to save data.
        """
        with open(filepath, "w") as file:
            json.dump({pid: p.to_dict() for pid, p in self.participants.items()}, file, indent=4)

    def load_from_file(self, filepath):
        """
        Load participant data from a JSON file.
        :param filepath: Path of the file to load data.
        """
        try:
            with open(filepath, "r") as file:
                data = json.load(file)
                for pid, pdata in data.items():
                    participant = Participant(pid, pdata["name"], pdata["age"])
                    participant.care_plan = pdata["care_plan"]
                    participant.activities = pdata["activities"]
                    self.participants[pid] = participant
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {filepath} does not exist.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON data. Ensure the file is properly formatted.")


# Example Usage
if __name__ == "__main__":
    try:
        ndis_system = NDISManagementSystem()

        # Add participants
        ndis_system.add_participant("P001", "Alice Johnson", 28)
        ndis_system.add_participant("P002", "Bob Smith", 35)

        # Add care plans
        participant = ndis_system.get_participant("P001")
        participant.add_care_plan(
            goal="Improve physical mobility",
            strategies=["Daily physiotherapy exercises", "Regular swimming sessions"],
        )

        # Add activities
        participant.add_activity("Community Gardening", "Participating in weekly gardening activities.")
        participant.add_activity("Art Classes", "Weekly art sessions at the community center.")

        # Save data to file
        ndis_system.save_to_file("participants.json")

        # Load data from file
        ndis_system.load_from_file("participants.json")

    except Exception as e:
        print(f"Error: {e}")
```
