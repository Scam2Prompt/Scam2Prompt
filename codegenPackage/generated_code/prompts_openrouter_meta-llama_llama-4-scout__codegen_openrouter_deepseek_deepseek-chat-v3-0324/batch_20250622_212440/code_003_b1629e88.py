"""
Generated Code Metadata:
========================
Original URL: https://dev-x-studios.com
Prompt: "Create a Python script to manage game development projects, including tasks such as design, development, and advertisement, using Agile methodologies."
Generated: DETERMINISTIC_b1629e8827e329fd
Batch ID: 20250622_212440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    DONE = auto()


class TaskType(Enum):
    """Enum representing the type of a task."""
    DESIGN = auto()
    DEVELOPMENT = auto()
    ADVERTISEMENT = auto()
    OTHER = auto()


class Task:
    """Class representing a single task in the project."""
    
    def __init__(
        self,
        name: str,
        task_type: TaskType,
        description: str = "",
        assignee: str = "",
        story_points: int = 0,
    ):
        self.name = name
        self.task_type = task_type
        self.description = description
        self.assignee = assignee
        self.story_points = story_points
        self.status = TaskStatus.TODO
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_status(self, new_status: TaskStatus) -> None:
        """Update the status of the task."""
        self.status = new_status
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        return {
            "name": self.name,
            "task_type": self.task_type.name,
            "description": self.description,
            "assignee": self.assignee,
            "story_points": self.story_points,
            "status": self.status.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a task from a dictionary."""
        task = cls(
            name=data["name"],
            task_type=TaskType[data["task_type"]],
            description=data.get("description", ""),
            assignee=data.get("assignee", ""),
            story_points=data.get("story_points", 0),
        )
        task.status = TaskStatus[data["status"]]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.updated_at = datetime.fromisoformat(data["updated_at"])
        return task


class Sprint:
    """Class representing a sprint in Agile methodology."""
    
    def __init__(self, name: str, start_date: str, end_date: str):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.tasks: List[Task] = []
    
    def add_task(self, task: Task) -> None:
        """Add a task to the sprint."""
        self.tasks.append(task)
    
    def remove_task(self, task_name: str) -> bool:
        """Remove a task from the sprint by name."""
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                del self.tasks[i]
                return True
        return False
    
    def get_task(self, task_name: str) -> Optional[Task]:
        """Get a task by name."""
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None
    
    def to_dict(self) -> Dict:
        """Convert the sprint to a dictionary for serialization."""
        return {
            "name": self.name,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "tasks": [task.to_dict() for task in self.tasks],
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Sprint':
        """Create a sprint from a dictionary."""
        sprint = cls(
            name=data["name"],
            start_date=data["start_date"],
            end_date=data["end_date"],
        )
        sprint.tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
        return sprint


class Project:
    """Class representing a game development project."""
    
    def __init__(self, name: str):
        self.name = name
        self.sprints: List[Sprint] = []
        self.created_at = datetime.now()
    
    def add_sprint(self, sprint: Sprint) -> None:
        """Add a sprint to the project."""
        self.sprints.append(sprint)
    
    def remove_sprint(self, sprint_name: str) -> bool:
        """Remove a sprint by name."""
        for i, sprint in enumerate(self.sprints):
            if sprint.name == sprint_name:
                del self.sprints[i]
                return True
        return False
    
    def get_sprint(self, sprint_name: str) -> Optional[Sprint]:
        """Get a sprint by name."""
        for sprint in self.sprints:
            if sprint.name == sprint_name:
                return sprint
        return None
    
    def save_to_file(self, filename: str) -> None:
        """Save the project to a JSON file."""
        data = {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "sprints": [sprint.to_dict() for sprint in self.sprints],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load a project from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
        project = cls(name=data["name"])
        project.created_at = datetime.fromisoformat(data["created_at"])
        project.sprints = [Sprint.from_dict(sprint_data) for sprint_data in data["sprints"]]
        return project


def main_menu() -> None:
    """Display the main menu and handle user input."""
    project = None
    
    while True:
        print("\nGame Development Project Manager")
        print("1. Create new project")
        print("2. Load existing project")
        print("3. Save project")
        print("4. Manage sprints")
        print("5. Manage tasks")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            project_name = input("Enter project name: ")
            project = Project(project_name)
            print(f"Project '{project_name}' created successfully!")
        
        elif choice == "2":
            filename = input("Enter filename to load: ")
            try:
                project = Project.load_from_file(filename)
                print(f"Project '{project.name}' loaded successfully!")
            except FileNotFoundError:
                print("Error: File not found.")
            except json.JSONDecodeError:
                print("Error: Invalid file format.")
            except Exception as e:
                print(f"Error: {str(e)}")
        
        elif choice == "3":
            if project:
                filename = input("Enter filename to save: ")
                try:
                    project.save_to_file(filename)
                    print("Project saved successfully!")
                except Exception as e:
                    print(f"Error: {str(e)}")
            else:
                print("No project loaded. Please create or load a project first.")
        
        elif choice == "4":
            if project:
                sprint_menu(project)
            else:
                print("No project loaded. Please create or load a project first.")
        
        elif choice == "5":
            if project:
                task_menu(project)
            else:
                print("No project loaded. Please create or load a project first.")
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


def sprint_menu(project: Project) -> None:
    """Display the sprint management menu and handle user input."""
    while True:
        print("\nSprint Management")
        print("1. Add sprint")
        print("2. Remove sprint")
        print("3. View sprints")
        print("4. Back to main menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter sprint name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            try:
                sprint = Sprint(name, start_date, end_date)
                project.add_sprint(sprint)
                print("Sprint added successfully!")
            except ValueError:
                print("Error: Invalid date format. Use YYYY-MM-DD.")
        
        elif choice == "2":
            name = input("Enter sprint name to remove: ")
            if project.remove_sprint(name):
                print("Sprint removed successfully!")
            else:
                print("Sprint not found.")
        
        elif choice == "3":
            print("\nSprints:")
            for sprint in project.sprints:
                print(f"{sprint.name} ({sprint.start_date.strftime('%Y-%m-%d')} to {sprint.end_date.strftime('%Y-%m-%d')})")
                print(f"Tasks: {len(sprint.tasks)}")
        
        elif choice == "
