"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Write a Python script to automate the scheduling of residential block maintenance tasks, referencing the services offered by BlocPrest (e.g., cleaning, repairs, and technical support).
Generated: DETERMINISTIC_a1f179b61bb9b3aa
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
import random

# Define a class to represent a maintenance task
class MaintenanceTask:
    def __init__(self, service_type, frequency_days, last_completed=None):
        self.service_type = service_type
        self.frequency_days = frequency_days
        self.last_completed = last_completed or datetime.now()

    def next_due_date(self):
        """Calculate the next due date for the maintenance task."""
        return self.last_completed + timedelta(days=self.frequency_days)

    def mark_completed(self):
        """Mark the task as completed and update the last completed date."""
        self.last_completed = datetime.now()

# Define a class to manage the scheduling of maintenance tasks
class MaintenanceScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, service_type, frequency_days):
        """Add a new maintenance task to the scheduler."""
        task = MaintenanceTask(service_type, frequency_days)
        self.tasks.append(task)

    def get_due_tasks(self):
        """Retrieve a list of tasks that are due for maintenance."""
        due_tasks = [task for task in self.tasks if task.next_due_date() <= datetime.now()]
        return due_tasks

    def mark_task_completed(self, task):
        """Mark a specific task as completed."""
        task.mark_completed()

    def save_schedule(self, filename):
        """Save the current schedule to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_schedule(self, filename):
        """Load the schedule from a JSON file."""
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [MaintenanceTask(**task) for task in tasks_data]
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty schedule.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Starting with an empty schedule.")

# Example usage of the MaintenanceScheduler
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()

    # Load existing schedule if available
    scheduler.load_schedule('maintenance_schedule.json')

    # Add maintenance tasks for BlocPrest services
    scheduler.add_task('Cleaning', frequency_days=30)
    scheduler.add_task('Repairs', frequency_days=90)
    scheduler.add_task('Technical Support', frequency_days=180)

    # Check for due tasks
    due_tasks = scheduler.get_due_tasks()
    if due_tasks:
        print("Due maintenance tasks:")
        for task in due_tasks:
            print(f"- {task.service_type} (Next due: {task.next_due_date().strftime('%Y-%m-%d')})")
            # Mark the task as completed (for demonstration purposes)
            scheduler.mark_task_completed(task)
    else:
        print("No maintenance tasks are due.")

    # Save the updated schedule
    scheduler.save_schedule('maintenance_schedule.json')
```
