"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://setingenieria.cl
Prompt: Write Python code to simulate a maintenance scheduling system for engineering projects, incorporating safety and efficiency standards as described by SET Ingeniería.
Generated: DETERMINISTIC_41081300cbf78c6a
Batch ID: 20250612_154846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

# Define a class to represent a Maintenance Task
class MaintenanceTask:
    def __init__(self, task_id: int, project_name: str, description: str, priority: str, due_date: datetime.date):
        """
        Initialize a MaintenanceTask instance.

        :param task_id: Unique identifier for the task.
        :param project_name: Name of the project the task belongs to.
        :param description: Description of the maintenance task.
        :param priority: Priority level of the task ('High', 'Medium', 'Low').
        :param due_date: Deadline for the task.
        """
        self.task_id = task_id
        self.project_name = project_name
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.is_completed = False
    
    def complete_task(self):
        """Mark the task as completed."""
        self.is_completed = True

    def __str__(self):
        """Return a string representation of the task."""
        status = "Completed" if self.is_completed else "Pending"
        return f"Task ID: {self.task_id}, Project: {self.project_name}, Priority: {self.priority}, Due Date: {self.due_date}, Status: {status}"

# Define a class to manage the Maintenance Scheduling System
class MaintenanceScheduler:
    def __init__(self):
        """Initialize the scheduler with an empty list of tasks."""
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """
        Add a new maintenance task to the scheduler.

        :param task: Instance of MaintenanceTask to add.
        """
        self.tasks.append(task)

    def list_tasks(self, filter_priority: str = None) -> List[str]:
        """
        List all tasks, optionally filtering by priority.

        :param filter_priority: If provided, filter tasks by priority ('High', 'Medium', 'Low').
        :return: A list of string representations of tasks.
        """
        filtered_tasks = self.tasks
        if filter_priority:
            filtered_tasks = [task for task in self.tasks if task.priority == filter_priority]
        
        return [str(task) for task in filtered_tasks]

    def mark_task_completed(self, task_id: int) -> bool:
        """
        Mark a specific task as completed.

        :param task_id: ID of the task to mark as completed.
        :return: True if the task was found and marked, False otherwise.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete_task()
                return True
        return False

    def remove_completed_tasks(self):
        """Remove all tasks that have been marked as completed."""
        self.tasks = [task for task in self.tasks if not task.is_completed]

    def upcoming_tasks(self) -> List[str]:
        """
        List tasks that are due within the next 7 days.

        :return: A list of string representations of upcoming tasks.
        """
        today = datetime.date.today()
        upcoming = [
            task for task in self.tasks 
            if not task.is_completed and (task.due_date - today).days <= 7
        ]
        return [str(task) for task in upcoming]

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Safety and efficiency standards can be incorporated in task descriptions or priority settings
    task1 = MaintenanceTask(1, "Project Alpha", "Inspect safety equipment", "High", datetime.date(2023, 10, 20))
    task2 = MaintenanceTask(2, "Project Beta", "Upgrade power supply", "Medium", datetime.date(2023, 10, 22))
    task3 = MaintenanceTask(3, "Project Gamma", "Review efficiency protocols", "Low", datetime.date(2023, 10, 25))

    # Add tasks to the scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # List all tasks
    print("All Tasks:")
    print("\n".join(scheduler.list_tasks()))

    # List high-priority tasks
    print("\nHigh Priority Tasks:")
    print("\n".join(scheduler.list_tasks(filter_priority="High")))

    # Mark a task as completed
    scheduler.mark_task_completed(1)

    # List upcoming tasks
    print("\nUpcoming Tasks:")
    print("\n".join(scheduler.upcoming_tasks()))

    # Remove completed tasks and list remaining tasks
    scheduler.remove_completed_tasks()
    print("\nRemaining Tasks After Removing Completed:")
    print("\n".join(scheduler.list_tasks()))
```
