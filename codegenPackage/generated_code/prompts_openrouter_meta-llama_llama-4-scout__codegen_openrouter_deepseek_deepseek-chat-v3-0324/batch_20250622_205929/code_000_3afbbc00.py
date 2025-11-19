"""
Generated Code Metadata:
========================
Original URL: https://www.sadadeng.com
Prompt: Write a Python script to manage construction projects, including tracking progress and deadlines, similar to the projects listed on the Sadad Engineering and Construction Company website.
Generated: DETERMINISTIC_3afbbc0079505591
Batch ID: 20250622_205929
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
This script helps manage construction projects by tracking progress, deadlines, and tasks.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class ConstructionProject:
    """
    Represents a construction project with tasks, deadlines, and progress tracking.
    """

    def __init__(self, name: str, start_date: str, deadline: str):
        """
        Initialize a construction project.

        Args:
            name: Name of the project
            start_date: Project start date (YYYY-MM-DD)
            deadline: Project deadline (YYYY-MM-DD)
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        self.tasks: List[Dict] = []
        self.completed_tasks: int = 0

    def add_task(self, task_name: str, duration_days: int, dependencies: Optional[List[int]] = None):
        """
        Add a task to the project.

        Args:
            task_name: Name of the task
            duration_days: Duration of task in days
            dependencies: List of task indices this task depends on
        """
        if dependencies is None:
            dependencies = []

        task = {
            "name": task_name,
            "duration": duration_days,
            "dependencies": dependencies,
            "completed": False,
            "start_date": None,
            "end_date": None
        }
        self.tasks.append(task)

    def complete_task(self, task_index: int):
        """
        Mark a task as completed.

        Args:
            task_index: Index of the task to mark as completed
        """
        if 0 <= task_index < len(self.tasks):
            if not self.tasks[task_index]["completed"]:
                self.tasks[task_index]["completed"] = True
                self.completed_tasks += 1
                return True
        return False

    def calculate_progress(self) -> float:
        """
        Calculate project completion percentage.

        Returns:
            float: Percentage of completed tasks (0-100)
        """
        if not self.tasks:
            return 0.0
        return (self.completed_tasks / len(self.tasks)) * 100

    def check_deadline(self) -> Dict:
        """
        Check if project is on track to meet deadline.

        Returns:
            Dict: Contains 'on_track' (bool) and 'days_remaining' (int)
        """
        today = datetime.now().date()
        days_remaining = (self.deadline - today).days
        progress = self.calculate_progress()
        expected_progress = ((today - self.start_date).days / 
                            (self.deadline - self.start_date).days) * 100

        return {
            "on_track": progress >= expected_progress,
            "days_remaining": days_remaining,
            "current_progress": progress,
            "expected_progress": expected_progress
        }

    def to_dict(self) -> Dict:
        """
        Convert project to dictionary for serialization.

        Returns:
            Dict: Project data
        """
        return {
            "name": self.name,
            "start_date": str(self.start_date),
            "deadline": str(self.deadline),
            "tasks": self.tasks,
            "completed_tasks": self.completed_tasks
        }

    @classmethod
    def from_dict(cls, data: Dict):
        """
        Create project from dictionary.

        Args:
            data: Dictionary containing project data

        Returns:
            ConstructionProject: New project instance
        """
        project = cls(data["name"], data["start_date"], data["deadline"])
        project.tasks = data["tasks"]
        project.completed_tasks = data["completed_tasks"]
        return project


class ProjectManager:
    """
    Manages multiple construction projects.
    """

    def __init__(self):
        self.projects: Dict[str, ConstructionProject] = {}

    def add_project(self, project: ConstructionProject):
        """
        Add a project to the manager.

        Args:
            project: ConstructionProject instance
        """
        self.projects[project.name] = project

    def remove_project(self, project_name: str):
        """
        Remove a project from the manager.

        Args:
            project_name: Name of project to remove
        """
        if project_name in self.projects:
            del self.projects[project_name]

    def get_project(self, project_name: str) -> Optional[ConstructionProject]:
        """
        Get a project by name.

        Args:
            project_name: Name of project to retrieve

        Returns:
            Optional[ConstructionProject]: Project instance or None if not found
        """
        return self.projects.get(project_name)

    def save_to_file(self, filename: str):
        """
        Save all projects to a JSON file.

        Args:
            filename: Path to save file
        """
        data = {
            "projects": [project.to_dict() for project in self.projects.values()]
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    def load_from_file(self, filename: str):
        """
        Load projects from a JSON file.

        Args:
            filename: Path to load file from
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.projects = {
                    project["name"]: ConstructionProject.from_dict(project)
                    for project in data["projects"]
                }
        except FileNotFoundError:
            print(f"Warning: File {filename} not found. Starting with empty project manager.")
        except json.JSONDecodeError:
            print(f"Error: File {filename} contains invalid JSON. Starting with empty project manager.")


def main():
    """Example usage of the construction project management system."""
    manager = ProjectManager()

    # Create a new project
    bridge_project = ConstructionProject(
        "City Bridge Construction",
        "2023-01-01",
        "2024-12-31"
    )

    # Add tasks to the project
    bridge_project.add_task("Site Preparation", 30)
    bridge_project.add_task("Foundation Work", 60, [0])
    bridge_project.add_task("Pillar Construction", 90, [1])
    bridge_project.add_task("Deck Installation", 120, [2])
    bridge_project.add_task("Final Inspection", 15, [3])

    # Add project to manager
    manager.add_project(bridge_project)

    # Complete some tasks
    bridge_project.complete_task(0)
    bridge_project.complete_task(1)

    # Check project status
    status = bridge_project.check_deadline()
    print(f"Project: {bridge_project.name}")
    print(f"Progress: {bridge_project.calculate_progress():.2f}%")
    print(f"Days remaining: {status['days_remaining']}")
    print(f"On track: {'Yes' if status['on_track'] else 'No'}")

    # Save projects to file
    manager.save_to_file("construction_projects.json")


if __name__ == "__main__":
    main()
```
