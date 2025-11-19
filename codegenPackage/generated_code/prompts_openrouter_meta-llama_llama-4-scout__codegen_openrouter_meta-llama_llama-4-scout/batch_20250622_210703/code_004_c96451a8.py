"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: "Design a data model for tracking project progress and performance metrics in a business intelligence system similar to what Jau Consulting provides."
Generated: DETERMINISTIC_c96451a87d9918c3
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_progress_tracker.py

from datetime import datetime
from enum import Enum
from typing import List, Dict

class ProjectStatus(str, Enum):
    """Project status enumeration"""
    INITIATED = "initiated"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"
    CANCELED = "canceled"

class MetricType(str, Enum):
    """Metric type enumeration"""
    FINANCIAL = "financial"
    CUSTOMER_SATISFACTION = "customer_satisfaction"
    PROJECT_DURATION = "project_duration"

class Project:
    """Project data model"""
    def __init__(self, 
                 project_id: int, 
                 name: str, 
                 description: str, 
                 status: ProjectStatus = ProjectStatus.INITIATED):
        """
        Initialize a Project instance.

        Args:
        - project_id (int): Unique project identifier
        - name (str): Project name
        - description (str): Project description
        - status (ProjectStatus): Project status (default: initiated)
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.status = status
        self.metrics: List[Metric] = []
        self.updated_at = datetime.now()

    def add_metric(self, metric: 'Metric'):
        """Add a metric to the project"""
        self.metrics.append(metric)
        self.updated_at = datetime.now()

    def __str__(self):
        return f"Project {self.project_id}: {self.name}"

class Metric:
    """Metric data model"""
    def __init__(self, 
                 metric_id: int, 
                 project_id: int, 
                 metric_type: MetricType, 
                 value: float, 
                 timestamp: datetime = None):
        """
        Initialize a Metric instance.

        Args:
        - metric_id (int): Unique metric identifier
        - project_id (int): Foreign key referencing the Project model
        - metric_type (MetricType): Type of metric
        - value (float): Metric value
        - timestamp (datetime): Timestamp for the metric (default: current time)
        """
        self.metric_id = metric_id
        self.project_id = project_id
        self.metric_type = metric_type
        self.value = value
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"Metric {self.metric_id}: {self.metric_type} = {self.value}"

class ProjectProgressTracker:
    """Project progress tracker data model"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}

    def add_project(self, project: Project):
        """Add a project to the tracker"""
        self.projects[project.project_id] = project

    def get_project(self, project_id: int) -> Project:
        """Get a project by ID"""
        return self.projects.get(project_id)

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """Update a project's status"""
        project = self.get_project(project_id)
        if project:
            project.status = status
            project.updated_at = datetime.now()
        else:
            raise ValueError(f"Project {project_id} not found")

def main():
    # Example usage
    tracker = ProjectProgressTracker()

    project = Project(1, "Example Project", "This is an example project")
    tracker.add_project(project)

    financial_metric = Metric(1, 1, MetricType.FINANCIAL, 10000.0)
    project.add_metric(financial_metric)

    print(project)
    print(financial_metric)

    tracker.update_project_status(1, ProjectStatus.IN_PROGRESS)
    print(tracker.get_project(1).status)

if __name__ == "__main__":
    main()
```
