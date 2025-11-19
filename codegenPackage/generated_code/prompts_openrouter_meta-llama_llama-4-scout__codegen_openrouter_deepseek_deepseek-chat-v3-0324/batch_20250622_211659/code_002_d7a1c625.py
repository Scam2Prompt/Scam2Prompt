"""
Generated Code Metadata:
========================
Original URL: https://sistemabox.com.br
Prompt: "Generate a maintenance schedule for IT support services, considering factors like response time and resolution rate, as described in Sistemabox's Suporte TI offerings."
Generated: DETERMINISTIC_d7a1c625c5b08b96
Batch ID: 20250622_211659
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

class Priority(Enum):
    """Priority levels for maintenance tasks."""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class MaintenanceTask:
    """Represents a maintenance task in the schedule."""
    task_id: str
    description: str
    priority: Priority
    estimated_duration: datetime.timedelta
    assigned_team: str
    due_date: datetime.datetime
    response_time: datetime.timedelta
    resolution_rate: float  # Percentage (0-100)

class MaintenanceScheduler:
    """Generates and manages a maintenance schedule for IT support services."""
    
    def __init__(self):
        self.tasks: List[MaintenanceTask] = []
    
    def add_task(self, task: MaintenanceTask) -> None:
        """Adds a task to the schedule."""
        if not isinstance(task, MaintenanceTask):
            raise ValueError("Invalid task type")
        self.tasks.append(task)
    
    def remove_task(self, task_id: str) -> bool:
        """Removes a task by ID. Returns True if successful."""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i]
                return True
        return False
    
    def get_tasks_by_priority(self, priority: Priority) -> List[MaintenanceTask]:
        """Returns tasks filtered by priority."""
        return [task for task in self.tasks if task.priority == priority]
    
    def get_overdue_tasks(self) -> List[MaintenanceTask]:
        """Returns tasks that are overdue."""
        now = datetime.datetime.now()
        return [task for task in self.tasks if task.due_date < now]
    
    def get_upcoming_tasks(self, days: int = 7) -> List[MaintenanceTask]:
        """Returns tasks due within the specified number of days."""
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days)
        return [task for task in self.tasks if now <= task.due_date <= end_date]
    
    def calculate_metrics(self) -> Dict[str, float]:
        """Calculates average response time and resolution rate."""
        if not self.tasks:
            return {
                'avg_response_time': 0,
                'avg_resolution_rate': 0
            }
        
        total_response = sum(
            task.response_time.total_seconds() for task in self.tasks
        )
        avg_response = total_response / len(self.tasks)
        
        avg_resolution = sum(
            task.resolution_rate for task in self.tasks
        ) / len(self.tasks)
        
        return {
            'avg_response_time': avg_response,
            'avg_resolution_rate': avg_resolution
        }
    
    def generate_schedule_report(self) -> str:
        """Generates a formatted report of the maintenance schedule."""
        report = []
        report.append("Maintenance Schedule Report")
        report.append("=" * 40)
        report.append(f"Total Tasks: {len(self.tasks)}")
        
        metrics = self.calculate_metrics()
        report.append(
            f"Avg Response Time: {metrics['avg_response_time']:.2f} seconds"
        )
        report.append(
            f"Avg Resolution Rate: {metrics['avg_resolution_rate']:.2f}%"
        )
        
        report.append("\nUpcoming Tasks (next 7 days):")
        for task in self.get_upcoming_tasks():
            report.append(
                f"- {task.task_id}: {task.description} (Due: {task.due_date})"
            )
        
        overdue = self.get_overdue_tasks()
        if overdue:
            report.append("\nOverdue Tasks:")
            for task in overdue:
                report.append(
                    f"- {task.task_id}: {task.description} (Due: {task.due_date})"
                )
        
        return "\n".join(report)

# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Add sample tasks
    task1 = MaintenanceTask(
        task_id="T001",
        description="Server maintenance",
        priority=Priority.HIGH,
        estimated_duration=datetime.timedelta(hours=2),
        assigned_team="Infrastructure",
        due_date=datetime.datetime.now() + datetime.timedelta(days=1),
        response_time=datetime.timedelta(minutes=30),
        resolution_rate=95.0
    )
    
    task2 = MaintenanceTask(
        task_id="T002",
        description="Software update",
        priority=Priority.MEDIUM,
        estimated_duration=datetime.timedelta(hours=1),
        assigned_team="Applications",
        due_date=datetime.datetime.now() + datetime.timedelta(days=3),
        response_time=datetime.timedelta(minutes=45),
        resolution_rate=85.0
    )
    
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    
    # Generate and print report
    print(scheduler.generate_schedule_report())
```
