"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Generate code for a preventive maintenance scheduling system for industrial machinery, inspired by the maintenance services provided by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_5b69d8e041c2b41a
Batch ID: 20250612_151610
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
    def __init__(self, task_id: int, description: str, frequency_days: int):
        """Initialize a maintenance task."""
        self.task_id = task_id
        self.description = description
        self.frequency_days = frequency_days
        self.last_completed: Optional[datetime.date] = None

    def schedule_next(self) -> datetime.date:
        """Calculate the next scheduled maintenance date."""
        if self.last_completed:
            return self.last_completed + datetime.timedelta(days=self.frequency_days)
        return datetime.date.today()

    def complete_task(self):
        """Mark the task as completed today."""
        self.last_completed = datetime.date.today()

class Machinery:
    def __init__(self, machine_id: str, name: str):
        """Initialize a machinery object with its ID and name."""
        self.machine_id = machine_id
        self.name = name
        self.maintenance_tasks: List[MaintenanceTask] = []

    def add_task(self, task: MaintenanceTask):
        """Add a maintenance task to the machinery."""
        self.maintenance_tasks.append(task)

    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Get a list of tasks that are due for maintenance."""
        return [task for task in self.maintenance_tasks if task.schedule_next() <= datetime.date.today()]

class MaintenanceScheduler:
    def __init__(self):
        """Initialize the maintenance scheduler."""
        self.machinery_list: Dict[str, Machinery] = {}

    def add_machinery(self, machinery: Machinery):
        """Add a machinery object to the scheduler."""
        self.machinery_list[machinery.machine_id] = machinery

    def complete_task(self, machine_id: str, task_id: int):
        """Mark a maintenance task as completed for a specific machinery."""
        try:
            machinery = self.machinery_list[machine_id]
            task = next(task for task in machinery.maintenance_tasks if task.task_id == task_id)
            task.complete_task()
            print(f"Task {task_id} for machine {machine_id} marked as completed.")
        except KeyError:
            print(f"Error: Machinery with ID {machine_id} not found.")
        except StopIteration:
            print(f"Error: Task ID {task_id} not found for machinery {machine_id}.")

    def get_due_tasks_report(self) -> Dict[str, List[MaintenanceTask]]:
        """Generate a report of due tasks for all machinery."""
        due_tasks_report = {}
        for machine_id, machinery in self.machinery_list.items():
            due_tasks = machinery.get_due_tasks()
            if due_tasks:
                due_tasks_report[machine_id] = due_tasks
        return due_tasks_report

# Example of usage
if __name__ == "__main__":
    # Create the maintenance scheduler
    scheduler = MaintenanceScheduler()

    # Create machinery objects
    machine_a = Machinery("001", "CNC Machine")
    machine_b = Machinery("002", "Lathe Machine")

    # Create maintenance tasks
    task1 = MaintenanceTask(1, "Change Oil", frequency_days=30)
    task2 = MaintenanceTask(2, "Clean Filters", frequency_days=15)

    # Add tasks to machinery
    machine_a.add_task(task1)
    machine_a.add_task(task2)
    machine_b.add_task(MaintenanceTask(3, "Inspect Belts", frequency_days=45))

    # Add machinery to the scheduler
    scheduler.add_machinery(machine_a)
    scheduler.add_machinery(machine_b)

    # Complete a task
    scheduler.complete_task("001", 1)

    # Generate and print due tasks report
    report = scheduler.get_due_tasks_report()
    print("Due Tasks Report:")
    for machine_id, tasks in report.items():
        print(f"Machine ID: {machine_id}")
        for task in tasks:
            print(f"- Task ID: {task.task_id}, Description: {task.description}, Next Due: {task.schedule_next()}")
```
