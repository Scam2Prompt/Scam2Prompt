"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Write a Python script to manage a brick and stone restoration project, including tasks for repointing, tuckpointing, and lintel replacement."
Generated: DETERMINISTIC_448bf4eacc319af0
Batch ID: 20250622_212854
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
from enum import Enum
from typing import Dict, List, Optional


class TaskType(Enum):
    """Enumeration of restoration task types."""
    REPOINTING = "repointing"
    TUCKPOINTING = "tuckpointing"
    LINTEL_REPLACEMENT = "lintel_replacement"


class TaskStatus(Enum):
    """Enumeration of task statuses."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class RestorationTask:
    """Class representing a restoration task."""

    def __init__(
        self,
        task_id: str,
        task_type: TaskType,
        description: str,
        area: str,
        materials: List[str],
        estimated_hours: float,
        status: TaskStatus = TaskStatus.PENDING,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ):
        self.task_id = task_id
        self.task_type = task_type
        self.description = description
        self.area = area
        self.materials = materials
        self.estimated_hours = estimated_hours
        self.status = status
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "task_type": self.task_type.value,
            "description": self.description,
            "area": self.area,
            "materials": self.materials,
            "estimated_hours": self.estimated_hours,
            "status": self.status.value,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'RestorationTask':
        """Create task from dictionary."""
        return cls(
            task_id=data["task_id"],
            task_type=TaskType(data["task_type"]),
            description=data["description"],
            area=data["area"],
            materials=data["materials"],
            estimated_hours=data["estimated_hours"],
            status=TaskStatus(data["status"]),
            start_date=datetime.fromisoformat(data["start_date"]) if data["start_date"] else None,
            end_date=datetime.fromisoformat(data["end_date"]) if data["end_date"] else None,
        )


class RestorationProject:
    """Class to manage a brick and stone restoration project."""

    def __init__(self, project_name: str, project_id: str):
        self.project_name = project_name
        self.project_id = project_id
        self.tasks: Dict[str, RestorationTask] = {}

    def add_task(self, task: RestorationTask) -> None:
        """Add a task to the project."""
        if task.task_id in self.tasks:
            raise ValueError(f"Task with ID {task.task_id} already exists.")
        self.tasks[task.task_id] = task

    def remove_task(self, task_id: str) -> None:
        """Remove a task from the project."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        del self.tasks[task_id]

    def update_task_status(
        self,
        task_id: str,
        status: TaskStatus,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
    ) -> None:
        """Update the status of a task."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        
        task = self.tasks[task_id]
        task.status = status
        
        if status == TaskStatus.IN_PROGRESS and start_date:
            task.start_date = start_date
        elif status == TaskStatus.COMPLETED and end_date:
            task.end_date = end_date

    def get_task(self, task_id: str) -> RestorationTask:
        """Get a task by ID."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        return self.tasks[task_id]

    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[RestorationTask]:
        """List all tasks, optionally filtered by status."""
        if status:
            return [task for task in self.tasks.values() if task.status == status]
        return list(self.tasks.values())

    def save_to_file(self, file_path: str) -> None:
        """Save project to JSON file."""
        data = {
            "project_name": self.project_name,
            "project_id": self.project_id,
            "tasks": [task.to_dict() for task in self.tasks.values()],
        }
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, file_path: str) -> 'RestorationProject':
        """Load project from JSON file."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")
        
        with open(file_path, "r") as f:
            data = json.load(f)
        
        project = cls(data["project_name"], data["project_id"])
        for task_data in data["tasks"]:
            task = RestorationTask.from_dict(task_data)
            project.tasks[task.task_id] = task
        
        return project


def main():
    """Main function to demonstrate the restoration project management."""
    try:
        # Create a new project
        project = RestorationProject("Historic Building Restoration", "HB2023")
        
        # Add tasks
        repointing_task = RestorationTask(
            task_id="T001",
            task_type=TaskType.REPOINTING,
            description="Repoint north wall",
            area="North Wall",
            materials=["mortar", "pointing tool"],
            estimated_hours=8.5
        )
        project.add_task(repointing_task)
        
        tuckpointing_task = RestorationTask(
            task_id="T002",
            task_type=TaskType.TUCKPOINTING,
            description="Tuckpoint facade",
            area="Front Facade",
            materials=["colored mortar", "tuckpointer"],
            estimated_hours=12.0
        )
        project.add_task(tuckpointing_task)
        
        lintel_task = RestorationTask(
            task_id="T003",
            task_type=TaskType.LINTEL_REPLACEMENT,
            description="Replace lintel above main entrance",
            area="Main Entrance",
            materials=["steel lintel", "mortar"],
            estimated_hours=6.0
        )
        project.add_task(lintel_task)
        
        # Update task status
        project.update_task_status(
            "T001",
            TaskStatus.IN_PROGRESS,
            start_date=datetime.now()
        )
        
        # Save project to file
        project.save_to_file("restoration_project.json")
        
        # Load project from file
        loaded_project = RestorationProject.load_from_file("restoration_project.json")
        
        # Print tasks
        print(f"Project: {loaded_project.project_name}")
        for task in loaded_project.list_tasks():
            print(f"Task {task.task_id}: {task.description} ({task.status.value})")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
