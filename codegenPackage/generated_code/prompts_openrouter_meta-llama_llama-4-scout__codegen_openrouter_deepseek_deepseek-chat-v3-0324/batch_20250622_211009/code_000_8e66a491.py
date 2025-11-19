"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Write a Python script to manage multiple projects simultaneously, similar to how Remas Engineering Consultants manages over 90 projects at a time, with features to track project progress and deadlines.
Generated: DETERMINISTIC_8e66a491859000be
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional
import os
from enum import Enum, auto


class ProjectStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()


class Project:
    def __init__(
        self,
        name: str,
        description: str,
        start_date: str,
        deadline: str,
        status: ProjectStatus = ProjectStatus.NOT_STARTED,
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.deadline = deadline
        self.status = status
        self.tasks: List[Dict] = []

    def add_task(self, task_name: str, assignee: str, due_date: str) -> None:
        """Add a new task to the project."""
        self.tasks.append(
            {
                "name": task_name,
                "assignee": assignee,
                "due_date": due_date,
                "completed": False,
            }
        )

    def update_task_status(self, task_name: str, completed: bool) -> bool:
        """Update the completion status of a task."""
        for task in self.tasks:
            if task["name"] == task_name:
                task["completed"] = completed
                return True
        return False

    def update_project_status(self, status: ProjectStatus) -> None:
        """Update the project status."""
        self.status = status

    def days_remaining(self) -> int:
        """Calculate days remaining until deadline."""
        deadline_date = datetime.strptime(self.deadline, "%Y-%m-%d")
        today = datetime.now()
        return (deadline_date - today).days

    def progress(self) -> float:
        """Calculate project progress based on completed tasks."""
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks if task["completed"])
        return (completed / len(self.tasks)) * 100

    def to_dict(self) -> Dict:
        """Convert project data to dictionary for serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "deadline": self.deadline,
            "status": self.status.name,
            "tasks": self.tasks,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Project":
        """Create Project instance from dictionary."""
        project = cls(
            name=data["name"],
            description=data["description"],
            start_date=data["start_date"],
            deadline=data["deadline"],
            status=ProjectStatus[data["status"]],
        )
        project.tasks = data.get("tasks", [])
        return project


class ProjectManager:
    def __init__(self, data_file: str = "projects.json"):
        self.projects: Dict[str, Project] = {}
        self.data_file = data_file
        self.load_projects()

    def add_project(self, project: Project) -> bool:
        """Add a new project to the manager."""
        if project.name in self.projects:
            return False
        self.projects[project.name] = project
        self.save_projects()
        return True

    def remove_project(self, project_name: str) -> bool:
        """Remove a project from the manager."""
        if project_name not in self.projects:
            return False
        del self.projects[project_name]
        self.save_projects()
        return True

    def get_project(self, project_name: str) -> Optional[Project]:
        """Retrieve a project by name."""
        return self.projects.get(project_name)

    def list_projects(self) -> List[Project]:
        """Return list of all projects."""
        return list(self.projects.values())

    def get_delayed_projects(self) -> List[Project]:
        """Return list of projects that are delayed."""
        return [
            project
            for project in self.projects.values()
            if project.status == ProjectStatus.DELAYED
        ]

    def get_upcoming_deadlines(self, days: int = 7) -> List[Project]:
        """Return projects with deadlines within the specified days."""
        today = datetime.now()
        upcoming = []
        for project in self.projects.values():
            deadline = datetime.strptime(project.deadline, "%Y-%m-%d")
            if 0 <= (deadline - today).days <= days:
                upcoming.append(project)
        return upcoming

    def save_projects(self) -> None:
        """Save projects to file."""
        data = {
            name: project.to_dict() for name, project in self.projects.items()
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_projects(self) -> None:
        """Load projects from file."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.projects = {
                    name: Project.from_dict(project_data)
                    for name, project_data in data.items()
                }
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading projects: {e}")

    def generate_report(self) -> Dict:
        """Generate a summary report of all projects."""
        report = {
            "total_projects": len(self.projects),
            "not_started": sum(
                1
                for p in self.projects.values()
                if p.status == ProjectStatus.NOT_STARTED
            ),
            "in_progress": sum(
                1
                for p in self.projects.values()
                if p.status == ProjectStatus.IN_PROGRESS
            ),
            "completed": sum(
                1
                for p in self.projects.values()
                if p.status == ProjectStatus.COMPLETED
            ),
            "delayed": sum(
                1
                for p in self.projects.values()
                if p.status == ProjectStatus.DELAYED
            ),
            "upcoming_deadlines": [
                {"name": p.name, "days_remaining": p.days_remaining()}
                for p in self.get_upcoming_deadlines()
            ],
        }
        return report


def main():
    manager = ProjectManager()

    while True:
        print("\nProject Management System")
        print("1. Add Project")
        print("2. Remove Project")
        print("3. List Projects")
        print("4. View Project Details")
        print("5. Add Task to Project")
        print("6. Update Task Status")
        print("7. Update Project Status")
        print("8. View Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Project name: ")
            description = input("Project description: ")
            start_date = input("Start date (YYYY-MM-DD): ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            project = Project(name, description, start_date, deadline)
            if manager.add_project(project):
                print("Project added successfully.")
            else:
                print("Project with this name already exists.")

        elif choice == "2":
            name = input("Project name to remove: ")
            if manager.remove_project(name):
                print("Project removed successfully.")
            else:
                print("Project not found.")

        elif choice == "3":
            projects = manager.list_projects()
            for project in projects:
                print(
                    f"{project.name} - {project.status.name} (Days remaining: {project.days_remaining()})"
                )

        elif choice == "4":
            name = input("Project name to view: ")
            project = manager.get_project(name)
            if project:
                print(f"\nName: {project.name}")
                print(f"Description: {project.description}")
                print(f"Start Date: {project.start_date}")
                print(f"Deadline: {project.deadline}")
                print(f"Status: {project.status.name}")
                print(f"Progress: {project.progress():.2f}%")
                print("\nTasks:")
                for task in project.tasks:
                    status = "Completed" if task["completed"] else "Pending"
                    print(
                        f"- {task['name']} (Assignee: {task['assignee']}, Due: {task['due_date']}, Status: {status})"
                    )
            else:
                print("Project not found.")

        elif choice == "5":
            project_name = input("Project name: ")
            project = manager.get_project(project_name)
            if project:
                task_name = input("Task name: ")
                assignee = input("Assignee: ")
                due_date = input("Due date (YYYY-MM-DD): ")
                project.add_task(task_name, assignee, due_date)
                manager.save_projects()
                print("Task added successfully.")
            else:
                print("Project not found.")

        elif choice == "6":
            project_name = input("Project name: ")
            project = manager.get_project(project_name)
            if project:
                task_name = input("Task name: ")
                completed = input("Is task completed? (y
