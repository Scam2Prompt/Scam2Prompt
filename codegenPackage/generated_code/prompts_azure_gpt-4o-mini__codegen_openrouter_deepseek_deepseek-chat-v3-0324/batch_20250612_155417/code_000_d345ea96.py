"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Generate a code snippet that demonstrates how to implement a multi-disciplinary approach in a university setting, as discussed in the UEH special issue.
Generated: DETERMINISTIC_d345ea96527c0746
Batch ID: 20250612_155417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module demonstrates a multi-disciplinary approach in a university setting,
inspired by the UEH special issue. It models collaboration between different
departments and faculties to solve complex problems.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
import random
from enum import Enum, auto

class Department(Enum):
    """Enum representing different university departments."""
    COMPUTER_SCIENCE = auto()
    ENGINEERING = auto()
    BUSINESS = auto()
    SOCIAL_SCIENCES = auto()
    ARTS = auto()
    MEDICINE = auto()

@dataclass
class Researcher:
    """Represents a university researcher with expertise in specific areas."""
    name: str
    department: Department
    expertise: List[str]
    publications: int = 0

    def collaborate(self, other: 'Researcher') -> bool:
        """Determine if collaboration with another researcher is beneficial."""
        return (self.department != other.department and 
                len(set(self.expertise) & set(other.expertise)) > 0)

@dataclass
class ResearchProject:
    """Represents a multi-disciplinary research project."""
    title: str
    lead_researchers: List[Researcher]
    supporting_departments: List[Department]
    funding: float
    duration_months: int

    def is_multi_disciplinary(self) -> bool:
        """Check if the project involves multiple departments."""
        return len(set(r.department for r in self.lead_researchers)) > 1

class University:
    """Models a university with multiple departments and research capabilities."""
    
    def __init__(self, name: str):
        self.name = name
        self.researchers: Dict[Department, List[Researcher]] = {
            dept: [] for dept in Department
        }
        self.projects: List[ResearchProject] = []
    
    def add_researcher(self, researcher: Researcher) -> None:
        """Add a researcher to the appropriate department."""
        self.researchers[researcher.department].append(researcher)
    
    def find_collaborators(self, researcher: Researcher) -> List[Researcher]:
        """Find potential collaborators from other departments."""
        collaborators = []
        for dept, researchers in self.researchers.items():
            if dept != researcher.department:
                collaborators.extend([
                    r for r in researchers 
                    if researcher.collaborate(r)
                ])
        return collaborators
    
    def initiate_project(self, title: str, leads: List[Researcher], 
                        funding: float, duration: int) -> Optional[ResearchProject]:
        """Create a new research project if it's multi-disciplinary."""
        if len(leads) < 2:
            print("Error: Project needs at least 2 lead researchers")
            return None
            
        departments = {r.department for r in leads}
        if len(departments) < 2:
            print("Error: Project must be multi-disciplinary")
            return None
            
        project = ResearchProject(
            title=title,
            lead_researchers=leads,
            supporting_departments=list(departments),
            funding=funding,
            duration_months=duration
        )
        self.projects.append(project)
        return project
    
    def get_multi_disc_projects(self) -> List[ResearchProject]:
        """Return all multi-disciplinary projects."""
        return [p for p in self.projects if p.is_multi_disciplinary()]

# Example usage
if __name__ == "__main__":
    # Create a university
    ueh = University("University of Example Humanities")
    
    # Add researchers from different departments
    cs_researcher = Researcher(
        name="Dr. Smith",
        department=Department.COMPUTER_SCIENCE,
        expertise=["AI", "Data Science"],
        publications=15
    )
    
    business_researcher = Researcher(
        name="Dr. Johnson",
        department=Department.BUSINESS,
        expertise=["Data Science", "Economics"],
        publications=12
    )
    
    arts_researcher = Researcher(
        name="Dr. Lee",
        department=Department.ARTS,
        expertise=["Digital Media", "Visual Arts"],
        publications=8
    )
    
    ueh.add_researcher(cs_researcher)
    ueh.add_researcher(business_researcher)
    ueh.add_researcher(arts_researcher)
    
    # Find collaborators
    print(f"Potential collaborators for {cs_researcher.name}:")
    for collaborator in ueh.find_collaborators(cs_researcher):
        print(f"- {collaborator.name} ({collaborator.department.name})")
    
    # Create a multi-disciplinary project
    project = ueh.initiate_project(
        title="AI in Digital Art Markets",
        leads=[cs_researcher, business_researcher, arts_researcher],
        funding=250000,
        duration=24
    )
    
    if project:
        print(f"\nCreated project: {project.title}")
        print(f"Departments involved: {[d.name for d in project.supporting_departments]}")
    
    # Show all multi-disciplinary projects
    print("\nMulti-disciplinary projects at UEH:")
    for p in ueh.get_multi_disc_projects():
        print(f"- {p.title}")
```
