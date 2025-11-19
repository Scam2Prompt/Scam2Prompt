"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Create a project plan for integrating traffic signals and street lighting, inspired by the services provided by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_1b20cf0f5264443e
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_plan.py
# This script creates a project plan for integrating traffic signals and street lighting systems.
# Inspired by services provided by E.C. Power & Lighting Ltd.

# Import necessary modules
from datetime import datetime
import json

class ProjectPlan:
    """
    A class to represent and manage the project plan for integrating traffic signals and street lighting.
    """

    def __init__(self, project_name, start_date, end_date, stakeholders):
        """
        Initialize the ProjectPlan object.

        :param project_name: Name of the project.
        :param start_date: Project start date (YYYY-MM-DD format).
        :param end_date: Project end date (YYYY-MM-DD format).
        :param stakeholders: List of stakeholders involved in the project.
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.stakeholders = stakeholders
        self.milestones = []

    def add_milestone(self, name, description, due_date):
        """
        Add a milestone to the project plan.

        :param name: Milestone name.
        :param description: Milestone description.
        :param due_date: Milestone due date (YYYY-MM-DD format).
        """
        try:
            milestone = {
                "name": name,
                "description": description,
                "due_date": datetime.strptime(due_date, "%Y-%m-%d")
            }
            if milestone["due_date"] < self.start_date or milestone["due_date"] > self.end_date:
                raise ValueError("Milestone due date must be within the project timeline.")
            self.milestones.append(milestone)
            print(f"Milestone '{name}' added successfully.")
        except ValueError as ve:
            print(f"Error adding milestone: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_plan(self):
        """
        Display the entire project plan.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {self.end_date.strftime('%Y-%m-%d')}")
        print(f"Stakeholders: {', '.join(self.stakeholders)}")
        print("Milestones:")
        for milestone in self.milestones:
            print(
                f"  - {milestone['name']} (Due: {milestone['due_date'].strftime('%Y-%m-%d')})\n"
                f"    Description: {milestone['description']}"
            )

    def export_to_json(self, filename):
        """
        Export the project plan to a JSON file.

        :param filename: Filename to save the project plan (with .json extension).
        """
        try:
            project_data = {
                "project_name": self.project_name,
                "start_date": self.start_date.strftime("%Y-%m-%d"),
                "end_date": self.end_date.strftime("%Y-%m-%d"),
                "stakeholders": self.stakeholders,
                "milestones": [
                    {
                        "name": milestone["name"],
                        "description": milestone["description"],
                        "due_date": milestone["due_date"].strftime("%Y-%m-%d")
                    }
                    for milestone in self.milestones
                ]
            }
            with open(filename, 'w') as file:
                json.dump(project_data, file, indent=4)
            print(f"Project plan exported successfully to {filename}.")
        except Exception as e:
            print(f"An error occurred while exporting to JSON: {e}")


# Example usage
if __name__ == "__main__":
    # Create a new project plan
    project = ProjectPlan(
        project_name="Traffic Signals & Street Lighting Integration",
        start_date="2023-11-01",
        end_date="2024-03-31",
        stakeholders=["City Council", "E.C. Power & Lighting Ltd", "Traffic Department"]
    )

    # Add milestones to the project plan
    project.add_milestone(
        name="Initial Assessment",
        description="Conduct site surveys and initial feasibility studies.",
        due_date="2023-11-15"
    )
    project.add_milestone(
        name="Design Phase",
        description="Develop integration plans and system designs.",
        due_date="2023-12-15"
    )
    project.add_milestone(
        name="Implementation",
        description="Install traffic signals and street lighting systems.",
        due_date="2024-02-15"
    )
    project.add_milestone(
        name="Testing & Commissioning",
        description="Test and hand over the integrated systems.",
        due_date="2024-03-15"
    )

    # Display the project plan
    project.display_plan()

    # Export the project plan to a JSON file
    project.export_to_json("project_plan.json")
```
