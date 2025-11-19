"""
Generated Code Metadata:
========================
Original URL: https://corelabs.pe
Prompt: Suggest tools and libraries for managing IT outsourcing projects, considering CoreLabs' emphasis on providing specialized IT talent for efficient technology implementation.
Generated: DETERMINISTIC_eaaee6e4d0b3f469
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management.py

import datetime
from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    DELAYED = 4

class Project:
    """Represents an IT outsourcing project"""
    def __init__(self, id: int, name: str, status: ProjectStatus, 
                 start_date: datetime.date, end_date: datetime.date, 
                 team_members: List[str]):
        """
        Initializes a Project instance.

        Args:
        id (int): Unique project identifier
        name (str): Project name
        status (ProjectStatus): Current project status
        start_date (datetime.date): Project start date
        end_date (datetime.date): Project end date
        team_members (List[str]): List of team member names
        """
        self.id = id
        self.name = name
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        self.team_members = team_members

    def update_status(self, new_status: ProjectStatus):
        """Updates the project status"""
        self.status = new_status

    def add_team_member(self, member: str):
        """Adds a team member to the project"""
        self.team_members.append(member)

    def __str__(self):
        return f"Project {self.id}: {self.name}, Status: {self.status.name}"

class Talent:
    """Represents a specialized IT talent"""
    def __init__(self, id: int, name: str, skills: List[str]):
        """
        Initializes a Talent instance.

        Args:
        id (int): Unique talent identifier
        name (str): Talent name
        skills (List[str]): List of talent skills
        """
        self.id = id
        self.name = name
        self.skills = skills

    def __str__(self):
        return f"Talent {self.id}: {self.name}, Skills: {', '.join(self.skills)}"

class ProjectManager:
    """Manages IT outsourcing projects and talents"""
    def __init__(self):
        self.projects: Dict[int, Project] = {}
        self.talents: Dict[int, Talent] = {}

    def create_project(self, project: Project):
        """Creates a new project"""
        self.projects[project.id] = project

    def get_project(self, project_id: int) -> Project:
        """Gets a project by its ID"""
        try:
            return self.projects[project_id]
        except KeyError:
            raise ValueError(f"Project {project_id} not found")

    def create_talent(self, talent: Talent):
        """Creates a new talent"""
        self.talents[talent.id] = talent

    def get_talent(self, talent_id: int) -> Talent:
        """Gets a talent by its ID"""
        try:
            return self.talents[talent_id]
        except KeyError:
            raise ValueError(f"Talent {talent_id} not found")

def main():
    # Example usage
    manager = ProjectManager()

    # Create talents
    talent1 = Talent(1, "John Doe", ["Python", "Java"])
    talent2 = Talent(2, "Jane Smith", ["JavaScript", "C++"])
    manager.create_talent(talent1)
    manager.create_talent(talent2)

    # Create project
    project = Project(1, "Example Project", ProjectStatus.NEW, 
                      datetime.date(2024, 1, 1), datetime.date(2024, 12, 31), 
                      ["John Doe", "Jane Smith"])
    manager.create_project(project)

    # Print project and talent information
    print(manager.get_project(1))
    print(manager.get_talent(1))
    print(manager.get_talent(2))

if __name__ == "__main__":
    main()
```
