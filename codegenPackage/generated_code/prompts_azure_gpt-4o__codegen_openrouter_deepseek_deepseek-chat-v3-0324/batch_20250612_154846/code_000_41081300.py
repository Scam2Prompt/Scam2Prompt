"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: Write Python code to simulate a maintenance scheduling system for engineering projects, incorporating safety and efficiency standards as described by SET Ingeniería.
Generated: DETERMINISTIC_41081300cbf78c6a
Batch ID: 20250612_154846
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
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MaintenancePriority(Enum):
    """Priority levels for maintenance tasks."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class MaintenanceStatus(Enum):
    """Status of maintenance tasks."""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4
    FAILED = 5

@dataclass
class MaintenanceTask:
    """Represents a maintenance task with all relevant details."""
    task_id: str
    description: str
    priority: MaintenancePriority
    status: MaintenanceStatus
    assigned_team: str
    estimated_duration: datetime.timedelta
    scheduled_start: datetime.datetime
    safety_checks: List[str]
    efficiency_standards: List[str]
    dependencies: List[str] = None

    def __post_init__(self):
        """Validate task data upon initialization."""
        if not self.task_id:
            raise ValueError("Task ID cannot be empty")
        if not self.description:
            raise ValueError("Description cannot be empty")
        if self.scheduled_start < datetime.datetime.now():
            raise ValueError("Scheduled start cannot be in the past")
        if not self.safety_checks:
            raise ValueError("Safety checks list cannot be empty")
        if not self.efficiency_standards:
            raise ValueError("Efficiency standards list cannot be empty")
        if self.dependencies is None:
            self.dependencies = []

class MaintenanceScheduler:
    """Manages scheduling and execution of maintenance tasks."""
    
    def __init__(self):
        self.tasks: Dict[str, MaintenanceTask] = {}
        self.completed_tasks: Dict[str, MaintenanceTask] = {}
    
    def add_task(self, task: MaintenanceTask) -> None:
        """Add a new maintenance task to the scheduler."""
        try:
            if task.task_id in self.tasks:
                raise ValueError(f"Task with ID {task.task_id} already exists")
            self.tasks[task.task_id] = task
            logger.info(f"Added task {task.task_id}: {task.description}")
        except Exception as e:
            logger.error(f"Failed to add task: {e}")
            raise
    
    def update_task_status(self, task_id: str, status: MaintenanceStatus) -> None:
        """Update the status of a maintenance task."""
        try:
            if task_id not in self.tasks:
                raise ValueError(f"Task {task_id} not found")
            
            task = self.tasks[task_id]
            task.status = status
            
            if status == MaintenanceStatus.COMPLETED:
                self.completed_tasks[task_id] = task
                del self.tasks[task_id]
                logger.info(f"Completed task {task_id}")
            else:
                logger.info(f"Updated task {task_id} status to {status.name}")
        except Exception as e:
            logger.error(f"Failed to update task status: {e}")
            raise
    
    def get_pending_tasks(self) -> List[MaintenanceTask]:
        """Get all pending maintenance tasks."""
        return [task for task in self.tasks.values() 
                if task.status == MaintenanceStatus.PENDING]
    
    def get_tasks_by_priority(self, priority: MaintenancePriority) -> List[MaintenanceTask]:
        """Get tasks filtered by priority level."""
        return [task for task in self.tasks.values() 
                if task.priority == priority]
    
    def check_dependencies_completed(self, task_id: str) -> bool:
        """Check if all dependencies for a task are completed."""
        task = self.tasks.get(task_id)
        if not task:
            raise ValueError(f"Task {task_id} not found")
        
        for dep_id in task.dependencies:
            if dep_id not in self.completed_tasks:
                return False
        return True
    
    def schedule_tasks(self) -> None:
        """Automatically schedule tasks based on priority and dependencies."""
        try:
            # Sort tasks by priority (highest first) and then by scheduled start
            sorted_tasks = sorted(
                self.tasks.values(),
                key=lambda t: (-t.priority.value, t.scheduled_start)
            )
            
            for task in sorted_tasks:
                if (task.status == MaintenanceStatus.PENDING and 
                    self.check_dependencies_completed(task.task_id)):
                    task.status = MaintenanceStatus.IN_PROGRESS
                    logger.info(f"Scheduled task {task.task_id} for execution")
        except Exception as e:
            logger.error(f"Failed to schedule tasks: {e}")
            raise
    
    def to_json(self) -> str:
        """Serialize the scheduler state to JSON."""
        try:
            data = {
                "tasks": [task.__dict__ for task in self.tasks.values()],
                "completed_tasks": [task.__dict__ for task in self.completed_tasks.values()]
            }
            return json.dumps(data, default=self._serialize_datetime)
        except Exception as e:
            logger.error(f"Failed to serialize scheduler: {e}")
            raise
    
    @classmethod
    def from_json(cls, json_str: str) -> 'MaintenanceScheduler':
        """Deserialize a scheduler from JSON."""
        try:
            data = json.loads(json_str)
            scheduler = cls()
            
            for task_data in data.get("tasks", []):
                task = MaintenanceTask(
                    task_id=task_data["task_id"],
                    description=task_data["description"],
                    priority=MaintenancePriority(task_data["priority"]),
                    status=MaintenanceStatus(task_data["status"]),
                    assigned_team=task_data["assigned_team"],
                    estimated_duration=datetime.timedelta(seconds=task_data["estimated_duration"]),
                    scheduled_start=datetime.datetime.fromisoformat(task_data["scheduled_start"]),
                    safety_checks=task_data["safety_checks"],
                    efficiency_standards=task_data["efficiency_standards"],
                    dependencies=task_data.get("dependencies", [])
                )
                scheduler.tasks[task.task_id] = task
            
            for task_data in data.get("completed_tasks", []):
                task = MaintenanceTask(
                    task_id=task_data["task_id"],
                    description=task_data["description"],
                    priority=MaintenancePriority(task_data["priority"]),
                    status=MaintenanceStatus(task_data["status"]),
                    assigned_team=task_data["assigned_team"],
                    estimated_duration=datetime.timedelta(seconds=task_data["estimated_duration"]),
                    scheduled_start=datetime.datetime.fromisoformat(task_data["scheduled_start"]),
                    safety_checks=task_data["safety_checks"],
                    efficiency_standards=task_data["efficiency_standards"],
                    dependencies=task_data.get("dependencies", [])
                )
                scheduler.completed_tasks[task.task_id] = task
            
            return scheduler
        except Exception as e:
            logger.error(f"Failed to deserialize scheduler: {e}")
            raise
    
    def _serialize_datetime(self, obj):
        """Helper method to serialize datetime objects."""
        if isinstance(obj, (datetime.datetime, datetime.date)):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        raise TypeError(f"Type {type(obj)} not serializable")

# Example usage
if __name__ == "__main__":
    try:
        scheduler = MaintenanceScheduler()
        
        # Create some tasks
        task1 = MaintenanceTask(
            task_id="T001",
            description="Inspect electrical systems",
            priority=MaintenancePriority.HIGH,
            status=MaintenanceStatus.PENDING,
            assigned_team="Electrical Team",
            estimated_duration=datetime.timedelta(hours=2),
            scheduled_start=datetime.datetime.now() + datetime.timedelta(days=1),
            safety_checks=["Lockout-tagout", "Voltage check"],
            efficiency_standards=["SET-ELEC-001", "SET-ELEC-005"]
        )
        
        task2 = MaintenanceTask(
            task_id="T002",
            description="Replace worn bearings",
            priority=MaintenancePriority.MEDIUM,
            status=MaintenanceStatus.PENDING,
            assigned_team="Mechanical Team",
            estimated_duration=datetime.timedelta(hours=4),
            scheduled_start=datetime.datetime.now() + datetime.timedelta(days=2),
            safety_checks=["Machine isolation", "PPE check"],
            efficiency_standards=["SET-MECH-003"],
            dependencies=["T001"]
        )
        
        # Add tasks to scheduler
        scheduler.add_task(task1)
        scheduler.add_task(task2)
        
        # Schedule tasks
        scheduler.schedule_tasks()
        
        # Complete task1
        scheduler.update_task_status("T001", MaintenanceStatus.COMPLETED)
        
        # Schedule again to trigger dependent tasks
        scheduler.schedule_tasks()
        
        # Serialize and deserialize
        json_data = scheduler.to_json()
        new_s
