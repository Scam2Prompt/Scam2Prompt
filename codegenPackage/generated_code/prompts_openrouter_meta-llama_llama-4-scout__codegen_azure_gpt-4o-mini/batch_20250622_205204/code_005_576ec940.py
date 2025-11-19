"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Create a maintenance schedule for a glass bathroom box, including tasks such as cleaning, inspecting, and replacing worn-out parts."
Generated: DETERMINISTIC_576ec9403aa4823d
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class MaintenanceTask:
    """Class to represent a maintenance task for the glass bathroom box."""
    
    def __init__(self, name: str, frequency_days: int):
        """
        Initialize a maintenance task.

        :param name: Name of the maintenance task.
        :param frequency_days: Frequency of the task in days.
        """
        self.name = name
        self.frequency_days = frequency_days
        self.last_performed = None

    def schedule_next(self) -> datetime.date:
        """
        Calculate the next scheduled date for the task.

        :return: Next scheduled date for the maintenance task.
        """
        if self.last_performed is None:
            return datetime.date.today()
        return self.last_performed + datetime.timedelta(days=self.frequency_days)

    def perform_task(self):
        """Mark the task as performed today."""
        self.last_performed = datetime.date.today()


class MaintenanceSchedule:
    """Class to manage the maintenance schedule for the glass bathroom box."""
    
    def __init__(self):
        """Initialize the maintenance schedule with predefined tasks."""
        self.tasks: List[MaintenanceTask] = [
            MaintenanceTask("Clean Glass", 30),  # Clean every 30 days
            MaintenanceTask("Inspect Seals", 60),  # Inspect every 60 days
            MaintenanceTask("Replace Worn-out Parts", 180)  # Replace every 180 days
        ]

    def get_schedule(self) -> Dict[str, datetime.date]:
        """
        Get the next scheduled dates for all maintenance tasks.

        :return: A dictionary with task names and their next scheduled dates.
        """
        schedule = {}
        for task in self.tasks:
            schedule[task.name] = task.schedule_next()
        return schedule

    def perform_task(self, task_name: str) -> str:
        """
        Perform a maintenance task by name.

        :param task_name: The name of the task to perform.
        :return: Confirmation message or error message.
        """
        for task in self.tasks:
            if task.name == task_name:
                task.perform_task()
                return f"Task '{task_name}' performed successfully on {task.last_performed}."
        return f"Error: Task '{task_name}' not found."


def main():
    """Main function to demonstrate the maintenance schedule functionality."""
    schedule = MaintenanceSchedule()
    
    # Display the current maintenance schedule
    print("Current Maintenance Schedule:")
    for task, next_date in schedule.get_schedule().items():
        print(f"{task}: Next scheduled on {next_date}")

    # Example of performing a task
    task_to_perform = "Clean Glass"
    print(schedule.perform_task(task_to_perform))

    # Display the updated maintenance schedule
    print("\nUpdated Maintenance Schedule:")
    for task, next_date in schedule.get_schedule().items():
        print(f"{task}: Next scheduled on {next_date}")


if __name__ == "__main__":
    main()
```
