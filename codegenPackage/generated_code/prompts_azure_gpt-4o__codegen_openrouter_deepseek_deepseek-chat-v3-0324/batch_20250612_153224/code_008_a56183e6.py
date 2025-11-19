"""
Generated Code Metadata:
========================
Original URL: https://arpgroupcorp.com
Prompt: Create a project plan template for IT project management that ensures timelines and budgets are met, inspired by ARP Group Corporation's methodology.
Generated: DETERMINISTIC_a56183e65b95474c
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
IT Project Plan Template based on ARP Group Corporation's Methodology

This template provides a structured approach to IT project management,
ensuring timelines and budgets are met through defined phases,
milestones, and tracking mechanisms.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
from enum import Enum, auto


class ProjectPhase(Enum):
    INITIATION = auto()
    PLANNING = auto()
    EXECUTION = auto()
    MONITORING = auto()
    CLOSURE = auto()


class RiskLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Task:
    def __init__(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        owner: str,
        dependencies: List[str] = None,
        budget: float = 0.0,
        risk_level: RiskLevel = RiskLevel.LOW,
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.owner = owner
        self.dependencies = dependencies if dependencies else []
        self.budget = budget
        self.risk_level = risk_level
        self.completed = False
        self.actual_cost = 0.0
        self.actual_end_date = None

    def mark_complete(self, actual_cost: float, actual_end_date: datetime):
        self.completed = True
        self.actual_cost = actual_cost
        self.actual_end_date = actual_end_date

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "owner": self.owner,
            "dependencies": self.dependencies,
            "budget": self.budget,
            "risk_level": self.risk_level.name,
            "completed": self.completed,
            "actual_cost": self.actual_cost,
            "actual_end_date": (
                self.actual_end_date.isoformat() if self.actual_end_date else None
            ),
        }


class Milestone:
    def __init__(self, name: str, target_date: datetime, phase: ProjectPhase):
        self.name = name
        self.target_date = target_date
        self.phase = phase
        self.achieved = False
        self.achieved_date = None

    def mark_achieved(self, achieved_date: datetime):
        self.achieved = True
        self.achieved_date = achieved_date

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "target_date": self.target_date.isoformat(),
            "phase": self.phase.name,
            "achieved": self.achieved,
            "achieved_date": (
                self.achieved_date.isoformat() if self.achieved_date else None
            ),
        }


class ProjectPlan:
    def __init__(
        self,
        name: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
        budget: float,
        manager: str,
    ):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.manager = manager
        self.tasks: List[Task] = []
        self.milestones: List[Milestone] = []
        self.risks: List[Dict] = []
        self.actual_costs: float = 0.0

    def add_task(self, task: Task):
        self.tasks.append(task)

    def add_milestone(self, milestone: Milestone):
        self.milestones.append(milestone)

    def add_risk(
        self,
        description: str,
        impact: str,
        probability: RiskLevel,
        mitigation: str,
    ):
        self.risks.append(
            {
                "description": description,
                "impact": impact,
                "probability": probability.name,
                "mitigation": mitigation,
            }
        )

    def calculate_budget_variance(self) -> float:
        total_budget = sum(task.budget for task in self.tasks)
        return self.budget - total_budget

    def calculate_schedule_variance(self) -> Dict[str, timedelta]:
        schedule_variance = {}
        for task in self.tasks:
            if task.completed and task.actual_end_date:
                variance = task.actual_end_date - task.end_date
                schedule_variance[task.name] = variance
        return schedule_variance

    def get_project_status(self) -> Dict:
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        total_tasks = len(self.tasks)
        achieved_milestones = sum(
            1 for milestone in self.milestones if milestone.achieved
        )
        total_milestones = len(self.milestones)

        return {
            "completion_percentage": (
                completed_tasks / total_tasks * 100 if total_tasks > 0 else 0
            ),
            "milestone_achievement": (
                achieved_milestones / total_milestones * 100
                if total_milestones > 0
                else 0
            ),
            "budget_utilization": (
                self.actual_costs / self.budget * 100 if self.budget > 0 else 0
            ),
        }

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "budget": self.budget,
            "manager": self.manager,
            "tasks": [task.to_dict() for task in self.tasks],
            "milestones": [milestone.to_dict() for milestone in self.milestones],
            "risks": self.risks,
            "actual_costs": self.actual_costs,
        }

    def save_to_file(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> "ProjectPlan":
        with open(filename, "r") as f:
            data = json.load(f)

        project = cls(
            name=data["name"],
            description=data["description"],
            start_date=datetime.fromisoformat(data["start_date"]),
            end_date=datetime.fromisoformat(data["end_date"]),
            budget=data["budget"],
            manager=data["manager"],
        )

        for task_data in data["tasks"]:
            task = Task(
                name=task_data["name"],
                description=task_data["description"],
                start_date=datetime.fromisoformat(task_data["start_date"]),
                end_date=datetime.fromisoformat(task_data["end_date"]),
                owner=task_data["owner"],
                dependencies=task_data["dependencies"],
                budget=task_data["budget"],
                risk_level=RiskLevel[task_data["risk_level"]],
            )
            if task_data["completed"]:
                task.mark_complete(
                    task_data["actual_cost"],
                    datetime.fromisoformat(task_data["actual_end_date"])
                    if task_data["actual_end_date"]
                    else None,
                )
            project.add_task(task)

        for milestone_data in data["milestones"]:
            milestone = Milestone(
                name=milestone_data["name"],
                target_date=datetime.fromisoformat(milestone_data["target_date"]),
                phase=ProjectPhase[milestone_data["phase"]],
            )
            if milestone_data["achieved"]:
                milestone.mark_achieved(
                    datetime.fromisoformat(milestone_data["achieved_date"])
                    if milestone_data["achieved_date"]
                    else None,
                )
            project.add_milestone(milestone)

        project.risks = data["risks"]
        project.actual_costs = data["actual_costs"]

        return project


# Example usage
if __name__ == "__main__":
    # Create a new project
    project = ProjectPlan(
        name="ERP System Implementation",
        description="Implementation of new ERP system for finance department",
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2023, 6, 30),
        budget=500000,
        manager="John Doe",
    )

    # Add tasks
    requirements_task = Task(
        name="Requirements Gathering",
        description="Gather and document system requirements",
        start_date=datetime(2023, 1, 1),
        end_date=datetime(2023, 1, 15),
        owner="Business Analyst",
        budget=20000,
        risk_level=RiskLevel.MEDIUM,
    )
    project.add_task(requirements_task)

    development_task = Task(
        name="System Development",
        description="Develop ERP system modules",
        start_date=datetime(2023, 1, 16),
        end_date=datetime(2023, 4, 30),
        owner="Development Team",
        dependencies=["Requirements Gathering"],
        budget=
