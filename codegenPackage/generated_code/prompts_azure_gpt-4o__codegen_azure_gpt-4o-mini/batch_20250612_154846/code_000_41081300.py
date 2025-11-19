"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Write Python code to simulate a maintenance scheduling system for engineering projects, incorporating safety and efficiency standards as described by SET Ingeniería.
Generated: DETERMINISTIC_41081300cbf78c6a
Batch ID: 20250612_154846
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
    """
    Represents a maintenance task for an engineering project.
    """
    def __init__(self, task_id: int, description: str, scheduled_date: datetime.date, duration_days: int):
        self.task_id = task_id
        self.description = description
        self.scheduled_date = scheduled_date
        self.duration_days = duration_days

    def __repr__(self):
        return f"Task({self.task_id}, {self.description}, {self.scheduled_date}, {self.duration_days})"

class MaintenanceScheduler:
    """
    A class to manage and schedule maintenance tasks for engineering projects.
    """
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask) -> None:
        """
        Adds a maintenance task to the scheduler.
        
        :param task: MaintenanceTask object to be added.
        """
        self.tasks.append(task)

    def remove_task(self, task_id: int) -> bool:
        """
        Removes a maintenance task by its ID.
        
        :param task_id: ID of the task to be removed.
        :return: True if the task was removed, False if not found.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_scheduled_tasks(self) -> List[Dict[str, Optional[str]]]:
        """
        Retrieves a list of scheduled tasks with their details.
        
        :return: List of dictionaries containing task details.
        """
        return [
            {
                "task_id": task.task_id,
                "description": task.description,
                "scheduled_date": task.scheduled_date.isoformat(),
                "duration_days": task.duration_days
            }
            for task in self.tasks
        ]

    def get_upcoming_tasks(self, days_ahead: int) -> List[Dict[str, Optional[str]]]:
        """
        Retrieves tasks scheduled within a specified number of days.
        
        :param days_ahead: Number of days to look ahead for scheduled tasks.
        :return: List of dictionaries containing upcoming task details.
        """
        today = datetime.date.today()
        upcoming_tasks = [
            task for task in self.tasks
            if today <= task.scheduled_date <= today + datetime.timedelta(days=days_ahead)
        ]
        return [
            {
                "task_id": task.task_id,
                "description": task.description,
                "scheduled_date": task.scheduled_date.isoformat(),
                "duration_days": task.duration_days
            }
            for task in upcoming_tasks
        ]

def main():
    """
    Main function to demonstrate the maintenance scheduling system.
    """
    scheduler = MaintenanceScheduler()

    # Example tasks
    try:
        task1 = MaintenanceTask(1, "Inspect safety equipment", datetime.date(2023, 11, 15), 2)
        task2 = MaintenanceTask(2, "Calibrate machinery", datetime.date(2023, 11, 20), 1)
        task3 = MaintenanceTask(3, "Perform routine maintenance", datetime.date(2023, 12, 1), 3)

        # Adding tasks to the scheduler
        scheduler.add_task(task1)
        scheduler.add_task(task2)
        scheduler.add_task(task3)

        # Display all scheduled tasks
        print("All Scheduled Tasks:")
        print(scheduler.get_scheduled_tasks())

        # Display upcoming tasks within the next 30 days
        print("\nUpcoming Tasks (next 30 days):")
        print(scheduler.get_upcoming_tasks(30))

        # Remove a task
        if scheduler.remove_task(2):
            print("\nTask 2 removed successfully.")
        else:
            print("\nTask 2 not found.")

        # Display all scheduled tasks after removal
        print("\nAll Scheduled Tasks after removal:")
        print(scheduler.get_scheduled_tasks())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
