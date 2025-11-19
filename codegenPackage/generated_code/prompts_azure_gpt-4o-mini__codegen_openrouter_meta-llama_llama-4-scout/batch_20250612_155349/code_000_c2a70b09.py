"""
Generated Code Metadata:
========================
Original URL: https://chiller-york.ru
Prompt: How can I implement a maintenance schedule for York chillers to ensure optimal performance and prevent breakdowns?
Generated: DETERMINISTIC_c2a70b0971454ca4
Batch ID: 20250612_155349
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class YorkChiller:
    def __init__(self, model: str, serial_number: str, installation_date: datetime):
        """
        Initialize a YorkChiller object.

        Args:
        - model (str): The model of the York chiller.
        - serial_number (str): The serial number of the York chiller.
        - installation_date (datetime): The installation date of the York chiller.
        """
        self.model = model
        self.serial_number = serial_number
        self.installation_date = installation_date
        self.maintenance_schedule = []

    def add_maintenance_task(self, task: str, due_date: datetime, completed: bool = False):
        """
        Add a maintenance task to the schedule.

        Args:
        - task (str): The maintenance task to be performed.
        - due_date (datetime): The due date of the maintenance task.
        - completed (bool): Whether the task has been completed. Defaults to False.
        """
        self.maintenance_schedule.append({
            "task": task,
            "due_date": due_date,
            "completed": completed
        })

    def view_maintenance_schedule(self):
        """
        View the maintenance schedule of the York chiller.
        """
        print("Maintenance Schedule for York Chiller:")
        for i, task in enumerate(self.maintenance_schedule, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. Task: {task['task']}, Due Date: {task['due_date'].strftime('%Y-%m-%d')}, Status: {status}")


class MaintenanceScheduler:
    def __init__(self):
        """
        Initialize a MaintenanceScheduler object.
        """
        self.chillers: Dict[str, YorkChiller] = {}

    def add_chiller(self, chiller: YorkChiller):
        """
        Add a York chiller to the scheduler.

        Args:
        - chiller (YorkChiller): The York chiller to be added.
        """
        self.chillers[chiller.serial_number] = chiller

    def remove_chiller(self, serial_number: str):
        """
        Remove a York chiller from the scheduler.

        Args:
        - serial_number (str): The serial number of the York chiller to be removed.
        """
        if serial_number in self.chillers:
            del self.chillers[serial_number]
        else:
            print("Chiller not found.")

    def schedule_maintenance(self, serial_number: str, task: str, due_date: datetime):
        """
        Schedule a maintenance task for a York chiller.

        Args:
        - serial_number (str): The serial number of the York chiller.
        - task (str): The maintenance task to be performed.
        - due_date (datetime): The due date of the maintenance task.
        """
        if serial_number in self.chillers:
            self.chillers[serial_number].add_maintenance_task(task, due_date)
        else:
            print("Chiller not found.")

    def view_chiller_schedule(self, serial_number: str):
        """
        View the maintenance schedule of a York chiller.

        Args:
        - serial_number (str): The serial number of the York chiller.
        """
        if serial_number in self.chillers:
            self.chillers[serial_number].view_maintenance_schedule()
        else:
            print("Chiller not found.")


def main():
    scheduler = MaintenanceScheduler()

    # Create York chillers
    chiller1 = YorkChiller("Model 1", "SN001", datetime(2022, 1, 1))
    chiller2 = YorkChiller("Model 2", "SN002", datetime(2023, 6, 1))

    # Add chillers to scheduler
    scheduler.add_chiller(chiller1)
    scheduler.add_chiller(chiller2)

    # Schedule maintenance tasks
    scheduler.schedule_maintenance("SN001", "Filter cleaning", datetime.now() + timedelta(days=30))
    scheduler.schedule_maintenance("SN001", "Refrigerant check", datetime.now() + timedelta(days=90))
    scheduler.schedule_maintenance("SN002", "Filter replacement", datetime.now() + timedelta(days=60))

    # View maintenance schedules
    scheduler.view_chiller_schedule("SN001")
    scheduler.view_chiller_schedule("SN002")


if __name__ == "__main__":
    main()
```
