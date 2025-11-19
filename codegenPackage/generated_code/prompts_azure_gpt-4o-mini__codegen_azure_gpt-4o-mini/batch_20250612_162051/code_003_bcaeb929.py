"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Create a maintenance scheduling tool for infrastructure projects that integrates with existing construction management software.
Generated: DETERMINISTIC_bcaeb9297fa5fe30
Batch ID: 20250612_162051
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
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceTask:
    """Class representing a maintenance task for an infrastructure project."""
    
    def __init__(self, task_id: str, description: str, due_date: datetime.date, assigned_to: str):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
        logging.info(f"Task {self.task_id} marked as completed.")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the task to a dictionary for JSON serialization."""
        return {
            "task_id": self.task_id,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "assigned_to": self.assigned_to,
            "completed": self.completed
        }

class MaintenanceScheduler:
    """Class to manage maintenance tasks for infrastructure projects."""
    
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """Add a new maintenance task to the scheduler."""
        self.tasks.append(task)
        logging.info(f"Added task: {task.task_id}")

    def remove_task(self, task_id: str):
        """Remove a task from the scheduler by task ID."""
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        logging.info(f"Removed task: {task_id}")

    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Retrieve all tasks that are due today or earlier."""
        today = datetime.date.today()
        due_tasks = [task for task in self.tasks if task.due_date <= today and not task.completed]
        logging.info(f"Retrieved {len(due_tasks)} due tasks.")
        return due_tasks

    def save_to_file(self, filename: str):
        """Save the current tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
            logging.info(f"Tasks saved to {filename}.")
        except IOError as e:
            logging.error(f"Failed to save tasks to {filename}: {e}")

    def load_from_file(self, filename: str):
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [MaintenanceTask(**task) for task in tasks_data]
            logging.info(f"Tasks loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load tasks from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Load existing tasks from a file
    scheduler.load_from_file('tasks.json')

    # Add a new maintenance task
    new_task = MaintenanceTask(task_id="001", description="Inspect bridge integrity", due_date=datetime.date(2023, 10, 15), assigned_to="John Doe")
    scheduler.add_task(new_task)

    # Get and print due tasks
    due_tasks = scheduler.get_due_tasks()
    for task in due_tasks:
        print(f"Due Task: {task.description} (Assigned to: {task.assigned_to})")

    # Save tasks back to the file
    scheduler.save_to_file('tasks.json')
```
