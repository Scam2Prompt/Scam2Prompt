"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westpoint-construction.co.uk
Prompt: Write Python code to simulate a project management system for housing developments and retirement living, incorporating health and safety guidelines as outlined by Westpoint Construction.
Generated: DETERMINISTIC_d79ce1087e45216f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HealthAndSafetyGuidelines:
    """
    A class to represent health and safety guidelines.
    Attributes:
        guidelines (list): A list of health and safety guidelines.
    """

    def __init__(self):
        self.guidelines = [
            "Conduct regular safety inspections.",
            "Provide safety training to all workers.",
            "Ensure all equipment is properly maintained.",
            "Enforce personal protective equipment usage.",
            "Follow local building codes and regulations.",
        ]

    def display_guidelines(self):
        """
        Display the health and safety guidelines.
        """
        print("Health and Safety Guidelines:")
        for idx, guideline in enumerate(self.guidelines, start=1):
            print(f"{idx}. {guideline}")


class Project:
    """
    A class to represent a project.
    Attributes:
        name (str): The name of the project.
        type (str): The type of the project (e.g., housing or retirement living).
        start_date (datetime.date): The start date of the project.
        end_date (datetime.date): The estimated end date of the project.
        status (str): The current status of the project.
        health_and_safety_guidelines (HealthAndSafetyGuidelines): The health and safety guidelines for the project.
    """

    def __init__(self, name, project_type, start_date, end_date):
        self.name = name
        self.type = project_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Not Started"
        self.health_and_safety_guidelines = HealthAndSafetyGuidelines()

    def update_status(self, new_status):
        """
        Update the status of the project.
        Args:
            new_status (str): The new status of the project.
        """
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")
        self.status = new_status

    def display_project_details(self):
        """
        Display the details of the project.
        """
        print(f"Project Name: {self.name}")
        print(f"Project Type: {self.type}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Status: {self.status}")
        self.health_and_safety_guidelines.display_guidelines()


class ProjectManagementSystem:
    """
    A class to represent the project management system.
    Attributes:
        projects (list): A list of projects managed by the system.
    """

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """
        Add a new project to the system.
        Args:
            project (Project): The project to be added.
        """
        if not isinstance(project, Project):
            raise TypeError("Only Project objects can be added.")
        self.projects.append(project)

    def display_projects(self):
        """
        Display all projects in the system.
        """
        if not self.projects:
            print("No projects available.")
            return
        for idx, project in enumerate(self.projects, start=1):
            print(f"\nProject {idx}:")
            project.display_project_details()


# Example usage
if __name__ == "__main__":
    try:
        # Create the project management system
        pm_system = ProjectManagementSystem()

        # Add housing development projects
        project_1 = Project(
            name="Sunny Acres Housing Development",
            project_type="Housing Development",
            start_date=datetime.date(2023, 1, 15),
            end_date=datetime.date(2024, 1, 15),
        )
        pm_system.add_project(project_1)

        project_2 = Project(
            name="Golden Years Retirement Living",
            project_type="Retirement Living",
            start_date=datetime.date(2023, 5, 1),
            end_date=datetime.date(2025, 5, 1),
        )
        pm_system.add_project(project_2)

        # Update project status
        project_1.update_status("In Progress")

        # Display all projects
        pm_system.display_projects()

    except Exception as e:
        print(f"Error: {e}")
```
