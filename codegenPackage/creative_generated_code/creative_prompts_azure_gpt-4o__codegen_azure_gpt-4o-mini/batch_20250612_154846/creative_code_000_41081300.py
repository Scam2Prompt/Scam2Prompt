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
from typing import List, Dict, Optional

class MaintenanceTask:
    """
    Class to represent a maintenance task for an engineering project.
    """
    def __init__(self, task_id: int, description: str, due_date: datetime.date, safety_standards: str):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.safety_standards = safety_standards
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __repr__(self):
        return f"Task(id={self.task_id}, description='{self.description}', due_date={self.due_date}, completed={self.completed})"


class MaintenanceScheduler:
    """
    Class to schedule and manage maintenance tasks.
    """
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """Add a new maintenance task to the scheduler."""
        self.tasks.append(task)

    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Retrieve all tasks that are due (i.e., due date is today or earlier)."""
        today = datetime.date.today()
        return [task for task in self.tasks if task.due_date <= today and not task.completed]

    def get_upcoming_tasks(self, days_ahead: int) -> List[MaintenanceTask]:
        """Retrieve tasks that are due within the next 'days_ahead' days."""
        upcoming_due_date = datetime.date.today() + datetime.timedelta(days=days_ahead)
        return [task for task in self.tasks if today < task.due_date <= upcoming_due_date and not task.completed]

    def mark_task_completed(self, task_id: int):
        """Mark a specific task as completed based on its ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_completed()
                return
        raise ValueError(f"Task with ID {task_id} not found.")

    def __repr__(self):
        return f"MaintenanceScheduler(tasks={self.tasks})"


def main():
    """Main function to demonstrate task scheduling."""
    scheduler = MaintenanceScheduler()

    # Example tasks
    try:
        scheduler.add_task(MaintenanceTask(1, "Inspect safety equipment", datetime.date(2023, 10, 1), "SET-001"))
        scheduler.add_task(MaintenanceTask(2, "Calibrate measuring instruments", datetime.date(2023, 10, 15), "SET-002"))
        scheduler.add_task(MaintenanceTask(3, "Check structural integrity", datetime.date(2023, 9, 30), "SET-001"))
        
        # Display due tasks
        due_tasks = scheduler.get_due_tasks()
        print("Due tasks:", due_tasks)

        # Mark a task as completed
        scheduler.mark_task_completed(1)
        print("After completing task 1:", scheduler)

        # Display upcoming tasks
        upcoming_tasks = scheduler.get_upcoming_tasks(30)
        print("Upcoming tasks:", upcoming_tasks)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
