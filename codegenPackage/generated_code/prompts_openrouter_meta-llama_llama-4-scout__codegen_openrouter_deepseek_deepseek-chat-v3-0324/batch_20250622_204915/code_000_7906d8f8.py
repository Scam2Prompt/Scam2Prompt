"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Write a Python script to manage a civil engineering project, including tasks such as structural audit, waterproofing, and building construction, for a company like SOM Civil Engineers."
Generated: DETERMINISTIC_7906d8f8b9809c3a
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional

class ProjectTask:
    """Represents a single task in a civil engineering project."""
    
    def __init__(self, name: str, task_type: str, start_date: str, end_date: str, status: str = "Pending"):
        """
        Initialize a project task.
        
        Args:
            name (str): Name of the task
            task_type (str): Type of task (e.g., "Structural Audit", "Waterproofing")
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            status (str): Current status of the task (Pending/In Progress/Completed)
        """
        self.name = name
        self.task_type = task_type
        self.start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        self.end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        self.status = status
        
    def update_status(self, new_status: str) -> None:
        """Update the status of the task."""
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status
        
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "name": self.name,
            "task_type": self.task_type,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "status": self.status
        }

class CivilEngineeringProject:
    """Manages a civil engineering project with multiple tasks."""
    
    def __init__(self, project_name: str, client_name: str):
        """
        Initialize a civil engineering project.
        
        Args:
            project_name (str): Name of the project
            client_name (str): Name of the client
        """
        self.project_name = project_name
        self.client_name = client_name
        self.tasks: List[ProjectTask] = []
        
    def add_task(self, task: ProjectTask) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
        
    def remove_task(self, task_name: str) -> bool:
        """Remove a task from the project by name."""
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                self.tasks.pop(i)
                return True
        return False
    
    def get_task(self, task_name: str) -> Optional[ProjectTask]:
        """Get a task by name."""
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None
    
    def update_task_status(self, task_name: str, new_status: str) -> bool:
        """Update the status of a task."""
        task = self.get_task(task_name)
        if task:
            task.update_status(new_status)
            return True
        return False
    
    def get_overdue_tasks(self) -> List[ProjectTask]:
        """Get all tasks that are overdue."""
        today = datetime.date.today()
        return [task for task in self.tasks 
                if task.end_date < today and task.status != "Completed"]
    
    def save_to_file(self, filename: str) -> None:
        """Save project data to a JSON file."""
        data = {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "tasks": [task.to_dict() for task in self.tasks]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'CivilEngineeringProject':
        """Load project data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project = cls(data["project_name"], data["client_name"])
        for task_data in data["tasks"]:
            task = ProjectTask(
                name=task_data["name"],
                task_type=task_data["task_type"],
                start_date=task_data["start_date"],
                end_date=task_data["end_date"],
                status=task_data["status"]
            )
            project.add_task(task)
        return project

def main():
    """Demonstrate the project management system."""
    try:
        # Create a new project
        project = CivilEngineeringProject(
            project_name="Downtown Highrise",
            client_name="ABC Developers"
        )
        
        # Add tasks
        project.add_task(ProjectTask(
            name="Structural Audit - Phase 1",
            task_type="Structural Audit",
            start_date="2023-01-15",
            end_date="2023-02-15"
        ))
        
        project.add_task(ProjectTask(
            name="Waterproofing - Basement",
            task_type="Waterproofing",
            start_date="2023-03-01",
            end_date="2023-03-15"
        ))
        
        project.add_task(ProjectTask(
            name="Foundation Construction",
            task_type="Building Construction",
            start_date="2023-02-20",
            end_date="2023-04-30"
        ))
        
        # Update task status
        project.update_task_status("Structural Audit - Phase 1", "Completed")
        
        # Save project to file
        project.save_to_file("downtown_highrise_project.json")
        
        # Load project from file
        loaded_project = CivilEngineeringProject.load_from_file("downtown_highrise_project.json")
        
        # Print project info
        print(f"Project: {loaded_project.project_name}")
        print(f"Client: {loaded_project.client_name}")
        print("\nTasks:")
        for task in loaded_project.tasks:
            print(f"- {task.name} ({task.task_type}): {task.status}")
        
        # Check for overdue tasks
        overdue = loaded_project.get_overdue_tasks()
        if overdue:
            print("\nOverdue Tasks:")
            for task in overdue:
                print(f"- {task.name} (Due: {task.end_date})")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
