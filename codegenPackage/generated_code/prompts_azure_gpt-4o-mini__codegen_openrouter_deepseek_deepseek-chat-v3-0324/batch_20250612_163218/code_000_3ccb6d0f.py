"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Generate a code snippet for a project management tool that tracks construction timelines and responsibilities for a construction company like Construye RK.
Generated: DETERMINISTIC_3ccb6d0f59cad8a9
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management Tool for Construye RK

This module provides functionality to track construction project timelines,
tasks, and responsibilities. It includes features for adding projects, assigning
tasks to team members, and tracking progress.

Features:
- Project creation and management
- Task assignment and tracking
- Timeline visualization
- Responsibility tracking
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
import os


class Project:
    """Represents a construction project with tasks and timelines."""

    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        """
        Initialize a new project.

        Args:
            name: Name of the project
            start_date: Project start date
            end_date: Project end date
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.team_members: Dict[str, List[Task]] = {}

    def add_task(self, task: 'Task') -> None:
        """Add a task to the project."""
        if task.end_date > self.end_date:
            raise ValueError("Task end date cannot exceed project end date")
        self.tasks.append(task)

    def assign_task(self, task_name: str, team_member: str) -> None:
        """
        Assign a task to a team member.

        Args:
            task_name: Name of the task to assign
            team_member: Name of the team member
        """
        task = next((t for t in self.tasks if t.name == task_name), None)
        if not task:
            raise ValueError(f"Task '{task_name}' not found in project")

        if team_member not in self.team_members:
            self.team_members[team_member] = []
        self.team_members[team_member].append(task)

    def get_project_timeline(self) -> Dict:
        """Return project timeline with all tasks."""
        return {
            "project": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": [task.to_dict() for task in self.tasks]
        }

    def save_to_file(self, filename: str) -> None:
        """Save project data to JSON file."""
        data = {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": [task.to_dict() for task in self.tasks],
            "team_members": {
                member: [task.name for task in tasks]
                for member, tasks in self.team_members.items()
            }
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load project data from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)

        start_date = datetime.fromisoformat(data['start_date'])
        end_date = datetime.fromisoformat(data['end_date'])
        project = cls(data['name'], start_date, end_date)

        for task_data in data['tasks']:
            task = Task(
                task_data['name'],
                datetime.fromisoformat(task_data['start_date']),
                datetime.fromisoformat(task_data['end_date']),
                task_data['description']
            )
            project.add_task(task)

        for member, task_names in data['team_members'].items():
            for task_name in task_names:
                project.assign_task(task_name, member)

        return project


class Task:
    """Represents a task in a construction project."""

    def __init__(self, name: str, start_date: datetime, end_date: datetime, description: str = ""):
        """
        Initialize a new task.

        Args:
            name: Name of the task
            start_date: Task start date
            end_date: Task end date
            description: Task description
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.completed = False

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "description": self.description,
            "completed": self.completed
        }


class ProjectManager:
    """Manages multiple construction projects."""

    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project) -> None:
        """Add a project to the manager."""
        if project.name in self.projects:
            raise ValueError(f"Project '{project.name}' already exists")
        self.projects[project.name] = project

    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(name)

    def save_all_projects(self, directory: str) -> None:
        """Save all projects to files in the specified directory."""
        os.makedirs(directory, exist_ok=True)
        for name, project in self.projects.items():
            filename = os.path.join(directory, f"{name.replace(' ', '_')}.json")
            project.save_to_file(filename)

    def load_all_projects(self, directory: str) -> None:
        """Load all projects from files in the specified directory."""
        for filename in os.listdir(directory):
            if filename.endswith('.json'):
                filepath = os.path.join(directory, filename)
                project = Project.load_from_file(filepath)
                self.add_project(project)


# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create a new project
    start_date = datetime.now()
    end_date = start_date + timedelta(days=90)
    project = Project("RK Office Building", start_date, end_date)

    # Add tasks to the project
    foundation_task = Task(
        "Foundation Work",
        start_date,
        start_date + timedelta(days=14),
        "Excavation and foundation pouring"
    )
    framing_task = Task(
        "Framing",
        start_date + timedelta(days=15),
        start_date + timedelta(days=45),
        "Structural framing and roofing"
    )

    project.add_task(foundation_task)
    project.add_task(framing_task)

    # Assign tasks to team members
    project.assign_task("Foundation Work", "John Doe")
    project.assign_task("Framing", "Jane Smith")

    # Add project to manager
    manager.add_project(project)

    # Save project to file
    manager.save_all_projects("projects")

    # Print project timeline
    print(json.dumps(project.get_project_timeline(), indent=4))
```
