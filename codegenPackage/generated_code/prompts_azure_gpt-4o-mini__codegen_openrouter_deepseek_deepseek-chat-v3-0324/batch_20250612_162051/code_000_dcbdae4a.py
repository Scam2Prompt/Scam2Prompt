"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: Generate a custom software development project plan for a government agency that incorporates IT project management best practices as described by ARP Group Corporation.
Generated: DETERMINISTIC_dcbdae4ae55b2e83
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
Custom Software Development Project Plan for Government Agency
Incorporating IT Project Management Best Practices (ARP Group Corporation)
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass

class ProjectPhase(Enum):
    INITIATION = "Initiation"
    PLANNING = "Planning"
    EXECUTION = "Execution"
    MONITORING = "Monitoring & Control"
    CLOSURE = "Closure"

class RiskLevel(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

@dataclass
class Stakeholder:
    name: str
    role: str
    contact: str
    influence: str

@dataclass
class Deliverable:
    name: str
    description: str
    due_date: datetime.date
    owner: Stakeholder

@dataclass
class Risk:
    description: str
    level: RiskLevel
    mitigation_plan: str
    owner: Stakeholder

@dataclass
class Milestone:
    name: str
    date: datetime.date
    phase: ProjectPhase
    dependencies: List[str]

@dataclass
class Resource:
    name: str
    type: str  # Human, Equipment, Software, etc.
    quantity: int
    cost: float

@dataclass
class Task:
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    owner: Stakeholder
    dependencies: List[str]
    phase: ProjectPhase
    resources: List[Resource]

class ProjectPlan:
    def __init__(self, project_name: str, agency_name: str, start_date: datetime.date, end_date: datetime.date):
        self.project_name = project_name
        self.agency_name = agency_name
        self.start_date = start_date
        self.end_date = end_date
        self.stakeholders: List[Stakeholder] = []
        self.deliverables: List[Deliverable] = []
        self.risks: List[Risk] = []
        self.milestones: List[Milestone] = []
        self.tasks: List[Task] = []
        self.resources: List[Resource] = []
        self.phases = [phase for phase in ProjectPhase]

    def add_stakeholder(self, stakeholder: Stakeholder) -> None:
        """Add a stakeholder to the project"""
        self.stakeholders.append(stakeholder)

    def add_deliverable(self, deliverable: Deliverable) -> None:
        """Add a project deliverable"""
        if deliverable.due_date < self.start_date or deliverable.due_date > self.end_date:
            raise ValueError("Deliverable due date must be within project timeline")
        self.deliverables.append(deliverable)

    def add_risk(self, risk: Risk) -> None:
        """Add a project risk with mitigation plan"""
        self.risks.append(risk)

    def add_milestone(self, milestone: Milestone) -> None:
        """Add a project milestone"""
        if milestone.date < self.start_date or milestone.date > self.end_date:
            raise ValueError("Milestone date must be within project timeline")
        self.milestones.append(milestone)

    def add_task(self, task: Task) -> None:
        """Add a project task"""
        if task.start_date < self.start_date or task.end_date > self.end_date:
            raise ValueError("Task dates must be within project timeline")
        self.tasks.append(task)

    def add_resource(self, resource: Resource) -> None:
        """Add a project resource"""
        self.resources.append(resource)

    def validate_project_plan(self) -> bool:
        """Validate the project plan meets all requirements"""
        if not self.stakeholders:
            raise ValueError("Project must have at least one stakeholder")
        if not self.deliverables:
            raise ValueError("Project must have at least one deliverable")
        if not self.milestones:
            raise ValueError("Project must have at least one milestone")
        return True

    def generate_gantt_chart_data(self) -> Dict:
        """Generate data for Gantt chart visualization"""
        return {
            "project_name": self.project_name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": [
                {
                    "name": task.name,
                    "start": task.start_date.isoformat(),
                    "end": task.end_date.isoformat(),
                    "phase": task.phase.value,
                    "owner": task.owner.name
                } for task in self.tasks
            ],
            "milestones": [
                {
                    "name": milestone.name,
                    "date": milestone.date.isoformat(),
                    "phase": milestone.phase.value
                } for milestone in self.milestones
            ]
        }

    def calculate_budget(self) -> float:
        """Calculate total project budget based on resources"""
        return sum(resource.cost * resource.quantity for resource in self.resources)

def create_sample_government_project() -> ProjectPlan:
    """Create a sample government project plan following ARP Group best practices"""
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=180)
    
    project = ProjectPlan(
        project_name="Agency Digital Transformation",
        agency_name="Department of Technology",
        start_date=start_date,
        end_date=end_date
    )

    # Add stakeholders
    cio = Stakeholder("Jane Smith", "CIO", "jane.smith@agency.gov", "High")
    pm = Stakeholder("John Doe", "Project Manager", "john.doe@agency.gov", "High")
    dev_lead = Stakeholder("Alex Johnson", "Development Lead", "alex.johnson@agency.gov", "Medium")
    
    project.add_stakeholder(cio)
    project.add_stakeholder(pm)
    project.add_stakeholder(dev_lead)

    # Add deliverables
    project.add_deliverable(Deliverable(
        "Requirements Document",
        "Complete system requirements specification",
        start_date + datetime.timedelta(days=30),
        pm
    ))

    # Add risks
    project.add_risk(Risk(
        "Vendor delays",
        RiskLevel.MEDIUM,
        "Identify alternative vendors and establish SLAs",
        pm
    ))

    # Add milestones
    project.add_milestone(Milestone(
        "Kickoff Meeting",
        start_date,
        ProjectPhase.INITIATION,
        []
    ))

    # Add tasks
    project.add_task(Task(
        "Requirements Gathering",
        "Conduct stakeholder interviews and document requirements",
        start_date,
        start_date + datetime.timedelta(days=14),
        pm,
        [],
        ProjectPhase.INITIATION,
        []
    ))

    # Add resources
    project.add_resource(Resource(
        "Senior Developer",
        "Human",
        2,
        120000.00  # Annual salary
    ))

    try:
        project.validate_project_plan()
        return project
    except ValueError as e:
        print(f"Error creating sample project: {e}")
        raise

if __name__ == "__main__":
    try:
        sample_project = create_sample_government_project()
        print(f"Project '{sample_project.project_name}' created successfully")
        print(f"Total budget: ${sample_project.calculate_budget():,.2f}")
    except Exception as e:
        print(f"Failed to create project plan: {e}")
```
