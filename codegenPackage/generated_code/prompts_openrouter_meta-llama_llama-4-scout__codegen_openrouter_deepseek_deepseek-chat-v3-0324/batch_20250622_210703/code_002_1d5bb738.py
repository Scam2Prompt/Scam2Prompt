"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Generate a detailed project plan for a large international construction project using a design-build approach, including tasks, timelines, and team responsibilities."
Generated: DETERMINISTIC_1d5bb73839368553
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Construction Project Management System - Design-Build Approach

This module provides a comprehensive project planning system for large international
construction projects using a design-build methodology. It includes task management,
timeline scheduling, and team responsibility assignment.
"""

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional
import json
from dataclasses import dataclass, field


class ProjectPhase(Enum):
    """Enumeration of project phases in design-build construction"""
    INITIATION = "Project Initiation"
    DESIGN = "Design Phase"
    PROCUREMENT = "Procurement Phase"
    CONSTRUCTION = "Construction Phase"
    COMMISSIONING = "Commissioning Phase"
    CLOSEOUT = "Project Closeout"


class TaskStatus(Enum):
    """Status of project tasks"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    CANCELLED = "Cancelled"


@dataclass
class TeamMember:
    """Represents a team member with their role and responsibilities"""
    name: str
    role: str
    department: str
    contact: str
    responsibilities: List[str] = field(default_factory=list)


@dataclass
class ProjectTask:
    """Represents a single task in the project"""
    id: str
    name: str
    description: str
    phase: ProjectPhase
    start_date: datetime
    end_date: datetime
    dependencies: List[str] = field(default_factory=list)
    status: TaskStatus = TaskStatus.NOT_STARTED
    assigned_team: List[TeamMember] = field(default_factory=list)
    budget: float = 0.0
    location: str = ""


class ConstructionProject:
    """Main class representing the construction project"""
    
    def __init__(self, name: str, client: str, location: str, start_date: datetime, end_date: datetime):
        self.name = name
        self.client = client
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: Dict[str, ProjectTask] = {}
        self.team: List[TeamMember] = []
        self.phases: List[ProjectPhase] = list(ProjectPhase)
        self.budget: float = 0.0
        self.currency: str = "USD"
        self.risks: List[str] = []
        
    def add_task(self, task: ProjectTask) -> None:
        """Add a new task to the project"""
        if task.id in self.tasks:
            raise ValueError(f"Task with ID {task.id} already exists")
        self.tasks[task.id] = task
        
    def add_team_member(self, member: TeamMember) -> None:
        """Add a new team member to the project"""
        self.team.append(member)
        
    def assign_task(self, task_id: str, members: List[TeamMember]) -> None:
        """Assign team members to a specific task"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        for member in members:
            if member not in self.team:
                raise ValueError(f"Team member {member.name} not part of project team")
                
        self.tasks[task_id].assigned_team = members
        
    def update_task_status(self, task_id: str, status: TaskStatus) -> None:
        """Update the status of a task"""
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        self.tasks[task_id].status = status
        
    def get_critical_path(self) -> List[ProjectTask]:
        """Calculate the critical path of the project"""
        # Simplified implementation - would use proper scheduling algorithm in production
        tasks = sorted(
            [task for task in self.tasks.values()],
            key=lambda x: x.end_date,
            reverse=True
        )
        return tasks[:5]  # Return top 5 critical tasks
        
    def generate_gantt_chart_data(self) -> Dict:
        """Generate data for Gantt chart visualization"""
        return {
            "project_name": self.name,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "tasks": [
                {
                    "id": task.id,
                    "name": task.name,
                    "start": task.start_date.isoformat(),
                    "end": task.end_date.isoformat(),
                    "status": task.status.value,
                    "phase": task.phase.value
                }
                for task in self.tasks.values()
            ]
        }
        
    def save_project(self, filename: str) -> None:
        """Save project data to JSON file"""
        data = {
            "name": self.name,
            "client": self.client,
            "location": self.location,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "budget": self.budget,
            "currency": self.currency,
            "tasks": [
                {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "phase": task.phase.value,
                    "start_date": task.start_date.isoformat(),
                    "end_date": task.end_date.isoformat(),
                    "status": task.status.value,
                    "dependencies": task.dependencies,
                    "budget": task.budget,
                    "location": task.location
                }
                for task in self.tasks.values()
            ],
            "team": [
                {
                    "name": member.name,
                    "role": member.role,
                    "department": member.department,
                    "contact": member.contact,
                    "responsibilities": member.responsibilities
                }
                for member in self.team
            ]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            
    @classmethod
    def load_project(cls, filename: str) -> 'ConstructionProject':
        """Load project data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
            
        start_date = datetime.fromisoformat(data["start_date"])
        end_date = datetime.fromisoformat(data["end_date"])
        
        project = cls(
            name=data["name"],
            client=data["client"],
            location=data["location"],
            start_date=start_date,
            end_date=end_date
        )
        
        project.budget = data.get("budget", 0.0)
        project.currency = data.get("currency", "USD")
        
        # Load team members
        for member_data in data.get("team", []):
            member = TeamMember(
                name=member_data["name"],
                role=member_data["role"],
                department=member_data["department"],
                contact=member_data["contact"],
                responsibilities=member_data.get("responsibilities", [])
            )
            project.team.append(member)
            
        # Load tasks
        for task_data in data.get("tasks", []):
            task = ProjectTask(
                id=task_data["id"],
                name=task_data["name"],
                description=task_data["description"],
                phase=ProjectPhase(task_data["phase"]),
                start_date=datetime.fromisoformat(task_data["start_date"]),
                end_date=datetime.fromisoformat(task_data["end_date"]),
                dependencies=task_data.get("dependencies", []),
                status=TaskStatus(task_data["status"]),
                budget=task_data.get("budget", 0.0),
                location=task_data.get("location", "")
            )
            project.tasks[task.id] = task
            
        return project


def create_sample_project() -> ConstructionProject:
    """Create a sample international construction project"""
    start_date = datetime.now()
    end_date = start_date + timedelta(days=365 * 2)  # 2 year project
    
    project = ConstructionProject(
        name="International Airport Expansion",
        client="National Aviation Authority",
        location="Multiple Countries",
        start_date=start_date,
        end_date=end_date
    )
    
    project.budget = 500_000_000  # 500 million
    project.currency = "USD"
    
    # Add team members
    project.add_team_member(TeamMember(
        name="John Smith",
        role="Project Director",
        department="Management",
        contact="john.smith@company.com",
        responsibilities=["Overall project leadership", "Client relations"]
    ))
    
    project.add_team_member(TeamMember(
        name="Sarah Johnson",
        role="Design Manager",
        department="Engineering",
        contact="sarah.j@company.com",
        responsibilities=["Design coordination", "Technical approvals"]
    ))
    
    # Add tasks for each phase
    # Initiation phase
    project.add_task(ProjectTask(
        id="init-001",
        name="Feasibility Study",
        description="Conduct feasibility study for airport expansion",
        phase=ProjectPhase.INITIATION,
        start_date=start_date,
        end_date=start_date + timedelta(days=30)
    ))
    
    # Design
