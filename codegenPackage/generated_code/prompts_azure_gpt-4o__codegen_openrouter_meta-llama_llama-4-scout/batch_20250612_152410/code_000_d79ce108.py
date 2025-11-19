"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write Python code to simulate a project management system for housing developments and retirement living, incorporating health and safety guidelines as outlined by Westpoint Construction.
Generated: DETERMINISTIC_d79ce1087e45216f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PLANNING = 1
    UNDER_CONSTRUCTION = 2
    COMPLETED = 3

class HealthAndSafetyGuideline:
    """Health and safety guideline class"""
    def __init__(self, id: int, description: str, responsible_person: str):
        """
        Initialize health and safety guideline

        Args:
        id (int): Unique identifier
        description (str): Guideline description
        responsible_person (str): Person responsible for guideline
        """
        self.id = id
        self.description = description
        self.responsible_person = responsible_person

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, project_type: str, status: ProjectStatus):
        """
        Initialize project

        Args:
        id (int): Unique identifier
        name (str): Project name
        project_type (str): Project type (housing development or retirement living)
        status (ProjectStatus): Project status
        """
        self.id = id
        self.name = name
        self.project_type = project_type
        self.status = status
        self.health_and_safety_guidelines: List[HealthAndSafetyGuideline] = []
        self.tasks: List[str] = []

    def add_health_and_safety_guideline(self, guideline: HealthAndSafetyGuideline):
        """Add health and safety guideline to project"""
        self.health_and_safety_guidelines.append(guideline)

    def add_task(self, task: str):
        """Add task to project"""
        self.tasks.append(task)

class WestpointConstruction:
    """Westpoint Construction class"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def create_project(self, id: int, name: str, project_type: str, status: ProjectStatus):
        """
        Create new project

        Args:
        id (int): Unique identifier
        name (str): Project name
        project_type (str): Project type (housing development or retirement living)
        status (ProjectStatus): Project status

        Returns:
        Project: Created project
        """
        if id in self.projects:
            raise ValueError("Project with given ID already exists")

        project = Project(id, name, project_type, status)
        self.projects[id] = project
        return project

    def get_project(self, id: int) -> Project:
        """
        Get project by ID

        Args:
        id (int): Unique identifier

        Returns:
        Project: Project with given ID

        Raises:
        ValueError: If project with given ID does not exist
        """
        if id not in self.projects:
            raise ValueError("Project with given ID does not exist")

        return self.projects[id]

def main():
    westpoint_construction = WestpointConstruction()

    # Create health and safety guidelines
    guideline1 = HealthAndSafetyGuideline(1, "Hard hat must be worn at all times", "John Doe")
    guideline2 = HealthAndSafetyGuideline(2, "Safety harness must be worn when working at heights", "Jane Smith")

    # Create project
    project = westpoint_construction.create_project(1, "Housing Development Project", "housing development", ProjectStatus.PLANNING)

    # Add health and safety guidelines to project
    project.add_health_and_safety_guideline(guideline1)
    project.add_health_and_safety_guideline(guideline2)

    # Add tasks to project
    project.add_task("Conduct site survey")
    project.add_task("Obtain necessary permits")

    # Print project details
    print(f"Project ID: {project.id}")
    print(f"Project Name: {project.name}")
    print(f"Project Type: {project.project_type}")
    print(f"Project Status: {project.status.name}")
    print("Health and Safety Guidelines:")
    for guideline in project.health_and_safety_guidelines:
        print(f"ID: {guideline.id}, Description: {guideline.description}, Responsible Person: {guideline.responsible_person}")
    print("Tasks:")
    for task in project.tasks:
        print(task)

if __name__ == "__main__":
    main()
```
