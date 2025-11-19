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
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("program_log.log"), logging.StreamHandler()]
)

class CapacityDevelopmentProgram:
    """
    A class to represent a capacity development program for children's book professionals in Africa.
    """

    def __init__(self, program_name, description, goals, target_audience):
        """
        Initialize the program with basic details.

        :param program_name: Name of the program
        :param description: Description of the program
        :param goals: List of program goals
        :param target_audience: Target audience for the program
        """
        self.program_name = program_name
        self.description = description
        self.goals = goals
        self.target_audience = target_audience
        self.activities = []

    def add_activity(self, activity_name, activity_description, activity_date):
        """
        Add an activity to the program.

        :param activity_name: Name of the activity
        :param activity_description: Description of the activity
        :param activity_date: Date of the activity (YYYY-MM-DD)
        """
        try:
            activity_date = datetime.strptime(activity_date, "%Y-%m-%d")
            activity = {
                "name": activity_name,
                "description": activity_description,
                "date": activity_date.strftime("%Y-%m-%d")
            }
            self.activities.append(activity)
            logging.info(f"Activity '{activity_name}' added successfully.")
        except ValueError as e:
            logging.error(f"Invalid date format for activity '{activity_name}': {e}")

    def export_program(self, file_name):
        """
        Export the program details to a JSON file.

        :param file_name: Name of the file to export the program details
        """
        try:
            program_data = {
                "program_name": self.program_name,
                "description": self.description,
                "goals": self.goals,
                "target_audience": self.target_audience,
                "activities": self.activities
            }
            with open(file_name, "w") as file:
                json.dump(program_data, file, indent=4)
            logging.info(f"Program details exported successfully to {file_name}.")
        except Exception as e:
            logging.error(f"Failed to export program details: {e}")

def main():
    """
    Main function to create and manage the capacity development program.
    """
    # Initialize the program
    program = CapacityDevelopmentProgram(
        program_name="Muna Kalati Capacity Development Program",
        description="A program to empower children's book professionals in Africa.",
        goals=[
            "Enhance storytelling skills",
            "Promote cultural diversity in children's literature",
            "Build networks among professionals",
            "Provide access to publishing resources"
        ],
        target_audience="Children's book authors, illustrators, publishers, and educators in Africa"
    )

    # Add activities to the program
    program.add_activity(
        activity_name="Storytelling Workshop",
        activity_description="A workshop to improve storytelling techniques.",
        activity_date="2023-11-15"
    )
    program.add_activity(
        activity_name="Illustration Masterclass",
        activity_description="A masterclass on creating culturally relevant illustrations.",
        activity_date="2023-12-01"
    )
    program.add_activity(
        activity_name="Publishing Resources Seminar",
        activity_description="A seminar to provide insights into publishing opportunities.",
        activity_date="2023-12-10"
    )

    # Export program details to a JSON file
    program.export_program("muna_kalati_program.json")

if __name__ == "__main__":
    main()
```
