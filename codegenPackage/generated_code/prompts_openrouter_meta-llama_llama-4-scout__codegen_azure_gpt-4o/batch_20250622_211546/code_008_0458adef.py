"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Develop a maintenance schedule for a tube expansion drive, including routine checks and replacement of worn-out parts.
Generated: DETERMINISTIC_0458adefe3a71f4c
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class MaintenanceSchedule:
    """
    A class to manage the maintenance schedule for a tube expansion drive.
    Includes routine checks and replacement of worn-out parts.
    """

    def __init__(self):
        """
        Initializes the maintenance schedule with default tasks and intervals.
        """
        self.schedule = [
            {"task": "Inspect drive belts", "interval_days": 30},
            {"task": "Lubricate moving parts", "interval_days": 60},
            {"task": "Check hydraulic fluid levels", "interval_days": 90},
            {"task": "Replace worn-out drive belts", "interval_days": 180},
            {"task": "Inspect electrical connections", "interval_days": 120},
            {"task": "Replace worn-out bearings", "interval_days": 365},
        ]
        self.last_maintenance = {task["task"]: None for task in self.schedule}

    def perform_maintenance(self, task_name):
        """
        Marks a maintenance task as completed and updates the last maintenance date.

        Args:
            task_name (str): The name of the maintenance task to perform.

        Raises:
            ValueError: If the task name is not found in the schedule.
        """
        if task_name not in self.last_maintenance:
            raise ValueError(f"Task '{task_name}' not found in the maintenance schedule.")
        
        self.last_maintenance[task_name] = datetime.date.today()
        print(f"Maintenance task '{task_name}' completed on {datetime.date.today()}.")

    def get_due_tasks(self):
        """
        Retrieves a list of maintenance tasks that are due based on their intervals.

        Returns:
            list: A list of task names that are due for maintenance.
        """
        due_tasks = []
        today = datetime.date.today()

        for task in self.schedule:
            task_name = task["task"]
            interval_days = task["interval_days"]
            last_date = self.last_maintenance[task_name]

            if last_date is None or (today - last_date).days >= interval_days:
                due_tasks.append(task_name)

        return due_tasks

    def display_schedule(self):
        """
        Displays the maintenance schedule and the last maintenance dates.
        """
        print("Maintenance Schedule:")
        for task in self.schedule:
            task_name = task["task"]
            interval_days = task["interval_days"]
            last_date = self.last_maintenance[task_name]
            last_date_str = last_date.strftime("%Y-%m-%d") if last_date else "Never"
            print(f"- {task_name} (Interval: {interval_days} days, Last performed: {last_date_str})")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the maintenance schedule
        schedule = MaintenanceSchedule()

        # Display the current schedule
        schedule.display_schedule()

        # Perform a maintenance task
        schedule.perform_maintenance("Inspect drive belts")

        # Check for due tasks
        due_tasks = schedule.get_due_tasks()
        if due_tasks:
            print("\nTasks due for maintenance:")
            for task in due_tasks:
                print(f"- {task}")
        else:
            print("\nNo tasks are currently due for maintenance.")

        # Display the updated schedule
        print("\nUpdated Maintenance Schedule:")
        schedule.display_schedule()

    except Exception as e:
        print(f"An error occurred: {e}")
```
