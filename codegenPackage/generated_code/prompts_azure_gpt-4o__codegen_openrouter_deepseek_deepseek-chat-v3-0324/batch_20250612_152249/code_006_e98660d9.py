"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Write code to model the workflow of industrial construction projects, incorporating Rux Industrial's emphasis on safety, complexity, and deadlines.
Generated: DETERMINISTIC_e98660d988c2a6fa
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum, auto
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SafetyLevel(Enum):
    """Safety levels for construction tasks"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class TaskStatus(Enum):
    """Status of construction tasks"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()
    SAFETY_REVIEW = auto()

class ConstructionTask:
    """Represents a single task in a construction project"""
    
    def __init__(
        self,
        name: str,
        duration: timedelta,
        safety_level: SafetyLevel,
        dependencies: List[str] = None,
        deadline: Optional[datetime] = None
    ):
        """
        Initialize a construction task.
        
        Args:
            name: Name of the task
            duration: Estimated time to complete
            safety_level: Required safety level
            dependencies: List of task names this task depends on
            deadline: Optional deadline for the task
        """
        self.name = name
        self.duration = duration
        self.safety_level = safety_level
        self.dependencies = dependencies or []
        self.deadline = deadline
        self.status = TaskStatus.NOT_STARTED
        self.start_date = None
        self.end_date = None
        self.safety_checks = []
        
    def add_safety_check(self, check_name: str, passed: bool):
        """Record a safety check for this task"""
        self.safety_checks.append((check_name, passed))
        if not passed:
            self.status = TaskStatus.SAFETY_REVIEW
            logger.warning(f"Safety check failed for task {self.name}: {check_name}")
            
    def start(self, current_date: datetime):
        """Mark task as started"""
        if self.status != TaskStatus.NOT_STARTED:
            raise ValueError("Task can only be started from NOT_STARTED status")
            
        if not all(check[1] for check in self.safety_checks):
            raise ValueError("Cannot start task with failed safety checks")
            
        self.status = TaskStatus.IN_PROGRESS
        self.start_date = current_date
        logger.info(f"Task {self.name} started on {current_date}")
        
    def complete(self, current_date: datetime):
        """Mark task as completed"""
        if self.status != TaskStatus.IN_PROGRESS:
            raise ValueError("Task can only be completed from IN_PROGRESS status")
            
        self.status = TaskStatus.COMPLETED
        self.end_date = current_date
        logger.info(f"Task {self.name} completed on {current_date}")
        
    def check_deadline(self, current_date: datetime) -> bool:
        """Check if task is behind schedule"""
        if self.deadline and self.end_date and self.end_date > self.deadline:
            self.status = TaskStatus.DELAYED
            logger.warning(f"Task {self.name} missed deadline")
            return False
        return True

