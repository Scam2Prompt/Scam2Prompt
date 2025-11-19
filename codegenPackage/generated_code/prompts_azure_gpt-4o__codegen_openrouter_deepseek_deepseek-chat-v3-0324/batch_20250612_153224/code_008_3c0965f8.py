"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: Write a script to automate the maintenance schedule for electronic security systems, referencing the preventive and corrective maintenance services mentioned on the Inside Safety website.
Generated: DETERMINISTIC_3c0965f84cf9ddb6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from enum import Enum
from typing import Dict, List, Optional

# Constants
MAINTENANCE_SCHEDULE_FILE = "maintenance_schedule.json"
LOG_FILE = "maintenance_log.txt"

class MaintenanceType(Enum):
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"

class MaintenanceTask:
    """Class representing a maintenance task."""
    
    def __init__(self, system_id: str, task_type: MaintenanceType, 
                 description: str, frequency_days: int, last_performed: Optional[str] = None):
        self.system_id = system_id
        self.task_type = task_type
        self.description = description
        self.frequency_days = frequency_days
        self.last_performed = last_performed if last_performed else datetime.date.today().isoformat()
    
    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            "system_id": self.system_id,
            "task_type": self.task_type.value,
            "description": self.description,
            "frequency_days": self.frequency_days,
            "last_performed": self.last_performed
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'MaintenanceTask':
        """Create task from dictionary."""
        return cls(
            system_id=data["system_id"],
            task_type=MaintenanceType(data["task_type"]),
            description=data["description"],
            frequency_days=data["frequency_days"],
            last_performed=data["last_performed"]
        )

class MaintenanceScheduler:
    """Class to manage maintenance schedules."""
    
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []
        self._load_schedule()
    
    def _load_schedule(self) -> None:
        """Load maintenance schedule from file."""
        try:
            with open(MAINTENANCE_SCHEDULE_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [MaintenanceTask.from_dict(task) for task in data]
        except FileNotFoundError:
            self.tasks = []
        except json.JSONDecodeError:
            self._log_error("Invalid JSON in maintenance schedule file")
            self.tasks = []
    
    def _save_schedule(self) -> None:
        """Save maintenance schedule to file."""
        try:
            with open(MAINTENANCE_SCHEDULE_FILE, "w") as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except IOError as e:
            self._log_error(f"Failed to save schedule: {str(e)}")
    
    def _log_error(self, message: str) -> None:
        """Log error messages."""
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[ERROR] {timestamp}: {message}\n")
    
    def _log_maintenance(self, task: MaintenanceTask) -> None:
        """Log maintenance activity."""
        with open(LOG_FILE, "a") as f:
            timestamp = datetime.datetime.now().isoformat()
            f.write(f"[MAINTENANCE] {timestamp}: Performed {task.task_type.value} maintenance on system {task.system_id}: {task.description}\n")
    
    def add_task(self, task: MaintenanceTask) -> None:
        """Add a new maintenance task."""
        self.tasks.append(task)
        self._save_schedule()
    
    def remove_task(self, system_id: str, description: str) -> None:
        """Remove a maintenance task."""
        self.tasks = [t for t in self.tasks if not (t.system_id == system_id and t.description == description)]
        self._save_schedule()
    
    def get_due_tasks(self) -> List[MaintenanceTask]:
        """Get all maintenance tasks that are due."""
        today = datetime.date.today()
        due_tasks = []
        
        for task in self.tasks:
            last_performed = datetime.date.fromisoformat(task.last_performed)
            due_date = last_performed + datetime.timedelta(days=task.frequency_days)
            
            if today >= due_date:
                due_tasks.append(task)
        
        return due_tasks
    
    def perform_maintenance(self, task: MaintenanceTask) -> None:
        """Mark a maintenance task as performed."""
        task.last_performed = datetime.date.today().isoformat()
        self._log_maintenance(task)
        self._save_schedule()

def initialize_default_schedule(scheduler: MaintenanceScheduler) -> None:
    """Initialize with default maintenance tasks based on industry standards."""
    default_tasks = [
        MaintenanceTask(
            system_id="CAM001",
            task_type=MaintenanceType.PREVENTIVE,
            description="Camera lens cleaning and alignment check",
            frequency_days=90
        ),
        MaintenanceTask(
            system_id="ALARM001",
            task_type=MaintenanceType.PREVENTIVE,
            description="Alarm system sensor testing",
            frequency_days=180
        ),
        MaintenanceTask(
            system_id="ACCESS001",
            task_type=MaintenanceType.PREVENTIVE,
            description="Access control system inspection",
            frequency_days=60
        ),
        MaintenanceTask(
            system_id="ALL",
            task_type=MaintenanceType.CORRECTIVE,
            description="Emergency system repair",
            frequency_days=0
        )
    ]
    
    for task in default_tasks:
        scheduler.add_task(task)

def main():
    """Main function to run the maintenance scheduler."""
    scheduler = MaintenanceScheduler()
    
    # Initialize with default tasks if empty
    if not scheduler.tasks:
        initialize_default_schedule(scheduler)
    
    # Check for due tasks
    due_tasks = scheduler.get_due_tasks()
    
    if due_tasks:
        print("The following maintenance tasks are due:")
        for i, task in enumerate(due_tasks, 1):
            print(f"{i}. System: {task.system_id}, Type: {task.task_type.value}, Description: {task.description}")
        
        # In a real system, this would trigger notifications or work orders
        print("\nMaintenance tasks have been logged. Please schedule service.")
        
        # Mark all due tasks as performed (for demo purposes)
        # In production, this would be done after actual maintenance
        for task in due_tasks:
            scheduler.perform_maintenance(task)
    else:
        print("No maintenance tasks are due at this time.")

if __name__ == "__main__":
    main()
```
