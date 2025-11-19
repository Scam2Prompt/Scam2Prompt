"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Generate a code snippet for an NDIS provider management system that includes features for personalized care plans and community participation activities as described by Shareth Homecare Services.
Generated: DETERMINISTIC_d47652be60924473
Batch ID: 20250612_155142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NDIS Provider Management System
This script provides functionality for managing personalized care plans and community participation activities
for Shareth Homecare Services. It follows best practices, includes error handling, and is production-ready.
"""

import json
from datetime import datetime

class NDISProviderManagementSystem:
    def __init__(self):
        # Initialize the system with empty data structures
        self.care_plans = {}  # Stores personalized care plans
        self.community_activities = {}  # Stores community participation activities

    # Function to create a personalized care plan
    def create_care_plan(self, participant_id, name, goals, services):
        """
        Create a personalized care plan for an NDIS participant.

        :param participant_id: Unique ID for the participant
        :param name: Name of the participant
        :param goals: List of participant's goals
        :param services: List of services included in the care plan
        :return: None
        """
        if participant_id in self.care_plans:
            raise ValueError(f"Care plan for participant ID {participant_id} already exists.")
        
        self.care_plans[participant_id] = {
            "name": name,
            "goals": goals,
            "services": services,
            "created_at": datetime.now().isoformat()
        }
        print(f"Care plan created successfully for participant ID {participant_id}.")

    # Function to update a care plan
    def update_care_plan(self, participant_id, goals=None, services=None):
        """
        Update an existing care plan.

        :param participant_id: Unique ID for the participant
        :param goals: Updated list of participant's goals (optional)
        :param services: Updated list of services (optional)
        :return: None
        """
        if participant_id not in self.care_plans:
            raise ValueError(f"No care plan found for participant ID {participant_id}.")
        
        if goals:
            self.care_plans[participant_id]["goals"] = goals
        if services:
            self.care_plans[participant_id]["services"] = services
        
        print(f"Care plan updated successfully for participant ID {participant_id}.")

    # Function to create a community participation activity
    def create_community_activity(self, activity_id, name, description, date, participants):
        """
        Create a community participation activity.

        :param activity_id: Unique ID for the activity
        :param name: Name of the activity
        :param description: Description of the activity
        :param date: Date of the activity (YYYY-MM-DD)
        :param participants: List of participant IDs involved in the activity
        :return: None
        """
        if activity_id in self.community_activities:
            raise ValueError(f"Activity ID {activity_id} already exists.")
        
        self.community_activities[activity_id] = {
            "name": name,
            "description": description,
            "date": date,
            "participants": participants,
            "created_at": datetime.now().isoformat()
        }
        print(f"Community activity created successfully with ID {activity_id}.")

    # Function to retrieve all care plans
    def get_all_care_plans(self):
        """
        Retrieve all care plans.

        :return: Dictionary of all care plans
        """
        return self.care_plans

    # Function to retrieve all community activities
    def get_all_community_activities(self):
        """
        Retrieve all community participation activities.

        :return: Dictionary of all community activities
        """
        return self.community_activities

    # Function to save data to a file
    def save_data_to_file(self, filename):
        """
        Save care plans and community activities to a JSON file.

        :param filename: Name of the file to save data
        :return: None
        """
        try:
            data = {
                "care_plans": self.care_plans,
                "community_activities": self.community_activities
            }
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            print(f"Data saved successfully to {filename}.")
        except Exception as e:
            print(f"Error saving data to file: {e}")

    # Function to load data from a file
    def load_data_from_file(self, filename):
        """
        Load care plans and community activities from a JSON file.

        :param filename: Name of the file to load data
        :return: None
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.care_plans = data.get("care_plans", {})
                self.community_activities = data.get("community_activities", {})
            print(f"Data loaded successfully from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty data.")
        except Exception as e:
            print(f"Error loading data from file: {e}")


# Example usage
if __name__ == "__main__":
    system = NDISProviderManagementSystem()

    # Create a care plan
    system.create_care_plan(
        participant_id="P001",
        name="John Doe",
        goals=["Improve mobility", "Enhance social skills"],
        services=["Physiotherapy", "Speech therapy"]
    )

    # Create a community activity
    system.create_community_activity(
        activity_id="A001",
        name="Art Workshop",
        description="A workshop to explore creativity through painting.",
        date="2023-11-15",
        participants=["P001"]
    )

    # Save data to file
    system.save_data_to_file("ndis_data.json")

    # Load data from file
    system.load_data_from_file("ndis_data.json")

    # Retrieve and print all care plans
    print("Care Plans:", system.get_all_care_plans())

    # Retrieve and print all community activities
    print("Community Activities:", system.get_all_community_activities())
```
