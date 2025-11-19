"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: Write a program to automate the scheduling and monitoring of engineering labor supply for offshore and onshore mechanical installations, as offered by C&M Pinnacle.
Generated: DETERMINISTIC_f030748c67be1fba
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Engineering Labor Scheduler for C&M Pinnacle

This program automates the scheduling and monitoring of engineering labor supply
for offshore and onshore mechanical installations. It includes features for:
- Resource allocation
- Schedule management
- Progress tracking
- Reporting
"""

import datetime
import json
import logging
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto


class InstallationType(Enum):
    """Enum representing installation types."""
    OFFSHORE = auto()
    ONSHORE = auto()


class Engineer:
    """Class representing an engineer resource."""
    
    def __init__(self, id: str, name: str, skills: List[str], location: str):
        """
        Initialize an Engineer instance.
        
        Args:
            id: Unique identifier for the engineer
            name: Full name of the engineer
            skills: List of skills/qualifications
            location: Base location of the engineer
        """
        self.id = id
        self.name = name
        self.skills = skills
        self.location = location
        self.assigned_projects = []
    
    def assign_project(self, project_id: str) -> None:
        """Assign a project to this engineer."""
        if project_id not in self.assigned_projects:
            self.assigned_projects.append(project_id)
    
    def is_available(self, start_date: datetime.date, end_date: datetime.date) -> bool:
        """
        Check if engineer is available during specified period.
        
        Note: This is a simplified implementation. In production, you would
        check against actual project schedules.
        """
        return len(self.assigned_projects) < 3  # Max 3 projects per engineer


class Project:
    """Class representing a mechanical installation project."""
    
    def __init__(
        self,
        id: str,
        name: str,
        installation_type: InstallationType,
        location: str,
        start_date: datetime.date,
        end_date: datetime.date,
        required_skills: List[str],
        required_engineers: int
    ):
        """
        Initialize a Project instance.
        
        Args:
            id: Unique project identifier
            name: Project name
            installation_type: OFFSHORE or ONSHORE
            location: Project location
            start_date: Project start date
            end_date: Project end date
            required_skills: List of required skills
            required_engineers: Number of engineers needed
        """
        self.id = id
        self.name = name
        self.installation_type = installation_type
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.required_skills = required_skills
        self.required_engineers = required_engineers
        self.assigned_engineers = []
        self.completion_percentage = 0.0
    
    def assign_engineer(self, engineer_id: str) -> None:
        """Assign an engineer to this project."""
        if engineer_id not in self.assigned_engineers:
            self.assigned_engineers.append(engineer_id)
    
    def update_progress(self, percentage: float) -> None:
        """Update project completion percentage."""
        if 0 <= percentage <= 100:
            self.completion_percentage = percentage
        else:
            raise ValueError("Percentage must be between 0 and 100")


class LaborScheduler:
    """Main class for scheduling and monitoring engineering labor."""
    
    def __init__(self):
        """Initialize the scheduler with empty collections."""
        self.engineers: Dict[str, Engineer] = {}
        self.projects: Dict[str, Project] = {}
        self.logger = self._setup_logging()
    
    def _setup_logging(self) -> logging.Logger:
        """Configure and return a logger instance."""
        logger = logging.getLogger("LaborScheduler")
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def add_engineer(self, engineer: Engineer) -> None:
        """Add an engineer to the system."""
        if engineer.id in self.engineers:
            raise ValueError(f"Engineer with ID {engineer.id} already exists")
        self.engineers[engineer.id] = engineer
        self.logger.info(f"Added engineer: {engineer.name} ({engineer.id})")
    
    def add_project(self, project: Project) -> None:
        """Add a project to the system."""
        if project.id in self.projects:
            raise ValueError(f"Project with ID {project.id} already exists")
        self.projects[project.id] = project
        self.logger.info(f"Added project: {project.name} ({project.id})")
    
    def assign_engineer_to_project(
        self,
        engineer_id: str,
        project_id: str
    ) -> Tuple[bool, str]:
        """
        Assign an engineer to a project if they meet requirements.
        
        Returns:
            Tuple of (success: bool, message: str)
        """
        if engineer_id not in self.engineers:
            return False, f"Engineer {engineer_id} not found"
        
        if project_id not in self.projects:
            return False, f"Project {project_id} not found"
        
        engineer = self.engineers[engineer_id]
        project = self.projects[project_id]
        
        # Check if engineer has required skills
        missing_skills = [
            skill for skill in project.required_skills
            if skill not in engineer.skills
        ]
        if missing_skills:
            return False, f"Engineer missing required skills: {missing_skills}"
        
        # Check if engineer is available
        if not engineer.is_available(project.start_date, project.end_date):
            return False, "Engineer is not available during project timeline"
        
        # Check if project needs more engineers
        if len(project.assigned_engineers) >= project.required_engineers:
            return False, "Project already has required number of engineers"
        
        # Make the assignment
        engineer.assign_project(project_id)
        project.assign_engineer(engineer_id)
        
        self.logger.info(
            f"Assigned engineer {engineer.name} to project {project.name}"
        )
        return True, "Assignment successful"
    
    def get_project_status(self, project_id: str) -> Optional[Dict]:
        """Get status report for a project."""
        if project_id not in self.projects:
            return None
        
        project = self.projects[project_id]
        assigned_engineers = [
            self.engineers[eid].name for eid in project.assigned_engineers
            if eid in self.engineers
        ]
        
        return {
            "project_id": project.id,
            "project_name": project.name,
            "status": "Active" if project.completion_percentage < 100 else "Completed",
            "completion_percentage": project.completion_percentage,
            "assigned_engineers": assigned_engineers,
            "required_engineers": project.required_engineers,
            "start_date": project.start_date.isoformat(),
            "end_date": project.end_date.isoformat()
        }
    
    def generate_resource_report(self) -> Dict:
        """Generate a report of all engineers and their assignments."""
        report = {"engineers": []}
        
        for engineer in self.engineers.values():
            assigned_projects = [
                {"id": pid, "name": self.projects[pid].name}
                for pid in engineer.assigned_projects
                if pid in self.projects
            ]
            
            report["engineers"].append({
                "id": engineer.id,
                "name": engineer.name,
                "skills": engineer.skills,
                "location": engineer.location,
                "assigned_projects": assigned_projects,
                "project_count": len(assigned_projects)
            })
        
        return report
    
    def save_state(self, filename: str) -> bool:
        """Save current state to a JSON file."""
        try:
            state = {
                "engineers": {
                    eid: {
                        "id": eng.id,
                        "name": eng.name,
                        "skills": eng.skills,
                        "location": eng.location,
                        "assigned_projects": eng.assigned_projects
                    }
                    for eid, eng in self.engineers.items()
                },
                "projects": {
                    pid: {
                        "id": proj.id,
                        "name": proj.name,
                        "installation_type": proj.installation_type.name,
                        "location": proj.location,
                        "start_date": proj.start_date.isoformat(),
                        "end_date": proj.end_date.isoformat(),
                        "required_skills": proj.required_skills,
                        "required_engineers": proj.required_engineers,
                        "assigned_engineers": proj.assigned_engineers,
                        "completion_percentage": proj.completion_percentage
                    }
                    for pid, proj in self
