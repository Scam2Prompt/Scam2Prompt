"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: Write a Python script for managing IT project timelines and budgets, incorporating best practices in IT project management as described by ARP Group Corporation's services.
Generated: DETERMINISTIC_2e6c9e0007ed401d
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
IT Project Management Tool for ARP Group Corporation

This script provides functionalities to manage IT project timelines and budgets,
incorporating best practices in IT project management.

Features:
- Project creation and tracking
- Budget allocation and monitoring
- Timeline management with milestones
- Risk assessment and mitigation
- Reporting capabilities
"""

import json
import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import uuid
import csv
from pathlib import Path


@dataclass
class ProjectTask:
    """Represents a single task in a project."""
    name: str
    description: str
    assigned_to: str
    estimated_hours: float
    actual_hours: float = 0.0
    status: str = "Not Started"  # "Not Started", "In Progress", "Completed"
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    dependencies: List[str] = field(default_factory=list)


@dataclass
class ProjectMilestone:
    """Represents a milestone in a project timeline."""
    name: str
    target_date: datetime.date
    achieved_date: Optional[datetime.date] = None
    status: str = "Pending"  # "Pending", "Achieved", "Delayed"
    milestone_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    associated_tasks: List[str] = field(default_factory=list)


@dataclass
class Risk:
    """Represents a potential risk to the project."""
    description: str
    probability: float  # 0.0 to 1.0
    impact: float  # 0.0 to 1.0
    mitigation_plan: str
    risk_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    status: str = "Open"  # "Open", "Mitigated", "Occurred"


@dataclass
class Project:
    """Represents an IT project with timeline and budget information."""
    name: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    budget: float
    project_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tasks: Dict[str, ProjectTask] = field(default_factory=dict)
    milestones: Dict[str, ProjectMilestone] = field(default_factory=dict)
    risks: Dict[str, Risk] = field(default_factory=dict)
    actual_spending: float = 0.0
    status: str = "Planning"  # "Planning", "Active", "On Hold", "Completed", "Cancelled"

    def add_task(self, task: ProjectTask) -> None:
        """Add a task to the project."""
        self.tasks[task.task_id] = task

    def add_milestone(self, milestone: ProjectMilestone) -> None:
        """Add a milestone to the project."""
        self.milestones[milestone.milestone_id] = milestone

    def add_risk(self, risk: Risk) -> None:
        """Add a risk to the project."""
        self.risks[risk.risk_id] = risk

    def update_task_status(self, task_id: str, status: str, actual_hours: Optional[float] = None) -> None:
        """Update the status of a task and optionally update actual hours."""
        if task_id not in self.tasks:
            raise ValueError("Task ID not found")
        
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.tasks[task_id].status = status
        if actual_hours is not None:
            self.tasks[task_id].actual_hours = actual_hours

    def update_milestone_status(self, milestone_id: str, status: str, achieved_date: Optional[datetime.date] = None) -> None:
        """Update the status of a milestone."""
        if milestone_id not in self.milestones:
            raise ValueError("Milestone ID not found")
        
        valid_statuses = ["Pending", "Achieved", "Delayed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        
        self.milestones[milestone_id].status = status
        if achieved_date is not None:
            self.milestones[milestone_id].achieved_date = achieved_date

    def calculate_budget_utilization(self) -> float:
        """Calculate the percentage of budget utilized."""
        if self.budget == 0:
            return 0.0
        return (self.actual_spending / self.budget) * 100

    def calculate_project_progress(self) -> float:
        """Calculate the percentage of project completion based on tasks."""
        if not self.tasks:
            return 0.0
        
        completed_tasks = sum(1 for task in self.tasks.values() if task.status == "Completed")
        return (completed_tasks / len(self.tasks)) * 100

    def get_high_priority_risks(self, threshold: float = 0.5) -> List[Risk]:
        """Get risks with probability * impact above the threshold."""
        return [
            risk for risk in self.risks.values()
            if (risk.probability * risk.impact) >= threshold and risk.status == "Open"
        ]


class ProjectManager:
    """Manages multiple IT projects with persistence capabilities."""
    
    def __init__(self, data_file: str = "projects.json"):
        """Initialize the project manager with a data file."""
        self.data_file = Path(data_file)
        self.projects: Dict[str, Project] = {}
        self.load_projects()

    def load_projects(self) -> None:
        """Load projects from the data file."""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.projects = {
                        project_id: Project(
                            name=project_data['name'],
                            description=project_data['description'],
                            start_date=datetime.date.fromisoformat(project_data['start_date']),
                            end_date=datetime.date.fromisoformat(project_data['end_date']),
                            budget=project_data['budget'],
                            project_id=project_id,
                            tasks={
                                task_id: ProjectTask(**task_data)
                                for task_id, task_data in project_data['tasks'].items()
                            },
                            milestones={
                                milestone_id: ProjectMilestone(**milestone_data)
                                for milestone_id, milestone_data in project_data['milestones'].items()
                            },
                            risks={
                                risk_id: Risk(**risk_data)
                                for risk_id, risk_data in project_data['risks'].items()
                            },
                            actual_spending=project_data['actual_spending'],
                            status=project_data['status']
                        )
                        for project_id, project_data in data.items()
                    }
        except Exception as e:
            print(f"Error loading projects: {e}")
            self.projects = {}

    def save_projects(self) -> None:
        """Save projects to the data file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump({
                    project_id: {
                        'name': project.name,
                        'description': project.description,
                        'start_date': project.start_date.isoformat(),
                        'end_date': project.end_date.isoformat(),
                        'budget': project.budget,
                        'tasks': {
                            task_id: {
                                'name': task.name,
                                'description': task.description,
                                'assigned_to': task.assigned_to,
                                'estimated_hours': task.estimated_hours,
                                'actual_hours': task.actual_hours,
                                'status': task.status,
                                'task_id': task.task_id,
                                'dependencies': task.dependencies
                            }
                            for task_id, task in project.tasks.items()
                        },
                        'milestones': {
                            milestone_id: {
                                'name': milestone.name,
                                'target_date': milestone.target_date.isoformat(),
                                'achieved_date': milestone.achieved_date.isoformat() if milestone.achieved_date else None,
                                'status': milestone.status,
                                'milestone_id': milestone.milestone_id,
                                'associated_tasks': milestone.associated_tasks
                            }
                            for milestone_id, milestone in project.milestones.items()
                        },
                        'risks': {
                            risk_id: {
                                'description': risk.description,
                                'probability': risk.probability,
                                'impact': risk.impact,
                                'mitigation_plan': risk.mitigation_plan,
                                'risk_id': risk.risk_id,
                                'status': risk.status
                            }
                            for risk_id, risk in project.risks.items()
                        },
                        'actual_spending': project.actual_spending,
                        'status': project.status
                    }
                    for project_id, project in self.projects.items()
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving projects: {e}")

    def create_project(self, name: str, description: str, start_date: datetime.date,
                      end_date: datetime.date,
