"""
Generated Code Metadata:
========================
Original URL: https://allocation-optimismdao.app
Prompt: Generate code for a simple DAO that allocates funds to different projects based on a set of predefined rules.
Generated: DETERMINISTIC_633497387515e242
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_dao.py

from typing import Dict, List
from enum import Enum

class ProjectStatus(Enum):
    """Project status enumeration"""
    PENDING = 1
    ACTIVE = 2
    INACTIVE = 3

class Project:
    """Project data model"""
    def __init__(self, id: int, name: str, status: ProjectStatus):
        self.id = id
        self.name = name
        self.status = status
        self.allocated_funds = 0.0

class AllocationRule:
    """Allocation rule data model"""
    def __init__(self, project_status: ProjectStatus, allocation_percentage: float):
        self.project_status = project_status
        self.allocation_percentage = allocation_percentage

class ProjectDAO:
    """Project DAO class"""
    def __init__(self, total_funds: float, allocation_rules: List[AllocationRule]):
        self.total_funds = total_funds
        self.allocation_rules = allocation_rules
        self.projects: Dict[int, Project] = {}

    def add_project(self, project: Project):
        """Add a project to the DAO"""
        self.projects[project.id] = project

    def allocate_funds(self):
        """Allocate funds to projects based on predefined rules"""
        try:
            total_allocation_percentage = sum(rule.allocation_percentage for rule in self.allocation_rules)
            if total_allocation_percentage != 100.0:
                raise ValueError("Total allocation percentage must be 100.0")

            remaining_funds = self.total_funds
            for rule in self.allocation_rules:
                projects_matching_rule = [project for project in self.projects.values() if project.status == rule.project_status]
                allocation_amount = (rule.allocation_percentage / 100.0) * self.total_funds

                for project in projects_matching_rule:
                    project.allocated_funds = allocation_amount
                    remaining_funds -= allocation_amount

            if remaining_funds > 0.0:
                # Distribute remaining funds evenly among active projects
                active_projects = [project for project in self.projects.values() if project.status == ProjectStatus.ACTIVE]
                if active_projects:
                    remaining_funds_per_project = remaining_funds / len(active_projects)
                    for project in active_projects:
                        project.allocated_funds += remaining_funds_per_project

        except Exception as e:
            print(f"Error allocating funds: {str(e)}")

    def get_project(self, project_id: int) -> Project:
        """Get a project by ID"""
        return self.projects.get(project_id)

    def get_all_projects(self) -> List[Project]:
        """Get all projects"""
        return list(self.projects.values())

# Example usage
if __name__ == "__main__":
    # Create allocation rules
    allocation_rules = [
        AllocationRule(ProjectStatus.ACTIVE, 60.0),
        AllocationRule(ProjectStatus.PENDING, 20.0),
        AllocationRule(ProjectStatus.INACTIVE, 20.0)
    ]

    # Create project DAO
    total_funds = 10000.0
    project_dao = ProjectDAO(total_funds, allocation_rules)

    # Create projects
    project1 = Project(1, "Project 1", ProjectStatus.ACTIVE)
    project2 = Project(2, "Project 2", ProjectStatus.PENDING)
    project3 = Project(3, "Project 3", ProjectStatus.INACTIVE)

    # Add projects to DAO
    project_dao.add_project(project1)
    project_dao.add_project(project2)
    project_dao.add_project(project3)

    # Allocate funds
    project_dao.allocate_funds()

    # Print allocated funds
    for project in project_dao.get_all_projects():
        print(f"Project {project.name} (ID: {project.id}) - Allocated funds: {project.allocated_funds}")
```
