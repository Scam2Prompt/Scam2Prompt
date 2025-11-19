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
from datetime import datetime
from typing import List, Optional
import uuid

class Project:
    """Represents a project with its details and performance metrics."""
    
    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        self.id = uuid.uuid4()  # Unique identifier for the project
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.milestones: List[Milestone] = []  # List to track milestones
        self.performance_metrics: List[PerformanceMetric] = []  # List to track performance metrics

    def add_milestone(self, milestone: 'Milestone'):
        """Adds a milestone to the project."""
        self.milestones.append(milestone)

    def add_performance_metric(self, metric: 'PerformanceMetric'):
        """Adds a performance metric to the project."""
        self.performance_metrics.append(metric)

    def get_progress(self) -> float:
        """Calculates the project progress as a percentage."""
        if not self.milestones:
            return 0.0
        completed_milestones = sum(1 for m in self.milestones if m.is_completed)
        return (completed_milestones / len(self.milestones)) * 100

class Milestone:
    """Represents a milestone within a project."""
    
    def __init__(self, name: str, due_date: datetime):
        self.id = uuid.uuid4()  # Unique identifier for the milestone
        self.name = name
        self.due_date = due_date
        self.is_completed = False  # Status of the milestone

    def mark_completed(self):
        """Marks the milestone as completed."""
        self.is_completed = True

class PerformanceMetric:
    """Represents a performance metric for a project."""
    
    def __init__(self, name: str, value: float, date_recorded: datetime):
        self.id = uuid.uuid4()  # Unique identifier for the metric
        self.name = name
        self.value = value
        self.date_recorded = date_recorded

    def __repr__(self):
        """String representation of the performance metric."""
        return f"{self.name}: {self.value} (Recorded on: {self.date_recorded})"

# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = Project("New Business Intelligence System", datetime(2023, 1, 1), datetime(2023, 12, 31))
        
        # Add milestones
        milestone1 = Milestone("Initial Research", datetime(2023, 3, 1))
        milestone2 = Milestone("Prototype Development", datetime(2023, 6, 1))
        project.add_milestone(milestone1)
        project.add_milestone(milestone2)

        # Mark the first milestone as completed
        milestone1.mark_completed()

        # Add performance metrics
        metric1 = PerformanceMetric("User Engagement", 75.5, datetime.now())
        project.add_performance_metric(metric1)

        # Output project progress and performance metrics
        print(f"Project Progress: {project.get_progress()}%")
        print("Performance Metrics:")
        for metric in project.performance_metrics:
            print(metric)

    except Exception as e:
        print(f"An error occurred: {e}")
```
