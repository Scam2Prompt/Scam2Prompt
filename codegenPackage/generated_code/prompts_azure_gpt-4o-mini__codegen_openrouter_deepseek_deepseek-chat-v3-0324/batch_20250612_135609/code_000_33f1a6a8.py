"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Generate a code snippet for a construction project management application that includes features for building construction, renovation works, and fit-out works.
Generated: DETERMINISTIC_33f1a6a8923932a9
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management.py

from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict
import uuid


class ProjectType(Enum):
    BUILDING_CONSTRUCTION = "Building Construction"
    RENOVATION_WORKS = "Renovation Works"
    FIT_OUT_WORKS = "Fit-out Works"


class ProjectStatus(Enum):
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Task:
    def __init__(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        assigned_to: str,
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.assigned_to = assigned_to
        self.completed = False

    def mark_complete(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f"Task: {self.name} (Assigned to: {self.assigned_to})"


class Project:
    def __init__(
        self,
        name: str,
        description: str,
        project_type: ProjectType,
        start_date: datetime,
        end_date: datetime,
        budget: float,
    ):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.project_type = project_type
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.status = ProjectStatus.PLANNING
        self.tasks: List[Task] = []
        self.materials: Dict[str, int] = {}

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, task_id: str) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                self.tasks.pop(i)
                return True
        return False

    def update_status(self, status: ProjectStatus) -> None:
        self.status = status

    def add_material(self, name: str, quantity: int) -> None:
        if name in self.materials:
            self.materials[name] += quantity
        else:
            self.materials[name] = quantity

    def remove_material(self, name: str, quantity: int) -> bool:
        if name in self.materials and self.materials[name] >= quantity:
            self.materials[name] -= quantity
            if self.materials[name] == 0:
                del self.materials[name]
            return True
        return False

    def get_completion_percentage(self) -> float:
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks if task.completed)
        return (completed / len(self.tasks)) * 100

    def __str__(self) -> str:
        return (
            f"Project: {self.name} ({self.project_type.value})\n"
            f"Status: {self.status.value}\n"
            f"Budget: ${self.budget:,.2f}\n"
            f"Progress: {self.get_completion_percentage():.1f}%"
        )


class ConstructionProjectManager:
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(
        self,
        name: str,
        description: str,
        project_type: ProjectType,
        start_date: datetime,
        end_date: datetime,
        budget: float,
    ) -> Project:
        project = Project(
            name, description, project_type, start_date, end_date, budget
        )
        self.projects[project.id] = project
        return project

    def get_project(self, project_id: str) -> Optional[Project]:
        return self.projects.get(project_id)

    def update_project_status(self, project_id: str, status: ProjectStatus) -> bool:
        project = self.get_project(project_id)
        if project:
            project.update_status(status)
            return True
        return False

    def delete_project(self, project_id: str) -> bool:
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def list_projects(self) -> List[Project]:
        return list(self.projects.values())

    def list_projects_by_type(self, project_type: ProjectType) -> List[Project]:
        return [
            project
            for project in self.projects.values()
            if project.project_type == project_type
        ]


# Example usage
if __name__ == "__main__":
    manager = ConstructionProjectManager()

    # Create a building construction project
    building_project = manager.create_project(
        "Office Tower",
        "Construction of 20-story office building",
        ProjectType.BUILDING_CONSTRUCTION,
        datetime(2023, 1, 1),
        datetime(2024, 12, 31),
        5000000.00,
    )

    # Add tasks to the project
    foundation_task = Task(
        "Foundation Work",
        "Excavation and pouring of foundation",
        datetime(2023, 1, 15),
        datetime(2023, 3, 15),
        "Construction Team A",
    )
    building_project.add_task(foundation_task)

    # Add materials
    building_project.add_material("Concrete", 500)
    building_project.add_material("Steel Beams", 200)

    # Update project status
    manager.update_project_status(building_project.id, ProjectStatus.IN_PROGRESS)

    # Print project details
    print(building_project)
```
