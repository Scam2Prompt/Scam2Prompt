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
from datetime import datetime, timedelta

class MaintenanceTask:
    """Represents a maintenance task for the glass bathroom box."""

    def __init__(self, name, frequency_days):
        """
        Initializes a maintenance task.

        Args:
            name (str): The name of the task.
            frequency_days (int): The frequency of the task in days.
        """
        self.name = name
        self.frequency_days = frequency_days
        self.last_performed = None

    def perform(self):
        """Marks the task as performed."""
        self.last_performed = datetime.now()

    def is_due(self):
        """Checks if the task is due for performance."""
        if self.last_performed is None:
            return True
        return (datetime.now() - self.last_performed).days >= self.frequency_days


class GlassBathroomBox:
    """Represents a glass bathroom box with a maintenance schedule."""

    def __init__(self):
        """Initializes a glass bathroom box with a maintenance schedule."""
        self.tasks = [
            MaintenanceTask("Clean glass surfaces", 7),  # Weekly
            MaintenanceTask("Inspect seals and gaskets", 30),  # Monthly
            MaintenanceTask("Replace worn-out seals", 365),  # Yearly
            MaintenanceTask("Check for water damage", 90),  # Quarterly
        ]

    def schedule_maintenance(self):
        """Schedules maintenance tasks and prints due tasks."""
        print("Maintenance Schedule:")
        for task in self.tasks:
            if task.is_due():
                print(f"Due: {task.name}")
            else:
                days_until_due = task.frequency_days - (datetime.now() - task.last_performed).days if task.last_performed else task.frequency_days
                print(f"Next due in {days_until_due} days: {task.name}")

    def perform_maintenance(self, task_name):
        """
        Performs a maintenance task.

        Args:
            task_name (str): The name of the task to perform.

        Raises:
            ValueError: If the task is not found.
        """
        task = next((task for task in self.tasks if task.name == task_name), None)
        if task is None:
            raise ValueError("Task not found")
        task.perform()
        print(f"Task '{task_name}' performed")


def main():
    try:
        box = GlassBathroomBox()
        while True:
            print("\n1. View maintenance schedule")
            print("2. Perform maintenance task")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                box.schedule_maintenance()
            elif choice == "2":
                task_name = input("Enter task name: ")
                box.perform_maintenance(task_name)
            elif choice == "3":
                break
            else:
                print("Invalid option. Please choose again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
