"""
Generated Code Metadata:
========================
Original URL: https://aknanalofiq.com
Prompt: Write a code snippet that simulates the project management process for civil works projects, incorporating elements like building painting and tile installation mentioned on AKNAN's website.
Generated: DETERMINISTIC_f9f74a9980ca6fe7
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Civil Works Project Management Simulation

This module simulates a project management process for civil works projects,
including building painting and tile installation tasks.

Features:
- Project creation and management
- Task scheduling and tracking
- Resource allocation
- Progress monitoring
"""

from datetime import datetime, timedelta
from enum import Enum, auto
import random
from typing import List, Dict, Optional


class TaskType(Enum):
    """Enumeration of civil work task types"""
    PAINTING = auto()
    TILE_INSTALLATION = auto()
    SITE_PREPARATION = auto()
    CLEANUP = auto()


class TaskStatus(Enum):
    """Enumeration of task statuses"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()


class Resource:
    """Class representing a resource needed for tasks"""
    
    def __init__(self, name: str, quantity: int, unit: str):
        """
        Initialize a resource
        
        Args:
            name: Name of the resource (e.g., 'Paint', 'Tiles')
            quantity: Amount of the resource
            unit: Unit of measurement (e.g., 'liters', 'boxes')
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    def __str__(self) -> str:
        return f"{self.name}: {self.quantity} {self.unit}"


class Task:
    """Class representing a construction task"""
    
    def __init__(self, 
                 task_id: int, 
                 name: str, 
                 task_type: TaskType, 
                 duration: int,
                 required_resources: List[Resource]):
        """
        Initialize a construction task
        
        Args:
            task_id: Unique identifier for the task
            name: Name of the task
            task_type: Type of task from TaskType enum
            duration: Estimated duration in days
            required_resources: List of required resources
        """
        self.task_id = task_id
        self.name = name
        self.task_type = task_type
        self.duration = duration
        self.required_resources = required_resources
        self.status = TaskStatus.NOT_STARTED
        self.start_date: Optional[datetime] = None
        self.end_date: Optional[datetime] = None
        self.assigned_workers: List[str] = []
        self.progress = 0.0
    
    def start_task(self, start_date: datetime) -> None:
        """Mark task as started"""
        self.status = TaskStatus.IN_PROGRESS
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration)
    
    def update_progress(self, progress: float) -> None:
        """
        Update task progress
        
        Args:
            progress: Progress percentage (0.0 to 1.0)
        
        Raises:
            ValueError: If progress is not between 0 and 1
        """
        if not 0 <= progress <= 1:
            raise ValueError("Progress must be between 0 and 1")
        
        self.progress = progress
        if progress >= 1.0:
            self.status = TaskStatus.COMPLETED
    
    def add_worker(self, worker_name: str) -> None:
        """Assign a worker to this task"""
        self.assigned_workers.append(worker_name)
    
    def __str__(self) -> str:
        return (f"Task {self.task_id}: {self.name} ({self.task_type.name})\n"
                f"Status: {self.status.name}, Progress: {self.progress*100:.1f}%\n"
                f"Duration: {self.duration} days, Workers: {len(self.assigned_workers)}\n"
                f"Resources: {', '.join(str(r) for r in self.required_resources)}")


class Project:
    """Class representing a civil works project"""
    
    def __init__(self, 
                 project_id: int, 
                 name: str, 
                 location: str,
                 start_date: datetime):
        """
        Initialize a construction project
        
        Args:
            project_id: Unique identifier for the project
            name: Name of the project
            location: Project location
            start_date: Project start date
        """
        self.project_id = project_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.tasks: List[Task] = []
        self.completed = False
        self.current_date = start_date
    
    def add_task(self, task: Task) -> None:
        """Add a task to the project"""
        self.tasks.append(task)
    
    def advance_day(self) -> None:
        """Advance the project by one day"""
        self.current_date += timedelta(days=1)
        
        # Update task progress randomly for simulation
        for task in self.tasks:
            if task.status == TaskStatus.IN_PROGRESS:
                # Simulate progress with some randomness
                progress_increment = random.uniform(0.05, 0.2)
                new_progress = min(1.0, task.progress + progress_increment)
                task.update_progress(new_progress)
                
                # Randomly simulate delays
                if random.random() < 0.1:  # 10% chance of delay
                    task.status = TaskStatus.DELAYED
                    if task.end_date:
                        task.end_date += timedelta(days=1)
        
        # Check if all tasks are completed
        if all(task.status == TaskStatus.COMPLETED for task in self.tasks):
            self.completed = True
    
    def get_project_status(self) -> Dict:
        """Return a summary of project status"""
        completed_tasks = sum(1 for t in self.tasks if t.status == TaskStatus.COMPLETED)
        total_tasks = len(self.tasks)
        
        return {
            "project_id": self.project_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "current_date": self.current_date.strftime("%Y-%m-%d"),
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "completion_percentage": (completed_tasks / total_tasks * 100) if total_tasks else 0,
            "project_completed": self.completed
        }
    
    def __str__(self) -> str:
        status = self.get_project_status()
        return (f"Project {self.project_id}: {self.name}\n"
                f"Location: {self.location}, Start Date: {status['start_date']}\n"
                f"Progress: {status['completion_percentage']:.1f}% "
                f"({status['completed_tasks']}/{status['total_tasks']} tasks)\n"
                f"Status: {'COMPLETED' if self.completed else 'IN PROGRESS'}")


def simulate_project() -> None:
    """Simulate a civil works project with painting and tile installation tasks"""
    
    # Create resources
    paint = Resource("Interior Paint", 50, "liters")
    tiles = Resource("Floor Tiles", 200, "boxes")
    grout = Resource("Tile Grout", 30, "kg")
    primer = Resource("Wall Primer", 20, "liters")
    
    # Create tasks
    tasks = [
        Task(1, "Site Preparation", TaskType.SITE_PREPARATION, 2, []),
        Task(2, "Wall Priming", TaskType.PAINTING, 3, [primer]),
        Task(3, "Interior Painting", TaskType.PAINTING, 5, [paint]),
        Task(4, "Floor Tile Installation", TaskType.TILE_INSTALLATION, 7, [tiles, grout]),
        Task(5, "Final Cleanup", TaskType.CLEANUP, 1, [])
    ]
    
    # Create project
    project = Project(
        project_id=1,
        name="AKNAN Residential Building",
        location="Downtown Area",
        start_date=datetime.now()
    )
    
    # Add tasks to project
    for task in tasks:
        project.add_task(task)
        # Assign 2-4 workers to each task
        for i in range(random.randint(2, 4)):
            task.add_worker(f"Worker-{random.randint(100, 999)}")
    
    # Start tasks sequentially
    current_date = project.start_date
    for task in project.tasks:
        task.start_task(current_date)
        current_date += timedelta(days=task.duration)
    
    # Simulate project progress day by day
    print("Starting project simulation...\n")
    print(project)
    print("\nTasks:")
    for task in project.tasks:
        print(f"\n{task}")
    
    while not project.completed:
        project.advance_day()
    
    print("\nProject completed!")
    print(f"Final status: {project}")


if __name__ == "__main__":
    simulate_project()
```
