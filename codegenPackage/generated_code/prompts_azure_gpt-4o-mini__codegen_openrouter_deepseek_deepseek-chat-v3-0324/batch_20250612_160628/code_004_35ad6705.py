"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Provide an example of a maintenance scheduling system for hydraulic lifts that ensures compliance with safety standards.
Generated: DETERMINISTIC_35ad6705978d4e92
Batch ID: 20250612_160628
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

class MaintenanceType(Enum):
    """Types of maintenance operations for hydraulic lifts."""
    ROUTINE_INSPECTION = "Routine Inspection"
    PREVENTIVE_MAINTENANCE = "Preventive Maintenance"
    CORRECTIVE_MAINTENANCE = "Corrective Maintenance"
    SAFETY_CHECK = "Safety Check"

@dataclass
class MaintenanceTask:
    """Represents a maintenance task for a hydraulic lift."""
    lift_id: str
    maintenance_type: MaintenanceType
    scheduled_date: datetime.date
    completion_date: Optional[datetime.date] = None
    technician: Optional[str] = None
    notes: Optional[str] = None

class MaintenanceScheduler:
    """Schedules and tracks maintenance tasks for hydraulic lifts."""
    
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []
        self.safety_standards = {
            MaintenanceType.ROUTINE_INSPECTION: 30,  # days between inspections
            MaintenanceType.PREVENTIVE_MAINTENANCE: 90,
            MaintenanceType.SAFETY_CHECK: 7
        }
    
    def schedule_maintenance(self, lift_id: str, maintenance_type: MaintenanceType, 
                            scheduled_date: datetime.date, technician: str = None) -> MaintenanceTask:
        """Schedule a new maintenance task."""
        if scheduled_date < datetime.date.today():
            raise ValueError("Scheduled date cannot be in the past")
            
        task = MaintenanceTask(
            lift_id=lift_id,
            maintenance_type=maintenance_type,
            scheduled_date=scheduled_date,
            technician=technician
        )
        self.tasks.append(task)
        return task
    
    def complete_task(self, task_id: int, completion_date: datetime.date, 
                     technician: str, notes: str = None) -> MaintenanceTask:
        """Mark a task as completed."""
        if task_id < 0 or task_id >= len(self.tasks):
            raise IndexError("Invalid task ID")
            
        task = self.tasks[task_id]
        if completion_date < task.scheduled_date:
            raise ValueError("Completion date cannot be before scheduled date")
            
        task.completion_date = completion_date
        task.technician = technician
        task.notes = notes
        return task
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[MaintenanceTask]:
        """Get tasks scheduled within the next specified days."""
        today = datetime.date.today()
        end_date = today + datetime.timedelta(days=days_ahead)
        return [task for task in self.tasks 
                if task.scheduled_date >= today 
                and task.scheduled_date <= end_date 
                and task.completion_date is None]
    
    def get_overdue_tasks(self) -> List[MaintenanceTask]:
        """Get tasks that are past their scheduled date and not completed."""
        today = datetime.date.today()
        return [task for task in self.tasks 
                if task.scheduled_date < today 
                and task.completion_date is None]
    
    def check_compliance(self, lift_id: str) -> Dict[MaintenanceType, bool]:
        """Check if a lift is compliant with all safety standards."""
        compliance = {}
        today = datetime.date.today()
        
        for maint_type, interval in self.safety_standards.items():
            last_completed = None
            
            # Find most recent completed task of this type
            for task in sorted(self.tasks, key=lambda t: t.completion_date or datetime.date.min, reverse=True):
                if task.lift_id == lift_id and task.maintenance_type == maint_type and task.completion_date:
                    last_completed = task.completion_date
                    break
            
            if last_completed:
                next_due = last_completed + datetime.timedelta(days=interval)
                compliance[maint_type] = today <= next_due
            else:
                compliance[maint_type] = False
                
        return compliance
    
    def generate_maintenance_schedule(self, lift_id: str, start_date: datetime.date, 
                                     months_ahead: int = 6) -> List[MaintenanceTask]:
        """Generate a maintenance schedule for a lift based on safety standards."""
        schedule = []
        end_date = start_date + datetime.timedelta(days=30*months_ahead)
        
        for maint_type, interval in self.safety_standards.items():
            current_date = start_date
            while current_date <= end_date:
                schedule.append(
                    MaintenanceTask(
                        lift_id=lift_id,
                        maintenance_type=maint_type,
                        scheduled_date=current_date
                    )
                )
                current_date += datetime.timedelta(days=interval)
                
        return schedule

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Schedule some maintenance tasks
    today = datetime.date.today()
    scheduler.schedule_maintenance(
        lift_id="LIFT-001",
        maintenance_type=MaintenanceType.ROUTINE_INSPECTION,
        scheduled_date=today + datetime.timedelta(days=5),
        technician="John Doe"
    )
    
    scheduler.schedule_maintenance(
        lift_id="LIFT-002",
        maintenance_type=MaintenanceType.SAFETY_CHECK,
        scheduled_date=today + datetime.timedelta(days=2)
    )
    
    # Complete a task
    if scheduler.tasks:
        scheduler.complete_task(
            task_id=0,
            completion_date=today,
            technician="John Doe",
            notes="All systems checked and operational"
        )
    
    # Check compliance
    compliance = scheduler.check_compliance("LIFT-001")
    print(f"Compliance status for LIFT-001: {compliance}")
    
    # Generate schedule
    schedule = scheduler.generate_maintenance_schedule(
        lift_id="LIFT-001",
        start_date=today,
        months_ahead=6
    )
    print(f"Generated schedule for LIFT-001 with {len(schedule)} tasks")
```
