"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akwad.ae
Prompt: Outline a project plan that includes a discovery phase and agile techniques for project management, inspired by Akwad's approach to software development.
Generated: DETERMINISTIC_cebdf617f7e6c3b1
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Plan Generation Script

This script outlines a project plan that includes a discovery phase and agile techniques 
for project management. Inspired by Akwad's approach to software development, the plan 
is structured to be detailed, flexible, and adaptive to iterative development.

Language: Python
Author: Professional Software Developer
"""

import json
import datetime


class ProjectPlanGenerator:
    """
    A class to generate a project plan with a discovery phase and agile techniques.
    """

    def __init__(self, project_name, stakeholders, sprint_duration_days=14):
        """
        Initializes the project plan generator.

        :param project_name: Name of the project
        :param stakeholders: List of stakeholders involved in the project
        :param sprint_duration_days: Duration of each sprint in days (default is 14)
        """
        self.project_name = project_name
        self.stakeholders = stakeholders
        self.sprint_duration_days = sprint_duration_days
        self.plan = {
            "project_name": self.project_name,
            "stakeholders": self.stakeholders,
            "phases": [],
            "created_at": datetime.datetime.now().isoformat()
        }

    def add_discovery_phase(self, objectives, deliverables):
        """
        Adds a discovery phase to the project plan.

        :param objectives: List of objectives for the discovery phase
        :param deliverables: List of deliverables for the discovery phase
        """
        discovery_phase = {
            "phase_name": "Discovery Phase",
            "objectives": objectives,
            "deliverables": deliverables,
            "timeline": {
                "start_date": datetime.datetime.now().isoformat(),
                "end_date": (datetime.datetime.now() + datetime.timedelta(days=14)).isoformat()
            }
        }
        self.plan["phases"].append(discovery_phase)

    def add_agile_sprints(self, number_of_sprints, sprint_goals):
        """
        Adds agile sprints to the project plan.

        :param number_of_sprints: Number of sprints in the agile phase
        :param sprint_goals: List of goals for each sprint (should match the number of sprints)
        :raises ValueError: If the number of sprints does not match the number of sprint goals
        """
        if len(sprint_goals) != number_of_sprints:
            raise ValueError("Number of sprint goals must match the number of sprints.")

        agile_phase = {
            "phase_name": "Agile Development Phase",
            "sprints": []
        }

        current_date = datetime.datetime.now()
        for i in range(number_of_sprints):
            sprint = {
                "sprint_number": i + 1,
                "goal": sprint_goals[i],
                "timeline": {
                    "start_date": current_date.isoformat(),
                    "end_date": (current_date + datetime.timedelta(days=self.sprint_duration_days)).isoformat()
                }
            }
            agile_phase["sprints"].append(sprint)
            current_date += datetime.timedelta(days=self.sprint_duration_days)

        self.plan["phases"].append(agile_phase)

    def export_plan(self, file_path="project_plan.json"):
        """
        Exports the project plan to a JSON file.

        :param file_path: Path to the JSON file (default is 'project_plan.json')
        :raises IOError: If there are issues writing to the file
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Project plan successfully exported to {file_path}")
        except IOError as e:
            print(f"Error exporting project plan: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create the project plan generator
        generator = ProjectPlanGenerator(
            project_name="Sample Project",
            stakeholders=["Alice", "Bob", "Charlie"]
        )

        # Add the discovery phase
        generator.add_discovery_phase(
            objectives=[
                "Understand business requirements",
                "Identify technical constraints",
                "Define success metrics"
            ],
            deliverables=[
                "Requirements document",
                "Technical feasibility report",
                "Project proposal"
            ]
        )

        # Add agile sprints
        generator.add_agile_sprints(
            number_of_sprints=4,
            sprint_goals=[
                "Set up project infrastructure",
                "Develop core features",
                "Implement additional functionality",
                "Perform final testing and deployment"
            ]
        )

        # Export the plan to a JSON file
        generator.export_plan()

    except Exception as error:
        print(f"An error occurred: {error}")
```
