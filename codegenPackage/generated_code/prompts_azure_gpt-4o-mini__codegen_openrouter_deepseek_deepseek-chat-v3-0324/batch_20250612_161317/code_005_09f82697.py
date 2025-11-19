"""
Generated Code Metadata:
========================
Original URL: https://turpymobileapps.com
Prompt: Develop a project management plan for a web development project that aligns with the innovative approaches of Turpy Mobile Apps.
Generated: DETERMINISTIC_09f82697568b3408
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Plan for Web Development Project (Turpy Mobile Apps Style)
"""

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional
import json

class ProjectPhase(Enum):
    """Enum representing different phases of the project"""
    DISCOVERY = "Discovery"
    DESIGN = "Design"
    DEVELOPMENT = "Development"
    TESTING = "Testing"
    DEPLOYMENT = "Deployment"
    MAINTENANCE = "Maintenance"

class TaskStatus(Enum):
    """Enum representing task statuses"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"

class TeamMember:
    """Class representing a team member"""
    def __init__(self, name: str, role: str, skills: List[str]):
        self.name = name
        self.role = role
        self.skills = skills

    def to_dict(self) -> Dict:
        """Convert object to dictionary for serialization"""
        return {
            "name": self.name,
            "role": self.role,
            "skills": self.skills
        }

class ProjectTask:
    """Class representing a project task"""
    def __init__(self, 
                 name: str, 
                 description: str, 
                 phase: ProjectPhase, 
                 assigned_to: TeamMember,
                 estimated_hours: float,
                 dependencies: Optional[List[str]] = None):
        self.name = name
        self.description = description
        self.phase = phase
        self.assigned_to = assigned_to
        self.estimated_hours = estimated_hours
        self.dependencies = dependencies or []
        self.status = TaskStatus.NOT_STARTED
        self.actual_hours = 0.0
        self.start_date = None
        self.end_date = None

    def update_status(self, new_status: TaskStatus) -> None:
        """Update task status with validation"""
        if not isinstance(new_status, TaskStatus):
            raise ValueError("Invalid task status")
        self.status = new_status

    def log_hours(self, hours: float) -> None:
        """Log actual hours worked on task"""
        if hours < 0:
            raise ValueError("Hours cannot be negative")
        self.actual_hours += hours

    def to_dict(self) -> Dict:
        """Convert object to dictionary for serialization"""
        return {
            "name": self.name,
            "description": self.description,
            "phase": self.phase.value,
            "assigned_to": self.assigned_to.to_dict(),
            "estimated_hours": self.estimated_hours,
            "dependencies": self.dependencies,
            "status": self.status.value,
            "actual_hours": self.actual_hours,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None
        }

class ProjectMilestone:
    """Class representing a project milestone"""
    def __init__(self, name: str, description: str, due_date: datetime, phase: ProjectPhase):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.phase = phase
        self.completed = False
        self.completion_date = None

    def mark_completed(self) -> None:
        """Mark milestone as completed"""
        self.completed = True
        self.completion_date = datetime.now()

    def to_dict(self) -> Dict:
        """Convert object to dictionary for serialization"""
        return {
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date.isoformat(),
            "phase": self.phase.value,
            "completed": self.completed,
            "completion_date": self.completion_date.isoformat() if self.completion_date else None
        }

class Project:
    """Main project management class"""
    def __init__(self, name: str, description: str, start_date: datetime):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.team: List[TeamMember] = []
        self.tasks: List[ProjectTask] = []
        self.milestones: List[ProjectMilestone] = []
        self.risks: List[Dict] = []
        self.agile_sprints: List[Dict] = []

    def add_team_member(self, member: TeamMember) -> None:
        """Add a team member to the project"""
        self.team.append(member)

    def add_task(self, task: ProjectTask) -> None:
        """Add a task to the project"""
        self.tasks.append(task)

    def add_milestone(self, milestone: ProjectMilestone) -> None:
        """Add a milestone to the project"""
        self.milestones.append(milestone)

    def add_risk(self, description: str, impact: str, mitigation: str) -> None:
        """Add a risk to the project"""
        self.risks.append({
            "description": description,
            "impact": impact,
            "mitigation": mitigation,
            "status": "Open"
        })

    def add_sprint(self, name: str, duration_days: int, goals: List[str]) -> None:
        """Add an agile sprint to the project"""
        self.agile_sprints.append({
            "name": name,
            "duration_days": duration_days,
            "goals": goals,
            "completed": False
        })

    def get_project_status(self) -> Dict:
        """Get overall project status summary"""
        completed_tasks = sum(1 for task in self.tasks if task.status == TaskStatus.COMPLETED)
        total_tasks = len(self.tasks)
        
        completed_milestones = sum(1 for milestone in self.milestones if milestone.completed)
        total_milestones = len(self.milestones)

        return {
            "progress": {
                "tasks": f"{completed_tasks}/{total_tasks}",
                "milestones": f"{completed_milestones}/{total_milestones}"
            },
            "team_size": len(self.team),
            "open_risks": sum(1 for risk in self.risks if risk["status"] == "Open"),
            "active_sprints": sum(1 for sprint in self.agile_sprints if not sprint["completed"])
        }

    def generate_gantt_data(self) -> List[Dict]:
        """Generate data for Gantt chart visualization"""
        gantt_data = []
        for task in self.tasks:
            if task.start_date and task.end_date:
                gantt_data.append({
                    "task": task.name,
                    "start": task.start_date.isoformat(),
                    "end": task.end_date.isoformat(),
                    "phase": task.phase.value,
                    "assignee": task.assigned_to.name
                })
        return gantt_data

    def save_to_file(self, filename: str) -> None:
        """Save project data to JSON file"""
        data = {
            "project": {
                "name": self.name,
                "description": self.description,
                "start_date": self.start_date.isoformat()
            },
            "team": [member.to_dict() for member in self.team],
            "tasks": [task.to_dict() for task in self.tasks],
            "milestones": [milestone.to_dict() for milestone in self.milestones],
            "risks": self.risks,
            "agile_sprints": self.agile_sprints
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'Project':
        """Load project data from JSON file"""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        project_data = data["project"]
        project = cls(
            name=project_data["name"],
            description=project_data["description"],
            start_date=datetime.fromisoformat(project_data["start_date"])
        )
        
        # Load team members
        for member_data in data["team"]:
            project.add_team_member(TeamMember(
                name=member_data["name"],
                role=member_data["role"],
                skills=member_data["skills"]
            ))
        
        # Load tasks (requires team members to be loaded first)
        team_members = {member.name: member for member in project.team}
        for task_data in data["tasks"]:
            assigned_to = team_members[task_data["assigned_to"]["name"]]
            task = ProjectTask(
                name=task_data["name"],
                description=task_data["description"],
                phase=ProjectPhase(task_data["phase"]),
                assigned_to=assigned_to,
                estimated_hours=task_data["estimated_hours"],
                dependencies=task_data["dependencies"]
            )
            task.status = TaskStatus(task_data["status"])
            task.actual_hours = task_data["actual_hours"]
            task.start_date = datetime.fromisoformat(task_data["start_date"]) if task_data["start_date"] else None
            task.end_date = datetime.from
