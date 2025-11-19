"""
Generated Code Metadata:
========================
Original URL: https://timeformecenter.com
Prompt: "Discuss the benefits of using a centralized time management service for freelancers."
Generated: DETERMINISTIC_96bb382fe2219c1d
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
A centralized time management service for freelancers to track work hours, manage projects,
and generate invoices. This service provides benefits like automated time tracking, reporting,
and integration with payment systems.
"""

import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class TimeEntry:
    """Represents a single time entry for a freelancer's work."""
    project_id: str
    task_description: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    duration: datetime.timedelta = None

    def __post_init__(self):
        """Calculate duration if not provided."""
        if self.duration is None:
            self.duration = self.end_time - self.start_time

@dataclass
class Project:
    """Represents a freelancer's project."""
    project_id: str
    client_name: str
    hourly_rate: float
    time_entries: List[TimeEntry] = None

    def __post_init__(self):
        """Initialize time entries list if not provided."""
        if self.time_entries is None:
            self.time_entries = []

class TimeManagementService:
    """Centralized service for freelancers to manage their time and projects."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
    
    def add_project(self, project: Project) -> None:
        """Add a new project to the service."""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
    
    def log_time_entry(self, project_id: str, time_entry: TimeEntry) -> None:
        """Log a time entry for a specific project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].time_entries.append(time_entry)
    
    def get_project_hours(self, project_id: str) -> float:
        """Calculate total hours worked on a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        
        total_seconds = sum(
            (entry.duration.total_seconds() for entry in self.projects[project_id].time_entries),
            0.0
        )
        return total_seconds / 3600
    
    def generate_invoice(self, project_id: str) -> Dict[str, float]:
        """Generate invoice data for a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        
        project = self.projects[project_id]
        total_hours = self.get_project_hours(project_id)
        total_amount = total_hours * project.hourly_rate
        
        return {
            "client_name": project.client_name,
            "total_hours": total_hours,
            "hourly_rate": project.hourly_rate,
            "total_amount": total_amount,
            "time_entries": [
                {
                    "description": entry.task_description,
                    "date": entry.start_time.date().isoformat(),
                    "hours": entry.duration.total_seconds() / 3600
                }
                for entry in project.time_entries
            ]
        }
    
    def get_time_report(self, start_date: datetime.date, end_date: datetime.date) -> Dict[str, float]:
        """Generate a time report for all projects within a date range."""
        report = {}
        
        for project_id, project in self.projects.items():
            project_hours = 0.0
            for entry in project.time_entries:
                if start_date <= entry.start_time.date() <= end_date:
                    project_hours += entry.duration.total_seconds() / 3600
            
            if project_hours > 0:
                report[project_id] = {
                    "client_name": project.client_name,
                    "total_hours": project_hours,
                    "earnings": project_hours * project.hourly_rate
                }
        
        return report

# Example usage
if __name__ == "__main__":
    service = TimeManagementService()
    
    # Add a project
    project = Project(
        project_id="proj_123",
        client_name="Acme Corp",
        hourly_rate=50.0
    )
    service.add_project(project)
    
    # Log time entries
    today = datetime.datetime.now()
    service.log_time_entry("proj_123", TimeEntry(
        project_id="proj_123",
        task_description="Develop API endpoints",
        start_time=today.replace(hour=9, minute=0),
        end_time=today.replace(hour=12, minute=30)
    ))
    
    service.log_time_entry("proj_123", TimeEntry(
        project_id="proj_123",
        task_description="Code review",
        start_time=today.replace(hour=13, minute=30),
        end_time=today.replace(hour=15, minute=0)
    ))
    
    # Generate invoice
    invoice = service.generate_invoice("proj_123")
    print("Invoice:", invoice)
    
    # Generate time report
    report = service.get_time_report(
        start_date=today.date() - datetime.timedelta(days=7),
        end_date=today.date()
    )
    print("Weekly Report:", report)
```