class ConstructionProject:
    """Manages a complete industrial construction project"""
    
    def __init__(self, name: str, start_date: datetime):
        """
        Initialize a construction project.
        
        Args:
            name: Name of the project
            start_date: Project start date
        """
        self.name = name
        self.start_date = start_date
        self.tasks: Dict[str, ConstructionTask] = {}
        self.completed_tasks = 0
        self.delayed_tasks = 0
        self.safety_incidents = 0
        
    def add_task(self, task: ConstructionTask):
        """Add a task to the project"""
        if task.name in self.tasks:
            raise ValueError(f"Task {task.name} already exists in project")
        self.tasks[task.name] = task
        
    def get_task(self, task_name: str) -> ConstructionTask:
        """Retrieve a task by name"""
        if task_name not in self.tasks:
            raise ValueError(f"Task {task_name} not found in project")
        return self.tasks[task_name]
        
    def can_start_task(self, task_name: str) -> bool:
        """Check if a task can be started (dependencies met)"""
        task = self.get_task(task_name)
        
        # Check if all dependencies are completed
        for dep_name in task.dependencies:
            dep = self.get_task(dep_name)
            if dep.status != TaskStatus.COMPLETED:
                return False
                
        return True
        
    def update_project_status(self, current_date: datetime):
        """Update status of all tasks in the project"""
        for task in self.tasks.values():
            if task.status == TaskStatus.IN_PROGRESS:
                if task.end_date and task.end_date <= current_date:
                    task.complete(current_date)
                    self.completed_tasks += 1
                    
            if task.deadline and not task.check_deadline(current_date):
                self.delayed_tasks += 1
                
    def get_project_progress(self) -> float:
        """Calculate project completion percentage"""
        if not self.tasks:
            return 0.0
        return (self.completed_tasks / len(self.tasks)) * 100
        
    def record_safety_incident(self):
        """Record a safety incident in the project"""
        self.safety_incidents += 1
        logger.error("Safety incident recorded")
        
    def generate_safety_report(self) -> Dict[str, int]:
        """Generate a report of safety checks"""
        report = {
            "total_checks": 0,
            "passed_checks": 0,
            "failed_checks": 0,
            "critical_failures": 0
        }
        
        for task in self.tasks.values():
            for check_name, passed in task.safety_checks:
                report["total_checks"] += 1
                if passed:
                    report["passed_checks"] += 1
                else:
                    report["failed_checks"] += 1
                    if task.safety_level == SafetyLevel.CRITICAL:
                        report["critical_failures"] += 1
                        
        return report

class ProjectScheduler:
    """Schedules and manages construction project timelines"""
    
    def __init__(self, project: ConstructionProject):
        self.project = project
        self.current_date = project.start_date
        
    def advance_time(self, days: int = 1):
        """Advance the project timeline by specified days"""
        self.current_date += timedelta(days=days)
        self.project.update_project_status(self.current_date)
        
    def run_task(self, task_name: str):
        """Attempt to start and complete a task"""
        task = self.project.get_task(task_name)
        
        if not self.project.can_start_task(task_name):
            raise ValueError(f"Cannot start task {task_name} - dependencies not met")
            
        task.start(self.current_date)
        task.complete(self.current_date + task.duration)
        
    def get_critical_path(self) -> List[str]:
        """Calculate critical path for the project"""
        # Simplified implementation - would be more complex in real scenario
        critical_path = []
        remaining_tasks = set(self.project.tasks.keys())
        
        while remaining_tasks:
            # Find tasks with all dependencies met
            available = [
                t for t in remaining_tasks 
                if all(dep not in remaining_tasks for dep in self.project.tasks[t].dependencies)
            ]
            
            if not available:
                raise ValueError("Circular dependency detected in project tasks")
                
            # Select task with latest deadline (simplified critical path)
            selected = max(
                available,
                key=lambda t: self.project.tasks[t].deadline or datetime.max
            )
            
            critical_path.append(selected)
            remaining_tasks.remove(selected)
            
        return critical_path

# Example usage
if __name__ == "__main__":
    # Create a project
    project = ConstructionProject("Factory Construction", datetime.now())
    
    # Define tasks
    tasks = [
        ConstructionTask(
            "Site Preparation",
            timedelta(days=10),
            SafetyLevel.HIGH,
            deadline=datetime.now() + timedelta(days=15)
        ),
        ConstructionTask(
            "Foundation Work",
            timedelta(days=20),
            SafetyLevel.CRITICAL,
            dependencies=["Site Preparation"],
            deadline=datetime.now() + timedelta(days=40)
        ),
        ConstructionTask(
            "Structural Steel",
            timedelta(days=30),
            SafetyLevel.CRITICAL,
            dependencies=["Foundation Work"],
            deadline=datetime.now() + timedelta(days=75)
        ),
        ConstructionTask(
            "Electrical Installation",
            timedelta(days=15),
            SafetyLevel.MEDIUM,
            dependencies=["Structural Steel"],
            deadline=datetime.now() + timedelta(days=95)
        ),
        ConstructionTask(
            "Final Inspection",
            timedelta(days=5),
            SafetyLevel.HIGH,
            dependencies=["Electrical Installation"],
