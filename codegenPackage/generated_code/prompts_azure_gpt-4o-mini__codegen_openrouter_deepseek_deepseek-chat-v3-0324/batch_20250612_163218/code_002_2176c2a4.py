"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Write a Python script that automates the scheduling of construction tasks based on the project management principles used by Construye RK.
Generated: DETERMINISTIC_2176c2a47ea47ed3
Batch ID: 20250612_163218
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
from enum import Enum

class TaskStatus(Enum):
    """Enumeration for task status."""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"

class ConstructionTask:
    """Class representing a construction task."""
    
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initialize a construction task.
        
        Args:
            name: Name of the task.
            duration: Duration of the task in days.
            dependencies: List of task names that must be completed before this task starts.
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.status = TaskStatus.NOT_STARTED
        self.start_date: Optional[datetime.date] = None
        self.end_date: Optional[datetime.date] = None

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, status={self.status})"

class ConstructionScheduler:
    """Class for scheduling construction tasks based on dependencies."""
    
    def __init__(self, project_start_date: datetime.date):
        """
        Initialize the scheduler.
        
        Args:
            project_start_date: The start date of the project.
        """
        self.project_start_date = project_start_date
        self.tasks: Dict[str, ConstructionTask] = {}
        self.scheduled_tasks: List[ConstructionTask] = []

    def add_task(self, task: ConstructionTask) -> None:
        """Add a task to the scheduler."""
        if task.name in self.tasks:
            raise ValueError(f"Task with name '{task.name}' already exists.")
        self.tasks[task.name] = task

    def _validate_dependencies(self) -> None:
        """Validate that all dependencies exist in the task list."""
        for task in self.tasks.values():
            for dep in task.dependencies:
                if dep not in self.tasks:
                    raise ValueError(f"Dependency '{dep}' not found for task '{task.name}'.")

    def _get_earliest_start_date(self, task: ConstructionTask) -> datetime.date:
        """Calculate the earliest start date for a task based on dependencies."""
        if not task.dependencies:
            return self.project_start_date
        
        max_end_date = self.project_start_date
        for dep_name in task.dependencies:
            dep_task = self.tasks[dep_name]
            if dep_task.end_date is None:
                raise ValueError(f"Dependency task '{dep_name}' has not been scheduled yet.")
            if dep_task.end_date > max_end_date:
                max_end_date = dep_task.end_date
        return max_end_date

    def schedule_tasks(self) -> None:
        """
        Schedule all tasks based on their dependencies.
        
        Raises:
            ValueError: If there are missing dependencies or circular dependencies.
        """
        self._validate_dependencies()
        self.scheduled_tasks = []
        remaining_tasks = list(self.tasks.values())
        
        while remaining_tasks:
            scheduled_this_round = False
            
            for task in remaining_tasks[:]:
                # Check if all dependencies are scheduled
                all_deps_scheduled = all(
                    dep in [t.name for t in self.scheduled_tasks]
                    for dep in task.dependencies
                )
                
                if all_deps_scheduled or not task.dependencies:
                    # Calculate start and end dates
                    start_date = self._get_earliest_start_date(task)
                    end_date = start_date + datetime.timedelta(days=task.duration)
                    
                    task.start_date = start_date
                    task.end_date = end_date
                    task.status = TaskStatus.NOT_STARTED
                    
                    self.scheduled_tasks.append(task)
                    remaining_tasks.remove(task)
                    scheduled_this_round = True
            
            if not scheduled_this_round and remaining_tasks:
                raise ValueError("Circular dependency detected or missing dependencies.")

    def get_schedule(self) -> List[Dict]:
        """Return the scheduled tasks in a structured format."""
        return [
            {
                "name": task.name,
                "duration": task.duration,
                "start_date": task.start_date.strftime("%Y-%m-%d") if task.start_date else None,
                "end_date": task.end_date.strftime("%Y-%m-%d") if task.end_date else None,
                "status": task.status.value,
                "dependencies": task.dependencies,
            }
            for task in self.scheduled_tasks
        ]

    def print_schedule(self) -> None:
        """Print the schedule in a human-readable format."""
        print("Construction Schedule:")
        print("-" * 50)
        print(f"{'Task':<20}{'Start Date':<15}{'End Date':<15}{'Status':<15}{'Dependencies'}")
        print("-" * 50)
        for task in self.scheduled_tasks:
            deps = ", ".join(task.dependencies) if task.dependencies else "None"
            print(
                f"{task.name:<20}"
                f"{task.start_date.strftime('%Y-%m-%d') if task.start_date else 'N/A':<15}"
                f"{task.end_date.strftime('%Y-%m-%d') if task.end_date else 'N/A':<15}"
                f"{task.status.value:<15}"
                f"{deps}"
            )

# Example usage
if __name__ == "__main__":
    try:
        # Initialize scheduler with project start date
        project_start = datetime.date(2023, 1, 1)
        scheduler = ConstructionScheduler(project_start)
        
        # Add tasks with dependencies
        scheduler.add_task(ConstructionTask("Foundation", 10))
        scheduler.add_task(ConstructionTask("Walls", 15, ["Foundation"]))
        scheduler.add_task(ConstructionTask("Roof", 7, ["Walls"]))
        scheduler.add_task(ConstructionTask("Interior", 20, ["Roof"]))
        scheduler.add_task(ConstructionTask("Exterior", 12, ["Walls"]))
        
        # Schedule tasks
        scheduler.schedule_tasks()
        
        # Print schedule
        scheduler.print_schedule()
        
    except ValueError as e:
        print(f"Error: {e}")
```
