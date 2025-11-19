"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: Provide a step-by-step guide for implementing a cleaning service management system, including scheduling and tracking tasks, as described in the "شمس المملكة" services.
Generated: DETERMINISTIC_124da7533d7ffc36
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cleaning_service_management.py

from datetime import datetime, timedelta
import json

class Task:
    """Class to represent a cleaning task."""
    
    def __init__(self, task_id, description, scheduled_time):
        self.task_id = task_id
        self.description = description
        self.scheduled_time = scheduled_time
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert task to dictionary for easy serialization."""
        return {
            'task_id': self.task_id,
            'description': self.description,
            'scheduled_time': self.scheduled_time.isoformat(),
            'completed': self.completed
        }

class CleaningService:
    """Class to manage cleaning tasks."""
    
    def __init__(self):
        self.tasks = {}
        self.next_task_id = 1

    def schedule_task(self, description, scheduled_time):
        """Schedule a new cleaning task."""
        if not isinstance(scheduled_time, datetime):
            raise ValueError("scheduled_time must be a datetime object")
        
        task = Task(self.next_task_id, description, scheduled_time)
        self.tasks[self.next_task_id] = task
        self.next_task_id += 1
        return task

    def complete_task(self, task_id):
        """Mark a task as completed."""
        if task_id not in self.tasks:
            raise KeyError(f"Task ID {task_id} not found.")
        
        self.tasks[task_id].mark_completed()

    def get_tasks(self):
        """Retrieve all tasks."""
        return [task.to_dict() for task in self.tasks.values()]

    def save_tasks(self, filename):
        """Save tasks to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_tasks(), file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving tasks: {e}")

    def load_tasks(self, filename):
        """Load tasks from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                for task_data in tasks_data:
                    task = Task(
                        task_data['task_id'],
                        task_data['description'],
                        datetime.fromisoformat(task_data['scheduled_time'])
                    )
                    task.completed = task_data['completed']
                    self.tasks[task.task_id] = task
                    self.next_task_id = max(self.next_task_id, task.task_id + 1)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"An error occurred while loading tasks: {e}")

# Example usage
if __name__ == "__main__":
    service = CleaningService()
    
    # Schedule some tasks
    service.schedule_task("Clean the living room", datetime.now() + timedelta(days=1))
    service.schedule_task("Wash the windows", datetime.now() + timedelta(days=2))
    
    # Complete a task
    service.complete_task(1)
    
    # Save tasks to a file
    service.save_tasks("tasks.json")
    
    # Load tasks from a file
    service.load_tasks("tasks.json")
    
    # Print all tasks
    print(service.get_tasks())
```
