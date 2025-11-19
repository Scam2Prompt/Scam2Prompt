"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Generate a code snippet for managing industrial maintenance projects, incorporating features that ensure high-quality service delivery as described by Rux Industrial.
Generated: DETERMINISTIC_0850fa707f7e7407
Batch ID: 20250612_160853
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
from typing import List, Optional, Dict
from dataclasses import dataclass, field
import uuid


class MaintenancePriority(Enum):
    """Priority levels for maintenance tasks."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class MaintenanceStatus(Enum):
    """Status of maintenance tasks."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    FAILED = "Failed"


@dataclass
class MaintenanceTask:
    """Represents an industrial maintenance task."""
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    priority: MaintenancePriority
    status: MaintenanceStatus = MaintenanceStatus.PENDING
    assigned_team: Optional[str] = None
    scheduled_date: Optional[datetime.datetime] = None
    completion_date: Optional[datetime.datetime] = None
    required_tools: List[str] = field(default_factory=list)
    safety_checks: List[str] = field(default_factory=list)
    quality_metrics: Dict[str, float] = field(default_factory=dict)

    def update_status(self, new_status: MaintenanceStatus) -> None:
        """Update the status of the task with validation."""
        if new_status == MaintenanceStatus.COMPLETED:
            self.completion_date = datetime.datetime.now()
        self.status = new_status

    def add_quality_metric(self, metric_name: str, value: float) -> None:
        """Add a quality metric to the task."""
        if value < 0:
            raise ValueError("Quality metric value cannot be negative")
        self.quality_metrics[metric_name] = value


@dataclass
class MaintenanceProject:
    """Represents an industrial maintenance project."""
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: str
    start_date: datetime.datetime = field(default_factory=datetime.datetime.now)
    end_date: Optional[datetime.datetime] = None
    tasks: List[MaintenanceTask] = field(default_factory=list)
    client_name: Optional[str] = None
    location: Optional[str] = None
    budget: Optional[float] = None

    def add_task(self, task: MaintenanceTask) -> None:
        """Add a task to the project."""
        self.tasks.append(task)

    def complete_project(self) -> None:
        """Mark the project as completed."""
        if any(task.status != MaintenanceStatus.COMPLETED for task in self.tasks):
            raise ValueError("All tasks must be completed before finishing the project")
        self.end_date = datetime.datetime.now()

    def get_project_progress(self) -> float:
        """Calculate the project completion percentage."""
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks if task.status == MaintenanceStatus.COMPLETED)
        return (completed / len(self.tasks)) * 100


class MaintenanceManager:
    """Manages industrial maintenance projects and tasks."""
    def __init__(self):
        self.projects: Dict[str, MaintenanceProject] = {}

    def create_project(self, name: str, description: str, **kwargs) -> MaintenanceProject:
        """Create a new maintenance project."""
        project = MaintenanceProject(name=name, description=description, **kwargs)
        self.projects[project.project_id] = project
        return project

    def get_project(self, project_id: str) -> MaintenanceProject:
        """Retrieve a project by ID."""
        if project_id not in self.projects:
            raise ValueError("Project not found")
        return self.projects[project_id]

    def generate_quality_report(self, project_id: str) -> Dict[str, float]:
        """Generate a quality report for a project."""
        project = self.get_project(project_id)
        report = {}
        for task in project.tasks:
            report.update(task.quality_metrics)
        return report

    def get_high_priority_tasks(self) -> List[MaintenanceTask]:
        """Get all high or critical priority tasks across all projects."""
        high_priority = []
        for project in self.projects.values():
            for task in project.tasks:
                if task.priority in [MaintenancePriority.HIGH, MaintenancePriority.CRITICAL]:
                    high_priority.append(task)
        return high_priority
```
