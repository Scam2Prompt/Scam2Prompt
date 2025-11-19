"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Outline a library for managing home maintenance tasks, including features for scheduling plumbing and electrical services, based on the content from Felipe Muñoz Reparaciones.
Generated: DETERMINISTIC_02a31816881a8713
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Maintenance Task Management Library

This library provides functionality to manage home maintenance tasks, 
including scheduling plumbing and electrical services.
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import uuid
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ServiceType(Enum):
    """Enum representing different types of maintenance services."""
    PLUMBING = auto()
    ELECTRICAL = auto()
    GENERAL = auto()


class TaskStatus(Enum):
    """Enum representing different statuses of a maintenance task."""
    PENDING = auto()
    SCHEDULED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class MaintenanceTask:
    """Class representing a single maintenance task."""
    
    def __init__(
        self,
        service_type: ServiceType,
        description: str,
        priority: int = 1,
        scheduled_date: Optional[datetime] = None
    ):
        """
        Initialize a maintenance task.
        
        Args:
            service_type: Type of service (PLUMBING, ELECTRICAL, etc.)
            description: Description of the task
            priority: Priority level (1-5, 1 being highest)
            scheduled_date: Optional scheduled date for the task
        """
        self.task_id = str(uuid.uuid4())
        self.service_type = service_type
        self.description = description
        self.priority = priority
        self.scheduled_date = scheduled_date
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5")
    
    def update_status(self, new_status: TaskStatus) -> None:
        """Update the status of the task."""
        self.status = new_status
        self.updated_at = datetime.now()
        logger.info(f"Task {self.task_id} status updated to {new_status}")
    
    def reschedule(self, new_date: datetime) -> None:
        """Reschedule the task to a new date."""
        if new_date < datetime.now():
            raise ValueError("Cannot schedule task in the past")
        self.scheduled_date = new_date
        self.updated_at = datetime.now()
        logger.info(f"Task {self.task_id} rescheduled to {new_date}")


class HomeMaintenanceManager:
    """Class to manage all home maintenance tasks."""
    
    def __init__(self):
        """Initialize the maintenance manager."""
        self.tasks: Dict[str, MaintenanceTask] = {}
    
    def add_task(self, task: MaintenanceTask) -> str:
        """Add a new maintenance task."""
        if task.task_id in self.tasks:
            raise ValueError("Task with this ID already exists")
        self.tasks[task.task_id] = task
        logger.info(f"Added new task: {task.task_id}")
        return task.task_id
    
    def get_task(self, task_id: str) -> Optional[MaintenanceTask]:
        """Retrieve a task by its ID."""
        return self.tasks.get(task_id)
    
    def get_tasks_by_service_type(self, service_type: ServiceType) -> List[MaintenanceTask]:
        """Get all tasks of a specific service type."""
        return [task for task in self.tasks.values() if task.service_type == service_type]
    
    def get_pending_tasks(self) -> List[MaintenanceTask]:
        """Get all pending tasks."""
        return [task for task in self.tasks.values() if task.status == TaskStatus.PENDING]
    
    def get_scheduled_tasks(self) -> List[MaintenanceTask]:
        """Get all scheduled tasks."""
        return [task for task in self.tasks.values() if task.status == TaskStatus.SCHEDULED]
    
    def update_task_status(self, task_id: str, new_status: TaskStatus) -> None:
        """Update the status of a specific task."""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError("Task not found")
        task.update_status(new_status)
    
    def reschedule_task(self, task_id: str, new_date: datetime) -> None:
        """Reschedule a specific task."""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError("Task not found")
        task.reschedule(new_date)
    
    def cancel_task(self, task_id: str) -> None:
        """Cancel a specific task."""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError("Task not found")
        task.update_status(TaskStatus.CANCELLED)
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[MaintenanceTask]:
        """Get tasks scheduled within the next X days."""
        now = datetime.now()
        end_date = now + timedelta(days=days_ahead)
        return [
            task for task in self.tasks.values()
            if task.scheduled_date and now <= task.scheduled_date <= end_date
        ]


# Example usage
if __name__ == "__main__":
    manager = HomeMaintenanceManager()
    
    # Create some tasks
    plumbing_task = MaintenanceTask(
        service_type=ServiceType.PLUMBING,
        description="Fix leaking kitchen faucet",
        priority=2,
        scheduled_date=datetime(2023, 12, 15)
    )
    
    electrical_task = MaintenanceTask(
        service_type=ServiceType.ELECTRICAL,
        description="Install new light fixtures in living room",
        priority=3
    )
    
    # Add tasks to manager
    manager.add_task(plumbing_task)
    manager.add_task(electrical_task)
    
    # Update task status
    manager.update_task_status(plumbing_task.task_id, TaskStatus.SCHEDULED)
    
    # Get tasks by type
    plumbing_tasks = manager.get_tasks_by_service_type(ServiceType.PLUMBING)
    print(f"Found {len(plumbing_tasks)} plumbing tasks")
```
