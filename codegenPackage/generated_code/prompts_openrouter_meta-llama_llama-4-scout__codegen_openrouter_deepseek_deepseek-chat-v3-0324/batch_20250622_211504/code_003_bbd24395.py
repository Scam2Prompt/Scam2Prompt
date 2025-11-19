"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Develop a simple algorithm for scheduling pipe cleaning and maintenance tasks for a water utility company, taking into account factors like pipe diameter, material, and location.
Generated: DETERMINISTIC_bbd24395fc781087
Batch ID: 20250622_211504
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

class PipeMaterial(Enum):
    """Enumeration of pipe materials."""
    PVC = "PVC"
    CAST_IRON = "Cast Iron"
    STEEL = "Steel"
    COPPER = "Copper"
    HDPE = "HDPE"

class PipePriority(Enum):
    """Enumeration of pipe maintenance priorities."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class Pipe:
    """Represents a pipe with its attributes."""
    id: str
    diameter: float  # in millimeters
    material: PipeMaterial
    location: str
    last_maintenance_date: Optional[datetime.date]
    age: int  # in years

@dataclass
class MaintenanceTask:
    """Represents a maintenance task for a pipe."""
    pipe_id: str
    priority: PipePriority
    scheduled_date: datetime.date
    description: str

class PipeMaintenanceScheduler:
    """Schedules maintenance tasks for pipes based on various factors."""
    
    def __init__(self):
        self.pipes: List[Pipe] = []
        self.tasks: List[MaintenanceTask] = []
    
    def add_pipe(self, pipe: Pipe) -> None:
        """Add a pipe to the scheduler."""
        if not isinstance(pipe, Pipe):
            raise ValueError("Invalid pipe object")
        self.pipes.append(pipe)
    
    def _calculate_priority(self, pipe: Pipe) -> PipePriority:
        """Calculate the priority of maintenance for a pipe."""
        priority = PipePriority.LOW
        
        # Higher priority for older pipes
        if pipe.age > 30:
            priority = PipePriority.HIGH
        elif pipe.age > 20:
            priority = PipePriority.MEDIUM
        
        # Adjust priority based on material
        if pipe.material == PipeMaterial.CAST_IRON:
            priority = PipePriority(max(priority.value, PipePriority.HIGH.value))
        elif pipe.material == PipeMaterial.STEEL:
            priority = PipePriority(max(priority.value, PipePriority.MEDIUM.value))
        
        # Adjust priority if overdue for maintenance
        if pipe.last_maintenance_date:
            days_since_maintenance = (datetime.date.today() - pipe.last_maintenance_date).days
            if days_since_maintenance > 365 * 5:  # 5 years
                priority = PipePriority.CRITICAL
            elif days_since_maintenance > 365 * 3:  # 3 years
                priority = PipePriority(max(priority.value, PipePriority.HIGH.value))
        
        return priority
    
    def _calculate_schedule_date(self, priority: PipePriority) -> datetime.date:
        """Calculate the scheduled date based on priority."""
        today = datetime.date.today()
        
        if priority == PipePriority.CRITICAL:
            return today + datetime.timedelta(days=7)
        elif priority == PipePriority.HIGH:
            return today + datetime.timedelta(days=30)
        elif priority == PipePriority.MEDIUM:
            return today + datetime.timedelta(days=90)
        else:
            return today + datetime.timedelta(days=180)
    
    def generate_schedule(self) -> List[MaintenanceTask]:
        """Generate maintenance schedule for all pipes."""
        self.tasks.clear()
        
        for pipe in self.pipes:
            priority = self._calculate_priority(pipe)
            scheduled_date = self._calculate_schedule_date(priority)
            description = f"Maintenance for {pipe.material.value} pipe ({pipe.diameter}mm) at {pipe.location}"
            
            task = MaintenanceTask(
                pipe_id=pipe.id,
                priority=priority,
                scheduled_date=scheduled_date,
                description=description
            )
            self.tasks.append(task)
        
        # Sort tasks by priority and scheduled date
        self.tasks.sort(key=lambda t: (t.priority.value, t.scheduled_date))
        return self.tasks
    
    def get_upcoming_tasks(self, days_ahead: int = 30) -> List[MaintenanceTask]:
        """Get tasks scheduled within the next N days."""
        if days_ahead <= 0:
            raise ValueError("days_ahead must be positive")
        
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        
        return [task for task in self.tasks if today <= task.scheduled_date <= end_date]

# Example usage
if __name__ == "__main__":
    scheduler = PipeMaintenanceScheduler()
    
    # Add some pipes
    scheduler.add_pipe(Pipe(
        id="P001",
        diameter=150,
        material=PipeMaterial.CAST_IRON,
        location="Downtown",
        last_maintenance_date=datetime.date(2018, 1, 15),
        age=40
    ))
    
    scheduler.add_pipe(Pipe(
        id="P002",
        diameter=100,
        material=PipeMaterial.PVC,
        location="Suburb",
        last_maintenance_date=datetime.date(2020, 5, 20),
        age=15
    ))
    
    scheduler.add_pipe(Pipe(
        id="P003",
        diameter=200,
        material=PipeMaterial.STEEL,
        location="Industrial Zone",
        last_maintenance_date=None,
        age=25
    ))
    
    # Generate schedule
    tasks = scheduler.generate_schedule()
    
    # Print all tasks
    print("All Maintenance Tasks:")
    for task in tasks:
        print(f"{task.pipe_id}: {task.description} | Priority: {task.priority.name} | Scheduled: {task.scheduled_date}")
    
    # Print upcoming tasks
    print("\nUpcoming Tasks (next 30 days):")
    upcoming = scheduler.get_upcoming_tasks(30)
    for task in upcoming:
        print(f"{task.pipe_id}: {task.description} | Scheduled: {task.scheduled_date}")
```
