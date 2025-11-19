"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: Develop a Python-based solution for fiscalization and consultancy in civil engineering projects, aligned with Puma Ipce's specialized services.
Generated: DETERMINISTIC_8b9ac4b6ad6fada2
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Fiscalization and Consultancy System for Civil Engineering Projects
Aligned with Puma Ipce's specialized services.

This module provides functionalities for fiscalization, cost estimation,
and consultancy services for civil engineering projects.
"""

import logging
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
from datetime import date
import json
import csv
from pathlib import Path
from decimal import Decimal, getcontext

# Configure decimal precision
getcontext().prec = 6

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProjectStatus(Enum):
    """Enumeration for project status."""
    PLANNING = auto()
    ONGOING = auto()
    COMPLETED = auto()
    SUSPENDED = auto()


class ServiceType(Enum):
    """Enumeration for service types."""
    FISCALIZATION = auto()
    COST_ESTIMATION = auto()
    TECHNICAL_CONSULTANCY = auto()
    QUALITY_CONTROL = auto()
    PROJECT_MANAGEMENT = auto()


@dataclass
class Project:
    """Dataclass representing a civil engineering project."""
    project_id: str
    name: str
    client: str
    start_date: date
    end_date: Optional[date]
    budget: Decimal
    status: ProjectStatus
    services: List[ServiceType]
    description: str = ""


class FiscalizationEngine:
    """Core engine for fiscalization and consultancy services."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load project data from storage if available."""
        try:
            data_file = Path("projects_data.json")
            if data_file.exists():
                with open(data_file, 'r') as f:
                    data = json.load(f)
                    for project_data in data:
                        project = Project(
                            project_id=project_data['project_id'],
                            name=project_data['name'],
                            client=project_data['client'],
                            start_date=date.fromisoformat(project_data['start_date']),
                            end_date=date.fromisoformat(project_data['end_date']) if project_data['end_date'] else None,
                            budget=Decimal(project_data['budget']),
                            status=ProjectStatus[project_data['status']],
                            services=[ServiceType[service] for service in project_data['services']],
                            description=project_data.get('description', '')
                        )
                        self.projects[project.project_id] = project
                logger.info("Project data loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading project data: {e}")
    
    def _save_data(self) -> None:
        """Save project data to storage."""
        try:
            data = []
            for project in self.projects.values():
                project_data = {
                    'project_id': project.project_id,
                    'name': project.name,
                    'client': project.client,
                    'start_date': project.start_date.isoformat(),
                    'end_date': project.end_date.isoformat() if project.end_date else None,
                    'budget': str(project.budget),
                    'status': project.status.name,
                    'services': [service.name for service in project.services],
                    'description': project.description
                }
                data.append(project_data)
            
            with open("projects_data.json", 'w') as f:
                json.dump(data, f, indent=4)
            logger.info("Project data saved successfully.")
        except Exception as e:
            logger.error(f"Error saving project data: {e}")
    
    def create_project(self, project_data: Dict) -> str:
        """Create a new project."""
        try:
            project_id = f"PRJ-{len(self.projects) + 1:04d}"
            project = Project(
                project_id=project_id,
                name=project_data['name'],
                client=project_data['client'],
                start_date=date.fromisoformat(project_data['start_date']),
                end_date=date.fromisoformat(project_data['end_date']) if project_data.get('end_date') else None,
                budget=Decimal(project_data['budget']),
                status=ProjectStatus[project_data.get('status', 'PLANNING')],
                services=[ServiceType[service] for service in project_data.get('services', [])],
                description=project_data.get('description', '')
            )
            self.projects[project_id] = project
            self._save_data()
            logger.info(f"Project {project_id} created successfully.")
            return project_id
        except Exception as e:
            logger.error(f"Error creating project: {e}")
            raise ValueError(f"Failed to create project: {e}")
    
    def update_project(self, project_id: str, update_data: Dict) -> None:
        """Update an existing project."""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found.")
        
        try:
            project = self.projects[project_id]
            
            if 'name' in update_data:
                project.name = update_data['name']
            if 'client' in update_data:
                project.client = update_data['client']
            if 'start_date' in update_data:
                project.start_date = date.fromisoformat(update_data['start_date'])
            if 'end_date' in update_data:
                project.end_date = date.fromisoformat(update_data['end_date']) if update_data['end_date'] else None
            if 'budget' in update_data:
                project.budget = Decimal(update_data['budget'])
            if 'status' in update_data:
                project.status = ProjectStatus[update_data['status']]
            if 'services' in update_data:
                project.services = [ServiceType[service] for service in update_data['services']]
            if 'description' in update_data:
                project.description = update_data['description']
            
            self._save_data()
            logger.info(f"Project {project_id} updated successfully.")
        except Exception as e:
            logger.error(f"Error updating project {project_id}: {e}")
            raise ValueError(f"Failed to update project: {e}")
    
    def get_project(self, project_id: str) -> Dict:
        """Retrieve project details."""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found.")
        
        project = self.projects[project_id]
        return {
            'project_id': project.project_id,
            'name': project.name,
            'client': project.client,
            'start_date': project.start_date.isoformat(),
            'end_date': project.end_date.isoformat() if project.end_date else None,
            'budget': float(project.budget),
            'status': project.status.name,
            'services': [service.name for service in project.services],
            'description': project.description
        }
    
    def list_projects(self) -> List[Dict]:
        """List all projects."""
        return [self.get_project(pid) for pid in self.projects.keys()]
    
    def generate_cost_report(self, project_id: str) -> Dict:
        """Generate a cost report for a project."""
        if project_id not in self.projects:
            raise ValueError(f"Project {project_id} not found.")
        
        project = self.projects[project_id]
        return {
            'project_id': project.project_id,
            'project_name': project.name,
            'total_budget': float(project.budget),
            'services': [service.name for service in project.services],
            'status': project.status.name,
            'duration_days': (project.end_date - project.start_date).days if project.end_date else None
        }
    
    def export_to_csv(self, file_path: str) -> None:
        """Export all projects to a CSV file."""
        try:
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = [
                    'project_id', 'name', 'client', 'start_date', 'end_date',
                    'budget', 'status', 'services', 'description'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for project in self.projects.values():
                    writer.writerow({
                        'project_id': project.project_id,
                        'name': project.name,
                        'client': project.client,
                        'start_date': project.start_date.isoformat(),
                        'end_date': project.end_date.isoformat() if project.end_date else '',
                        'budget': str(project.budget),
                        'status': project.status.name,
                        'services': ', '.join([s.name for s in project.services]),
                        'description': project.description
                    })
            logger.info(f"Projects exported to {file_path} successfully.")
        except Exception as e:
            logger.error(f"Error exporting to CSV: {e}")
            raise ValueError(f"Failed to export to CSV: {e}")


# Example usage
if __name__ == "__main__":
    engine = FiscalizationEngine()
    
    # Create a new project
    new_project = {
        'name
