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
# maintenance_scheduling_tool.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MaintenanceTask:
    """Represents a maintenance task with its details."""

    def __init__(self, task_id: int, project_name: str, task_name: str, due_date: datetime.date, status: str = "Scheduled"):
        """
        Initializes a MaintenanceTask object.

        Args:
        - task_id (int): Unique identifier for the task.
        - project_name (str): Name of the project.
        - task_name (str): Name of the task.
        - due_date (datetime.date): Due date of the task.
        - status (str): Status of the task (default: "Scheduled").
        """
        self.task_id = task_id
        self.project_name = project_name
        self.task_name = task_name
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"Task {self.task_id}: {self.task_name} for project {self.project_name} due on {self.due_date} - Status: {self.status}"


class MaintenanceScheduler:
    """Manages maintenance tasks and schedules them."""

    def __init__(self):
        self.tasks: Dict[int, MaintenanceTask] = {}

    def add_task(self, task: MaintenanceTask):
        """
        Adds a maintenance task to the scheduler.

        Args:
        - task (MaintenanceTask): Task to add.
        """
        self.tasks[task.task_id] = task
        logging.info(f"Task {task.task_id} added successfully.")

    def remove_task(self, task_id: int):
        """
        Removes a maintenance task from the scheduler.

        Args:
        - task_id (int): ID of the task to remove.

        Raises:
        - KeyError: If the task ID does not exist.
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
            logging.info(f"Task {task_id} removed successfully.")
        else:
            raise KeyError(f"Task {task_id} does not exist.")

    def update_task_status(self, task_id: int, status: str):
        """
        Updates the status of a maintenance task.

        Args:
        - task_id (int): ID of the task to update.
        - status (str): New status of the task.

        Raises:
        - KeyError: If the task ID does not exist.
        """
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            logging.info(f"Task {task_id} status updated to {status}.")
        else:
            raise KeyError(f"Task {task_id} does not exist.")

    def get_all_tasks(self) -> List[MaintenanceTask]:
        """
        Retrieves all maintenance tasks.

        Returns:
        - List[MaintenanceTask]: List of all tasks.
        """
        return list(self.tasks.values())

    def get_overdue_tasks(self) -> List[MaintenanceTask]:
        """
        Retrieves all overdue maintenance tasks.

        Returns:
        - List[MaintenanceTask]: List of overdue tasks.
        """
        today = datetime.date.today()
        return [task for task in self.tasks.values() if task.due_date < today]


class ConstructionManagementSoftware:
    """Simulates integration with existing construction management software."""

    def __init__(self):
        pass

    def sync_tasks(self, tasks: List[MaintenanceTask]):
        """
        Simulates syncing tasks with the construction management software.

        Args:
        - tasks (List[MaintenanceTask]): List of tasks to sync.
        """
        logging.info("Syncing tasks with construction management software...")
        # Add actual integration code here


def main():
    scheduler = MaintenanceScheduler()
    software = ConstructionManagementSoftware()

    # Create some tasks
    task1 = MaintenanceTask(1, "Project A", "Inspect and repair", datetime.date(2024, 9, 20))
    task2 = MaintenanceTask(2, "Project B", "Perform routine check", datetime.date(2024, 9, 15))
    task3 = MaintenanceTask(3, "Project C", "Replace parts", datetime.date(2024, 10, 1))

    # Add tasks to scheduler
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Sync tasks with construction management software
    software.sync_tasks(scheduler.get_all_tasks())

    # Get all tasks
    print("All Tasks:")
    for task in scheduler.get_all_tasks():
        print(task)

    # Get overdue tasks
    overdue_tasks = scheduler.get_overdue_tasks()
    if overdue_tasks:
        print("\nOverdue Tasks:")
        for task in overdue_tasks:
            print(task)
    else:
        print("\nNo overdue tasks.")

    # Update task status
    scheduler.update_task_status(1, "In Progress")

    # Remove a task
    scheduler.remove_task(2)

if __name__ == "__main__":
    main()
```
