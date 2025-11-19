"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Create a schedule for a building construction project using Unison Plus's project management best practices."
Generated: DETERMINISTIC_28ccde933fed4bf8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Scheduler using Unison Plus Best Practices

This module implements a construction project scheduler following
Unison Plus's project management methodologies.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
from enum import Enum

class TaskStatus(Enum):
    """Enumeration for task statuses"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"

class ConstructionTask:
    """Represents a single task in the construction project"""
    
    def __init__(
        self,
        name: str,
        duration: int,
        dependencies: List[str] = None,
        resources: List[str] = None,
        status: TaskStatus = TaskStatus.NOT_STARTED
    ):
        """
        Initialize a construction task
        
        Args:
            name: Name of the task
            duration: Duration in days
            dependencies: List of task names this task depends on
            resources: List of resources required
            status: Current status of the task
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.resources = resources if resources else []
        self.status = status
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization"""
        return {
            "name": self.name,
            "duration": self.duration,
            "dependencies": self.dependencies,
            "resources": self.resources,
            "status": self.status.value,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

class ConstructionSchedule:
    """Manages the construction project schedule"""
    
    def __init__(self, project_name: str, start_date: datetime):
        """
        Initialize construction schedule
        
        Args:
            project_name: Name of the construction project
            start_date: Project start date
        """
        self.project_name = project_name
        self.start_date = start_date
        self.tasks: Dict[str, ConstructionTask] = {}
        self.critical_path: List[str] = []
    
    def add_task(self, task: ConstructionTask) -> None:
        """Add a task to the schedule"""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists in schedule")
        self.tasks[task.name] = task
    
    def calculate_schedule(self) -> None:
        """Calculate the schedule including start and end dates for all tasks"""
        scheduled_tasks = set()
        
        # Initialize all tasks with no dependencies
        for task in self.tasks.values():
            if not task.dependencies:
                task.start_date = self.start_date
                task.end_date = self.start_date + timedelta(days=task.duration)
                scheduled_tasks.add(task.name)
        
        # Schedule remaining tasks
        while len(scheduled_tasks) < len(self.tasks):
            progress_made = False
            
            for task in self.tasks.values():
                if task.name not in scheduled_tasks:
                    all_deps_scheduled = all(
                        dep in scheduled_tasks for dep in task.dependencies
                    )
                    
                    if all_deps_scheduled:
                        latest_end_date = max(
                            self.tasks[dep].end_date for dep in task.dependencies
                        )
                        task.start_date = latest_end_date
                        task.end_date = latest_end_date + timedelta(days=task.duration)
                        scheduled_tasks.add(task.name)
                        progress_made = True
            
            if not progress_made:
                raise ValueError("Circular dependency detected in task dependencies")
        
        self._calculate_critical_path()
    
    def _calculate_critical_path(self) -> None:
        """Calculate the critical path for the project"""
        if not self.tasks:
            return
        
        # Find project end date
        project_end_date = max(task.end_date for task in self.tasks.values())
        
        # Work backwards to find critical path
        critical_path = []
        current_tasks = [
            task for task in self.tasks.values() 
            if task.end_date == project_end_date
        ]
        
        while current_tasks:
            current_task = current_tasks.pop()
            critical_path.append(current_task.name)
            
            if current_task.dependencies:
                latest_dependency = max(
                    self.tasks[dep] for dep in current_task.dependencies,
                    key=lambda t: t.end_date
                )
                current_tasks.append(latest_dependency)
        
        self.critical_path = list(reversed(critical_path))
    
    def update_task_status(self, task_name: str, status: TaskStatus) -> None:
        """Update the status of a task"""
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' not found in schedule")
        self.tasks[task_name].status = status
    
    def get_project_end_date(self) -> Optional[datetime]:
        """Get the projected end date of the project"""
        if not self.tasks:
            return None
        return max(task.end_date for task in self.tasks.values())
    
    def to_json(self) -> str:
        """Serialize the schedule to JSON"""
        schedule_data = {
            "project_name": self.project_name,
            "start_date": self.start_date.isoformat(),
            "tasks": [task.to_dict() for task in self.tasks.values()],
            "critical_path": self.critical_path
        }
        return json.dumps(schedule_data, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'ConstructionSchedule':
        """Deserialize a schedule from JSON"""
        data = json.loads(json_str)
        schedule = cls(
            project_name=data["project_name"],
            start_date=datetime.fromisoformat(data["start_date"])
        )
        
        for task_data in data["tasks"]:
            task = ConstructionTask(
                name=task_data["name"],
                duration=task_data["duration"],
                dependencies=task_data["dependencies"],
                resources=task_data["resources"],
                status=TaskStatus(task_data["status"])
            )
            if task_data["start_date"]:
                task.start_date = datetime.fromisoformat(task_data["start_date"])
            if task_data["end_date"]:
                task.end_date = datetime.fromisoformat(task_data["end_date"])
            schedule.add_task(task)
        
        schedule.critical_path = data["critical_path"]
        return schedule

def create_sample_schedule() -> ConstructionSchedule:
    """Create a sample construction schedule for demonstration"""
    schedule = ConstructionSchedule(
        project_name="Office Building Construction",
        start_date=datetime(2023, 1, 1)
    )
    
    tasks = [
        ConstructionTask("Site Preparation", 10),
        ConstructionTask("Foundation", 15, ["Site Preparation"]),
        ConstructionTask("Structural Steel", 30, ["Foundation"]),
        ConstructionTask("Exterior Walls", 25, ["Structural Steel"]),
        ConstructionTask("Roofing", 15, ["Structural Steel"]),
        ConstructionTask("Interior Partitions", 20, ["Exterior Walls", "Roofing"]),
        ConstructionTask("HVAC", 15, ["Interior Partitions"]),
        ConstructionTask("Electrical", 15, ["Interior Partitions"]),
        ConstructionTask("Plumbing", 15, ["Interior Partitions"]),
        ConstructionTask("Interior Finishes", 30, ["HVAC", "Electrical", "Plumbing"]),
        ConstructionTask("Landscaping", 10, ["Exterior Walls"]),
        ConstructionTask("Final Inspection", 5, ["Interior Finishes", "Landscaping"])
    ]
    
    for task in tasks:
        schedule.add_task(task)
    
    schedule.calculate_schedule()
    return schedule

if __name__ == "__main__":
    # Example usage
    schedule = create_sample_schedule()
    print(f"Project: {schedule.project_name}")
    print(f"Start Date: {schedule.start_date.strftime('%Y-%m-%d')}")
    print(f"End Date: {schedule.get_project_end_date().strftime('%Y-%m-%d')}")
    print("\nCritical Path:")
    for task_name in schedule.critical_path:
        task = schedule.tasks[task_name]
        print(f"- {task.name}: {task.start_date.strftime('%Y-%m-%d')} to {task.end_date.strftime('%Y-%m-%d')}")
    
    # Save to JSON
    with open("construction_schedule.json", "w") as f:
        f.write(schedule.to_json())
```
