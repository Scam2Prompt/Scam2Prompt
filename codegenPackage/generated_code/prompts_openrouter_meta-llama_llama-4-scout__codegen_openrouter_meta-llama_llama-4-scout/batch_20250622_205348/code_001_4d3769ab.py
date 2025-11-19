"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write a Python code snippet to manage construction projects for a company like MGEL, including areas such as mineração, obras civis, and rodovias.
Generated: DETERMINISTIC_4d3769ab1873861f
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_manager.py

from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class ProjectType(Enum):
    """Project type enumeration"""
    MINERACAO = 1
    OBRAS_CIVIS = 2
    RODOVIAS = 3

class ConstructionProject:
    """Represents a construction project"""

    def __init__(self, 
                 project_id: int, 
                 project_name: str, 
                 project_type: ProjectType, 
                 status: ProjectStatus = ProjectStatus.PENDING):
        """
        Initializes a construction project

        Args:
        - project_id (int): Unique project identifier
        - project_name (str): Project name
        - project_type (ProjectType): Project type
        - status (ProjectStatus): Project status (default: PENDING)
        """
        self.project_id = project_id
        self.project_name = project_name
        self.project_type = project_type
        self.status = status
        self.tasks: List[Dict] = []

    def add_task(self, task_name: str, task_description: str):
        """
        Adds a task to the project

        Args:
        - task_name (str): Task name
        - task_description (str): Task description
        """
        self.tasks.append({"task_name": task_name, "task_description": task_description})

    def update_status(self, status: ProjectStatus):
        """
        Updates the project status

        Args:
        - status (ProjectStatus): New project status
        """
        self.status = status

    def __str__(self):
        return f"Project ID: {self.project_id}, Name: {self.project_name}, Type: {self.project_type.name}, Status: {self.status.name}"

class ConstructionProjectManager:
    """Manages construction projects"""

    def __init__(self):
        self.projects: Dict[int, ConstructionProject] = {}

    def create_project(self, project_id: int, project_name: str, project_type: ProjectType):
        """
        Creates a new construction project

        Args:
        - project_id (int): Unique project identifier
        - project_name (str): Project name
        - project_type (ProjectType): Project type

        Raises:
        - ValueError: If project ID already exists
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists")
        project = ConstructionProject(project_id, project_name, project_type)
        self.projects[project_id] = project

    def get_project(self, project_id: int) -> ConstructionProject:
        """
        Retrieves a construction project by ID

        Args:
        - project_id (int): Unique project identifier

        Returns:
        - ConstructionProject: Project instance or None if not found
        """
        return self.projects.get(project_id)

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """
        Updates the status of a construction project

        Args:
        - project_id (int): Unique project identifier
        - status (ProjectStatus): New project status

        Raises:
        - ValueError: If project ID does not exist
        """
        project = self.get_project(project_id)
        if project:
            project.update_status(status)
        else:
            raise ValueError("Project ID does not exist")

def main():
    # Example usage
    project_manager = ConstructionProjectManager()

    project_manager.create_project(1, "Mineração Project", ProjectType.MINERACAO)
    project_manager.create_project(2, "Obras Civis Project", ProjectType.OBRAS_CIVIS)
    project_manager.create_project(3, "Rodovias Project", ProjectType.RODOVIAS)

    project = project_manager.get_project(1)
    if project:
        print(project)
        project.add_task("Task 1", "Task 1 description")
        print(project.tasks)
        project_manager.update_project_status(1, ProjectStatus.IN_PROGRESS)
        print(project)

if __name__ == "__main__":
    main()
```
