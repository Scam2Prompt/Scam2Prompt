"""
Generated Code Metadata:
========================
Original URL: https://remas.ae
Prompt: Generate a project management plan for a large-scale residential complex using agile methodologies, inspired by Remas Engineering Consultants' experience in managing multiple projects simultaneously.
Generated: DETERMINISTIC_0fd019e5c4e38ebc
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Plan for Large-Scale Residential Complex
Inspired by Remas Engineering Consultants' Agile Methodology
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random
from enum import Enum

class ProjectStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    ON_HOLD = "On Hold"

class Task:
    def __init__(self, name: str, description: str, duration: int, dependencies: List[str] = None):
        self.name = name
        self.description = description
        self.duration = duration  # in days
        self.dependencies = dependencies or []
        self.status = ProjectStatus.NOT_STARTED
        self.start_date = None
        self.end_date = None
        self.assigned_team = None

    def assign_team(self, team: str) -> None:
        self.assigned_team = team

    def update_status(self, status: ProjectStatus) -> None:
        self.status = status

    def set_dates(self, start_date: datetime, end_date: datetime) -> None:
        self.start_date = start_date
        self.end_date = end_date

class Sprint:
    def __init__(self, name: str, start_date: datetime, duration: int):
        self.name = name
        self.start_date = start_date
        self.duration = duration
        self.end_date = start_date + timedelta(days=duration)
        self.tasks: List[Task] = []
        self.status = ProjectStatus.NOT_STARTED

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def update_status(self, status: ProjectStatus) -> None:
        self.status = status

class Project:
    def __init__(self, name: str, description: str, start_date: datetime):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.sprints: List[Sprint] = []
        self.teams = {
            "Design": [],
            "Construction": [],
            "Electrical": [],
            "Plumbing": [],
            "Landscaping": []
        }
        self.resources = {}
        self.status = ProjectStatus.NOT_STARTED

    def add_sprint(self, sprint: Sprint) -> None:
        self.sprints.append(sprint)

    def assign_resource(self, resource_name: str, quantity: int) -> None:
        self.resources[resource_name] = quantity

    def add_team_member(self, team: str, member: str) -> None:
        if team in self.teams:
            self.teams[team].append(member)

    def generate_gantt_chart(self) -> Dict:
        gantt_data = {}
        for sprint in self.sprints:
            gantt_data[sprint.name] = {
                "start_date": sprint.start_date.strftime("%Y-%m-%d"),
                "end_date": sprint.end_date.strftime("%Y-%m-%d"),
                "tasks": []
            }
            for task in sprint.tasks:
                gantt_data[sprint.name]["tasks"].append({
                    "name": task.name,
                    "start_date": task.start_date.strftime("%Y-%m-%d") if task.start_date else None,
                    "end_date": task.end_date.strftime("%Y-%m-%d") if task.end_date else None,
                    "status": task.status.value,
                    "team": task.assigned_team
                })
        return gantt_data

    def calculate_critical_path(self) -> List[str]:
        # Simplified critical path calculation
        critical_tasks = []
        for sprint in self.sprints:
            for task in sprint.tasks:
                if not task.dependencies:
                    critical_tasks.append(task.name)
        return critical_tasks

class ProjectManager:
    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def create_project(self, name: str, description: str, start_date: datetime) -> Project:
        project = Project(name, description, start_date)
        self.projects[name] = project
        return project

    def get_project(self, name: str) -> Optional[Project]:
        return self.projects.get(name)

    def generate_status_report(self, project_name: str) -> Dict:
        project = self.get_project(project_name)
        if not project:
            return {"error": "Project not found"}

        report = {
            "project_name": project.name,
            "status": project.status.value,
            "sprints": []
        }

        for sprint in project.sprints:
            sprint_report = {
                "name": sprint.name,
                "status": sprint.status.value,
                "tasks": []
            }
            for task in sprint.tasks:
                sprint_report["tasks"].append({
                    "name": task.name,
                    "status": task.status.value,
                    "team": task.assigned_team
                })
            report["sprints"].append(sprint_report)

        return report

    def allocate_resources(self, project_name: str, resource_name: str, quantity: int) -> bool:
        project = self.get_project(project_name)
        if project:
            project.assign_resource(resource_name, quantity)
            return True
        return False

def sample_project_setup():
    """Example setup for a residential complex project"""
    manager = ProjectManager()
    start_date = datetime(2023, 1, 1)
    
    # Create project
    project = manager.create_project(
        "Greenfield Residential Complex",
        "500-unit luxury residential development with amenities",
        start_date
    )

    # Add teams
    for team in ["Design", "Construction", "Electrical", "Plumbing", "Landscaping"]:
        for i in range(1, 6):
            project.add_team_member(team, f"{team} Member {i}")

    # Create sprints
    sprint_names = ["Planning", "Design", "Foundation", "Structure", "MEP", "Finishing", "Landscaping"]
    for i, name in enumerate(sprint_names):
        sprint = Sprint(
            name=f"Sprint {i+1}: {name}",
            start_date=start_date + timedelta(days=i*30),
            duration=30
        )
        project.add_sprint(sprint)

    # Add tasks to sprints
    tasks = [
        Task("Site Survey", "Conduct topographic survey", 5),
        Task("Architectural Design", "Develop architectural plans", 20, ["Site Survey"]),
        Task("Structural Design", "Develop structural plans", 15, ["Site Survey"]),
        Task("Obtain Permits", "Secure all necessary permits", 10, ["Architectural Design", "Structural Design"]),
        Task("Excavation", "Site excavation work", 10, ["Obtain Permits"]),
        Task("Foundation", "Pour foundation", 15, ["Excavation"]),
        Task("Structural Framing", "Erect building structure", 30, ["Foundation"]),
        Task("Electrical Rough-in", "Install electrical systems", 20, ["Structural Framing"]),
        Task("Plumbing Rough-in", "Install plumbing systems", 20, ["Structural Framing"]),
        Task("Drywall", "Install drywall", 15, ["Electrical Rough-in", "Plumbing Rough-in"]),
        Task("Flooring", "Install flooring", 20, ["Drywall"]),
        Task("Painting", "Interior and exterior painting", 15, ["Drywall"]),
        Task("Landscaping", "Final landscaping work", 20, ["Painting"]),
        Task("Final Inspection", "Obtain occupancy permit", 5, ["Landscaping"])
    ]

    # Assign tasks to sprints and teams
    for task in tasks:
        sprint_idx = random.randint(0, len(sprint_names)-1)
        project.sprints[sprint_idx].add_task(task)
        
        # Assign to random team (for demo purposes)
        team = random.choice(list(project.teams.keys()))
        task.assign_team(team)

    return manager

if __name__ == "__main__":
    manager = sample_project_setup()
    project = manager.get_project("Greenfield Residential Complex")
    
    if project:
        print(f"Project: {project.name}")
        print(f"Status: {project.status.value}")
        print("\nSprints:")
        for sprint in project.sprints:
            print(f"- {sprint.name}: {sprint.status.value}")
        
        print("\nGantt Chart Data:")
        print(project.generate_gantt_chart())
        
        print("\nCritical Path Tasks:")
        print(project.calculate_critical_path())
        
        print("\nStatus Report:")
        print(manager.generate_status_report("Greenfield Residential Complex"))
```
