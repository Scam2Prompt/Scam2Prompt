"""
Generated Code Metadata:
========================
Original URL: https://payeshnirooco.com
Prompt: Write a Python script to automate the maintenance scheduling for diesel and gas generators based on the guidelines provided by Payesh Niroo.
Generated: DETERMINISTIC_dd95f23cb69c7b41
Batch ID: 20250612_162325
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
from typing import Dict, List, Optional, Tuple


class GeneratorType(Enum):
    """Enum representing the type of generator."""
    DIESEL = "Diesel"
    GAS = "Gas"


class MaintenanceTask:
    """Class representing a maintenance task for a generator."""

    def __init__(self, name: str, interval_days: int, description: str):
        """Initialize a maintenance task.

        Args:
            name: Name of the maintenance task.
            interval_days: Interval in days between each maintenance.
            description: Description of the task.
        """
        self.name = name
        self.interval_days = interval_days
        self.description = description


class Generator:
    """Class representing a generator with maintenance schedule."""

    def __init__(self, generator_id: str, generator_type: GeneratorType, last_maintenance_date: datetime.date):
        """Initialize a generator.

        Args:
            generator_id: Unique identifier for the generator.
            generator_type: Type of the generator (Diesel or Gas).
            last_maintenance_date: Date when the last maintenance was performed.
        """
        self.generator_id = generator_id
        self.generator_type = generator_type
        self.last_maintenance_date = last_maintenance_date
        self.maintenance_tasks: List[MaintenanceTask] = []

    def add_maintenance_task(self, task: MaintenanceTask) -> None:
        """Add a maintenance task to the generator.

        Args:
            task: MaintenanceTask to be added.
        """
        self.maintenance_tasks.append(task)

    def get_next_maintenance_dates(self) -> Dict[str, datetime.date]:
        """Calculate the next maintenance dates for all tasks.

        Returns:
            A dictionary mapping task names to their next due dates.
        """
        next_dates = {}
        for task in self.maintenance_tasks:
            next_date = self.last_maintenance_date + datetime.timedelta(days=task.interval_days)
            next_dates[task.name] = next_date
        return next_dates

    def is_maintenance_due(self, current_date: Optional[datetime.date] = None) -> Tuple[bool, Dict[str, datetime.date]]:
        """Check if any maintenance is due for the generator.

        Args:
            current_date: Date to check against. Defaults to today.

        Returns:
            A tuple containing a boolean indicating if maintenance is due,
            and a dictionary of due tasks and their due dates.
        """
        if current_date is None:
            current_date = datetime.date.today()

        next_dates = self.get_next_maintenance_dates()
        due_tasks = {
            task: due_date
            for task, due_date in next_dates.items()
            if due_date <= current_date
        }
        return (len(due_tasks) > 0, due_tasks)


class MaintenanceScheduler:
    """Class to manage maintenance scheduling for multiple generators."""

    def __init__(self):
        """Initialize the maintenance scheduler."""
        self.generators: Dict[str, Generator] = {}

    def add_generator(self, generator: Generator) -> None:
        """Add a generator to the scheduler.

        Args:
            generator: Generator to be added.
        """
        if generator.generator_id in self.generators:
            raise ValueError(f"Generator with ID {generator.generator_id} already exists.")
        self.generators[generator.generator_id] = generator

    def get_due_maintenance(self, current_date: Optional[datetime.date] = None) -> Dict[str, Dict[str, datetime.date]]:
        """Get all generators with due maintenance tasks.

        Args:
            current_date: Date to check against. Defaults to today.

        Returns:
            A dictionary mapping generator IDs to their due tasks and due dates.
        """
        if current_date is None:
            current_date = datetime.date.today()

        due_maintenance = {}
        for generator_id, generator in self.generators.items():
            is_due, due_tasks = generator.is_maintenance_due(current_date)
            if is_due:
                due_maintenance[generator_id] = due_tasks
        return due_maintenance

    def schedule_maintenance(self, generator_id: str, task_name: str, completion_date: datetime.date) -> None:
        """Update the last maintenance date for a completed task.

        Args:
            generator_id: ID of the generator.
            task_name: Name of the completed task.
            completion_date: Date when the task was completed.
        """
        if generator_id not in self.generators:
            raise ValueError(f"Generator with ID {generator_id} not found.")

        generator = self.generators[generator_id]
        task_exists = any(task.name == task_name for task in generator.maintenance_tasks)
        if not task_exists:
            raise ValueError(f"Task {task_name} not found for generator {generator_id}.")

        generator.last_maintenance_date = completion_date


# Example usage
if __name__ == "__main__":
    # Define maintenance tasks for Diesel generators
    diesel_tasks = [
        MaintenanceTask("Oil Change", 180, "Change engine oil and oil filter"),
        MaintenanceTask("Air Filter", 90, "Clean or replace air filter"),
        MaintenanceTask("Coolant Check", 60, "Check and top up coolant levels"),
    ]

    # Define maintenance tasks for Gas generators
    gas_tasks = [
        MaintenanceTask("Spark Plug Replacement", 365, "Replace spark plugs"),
        MaintenanceTask("Gas Filter", 180, "Replace gas filter"),
        MaintenanceTask("Coolant Check", 60, "Check and top up coolant levels"),
    ]

    # Create generators
    diesel_gen = Generator("GEN001", GeneratorType.DIESEL, datetime.date(2023, 1, 1))
    for task in diesel_tasks:
        diesel_gen.add_maintenance_task(task)

    gas_gen = Generator("GEN002", GeneratorType.GAS, datetime.date(2023, 1, 1))
    for task in gas_tasks:
        gas_gen.add_maintenance_task(task)

    # Create scheduler and add generators
    scheduler = MaintenanceScheduler()
    scheduler.add_generator(diesel_gen)
    scheduler.add_generator(gas_gen)

    # Check for due maintenance
    due_maintenance = scheduler.get_due_maintenance(datetime.date(2023, 7, 1))
    print("Due Maintenance:", due_maintenance)

    # Schedule a completed maintenance task
    try:
        scheduler.schedule_maintenance("GEN001", "Oil Change", datetime.date(2023, 7, 1))
        print("Maintenance scheduled successfully.")
    except ValueError as e:
        print(f"Error scheduling maintenance: {e}")
```
