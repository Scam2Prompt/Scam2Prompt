"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: Write code to automate the scheduling of water system maintenance and replacement parts for Kenmore, Hydrotech, AquaCliniq, or NOVO systems, as mentioned on Provincial Water Solutions' website.
Generated: DETERMINISTIC_8bc5e7efdf7d2fdf
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import logging
from enum import Enum
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class WaterSystemType(Enum):
    """Enumeration of supported water system brands."""
    KENMORE = "Kenmore"
    HYDROTECH = "Hydrotech"
    AQUACLINIQ = "AquaCliniq"
    NOVO = "NOVO"


class MaintenanceTask:
    """Represents a maintenance task for a water system."""

    def __init__(
        self,
        system_type: WaterSystemType,
        task_name: str,
        frequency_days: int,
        last_performed: Optional[datetime.date] = None,
        parts_needed: Optional[List[str]] = None
    ):
        self.system_type = system_type
        self.task_name = task_name
        self.frequency_days = frequency_days
        self.last_performed = last_performed or datetime.date.today()
        self.parts_needed = parts_needed or []

    def is_due(self) -> bool:
        """Check if the maintenance task is due."""
        next_due_date = self.last_performed + datetime.timedelta(days=self.frequency_days)
        return datetime.date.today() >= next_due_date

    def to_dict(self) -> Dict:
        """Convert the task to a dictionary for serialization."""
        return {
            "system_type": self.system_type.value,
            "task_name": self.task_name,
            "frequency_days": self.frequency_days,
            "last_performed": self.last_performed.isoformat(),
            "parts_needed": self.parts_needed
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'MaintenanceTask':
        """Create a task from a dictionary."""
        return cls(
            system_type=WaterSystemType(data["system_type"]),
            task_name=data["task_name"],
            frequency_days=data["frequency_days"],
            last_performed=datetime.date.fromisoformat(data["last_performed"]),
            parts_needed=data["parts_needed"]
        )


class WaterSystemMaintenanceScheduler:
    """Manages scheduling and tracking of water system maintenance tasks."""

    def __init__(self, data_file: str = "maintenance_schedule.json"):
        self.data_file = data_file
        self.tasks: List[MaintenanceTask] = []
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from the data file."""
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.tasks = [MaintenanceTask.from_dict(task) for task in data]
            logger.info(f"Loaded {len(self.tasks)} tasks from {self.data_file}")
        except FileNotFoundError:
            logger.info("No existing data file found. Starting with empty task list.")
        except json.JSONDecodeError:
            logger.error("Error decoding JSON data. Starting with empty task list.")
        except Exception as e:
            logger.error(f"Error loading tasks: {str(e)}")

    def _save_tasks(self) -> None:
        """Save tasks to the data file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
            logger.info(f"Saved {len(self.tasks)} tasks to {self.data_file}")
        except Exception as e:
            logger.error(f"Error saving tasks: {str(e)}")

    def add_task(self, task: MaintenanceTask) -> None:
        """Add a new maintenance task."""
        self.tasks.append(task)
        self._save_tasks()
        logger.info(f"Added task: {task.task_name} for {task.system_type.value}")

    def mark_task_completed(self, task_name: str, system_type: WaterSystemType) -> None:
        """Mark a task as completed and update last performed date."""
        for task in self.tasks:
            if task.task_name == task_name and task.system_type == system_type:
                task.last_performed = datetime.date.today()
                self._save_tasks()
                logger.info(f"Marked task '{task_name}' for {system_type.value} as completed")
                return
        logger.warning(f"Task '{task_name}' for {system_type.value} not found")

    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Get all tasks that are currently due."""
        return [task for task in self.tasks if task.is_due()]

    def get_parts_needed(self) -> Dict[str, List[str]]:
        """Get all parts needed for due tasks, grouped by system type."""
        parts_needed = {}
        for task in self.get_due_tasks():
            if task.system_type.value not in parts_needed:
                parts_needed[task.system_type.value] = []
            parts_needed[task.system_type.value].extend(task.parts_needed)
        return parts_needed

    def generate_maintenance_schedule(self, days_ahead: int = 30) -> Dict[str, List[str]]:
        """Generate a maintenance schedule for the next specified days."""
        schedule = {}
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)

        for task in self.tasks:
            next_due = task.last_performed + datetime.timedelta(days=task.frequency_days)
            if today <= next_due <= end_date:
                date_str = next_due.isoformat()
                if date_str not in schedule:
                    schedule[date_str] = []
                schedule[date_str].append(
                    f"{task.system_type.value}: {task.task_name}"
                )
        return schedule


# Example usage
if __name__ == "__main__":
    scheduler = WaterSystemMaintenanceScheduler()

    # Add sample tasks if none exist
    if not scheduler.tasks:
        scheduler.add_task(MaintenanceTask(
            system_type=WaterSystemType.KENMORE,
            task_name="Filter Replacement",
            frequency_days=90,
            parts_needed=["Sediment Filter", "Carbon Filter"]
        ))
        scheduler.add_task(MaintenanceTask(
            system_type=WaterSystemType.HYDROTECH,
            task_name="Membrane Cleaning",
            frequency_days=180,
            parts_needed=["Cleaning Solution"]
        ))

    # Check for due tasks
    due_tasks = scheduler.get_due_tasks()
    if due_tasks:
        print("Due Maintenance Tasks:")
        for task in due_tasks:
            print(f"- {task.system_type.value}: {task.task_name}")
            if task.parts_needed:
                print(f"  Parts needed: {', '.join(task.parts_needed)}")
    else:
        print("No maintenance tasks are currently due.")

    # Generate upcoming schedule
    print("\nUpcoming Maintenance Schedule (next 30 days):")
    schedule = scheduler.generate_maintenance_schedule()
    for date, tasks in sorted(schedule.items()):
        print(f"{date}:")
        for task in tasks:
            print(f"  - {task}")
```
