"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: Generate a code snippet for a construction project management tool that tracks underground construction work, referencing URANPRES's expertise in underground and engineering construction.
Generated: DETERMINISTIC_396704f3559997c5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management Tool for Underground Work
Inspired by URANPRES's expertise in underground and engineering construction.

This module provides functionality to track underground construction projects,
including progress monitoring, resource allocation, and safety compliance.
"""

import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict


class ConstructionPhase(Enum):
    """Enum representing different phases of underground construction."""
    PLANNING = auto()
    EXCAVATION = auto()
    SUPPORT_INSTALLATION = auto()
    UTILITY_INSTALLATION = auto()
    BACKFILLING = auto()
    COMPLETION = auto()


class SafetyStatus(Enum):
    """Enum representing safety compliance status."""
    COMPLIANT = auto()
    WARNING = auto()
    NON_COMPLIANT = auto()
    EMERGENCY = auto()


@dataclass
class UndergroundConstructionSite:
    """Data class representing an underground construction site."""
    project_id: str
    project_name: str
    location: str
    depth: float  # in meters
    start_date: datetime.date
    estimated_completion: datetime.date
    current_phase: ConstructionPhase
    safety_status: SafetyStatus
    progress_percentage: float
    resources: Dict[str, int]  # resource_name: quantity


class UndergroundConstructionTracker:
    """Main class for tracking underground construction projects."""
    
    def __init__(self):
        self.projects: Dict[str, UndergroundConstructionSite] = {}
    
    def add_project(self, project: UndergroundConstructionSite) -> None:
        """Add a new underground construction project to track."""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
    
    def update_project_phase(self, project_id: str, new_phase: ConstructionPhase) -> None:
        """Update the construction phase of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].current_phase = new_phase
    
    def update_safety_status(self, project_id: str, new_status: SafetyStatus) -> None:
        """Update the safety status of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        self.projects[project_id].safety_status = new_status
    
    def update_progress(self, project_id: str, progress: float) -> None:
        """Update the progress percentage of a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        if not 0 <= progress <= 100:
            raise ValueError("Progress must be between 0 and 100")
        self.projects[project_id].progress_percentage = progress
    
    def allocate_resources(self, project_id: str, resource_name: str, quantity: int) -> None:
        """Allocate resources to a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if resource_name in self.projects[project_id].resources:
            self.projects[project_id].resources[resource_name] += quantity
        else:
            self.projects[project_id].resources[resource_name] = quantity
    
    def get_project(self, project_id: str) -> UndergroundConstructionSite:
        """Retrieve a project by its ID."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        return self.projects[project_id]
    
    def get_projects_by_phase(self, phase: ConstructionPhase) -> List[UndergroundConstructionSite]:
        """Retrieve all projects in a specific construction phase."""
        return [p for p in self.projects.values() if p.current_phase == phase]
    
    def get_projects_by_safety_status(self, status: SafetyStatus) -> List[UndergroundConstructionSite]:
        """Retrieve all projects with a specific safety status."""
        return [p for p in self.projects.values() if p.safety_status == status]
    
    def generate_project_report(self, project_id: str) -> Dict:
        """Generate a comprehensive report for a project."""
        project = self.get_project(project_id)
        return {
            "project_id": project.project_id,
            "project_name": project.project_name,
            "location": project.location,
            "current_phase": project.current_phase.name,
            "safety_status": project.safety_status.name,
            "progress": f"{project.progress_percentage}%",
            "days_remaining": (project.estimated_completion - datetime.date.today()).days,
            "resources": project.resources
        }


# Example usage
if __name__ == "__main__":
    tracker = UndergroundConstructionTracker()
    
    # Create a sample project
    sample_project = UndergroundConstructionSite(
        project_id="UC-2023-001",
        project_name="Metro Line Extension",
        location="Downtown Area",
        depth=25.5,
        start_date=datetime.date(2023, 1, 15),
        estimated_completion=datetime.date(2024, 6, 30),
        current_phase=ConstructionPhase.EXCAVATION,
        safety_status=SafetyStatus.COMPLIANT,
        progress_percentage=35.0,
        resources={"excavators": 3, "workers": 25}
    )
    
    # Add and manage the project
    tracker.add_project(sample_project)
    tracker.allocate_resources("UC-2023-001", "support_beams", 150)
    tracker.update_progress("UC-2023-001", 37.5)
    
    # Generate a report
    report = tracker.generate_project_report("UC-2023-001")
    print(report)
```
