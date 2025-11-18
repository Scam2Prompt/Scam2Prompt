"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a task tracker system that categorizes tasks by priority (low, medium, high) and status (To do, In progress, Done, Backlog), with role-based project oversight as described on the Zapper website.
Generated: DETERMINISTIC_15c8a6d9101d4ccf
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from enum import Enum
from typing import List, Dict, Optional
import json

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"
    BACKLOG = "Backlog"

class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Task:
    def __init__(self, title: str, description: str, priority: TaskPriority, status: TaskStatus):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value
        }

class TaskTracker:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, priority: TaskPriority, status: TaskStatus):
        """Add a new task to the tracker."""
        new_task = Task(title, description, priority, status)
        self.tasks.append(new_task)

    def update_task(self, title: str, status: Optional[TaskStatus] = None, priority: Optional[TaskPriority] = None):
        """Update an existing task's status or priority."""
        for task in self.tasks:
            if task.title == title:
                if status is not None:
                    task.status = status
                if priority is not None:
                    task.priority = priority
                return
        raise ValueError(f"Task with title '{title}' not found.")

    def delete_task(self, title: str):
        """Delete a task from the tracker based on its title."""
        self.tasks = [task for task in self.tasks if task.title != title]

    def get_tasks_by_status(self, status: TaskStatus) -> List[Dict]:
        """Retrieve tasks filtered by their status."""
        return [task.to_dict() for task in self.tasks if task.status == status]

    def get_tasks_by_priority(self, priority: TaskPriority) -> List[Dict]:
        """Retrieve tasks filtered by their priority."""
        return [task.to_dict() for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename: str):
        """Save tasks to a JSON file for persistence."""
        with open(filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def load_from_file(self, filename: str):
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    title = task_data['title']
                    description = task_data['description']
                    priority = TaskPriority(task_data['priority'])
                    status = TaskStatus(task_data['status'])
                    self.add_task(title, description, priority, status)
        except FileNotFoundError:
            print("Warning: The file was not found. No tasks loaded.")
        except json.JSONDecodeError:
            print("Error: The file could not be decoded. No tasks loaded.")

# Example usage:
if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.add_task("Finish report", "Complete the Q1 financial report", TaskPriority.HIGH, TaskStatus.TODO)
    tracker.add_task("Code review", "Review the new pull request", TaskPriority.MEDIUM, TaskStatus.IN_PROGRESS)
    
    print(tracker.get_tasks_by_status(TaskStatus.TODO))  # Output tasks with status 'To Do'
    tracker.save_to_file("tasks.json")
    tracker.load_from_file("tasks.json")
```
