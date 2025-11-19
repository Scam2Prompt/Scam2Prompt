"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Create a template for a project management plan using agile methodologies, incorporating Matter's approach to project development and monitoring."
Generated: DETERMINISTIC_ba6d64257576327d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Agile Project Management Plan Template
Incorporating Matter's approach to project development and monitoring.
"""

from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum, auto
from typing import List, Optional, Dict, Any


class ProjectStatus(Enum):
    """Current status of the project"""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class TaskPriority(Enum):
    """Priority levels for tasks"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


@dataclass
class TeamMember:
    """Team member information"""
    name: str
    role: str
    email: str
    capacity_hours: float = 40.0


@dataclass
class UserStory:
    """Agile user story"""
    id: str
    title: str
    description: str
    acceptance_criteria: List[str]
    priority: TaskPriority
    story_points: int
    status: ProjectStatus = ProjectStatus.NOT_STARTED


@dataclass
class Sprint:
    """Agile sprint information"""
    id: str
    name: str
    start_date: date
    end_date: date
    goal: str
    user_stories: List[UserStory]
    status: ProjectStatus = ProjectStatus.NOT_STARTED

    def duration_days(self) -> int:
        """Calculate sprint duration in days"""
        return (self.end_date - self.start_date).days + 1


@dataclass
class Risk:
    """Project risk information"""
    id: str
    description: str
    impact: str
    probability: float  # 0.0 to 1.0
    mitigation_plan: str
    status: ProjectStatus = ProjectStatus.NOT_STARTED


@dataclass
class ProjectMetrics:
    """Metrics for project monitoring"""
    velocity: float
    burn_down: List[float]
    cycle_time: float
    defect_rate: float


@dataclass
class Retrospective:
    """Sprint retrospective information"""
    sprint_id: str
    what_went_well: List[str]
    what_didnt_go_well: List[str]
    action_items: List[str]


class AgileProjectPlan:
    """Main project management plan template"""
    
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.start_date: Optional[date] = None
        self.end_date: Optional[date] = None
        self.project_manager: Optional[str] = None
        self.team: List[TeamMember] = []
        self.sprints: List[Sprint] = []
        self.product_backlog: List[UserStory] = []
        self.risks: List[Risk] = []
        self.metrics: Optional[ProjectMetrics] = None
        self.retrospectives: List[Retrospective] = []
        self.status: ProjectStatus = ProjectStatus.NOT_STARTED
    
    def add_team_member(self, member: TeamMember) -> None:
        """Add a team member to the project"""
        self.team.append(member)
    
    def add_sprint(self, sprint: Sprint) -> None:
        """Add a sprint to the project"""
        self.sprints.append(sprint)
    
    def add_user_story(self, user_story: UserStory) -> None:
        """Add a user story to the product backlog"""
        self.product_backlog.append(user_story)
    
    def add_risk(self, risk: Risk) -> None:
        """Add a risk to the project"""
        self.risks.append(risk)
    
    def record_retrospective(self, retrospective: Retrospective) -> None:
        """Record a sprint retrospective"""
        self.retrospectives.append(retrospective)
    
    def update_metrics(self, metrics: ProjectMetrics) -> None:
        """Update project metrics"""
        self.metrics = metrics
    
    def get_project_duration(self) -> Optional[int]:
        """Calculate project duration in days"""
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days + 1
        return None
    
    def get_active_sprint(self) -> Optional[Sprint]:
        """Get the currently active sprint"""
        today = date.today()
        for sprint in self.sprints:
            if sprint.start_date <= today <= sprint.end_date:
                return sprint
        return None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert project plan to dictionary for serialization"""
        return {
            "project_name": self.project_name,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "project_manager": self.project_manager,
            "team": [member.__dict__ for member in self.team],
            "sprints": [sprint.__dict__ for sprint in self.sprints],
            "product_backlog": [story.__dict__ for story in self.product_backlog],
            "risks": [risk.__dict__ for risk in self.risks],
            "metrics": self.metrics.__dict__ if self.metrics else None,
            "retrospectives": [retro.__dict__ for retro in self.retrospectives],
            "status": self.status.name
        }
```
