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
import datetime
from enum import Enum
from typing import List, Dict, Optional

class MaintenanceTaskType(Enum):
    DAILY_CHECK = "Daily System Check"
    WEEKLY_CLEANING = "Weekly Cleaning"
    MONTHLY_INSPECTION = "Monthly Inspection"
    QUARTERLY_SERVICE = "Quarterly Service"
    ANNUAL_OVERHAUL = "Annual Overhaul"

class MaintenanceTask:
    def __init__(self, task_type: MaintenanceTaskType, description: str, frequency_days: int):
        self.task_type = task_type
        self.description = description
        self.frequency_days = frequency_days
        self.last_performed: Optional[datetime.date] = None

    def is_due(self) -> bool:
        if not self.last_performed:
            return True
        days_since_last = (datetime.date.today() - self.last_performed).days
        return days_since_last >= self.frequency_days

    def perform(self) -> None:
        self.last_performed = datetime.date.today()
        print(f"Performed {self.task_type.value}: {self.description}")

class Chiller:
    def __init__(self, model: str, serial_number: str, installation_date: datetime.date):
        self.model = model
        self.serial_number = serial_number
        self.installation_date = installation_date
        self.maintenance_tasks: List[MaintenanceTask] = []
        self.service_history: List[Dict] = []

    def add_maintenance_task(self, task: MaintenanceTask) -> None:
        self.maintenance_tasks.append(task)

    def check_maintenance(self) -> List[MaintenanceTask]:
        due_tasks = [task for task in self.maintenance_tasks if task.is_due()]
        return due_tasks

    def perform_maintenance(self, task_type: MaintenanceTaskType) -> bool:
        for task in self.maintenance_tasks:
            if task.task_type == task_type and task.is_due():
                task.perform()
                self.service_history.append({
                    "date": datetime.date.today(),
                    "task": task.task_type.value,
                    "description": task.description
                })
                return True
        return False

    def get_service_history(self) -> List[Dict]:
        return self.service_history

def setup_default_maintenance_schedule(chiller: Chiller) -> None:
    chiller.add_maintenance_task(MaintenanceTask(
        MaintenanceTaskType.DAILY_CHECK,
        "Check pressure, temperature, and fluid levels",
        1
    ))
    chiller.add_maintenance_task(MaintenanceTask(
        MaintenanceTaskType.WEEKLY_CLEANING,
        "Clean condenser tubes and check for leaks",
        7
    ))
    chiller.add_maintenance_task(MaintenanceTask(
        MaintenanceTaskType.MONTHLY_INSPECTION,
        "Inspect electrical connections and refrigerant levels",
        30
    ))
    chiller.add_maintenance_task(MaintenanceTask(
        MaintenanceTaskType.QUARTERLY_SERVICE,
        "Lubricate moving parts and check compressor",
        90
    ))
    chiller.add_maintenance_task(MaintenanceTask(
        MaintenanceTaskType.ANNUAL_OVERHAUL,
        "Complete system overhaul and performance test",
        365
    ))

def main():
    # Example usage
    chiller = Chiller(
        model="YVAA",
        serial_number="YC123456",
        installation_date=datetime.date(2020, 1, 15)
    )
    
    setup_default_maintenance_schedule(chiller)
    
    # Check for due maintenance
    due_tasks = chiller.check_maintenance()
    print(f"Due tasks: {[task.task_type.value for task in due_tasks]}")
    
    # Perform a specific maintenance task
    chiller.perform_maintenance(MaintenanceTaskType.DAILY_CHECK)
    
    # View service history
    print("Service History:")
    for entry in chiller.get_service_history():
        print(f"{entry['date']}: {entry['task']} - {entry['description']}")

if __name__ == "__main__":
    main()
```
