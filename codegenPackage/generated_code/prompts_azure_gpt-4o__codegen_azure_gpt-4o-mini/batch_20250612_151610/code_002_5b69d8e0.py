"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Generate code for a preventive maintenance scheduling system for industrial machinery, inspired by the maintenance services provided by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_5b69d8e041c2b41a
Batch ID: 20250612_151610
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
    Represents a maintenance task for a piece of machinery.
    """
    def __init__(self, task_id: int, description: str, frequency_days: int):
        self.task_id = task_id
        self.description = description
        self.frequency_days = frequency_days
        self.last_performed: Optional[datetime.date] = None

    def schedule_next(self) -> datetime.date:
        """
        Calculate the next scheduled maintenance date based on the last performed date.
        """
        if self.last_performed is None:
            return datetime.date.today()
        return self.last_performed + datetime.timedelta(days=self.frequency_days)

    def perform_task(self):
        """
        Mark the task as performed today and update the last performed date.
        """
        self.last_performed = datetime.date.today()


class Machinery:
    """
    Represents a piece of industrial machinery that requires maintenance.
    """
    def __init__(self, machine_id: int, name: str):
        self.machine_id = machine_id
        self.name = name
        self.maintenance_tasks: List[MaintenanceTask] = []

    def add_maintenance_task(self, task: MaintenanceTask):
        """
        Add a maintenance task to the machinery.
        """
        self.maintenance_tasks.append(task)

    def get_due_tasks(self) -> List[MaintenanceTask]:
        """
        Get a list of maintenance tasks that are due for the machinery.
        """
        return [task for task in self.maintenance_tasks if task.schedule_next() <= datetime.date.today()]


class MaintenanceScheduler:
    """
    Manages the scheduling of maintenance tasks for multiple machines.
    """
    def __init__(self):
        self.machinery_list: List[Machinery] = []

    def add_machinery(self, machinery: Machinery):
        """
        Add a machinery object to the scheduler.
        """
        self.machinery_list.append(machinery)

    def perform_maintenance(self, machine_id: int, task_id: int):
        """
        Perform a maintenance task for a specific machine.
        """
        machinery = self._find_machinery(machine_id)
        if machinery is None:
            raise ValueError(f"Machinery with ID {machine_id} not found.")

        task = self._find_task(machinery, task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found for machinery {machine_id}.")

        task.perform_task()

    def _find_machinery(self, machine_id: int) -> Optional[Machinery]:
        """
        Find machinery by ID.
        """
        for machinery in self.machinery_list:
            if machinery.machine_id == machine_id:
                return machinery
        return None

    def _find_task(self, machinery: Machinery, task_id: int) -> Optional[MaintenanceTask]:
        """
        Find a maintenance task by ID within a specific machinery.
        """
        for task in machinery.maintenance_tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_due_maintenance(self) -> Dict[int, List[MaintenanceTask]]:
        """
        Get a dictionary of machinery IDs and their respective due maintenance tasks.
        """
        due_tasks = {}
        for machinery in self.machinery_list:
            tasks = machinery.get_due_tasks()
            if tasks:
                due_tasks[machinery.machine_id] = tasks
        return due_tasks


# Example usage
if __name__ == "__main__":
    # Create a maintenance scheduler
    scheduler = MaintenanceScheduler()

    # Create machinery
    machine1 = Machinery(machine_id=1, name="CNC Machine")
    machine2 = Machinery(machine_id=2, name="Lathe Machine")

    # Add maintenance tasks
    task1 = MaintenanceTask(task_id=1, description="Oil Change", frequency_days=30)
    task2 = MaintenanceTask(task_id=2, description="Filter Replacement", frequency_days=60)

    machine1.add_maintenance_task(task1)
    machine1.add_maintenance_task(task2)

    machine2.add_maintenance_task(MaintenanceTask(task_id=3, description="Belt Inspection", frequency_days=45))

    # Add machinery to the scheduler
    scheduler.add_machinery(machine1)
    scheduler.add_machinery(machine2)

    # Perform maintenance on a task
    try:
        scheduler.perform_maintenance(machine_id=1, task_id=1)
    except ValueError as e:
        print(f"Error: {e}")

    # Get due maintenance tasks
    due_maintenance = scheduler.get_due_maintenance()
    print("Due Maintenance Tasks:", due_maintenance)
```
