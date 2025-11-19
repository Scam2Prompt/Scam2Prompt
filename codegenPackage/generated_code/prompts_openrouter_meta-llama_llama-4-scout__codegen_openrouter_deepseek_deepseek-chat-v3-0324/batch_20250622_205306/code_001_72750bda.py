"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script to manage construction projects for a company like Peace City Contracting LLC, including tasks for building construction, renovation, and MEP works.
Generated: DETERMINISTIC_72750bda4a16efd5
Batch ID: 20250622_205306
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
from typing import List, Dict, Optional, Union
import uuid
import os

class Task:
    """Represents a construction task with details."""
    
    def __init__(self, name: str, description: str, task_type: str, 
                 start_date: str, end_date: str, status: str = "Pending"):
        """
        Initialize a construction task.
        
        Args:
            name: Name of the task
            description: Detailed description
            task_type: Type of task (construction/renovation/MEP)
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            status: Current status (Pending/In Progress/Completed)
        """
        self.task_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.task_type = task_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def update_status(self, new_status: str) -> None:
        """Update the task status."""
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "task_type": self.task_type,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class Project:
    """Represents a construction project containing multiple tasks."""
    
    def __init__(self, name: str, description: str, location: str):
        """
        Initialize a construction project.
        
        Args:
            name: Name of the project
            description: Detailed description
            location: Physical location of the project
        """
        self.project_id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.location = location
        self.tasks: List[Task] = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = self.created_at

    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def remove_task(self, task_id: str) -> bool:
        """Remove a task from the project by task_id."""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(i)
                self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return True
        return False

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by task_id."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task_status(self, task_id: str, new_status: str) -> bool:
        """Update status of a specific task."""
        task = self.get_task(task_id)
        if task:
            task.update_status(new_status)
            self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
        return False

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization."""
        return {
            "project_id": self.project_id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "tasks": [task.to_dict() for task in self.tasks],
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

class ConstructionManager:
    """Manages multiple construction projects."""
    
    def __init__(self, data_file: str = "construction_data.json"):
        """
        Initialize the construction manager.
        
        Args:
            data_file: Path to JSON file for data persistence
        """
        self.data_file = data_file
        self.projects: Dict[str, Project] = {}
        self.load_data()

    def add_project(self, project: Project) -> None:
        """Add a project to the manager."""
        self.projects[project.project_id] = project
        self.save_data()

    def remove_project(self, project_id: str) -> bool:
        """Remove a project by project_id."""
        if project_id in self.projects:
            del self.projects[project_id]
            self.save_data()
            return True
        return False

    def get_project(self, project_id: str) -> Optional[Project]:
        """Get a project by project_id."""
        return self.projects.get(project_id)

    def add_task_to_project(self, project_id: str, task: Task) -> bool:
        """Add a task to a specific project."""
        project = self.get_project(project_id)
        if project:
            project.add_task(task)
            self.save_data()
            return True
        return False

    def update_task_status_in_project(self, project_id: str, task_id: str, 
                                    new_status: str) -> bool:
        """Update task status in a specific project."""
        project = self.get_project(project_id)
        if project:
            success = project.update_task_status(task_id, new_status)
            if success:
                self.save_data()
            return success
        return False

    def load_data(self) -> None:
        """Load project data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    for project_data in data.get("projects", []):
                        project = Project(
                            name=project_data["name"],
                            description=project_data["description"],
                            location=project_data["location"]
                        )
                        project.project_id = project_data["project_id"]
                        project.created_at = project_data["created_at"]
                        project.updated_at = project_data["updated_at"]
                        
                        for task_data in project_data.get("tasks", []):
                            task = Task(
                                name=task_data["name"],
                                description=task_data["description"],
                                task_type=task_data["task_type"],
                                start_date=task_data["start_date"],
                                end_date=task_data["end_date"],
                                status=task_data["status"]
                            )
                            task.task_id = task_data["task_id"]
                            task.created_at = task_data["created_at"]
                            task.updated_at = task_data["updated_at"]
                            project.add_task(task)
                        
                        self.projects[project.project_id] = project
            except Exception as e:
                print(f"Error loading data: {e}")

    def save_data(self) -> None:
        """Save project data to JSON file."""
        try:
            data = {
                "projects": [project.to_dict() for project in self.projects.values()]
            }
            with open(self.data_file, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def get_all_projects(self) -> List[Dict]:
        """Get all projects as dictionaries."""
        return [project.to_dict() for project in self.projects.values()]

    def get_project_tasks(self, project_id: str) -> Optional[List[Dict]]:
        """Get all tasks for a project as dictionaries."""
        project = self.get_project(project_id)
        if project:
            return [task.to_dict() for task in project.tasks]
        return None

def main():
    """Example usage of the Construction Manager."""
    manager = ConstructionManager()
    
    # Create a new project
    project = Project(
        name="Downtown Office Building",
        description="Construction of a 10-story office building",
        location="123 Main St, Anytown, USA"
    )
    manager.add_project(project)
    
    # Add tasks to the project
    construction_task = Task(
        name="Foundation Work",
        description="Excavation and pouring concrete foundation",
        task_type="construction",
        start_date="2023-01-15",
        end_date="2023-02-28"
    )
    
    mep_task = Task(
        name="Electrical Wiring",
        description="Installation of electrical systems",
        task_type="MEP",
        start_date="2023-03-01",
        end_date="2023-04-15"
    )
    
    manager.add_task_to_project(project.project_id, construction_task)
    manager.add_task_to_project(project.project_id, mep_task)
    
    # Update task status
    manager.update_task_status_in_project
