"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Provide a code example for a maintenance tracking system for glass installations, including features for scheduling repairs for blindex doors, replacing roldanas, and adjusting tempered glass panels.
Generated: DETERMINISTIC_cd3774861343b607
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maintenance_tracking_system.py
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass


class MaintenanceType(Enum):
    """Enumeration of maintenance types for glass installations."""
    REPAIR_BLINDEX_DOOR = "Repair Blindex Door"
    REPLACE_ROLDANA = "Replace Roldana"
    ADJUST_TEMPERED_GLASS = "Adjust Tempered Glass Panel"


class MaintenanceStatus(Enum):
    """Enumeration of maintenance statuses."""
    SCHEDULED = "Scheduled"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


@dataclass
class GlassInstallation:
    """Data class representing a glass installation."""
    installation_id: str
    location: str
    installation_date: datetime.date
    last_maintenance_date: Optional[datetime.date] = None


@dataclass
class MaintenanceTask:
    """Data class representing a maintenance task."""
    task_id: str
    installation: GlassInstallation
    maintenance_type: MaintenanceType
    scheduled_date: datetime.date
    assigned_technician: str
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED
    notes: str = ""


class MaintenanceTrackingSystem:
    """System for tracking maintenance of glass installations."""
    
    def __init__(self):
        self.installations: Dict[str, GlassInstallation] = {}
        self.tasks: Dict[str, MaintenanceTask] = {}
    
    def add_installation(self, installation: GlassInstallation) -> None:
        """Add a new glass installation to the system."""
        if installation.installation_id in self.installations:
            raise ValueError(f"Installation with ID {installation.installation_id} already exists.")
        self.installations[installation.installation_id] = installation
    
    def schedule_maintenance(
        self,
        installation_id: str,
        maintenance_type: MaintenanceType,
        scheduled_date: datetime.date,
        technician: str,
        notes: str = ""
    ) -> MaintenanceTask:
        """Schedule a new maintenance task."""
        if installation_id not in self.installations:
            raise ValueError(f"Installation with ID {installation_id} not found.")
        
        task_id = f"TASK-{datetime.datetime.now().timestamp()}"
        task = MaintenanceTask(
            task_id=task_id,
            installation=self.installations[installation_id],
            maintenance_type=maintenance_type,
            scheduled_date=scheduled_date,
            assigned_technician=technician,
            notes=notes
        )
        
        self.tasks[task_id] = task
        return task
    
    def update_task_status(self, task_id: str, new_status: MaintenanceStatus) -> None:
        """Update the status of a maintenance task."""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found.")
        
        task = self.tasks[task_id]
        task.status = new_status
        
        if new_status == MaintenanceStatus.COMPLETED:
            task.installation.last_maintenance_date = datetime.date.today()
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[MaintenanceTask]:
        """Get all tasks scheduled within the next specified days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        
        return [
            task for task in self.tasks.values()
            if today <= task.scheduled_date <= end_date
            and task.status == MaintenanceStatus.SCHEDULED
        ]
    
    def get_tasks_by_installation(self, installation_id: str) -> List[MaintenanceTask]:
        """Get all maintenance tasks for a specific installation."""
        if installation_id not in self.installations:
            raise ValueError(f"Installation with ID {installation_id} not found.")
        
        return [
            task for task in self.tasks.values()
            if task.installation.installation_id == installation_id
        ]
    
    def get_tasks_by_type(self, maintenance_type: MaintenanceType) -> List[MaintenanceTask]:
        """Get all maintenance tasks of a specific type."""
        return [
            task for task in self.tasks.values()
            if task.maintenance_type == maintenance_type
        ]


# Example usage
if __name__ == "__main__":
    system = MaintenanceTrackingSystem()
    
    # Add installations
    installation1 = GlassInstallation(
        installation_id="INST-001",
        location="Main Entrance",
        installation_date=datetime.date(2020, 5, 15)
    )
    system.add_installation(installation1)
    
    installation2 = GlassInstallation(
        installation_id="INST-002",
        location="Conference Room",
        installation_date=datetime.date(2021, 2, 10)
    )
    system.add_installation(installation2)
    
    # Schedule maintenance tasks
    task1 = system.schedule_maintenance(
        installation_id="INST-001",
        maintenance_type=MaintenanceType.REPAIR_BLINDEX_DOOR,
        scheduled_date=datetime.date.today() + datetime.timedelta(days=3),
        technician="John Doe",
        notes="Door not closing properly"
    )
    
    task2 = system.schedule_maintenance(
        installation_id="INST-002",
        maintenance_type=MaintenanceType.REPLACE_ROLDANA,
        scheduled_date=datetime.date.today() + datetime.timedelta(days=5),
        technician="Jane Smith"
    )
    
    # Update task status
    system.update_task_status(task1.task_id, MaintenanceStatus.IN_PROGRESS)
    
    # Get upcoming tasks
    upcoming = system.get_upcoming_tasks()
    print(f"Upcoming tasks: {[t.task_id for t in upcoming]}")
    
    # Get tasks by installation
    inst_tasks = system.get_tasks_by_installation("INST-001")
    print(f"Tasks for INST-001: {[t.task_id for t in inst_tasks]}")
```
