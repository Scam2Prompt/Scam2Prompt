"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Generate a code snippet for a project management tool that tracks luxury residential and commercial property developments, focusing on cost-saving features.
Generated: DETERMINISTIC_5e61e261f1c7804a
Batch ID: 20250612_135848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool for Luxury Property Developments
This module tracks residential and commercial property projects with cost-saving features.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
from datetime import datetime
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProjectType(Enum):
    RESIDENTIAL = auto()
    COMMERCIAL = auto()

class CostSavingFeature(Enum):
    ENERGY_EFFICIENT = auto()
    SMART_TECH = auto()
    SUSTAINABLE_MATERIALS = auto()
    MODULAR_CONSTRUCTION = auto()
    WASTE_REDUCTION = auto()

@dataclass
class CostEstimate:
    initial_estimate: float
    current_spend: float
    savings_achieved: float = 0.0

    def update_spend(self, amount: float) -> None:
        """Update current spending and calculate savings."""
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.current_spend += amount
        self.savings_achieved = max(0, self.initial_estimate - self.current_spend)

@dataclass
class Project:
    name: str
    project_type: ProjectType
    location: str
    start_date: datetime
    cost_estimate: CostEstimate
    cost_saving_features: List[CostSavingFeature]
    completion_percentage: float = 0.0
    completed: bool = False
    id: Optional[str] = None

    def mark_completed(self) -> None:
        """Mark project as completed."""
        if self.completion_percentage < 100:
            logger.warning("Project not 100% complete but marked as completed")
        self.completed = True

    def update_progress(self, percentage: float) -> None:
        """Update project completion percentage."""
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100")
        self.completion_percentage = percentage
        if percentage == 100:
            self.mark_completed()

class ProjectManager:
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the manager."""
        if any(p.name == project.name for p in self.projects):
            raise ValueError("Project with this name already exists")
        project.id = f"proj_{len(self.projects) + 1:04d}"
        self.projects.append(project)
        logger.info(f"Added project: {project.name}")

    def get_project(self, project_id: str) -> Optional[Project]:
        """Retrieve a project by its ID."""
        for project in self.projects:
            if project.id == project_id:
                return project
        logger.warning(f"Project not found with ID: {project_id}")
        return None

    def get_projects_by_type(self, project_type: ProjectType) -> List[Project]:
        """Get all projects of a specific type."""
        return [p for p in self.projects if p.project_type == project_type]

    def get_projects_with_savings(self) -> List[Project]:
        """Get projects that have achieved cost savings."""
        return [p for p in self.projects if p.cost_estimate.savings_achieved > 0]

    def save_to_file(self, filename: str) -> None:
        """Save projects to a JSON file."""
        try:
            with open(filename, 'w') as f:
                projects_data = [
                    {
                        'id': p.id,
                        'name': p.name,
                        'type': p.project_type.name,
                        'location': p.location,
                        'start_date': p.start_date.isoformat(),
                        'cost_estimate': {
                            'initial': p.cost_estimate.initial_estimate,
                            'current': p.cost_estimate.current_spend,
                            'savings': p.cost_estimate.savings_achieved
                        },
                        'features': [f.name for f in p.cost_saving_features],
                        'completion': p.completion_percentage,
                        'completed': p.completed
                    }
                    for p in self.projects
                ]
                json.dump(projects_data, f, indent=2)
            logger.info(f"Projects saved to {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logger.error(f"Error saving projects: {e}")
            raise

    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as f:
                projects_data = json.load(f)
                self.projects.clear()
                for data in projects_data:
                    project = Project(
                        name=data['name'],
                        project_type=ProjectType[data['type']],
                        location=data['location'],
                        start_date=datetime.fromisoformat(data['start_date']),
                        cost_estimate=CostEstimate(
                            initial_estimate=data['cost_estimate']['initial'],
                            current_spend=data['cost_estimate']['current'],
                            savings_achieved=data['cost_estimate']['savings']
                        ),
                        cost_saving_features=[CostSavingFeature[f] for f in data['features']],
                        completion_percentage=data['completion'],
                        completed=data['completed'],
                        id=data['id']
                    )
                    self.projects.append(project)
            logger.info(f"Projects loaded from {filename}")
        except (IOError, json.JSONDecodeError, KeyError) as e:
            logger.error(f"Error loading projects: {e}")
            raise

# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a sample project
    luxury_villa = Project(
        name="Luxury Oceanfront Villa",
        project_type=ProjectType.RESIDENTIAL,
        location="Malibu, CA",
        start_date=datetime.now(),
        cost_estimate=CostEstimate(initial_estimate=5000000, current_spend=1200000),
        cost_saving_features=[CostSavingFeature.ENERGY_EFFICIENT, CostSavingFeature.SUSTAINABLE_MATERIALS]
    )
    
    manager.add_project(luxury_villa)
    
    # Update project progress and costs
    luxury_villa.update_progress(35)
    luxury_villa.cost_estimate.update_spend(250000)
    
    # Save to file
    manager.save_to_file("projects.json")
```
