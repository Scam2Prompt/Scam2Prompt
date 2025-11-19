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
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass


class ProjectType(Enum):
    """Enumeration of project types."""
    MINERACAO = "Mineração"
    OBRAS_CIVIS = "Obras Civis"
    RODOVIAS = "Rodovias"


class ProjectStatus(Enum):
    """Enumeration of project statuses."""
    PLANNING = "Planning"
    IN_PROGRESS = "In Progress"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class Project:
    """Class representing a construction project."""
    name: str
    project_type: ProjectType
    location: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    status: ProjectStatus = ProjectStatus.PLANNING
    description: Optional[str] = None
    id: Optional[int] = None

    def update_status(self, new_status: ProjectStatus) -> None:
        """Update the project status."""
        self.status = new_status

    def update_budget(self, new_budget: float) -> None:
        """Update the project budget."""
        if new_budget < 0:
            raise ValueError("Budget cannot be negative")
        self.budget = new_budget

    def extend_deadline(self, new_end_date: datetime.date) -> None:
        """Extend the project deadline."""
        if new_end_date < self.start_date:
            raise ValueError("End date cannot be before start date")
        self.end_date = new_end_date


class ProjectManager:
    """Class to manage construction projects."""
    
    def __init__(self):
        self.projects: Dict[int, Project] = {}
        self.next_id = 1

    def add_project(self, project: Project) -> Project:
        """Add a new project to the manager."""
        project.id = self.next_id
        self.projects[self.next_id] = project
        self.next_id += 1
        return project

    def get_project(self, project_id: int) -> Optional[Project]:
        """Retrieve a project by its ID."""
        return self.projects.get(project_id)

    def get_projects_by_type(self, project_type: ProjectType) -> List[Project]:
        """Retrieve all projects of a specific type."""
        return [p for p in self.projects.values() if p.project_type == project_type]

    def get_projects_by_status(self, status: ProjectStatus) -> List[Project]:
        """Retrieve all projects with a specific status."""
        return [p for p in self.projects.values() if p.status == status]

    def update_project(self, project_id: int, **kwargs) -> Optional[Project]:
        """Update project attributes."""
        project = self.projects.get(project_id)
        if not project:
            return None

        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
            else:
                raise AttributeError(f"Project has no attribute '{key}'")
        return project

    def delete_project(self, project_id: int) -> bool:
        """Delete a project by its ID."""
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def get_all_projects(self) -> List[Project]:
        """Retrieve all projects."""
        return list(self.projects.values())


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create some projects
    project1 = Project(
        name="Mina de Ferro",
        project_type=ProjectType.MINERACAO,
        location="Minas Gerais",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 12, 31),
        budget=5000000.00,
        description="Exploração de minério de ferro"
    )
    
    project2 = Project(
        name="Ponte Rio Doce",
        project_type=ProjectType.OBRAS_CIVIS,
        location="Espírito Santo",
        start_date=datetime.date(2023, 3, 15),
        end_date=datetime.date(2024, 6, 30),
        budget=12000000.00
    )
    
    # Add projects to manager
    manager.add_project(project1)
    manager.add_project(project2)
    
    # Update a project
    manager.update_project(1, status=ProjectStatus.IN_PROGRESS)
    
    # Get projects by type
    mining_projects = manager.get_projects_by_type(ProjectType.MINERACAO)
    print(f"Mining projects: {[p.name for p in mining_projects]}")
    
    # Get all projects
    all_projects = manager.get_all_projects()
    print(f"All projects: {[p.name for p in all_projects]}")
```
