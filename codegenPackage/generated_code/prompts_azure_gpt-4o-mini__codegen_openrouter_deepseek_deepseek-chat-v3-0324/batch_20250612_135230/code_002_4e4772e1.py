"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Write a Python script that automates the scheduling of tasks related to the installation of ball protection nets and fences in construction sites.
Generated: DETERMINISTIC_4e4772e18e557169
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional
from enum import Enum


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Task:
    """Class representing a task for installing protection nets/fences."""

    def __init__(
        self,
        task_id: str,
        site_name: str,
        task_type: str,
        scheduled_date: datetime.date,
        duration_days: int,
        assigned_team: str,
        status: TaskStatus = TaskStatus.PENDING,
    ):
        self.task_id = task_id
        self.site_name = site_name
        self.task_type = task_type
        self.scheduled_date = scheduled_date
        self.duration_days = duration_days
        self.assigned_team = assigned_team
        self.status = status

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "task_id": self.task_id,
            "site_name": self.site_name,
            "task_type": self.task_type,
            "scheduled_date": self.scheduled_date.isoformat(),
            "duration_days": self.duration_days,
            "assigned_team": self.assigned_team,
            "status": self.status.value,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Task":
        """Create task from dictionary."""
        return cls(
            task_id=data["task_id"],
            site_name=data["site_name"],
            task_type=data["task_type"],
            scheduled_date=datetime.date.fromisoformat(data["scheduled_date"]),
            duration_days=data["duration_days"],
            assigned_team=data["assigned_team"],
            status=TaskStatus(data["status"]),
        )


class TaskScheduler:
    """Class for managing and scheduling installation tasks."""

    def __init__(self, data_file: str = "tasks.json"):
        self.data_file = data_file
        self.tasks: List[Task] = []
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from the data file."""
        if not os.path.exists(self.data_file):
            return

        try:
            with open(self.data_file, "r") as f:
                tasks_data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Failed to load tasks: {e}")

    def _save_tasks(self) -> None:
        """Save tasks to the data file."""
        try:
            with open(self.data_file, "w") as f:
                tasks_data = [task.to_dict() for task in self.tasks]
                json.dump(tasks_data, f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Failed to save tasks: {e}")

    def add_task(self, task: Task) -> None:
        """Add a new task to the scheduler."""
        if any(t.task_id == task.task_id for t in self.tasks):
            raise ValueError(f"Task with ID {task.task_id} already exists")
        self.tasks.append(task)
        self._save_tasks()

    def get_task(self, task_id: str) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task_status(self, task_id: str, status: TaskStatus) -> None:
        """Update the status of a task."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        task.status = status
        self._save_tasks()

    def get_tasks_by_site(self, site_name: str) -> List[Task]:
        """Get all tasks for a specific construction site."""
        return [task for task in self.tasks if task.site_name == site_name]

    def get_tasks_by_date_range(
        self, start_date: datetime.date, end_date: datetime.date
    ) -> List[Task]:
        """Get tasks scheduled within a date range."""
        return [
            task
            for task in self.tasks
            if start_date <= task.scheduled_date <= end_date
        ]

    def delete_task(self, task_id: str) -> None:
        """Delete a task by its ID."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        self.tasks.remove(task)
        self._save_tasks()


def main():
    """Example usage of the TaskScheduler."""
    scheduler = TaskScheduler()

    # Example: Add a new task
    new_task = Task(
        task_id="T001",
        site_name="Downtown Highrise",
        task_type="Net Installation",
        scheduled_date=datetime.date(2023, 12, 15),
        duration_days=2,
        assigned_team="Team A",
    )
    scheduler.add_task(new_task)

    # Example: Update task status
    scheduler.update_task_status("T001", TaskStatus.IN_PROGRESS)

    # Example: Get tasks for a site
    site_tasks = scheduler.get_tasks_by_site("Downtown Highrise")
    print(f"Tasks for Downtown Highrise: {len(site_tasks)}")

    # Example: Get tasks in a date range
    start_date = datetime.date(2023, 12, 1)
    end_date = datetime.date(2023, 12, 31)
    date_tasks = scheduler.get_tasks_by_date_range(start_date, end_date)
    print(f"Tasks in December 2023: {len(date_tasks)}")


if __name__ == "__main__":
    main()
```
