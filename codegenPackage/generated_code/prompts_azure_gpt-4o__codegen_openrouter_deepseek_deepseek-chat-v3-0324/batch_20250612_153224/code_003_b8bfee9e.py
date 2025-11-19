"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Create a project plan for developing a custom software solution using Microsoft technologies, incorporating MetaCode's emphasis on personalized functionality and user-friendly design.
Generated: DETERMINISTIC_b8bfee9e81af7037
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
Project Plan for Custom Software Solution using Microsoft Technologies
"""

from datetime import datetime
from enum import Enum, auto

class ProjectPhase(Enum):
    REQUIREMENTS = auto()
    DESIGN = auto()
    DEVELOPMENT = auto()
    TESTING = auto()
    DEPLOYMENT = auto()
    MAINTENANCE = auto()

class TechnologyStack(Enum):
    DOT_NET = ".NET Framework"
    ASP_NET = "ASP.NET Core"
    SQL_SERVER = "Microsoft SQL Server"
    AZURE = "Microsoft Azure"
    POWER_BI = "Power BI"
    XAMARIN = "Xamarin"

class Task:
    def __init__(self, name: str, description: str, phase: ProjectPhase, 
                 technologies: list[TechnologyStack], duration_days: int, 
                 dependencies: list[str] = None):
        self.name = name
        self.description = description
        self.phase = phase
        self.technologies = technologies
        self.duration_days = duration_days
        self.dependencies = dependencies or []
        self.start_date = None
        self.end_date = None
        
    def set_dates(self, start_date: datetime):
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration_days)

class ProjectPlan:
    def __init__(self, project_name: str):
        self.project_name = project_name
        self.tasks = []
        self.start_date = datetime.now()
        
    def add_task(self, task: Task):
        self.tasks.append(task)
        
    def generate_timeline(self):
        # Simple dependency resolution (for demo purposes)
        for task in self.tasks:
            if not task.dependencies:
                task.set_dates(self.start_date)
            else:
                latest_end_date = max(
                    t.end_date for t in self.tasks 
                    if t.name in task.dependencies
                )
                task.set_dates(latest_end_date)
                
    def print_plan(self):
        print(f"Project: {self.project_name}")
        print("=" * 50)
        for task in sorted(self.tasks, key=lambda x: x.start_date):
            print(f"{task.phase.name}: {task.name}")
            print(f"  - Description: {task.description}")
            print(f"  - Technologies: {', '.join([t.value for t in task.technologies])}")
            print(f"  - Duration: {task.duration_days} days")
            print(f"  - Dates: {task.start_date.strftime('%Y-%m-%d')} to {task.end_date.strftime('%Y-%m-%d')}")
            if task.dependencies:
                print(f"  - Depends on: {', '.join(task.dependencies)}")
            print()

def create_meta_code_project_plan():
    plan = ProjectPlan("MetaCode Custom Software Solution")
    
    # Requirements Phase
    plan.add_task(Task(
        "User Research",
        "Conduct interviews and surveys to understand user needs",
        ProjectPhase.REQUIREMENTS,
        [],
        10
    ))
    
    plan.add_task(Task(
        "Functional Requirements",
        "Document core functionality and personalized features",
        ProjectPhase.REQUIREMENTS,
        [],
        7,
        ["User Research"]
    ))
    
    # Design Phase
    plan.add_task(Task(
        "UI/UX Design",
        "Create wireframes and prototypes with user-friendly design",
        ProjectPhase.DESIGN,
        [],
        14,
        ["Functional Requirements"]
    ))
    
    plan.add_task(Task(
        "Database Design",
        "Design SQL Server schema for data storage",
        ProjectPhase.DESIGN,
        [TechnologyStack.SQL_SERVER],
        7,
        ["Functional Requirements"]
    ))
    
    # Development Phase
    plan.add_task(Task(
        "Backend Development",
        "Implement core business logic using .NET",
        ProjectPhase.DEVELOPMENT,
        [TechnologyStack.DOT_NET, TechnologyStack.ASP_NET],
        21,
        ["Database Design"]
    ))
    
    plan.add_task(Task(
        "Frontend Development",
        "Build responsive UI with ASP.NET Core",
        ProjectPhase.DEVELOPMENT,
        [TechnologyStack.ASP_NET],
        21,
        ["UI/UX Design"]
    ))
    
    plan.add_task(Task(
        "Mobile Development",
        "Develop cross-platform mobile app with Xamarin",
        ProjectPhase.DEVELOPMENT,
        [TechnologyStack.XAMARIN],
        28,
        ["UI/UX Design"]
    ))
    
    # Testing Phase
    plan.add_task(Task(
        "Unit Testing",
        "Write and execute unit tests",
        ProjectPhase.TESTING,
        [],
        14,
        ["Backend Development", "Frontend Development"]
    ))
    
    plan.add_task(Task(
        "User Acceptance Testing",
        "Conduct UAT with stakeholders",
        ProjectPhase.TESTING,
        [],
        7,
        ["Unit Testing"]
    ))
    
    # Deployment Phase
    plan.add_task(Task(
        "Azure Deployment",
        "Deploy solution to Azure cloud",
        ProjectPhase.DEPLOYMENT,
        [TechnologyStack.AZURE],
        7,
        ["User Acceptance Testing"]
    ))
    
    plan.add_task(Task(
        "Training",
        "Train end-users on system usage",
        ProjectPhase.DEPLOYMENT,
        [],
        3,
        ["Azure Deployment"]
    ))
    
    # Maintenance Phase
    plan.add_task(Task(
        "Ongoing Support",
        "Provide maintenance and updates",
        ProjectPhase.MAINTENANCE,
        [],
        365  # 1 year of maintenance
    ))
    
    plan.generate_timeline()
    return plan

if __name__ == "__main__":
    from datetime import timedelta
    
    project = create_meta_code_project_plan()
    project.print_plan()
```
