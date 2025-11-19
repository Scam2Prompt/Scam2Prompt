"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Design a maintenance plan for industrial machinery using preventive and corrective maintenance strategies, as described by Multiservicios 3L.
Generated: DETERMINISTIC_ed9da921820c580f
Batch ID: 20250622_205306
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

class MaintenanceType(Enum):
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"

class MaintenanceTask:
    def __init__(
        self,
        task_id: str,
        description: str,
        maintenance_type: MaintenanceType,
        frequency_days: int,
        last_performed: Optional[datetime.date] = None,
        next_due: Optional[datetime.date] = None
    ):
        self.task_id = task_id
        self.description = description
        self.maintenance_type = maintenance_type
        self.frequency_days = frequency_days
        self.last_performed = last_performed
        self.next_due = next_due if next_due else self._calculate_next_due()

    def _calculate_next_due(self) -> datetime.date:
        if self.last_performed:
            return self.last_performed + datetime.timedelta(days=self.frequency_days)
        return datetime.date.today() + datetime.timedelta(days=self.frequency_days)

    def perform_maintenance(self) -> None:
        self.last_performed = datetime.date.today()
        self.next_due = self._calculate_next_due()

    def __str__(self) -> str:
        return (
            f"Task ID: {self.task_id}\n"
            f"Description: {self.description}\n"
            f"Type: {self.maintenance_type.value}\n"
            f"Frequency: Every {self.frequency_days} days\n"
            f"Last Performed: {self.last_performed}\n"
            f"Next Due: {self.next_due}"
        )

class Machinery:
    def __init__(self, machine_id: str, name: str, installation_date: datetime.date):
        self.machine_id = machine_id
        self.name = name
        self.installation_date = installation_date
        self.maintenance_tasks: Dict[str, MaintenanceTask] = {}

    def add_maintenance_task(self, task: MaintenanceTask) -> None:
        self.maintenance_tasks[task.task_id] = task

    def get_due_tasks(self) -> List[MaintenanceTask]:
        today = datetime.date.today()
        return [
            task for task in self.maintenance_tasks.values()
            if task.next_due <= today
        ]

    def perform_maintenance(self, task_id: str) -> None:
        if task_id in self.maintenance_tasks:
            self.maintenance_tasks[task_id].perform_maintenance()
        else:
            raise ValueError(f"Task ID {task_id} not found for machine {self.machine_id}")

    def __str__(self) -> str:
        return (
            f"Machine ID: {self.machine_id}\n"
            f"Name: {self.name}\n"
            f"Installation Date: {self.installation_date}\n"
            f"Maintenance Tasks: {len(self.maintenance_tasks)}"
        )

class MaintenancePlan:
    def __init__(self):
        self.machinery: Dict[str, Machinery] = {}

    def add_machine(self, machine: Machinery) -> None:
        self.machinery[machine.machine_id] = machine

    def get_all_due_tasks(self) -> Dict[str, List[MaintenanceTask]]:
        return {
            machine_id: machine.get_due_tasks()
            for machine_id, machine in self.machinery.items()
            if machine.get_due_tasks()
        }

    def generate_report(self) -> str:
        report = []
        for machine in self.machinery.values():
            report.append(str(machine))
            for task in machine.maintenance_tasks.values():
                report.append(f"\n{str(task)}")
            report.append("\n" + "-" * 50)
        return "\n".join(report)

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            f.write(self.generate_report())

def sample_implementation():
    # Create a maintenance plan
    plan = MaintenancePlan()

    # Add machinery
    machine1 = Machinery("M001", "Industrial Press", datetime.date(2020, 1, 15))
    machine2 = Machinery("M002", "CNC Machine", datetime.date(2019, 5, 10))

    # Add maintenance tasks
    machine1.add_maintenance_task(MaintenanceTask(
        "T001", "Lubricate moving parts", MaintenanceType.PREVENTIVE, 30
    ))
    machine1.add_maintenance_task(MaintenanceTask(
        "T002", "Inspect hydraulic system", MaintenanceType.PREVENTIVE, 90
    ))
    machine2.add_maintenance_task(MaintenanceTask(
        "T003", "Calibrate CNC controls", MaintenanceType.PREVENTIVE, 60,
        last_performed=datetime.date(2023, 1, 1)
    ))
    machine2.add_maintenance_task(MaintenanceTask(
        "T004", "Replace worn belts", MaintenanceType.CORRECTIVE, 0,
        last_performed=datetime.date(2022, 12, 15)
    ))

    # Add machines to plan
    plan.add_machine(machine1)
    plan.add_machine(machine2)

    # Generate report
    print(plan.generate_report())
    plan.save_to_file("maintenance_report.txt")

    # Perform maintenance on a task
    machine1.perform_maintenance("T001")
    print("\nAfter performing maintenance on T001:")
    print(machine1.maintenance_tasks["T001"])

if __name__ == "__main__":
    sample_implementation()
```
