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
# block_maintenance_scheduler.py

import datetime
import logging
from enum import Enum
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceType(str, Enum):
    """Enum for BlocPrest services"""
    CLEANING = "cleaning"
    REPAIRS = "repairs"
    TECHNICAL_SUPPORT = "technical_support"

class MaintenanceTask:
    """Represents a maintenance task"""
    def __init__(self, service_type: ServiceType, block_name: str, scheduled_date: datetime.date):
        self.service_type = service_type
        self.block_name = block_name
        self.scheduled_date = scheduled_date

    def __str__(self):
        return f"{self.service_type.value.capitalize()} for {self.block_name} on {self.scheduled_date}"

class MaintenanceScheduler:
    """Schedules maintenance tasks for residential blocks"""
    def __init__(self):
        self.tasks = []

    def schedule_task(self, service_type: ServiceType, block_name: str, scheduled_date: datetime.date):
        """Schedules a maintenance task"""
        task = MaintenanceTask(service_type, block_name, scheduled_date)
        self.tasks.append(task)
        logging.info(f"Scheduled task: {task}")

    def get_scheduled_tasks(self) -> List[MaintenanceTask]:
        """Returns a list of scheduled tasks"""
        return self.tasks

    def get_tasks_by_block(self, block_name: str) -> List[MaintenanceTask]:
        """Returns a list of tasks for a specific block"""
        return [task for task in self.tasks if task.block_name == block_name]

def main():
    try:
        scheduler = MaintenanceScheduler()

        # Schedule tasks
        scheduler.schedule_task(ServiceType.CLEANING, "Block A", datetime.date(2024, 9, 20))
        scheduler.schedule_task(ServiceType.REPAIRS, "Block B", datetime.date(2024, 9, 22))
        scheduler.schedule_task(ServiceType.TECHNICAL_SUPPORT, "Block A", datetime.date(2024, 9, 25))

        # Get all scheduled tasks
        print("All Scheduled Tasks:")
        for task in scheduler.get_scheduled_tasks():
            print(task)

        # Get tasks for a specific block
        print("\nTasks for Block A:")
        for task in scheduler.get_tasks_by_block("Block A"):
            print(task)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
