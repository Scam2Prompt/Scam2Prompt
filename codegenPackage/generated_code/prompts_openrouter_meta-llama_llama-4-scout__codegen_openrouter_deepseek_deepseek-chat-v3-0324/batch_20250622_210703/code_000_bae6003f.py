"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Write a Python code snippet to manage construction projects using design-build and turnkey construction services, considering factors like project planning, client requirements, and team collaboration."
Generated: DETERMINISTIC_bae6003ff7810109
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management System
Handles design-build and turnkey construction projects with features for:
- Project planning
- Client requirements tracking
- Team collaboration
"""

from datetime import datetime
from typing import List, Dict, Optional
import uuid
from enum import Enum, auto


class ProjectType(Enum):
    DESIGN_BUILD = auto()
    TURNKEY = auto()


class ProjectStatus(Enum):
    PLANNING = auto()
    DESIGN = auto()
    CONSTRUCTION = auto()
    COMPLETED = auto()
    ON_HOLD = auto()


class TeamMember:
    def __init__(self, name: str, role: str, contact: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.role = role
        self.contact = contact
        self.tasks: List['Task'] = []

    def assign_task(self, task: 'Task') -> None:
        self.tasks.append(task)

    def __str__(self) -> str:
        return f"{self.name} ({self.role})"


class Task:
    def __init__(self, description: str, deadline: datetime, priority: int):
        self.id = str(uuid.uuid4())
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.completed = False
        self.assigned_to: Optional[TeamMember] = None

    def mark_complete(self) -> None:
        self.completed = True

    def assign_to(self, team_member: TeamMember) -> None:
        self.assigned_to = team_member
        team_member.assign_task(self)

    def __str__(self) -> str:
        status = "Completed" if self.completed else "Pending"
        return f"{self.description} - {status} (Priority: {self.priority})"


class ClientRequirement:
    def __init__(self, description: str, priority: int):
        self.id = str(uuid.uuid4())
        self.description = description
        self.priority = priority
        self.fulfilled = False

    def mark_fulfilled(self) -> None:
        self.fulfilled = True

    def __str__(self) -> str:
        status = "Fulfilled" if self.fulfilled else "Pending"
        return f"{self.description} - {status} (Priority: {self.priority})"


class ConstructionProject:
    def __init__(self, name: str, project_type: ProjectType, client_name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.project_type = project_type
        self.client_name = client_name
        self.start_date = datetime.now()
        self.estimated_end_date: Optional[datetime] = None
        self.status = ProjectStatus.PLANNING
        self.team: List[TeamMember] = []
        self.tasks: List[Task] = []
        self.requirements: List[ClientRequirement] = []
        self.budget: float = 0.0
        self.notes: List[str] = []

    def add_team_member(self, member: TeamMember) -> None:
        self.team.append(member)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def add_requirement(self, requirement: ClientRequirement) -> None:
        self.requirements.append(requirement)

    def update_status(self, new_status: ProjectStatus) -> None:
        self.status = new_status

    def set_budget(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Budget cannot be negative")
        self.budget = amount

    def add_note(self, note: str) -> None:
        self.notes.append(note)

    def get_pending_tasks(self) -> List[Task]:
        return [task for task in self.tasks if not task.completed]

    def get_unfulfilled_requirements(self) -> List[ClientRequirement]:
        return [req for req in self.requirements if not req.fulfilled]

    def __str__(self) -> str:
        return (f"Project: {self.name} ({self.project_type.name})\n"
                f"Client: {self.client_name}\n"
                f"Status: {self.status.name}\n"
                f"Team Size: {len(self.team)}\n"
                f"Tasks: {len(self.tasks)} total, {len(self.get_pending_tasks())} pending\n"
                f"Requirements: {len(self.requirements)} total, {len(self.get_unfulfilled_requirements())} unfulfilled")


class ProjectManager:
    def __init__(self):
        self.projects: Dict[str, ConstructionProject] = {}

    def create_project(self, name: str, project_type: ProjectType, client_name: str) -> ConstructionProject:
        project = ConstructionProject(name, project_type, client_name)
        self.projects[project.id] = project
        return project

    def get_project(self, project_id: str) -> Optional[ConstructionProject]:
        return self.projects.get(project_id)

    def delete_project(self, project_id: str) -> bool:
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

    def list_projects(self) -> List[ConstructionProject]:
        return list(self.projects.values())

    def get_projects_by_status(self, status: ProjectStatus) -> List[ConstructionProject]:
        return [p for p in self.projects.values() if p.status == status]

    def get_projects_by_type(self, project_type: ProjectType) -> List[ConstructionProject]:
        return [p for p in self.projects.values() if p.project_type == project_type]


def main():
    # Example usage
    manager = ProjectManager()

    # Create a new project
    project = manager.create_project(
        "Downtown Office Tower",
        ProjectType.TURNKEY,
        "Acme Corp"
    )

    # Set project details
    project.set_budget(5000000.00)
    project.estimated_end_date = datetime(2024, 12, 31)

    # Add team members
    architect = TeamMember("John Doe", "Lead Architect", "john@example.com")
    engineer = TeamMember("Jane Smith", "Structural Engineer", "jane@example.com")
    project.add_team_member(architect)
    project.add_team_member(engineer)

    # Add client requirements
    requirement1 = ClientRequirement("LEED Gold Certification", 1)
    requirement2 = ClientRequirement("Underground Parking", 2)
    project.add_requirement(requirement1)
    project.add_requirement(requirement2)

    # Add tasks
    design_task = Task("Create initial design", datetime(2023, 6, 30), 1)
    permit_task = Task("Obtain construction permits", datetime(2023, 8, 15), 2)
    project.add_task(design_task)
    project.add_task(permit_task)

    # Assign tasks
    design_task.assign_to(architect)
    permit_task.assign_to(engineer)

    # Update project status
    project.update_status(ProjectStatus.DESIGN)

    # Print project summary
    print(project)


if __name__ == "__main__":
    main()
```
