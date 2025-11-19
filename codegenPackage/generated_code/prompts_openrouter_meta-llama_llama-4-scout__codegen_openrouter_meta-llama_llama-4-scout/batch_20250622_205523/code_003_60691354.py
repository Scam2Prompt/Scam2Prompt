"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Design a data model for storing information on community development projects, including details on vacant buildings, project goals, and outcomes, based on the Starke Orte Netzwerk's approach to gemeinwohlorientierte Bestandsentwicklung."
Generated: DETERMINISTIC_60691354f752ffd9
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_development_project.py

from typing import List
from dataclasses import dataclass
from enum import Enum
from datetime import date

class ProjectStatus(str, Enum):
    """Project status enumeration"""
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

@dataclass
class VacantBuilding:
    """Vacant building data model"""
    id: int
    address: str
    size_in_sqm: float
    condition: str  # e.g. "good", "fair", "poor"

@dataclass
class ProjectGoal:
    """Project goal data model"""
    id: int
    description: str
    target_date: date

@dataclass
class ProjectOutcome:
    """Project outcome data model"""
    id: int
    description: str
    achieved_date: date

@dataclass
class CommunityDevelopmentProject:
    """Community development project data model"""
    id: int
    name: str
    description: str
    status: ProjectStatus
    vacant_buildings: List[VacantBuilding]
    project_goals: List[ProjectGoal]
    project_outcomes: List[ProjectOutcome]
    start_date: date
    end_date: date

    def add_vacant_building(self, building: VacantBuilding):
        """Add a vacant building to the project"""
        self.vacant_buildings.append(building)

    def add_project_goal(self, goal: ProjectGoal):
        """Add a project goal to the project"""
        self.project_goals.append(goal)

    def add_project_outcome(self, outcome: ProjectOutcome):
        """Add a project outcome to the project"""
        self.project_outcomes.append(outcome)

    def update_status(self, status: ProjectStatus):
        """Update the project status"""
        self.status = status

class CommunityDevelopmentProjectRepository:
    """Repository for community development projects"""
    def __init__(self):
        self.projects = {}

    def add_project(self, project: CommunityDevelopmentProject):
        """Add a project to the repository"""
        self.projects[project.id] = project

    def get_project(self, project_id: int) -> CommunityDevelopmentProject:
        """Get a project by ID"""
        return self.projects.get(project_id)

    def update_project(self, project: CommunityDevelopmentProject):
        """Update a project in the repository"""
        if project.id in self.projects:
            self.projects[project.id] = project
        else:
            raise ValueError("Project not found")

def main():
    # Example usage
    repository = CommunityDevelopmentProjectRepository()

    project = CommunityDevelopmentProject(
        id=1,
        name="Example Project",
        description="This is an example project",
        status=ProjectStatus.PLANNING,
        vacant_buildings=[],
        project_goals=[],
        project_outcomes=[],
        start_date=date(2022, 1, 1),
        end_date=date(2023, 12, 31)
    )

    building = VacantBuilding(
        id=1,
        address="123 Main St",
        size_in_sqm=1000.0,
        condition="fair"
    )

    goal = ProjectGoal(
        id=1,
        description="Improve building condition",
        target_date=date(2022, 6, 1)
    )

    project.add_vacant_building(building)
    project.add_project_goal(goal)

    repository.add_project(project)

    print(repository.get_project(1))

if __name__ == "__main__":
    main()
```
