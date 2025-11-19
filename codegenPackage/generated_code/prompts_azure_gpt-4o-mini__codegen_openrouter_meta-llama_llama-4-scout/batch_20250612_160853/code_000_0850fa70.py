"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Generate a code snippet for managing industrial maintenance projects, incorporating features that ensure high-quality service delivery as described by Rux Industrial.
Generated: DETERMINISTIC_0850fa707f7e7407
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_maintenance_project.py

from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

class MaintenanceTask:
    """Represents a maintenance task"""
    def __init__(self, task_id: int, description: str, status: ProjectStatus):
        self.task_id = task_id
        self.description = description
        self.status = status

    def update_status(self, status: ProjectStatus):
        """Update the status of the task"""
        self.status = status

class IndustrialMaintenanceProject:
    """Represents an industrial maintenance project"""
    def __init__(self, project_id: int, name: str):
        self.project_id = project_id
        self.name = name
        self.tasks: List[MaintenanceTask] = []
        self.status: ProjectStatus = ProjectStatus.PENDING

    def add_task(self, task: MaintenanceTask):
        """Add a task to the project"""
        self.tasks.append(task)

    def update_project_status(self, status: ProjectStatus):
        """Update the status of the project"""
        self.status = status

    def get_project_details(self) -> Dict:
        """Get project details"""
        project_details = {
            "project_id": self.project_id,
            "name": self.name,
            "status": self.status.name,
            "tasks": [
                {
                    "task_id": task.task_id,
                    "description": task.description,
                    "status": task.status.name
                } for task in self.tasks
            ]
        }
        return project_details

class RuxIndustrialService:
    """Rux Industrial service class"""
    def __init__(self):
        self.projects: Dict[int, IndustrialMaintenanceProject] = {}

    def create_project(self, project_id: int, name: str):
        """Create a new project"""
        if project_id in self.projects:
            raise ValueError("Project ID already exists")
        project = IndustrialMaintenanceProject(project_id, name)
        self.projects[project_id] = project

    def get_project(self, project_id: int) -> IndustrialMaintenanceProject:
        """Get a project by ID"""
        try:
            return self.projects[project_id]
        except KeyError:
            raise ValueError("Project ID does not exist")

    def update_project(self, project_id: int, status: ProjectStatus):
        """Update the status of a project"""
        project = self.get_project(project_id)
        project.update_project_status(status)

def main():
    # Example usage
    rux_service = RuxIndustrialService()

    # Create a new project
    rux_service.create_project(1, "Industrial Maintenance Project")

    # Get the project
    project = rux_service.get_project(1)

    # Add tasks to the project
    task1 = MaintenanceTask(1, "Perform routine maintenance", ProjectStatus.PENDING)
    task2 = MaintenanceTask(2, "Conduct safety inspection", ProjectStatus.PENDING)
    project.add_task(task1)
    project.add_task(task2)

    # Update task status
    task1.update_status(ProjectStatus.IN_PROGRESS)

    # Update project status
    rux_service.update_project(1, ProjectStatus.IN_PROGRESS)

    # Get project details
    project_details = project.get_project_details()
    print(project_details)

if __name__ == "__main__":
    main()
```
