"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Design a maintenance plan for industrial machinery using preventive and corrective maintenance strategies, as described by Multiservicios 3L.
Generated: DETERMINISTIC_ed9da921820c580f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class MaintenanceTask:
    """Class representing a maintenance task for industrial machinery."""
    
    def __init__(self, task_id: int, description: str, frequency_days: int):
        """
        Initialize a maintenance task.

        :param task_id: Unique identifier for the task.
        :param description: Description of the maintenance task.
        :param frequency_days: Frequency of the task in days.
        """
        self.task_id = task_id
        self.description = description
        self.frequency_days = frequency_days
        self.last_performed = None

    def schedule_next(self) -> datetime.date:
        """Calculate the next scheduled date for the maintenance task."""
        if self.last_performed is None:
            return datetime.date.today()
        return self.last_performed + datetime.timedelta(days=self.frequency_days)

    def perform_task(self):
        """Mark the task as performed and update the last performed date."""
        self.last_performed = datetime.date.today()


class MaintenancePlan:
    """Class to manage a maintenance plan for industrial machinery."""
    
    def __init__(self):
        """Initialize the maintenance plan with an empty task list."""
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """Add a maintenance task to the plan.

        :param task: MaintenanceTask object to be added.
        """
        self.tasks.append(task)

    def get_due_tasks(self) -> List[Dict[str, Optional[str]]]:
        """Get a list of tasks that are due for maintenance.

        :return: List of dictionaries containing task details.
        """
        due_tasks = []
        today = datetime.date.today()
        for task in self.tasks:
            if task.schedule_next() <= today:
                due_tasks.append({
                    'task_id': task.task_id,
                    'description': task.description,
                    'next_due': task.schedule_next()
                })
        return due_tasks

    def perform_task(self, task_id: int) -> Optional[str]:
        """Perform a maintenance task by its ID.

        :param task_id: ID of the task to perform.
        :return: Success message or error message if task not found.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.perform_task()
                return f"Task {task_id} performed successfully."
        return f"Task {task_id} not found."


# Example usage
if __name__ == "__main__":
    # Create a maintenance plan
    maintenance_plan = MaintenancePlan()

    # Add some maintenance tasks
    maintenance_plan.add_task(MaintenanceTask(1, "Oil Change", 30))
    maintenance_plan.add_task(MaintenanceTask(2, "Filter Replacement", 60))
    maintenance_plan.add_task(MaintenanceTask(3, "Belt Inspection", 90))

    # Perform a task
    print(maintenance_plan.perform_task(1))

    # Get due tasks
    due_tasks = maintenance_plan.get_due_tasks()
    print("Due Maintenance Tasks:")
    for task in due_tasks:
        print(task)
```
