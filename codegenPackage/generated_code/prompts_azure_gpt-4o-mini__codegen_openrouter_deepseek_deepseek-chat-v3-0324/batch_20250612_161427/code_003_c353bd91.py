"""
Generated Code Metadata:
========================
Original URL: https://trekk.com
Prompt: Generate a sample project plan for a complete rebranding and website migration similar to what Trekk has done for their clients.
Generated: DETERMINISTIC_c353bd911bb48e2b
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Plan for Complete Rebranding and Website Migration
"""

from datetime import datetime, timedelta
from enum import Enum
from typing import List, Dict, Optional


class TaskStatus(Enum):
    """Enum for task statuses"""
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    BLOCKED = "Blocked"


class Task:
    """Class representing a project task"""
    
    def __init__(
        self,
        name: str,
        description: str,
        owner: str,
        duration_days: int,
        dependencies: Optional[List[str]] = None,
        status: TaskStatus = TaskStatus.NOT_STARTED
    ):
        self.name = name
        self.description = description
        self.owner = owner
        self.duration_days = duration_days
        self.dependencies = dependencies or []
        self.status = status
        self.start_date = None
        self.end_date = None

    def set_dates(self, start_date: datetime):
        """Set start and end dates for the task"""
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration_days)


class ProjectPhase:
    """Class representing a project phase"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to this phase"""
        self.tasks.append(task)


class ProjectPlan:
    """Main project plan class"""
    
    def __init__(self, project_name: str, start_date: datetime):
        self.project_name = project_name
        self.start_date = start_date
        self.phases: List[ProjectPhase] = []
        self.current_date = start_date

    def add_phase(self, phase: ProjectPhase):
        """Add a phase to the project"""
        self.phases.append(phase)

    def generate_timeline(self):
        """Generate timeline with dates for all tasks"""
        for phase in self.phases:
            for task in phase.tasks:
                # Check if task has dependencies
                if task.dependencies:
                    # Find the latest end date among dependencies
                    latest_dep_end = None
                    for dep_name in task.dependencies:
                        for p in self.phases:
                            for t in p.tasks:
                                if t.name == dep_name:
                                    if latest_dep_end is None or t.end_date > latest_dep_end:
                                        latest_dep_end = t.end_date
                    
                    if latest_dep_end:
                        task.set_dates(latest_dep_end)
                        self.current_date = latest_dep_end
                    else:
                        raise ValueError(f"Dependency {task.dependencies} not found")
                else:
                    task.set_dates(self.current_date)
                
                self.current_date = task.end_date

    def print_plan(self):
        """Print the project plan in a readable format"""
        print(f"Project: {self.project_name}")
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}\n")
        
        for phase in self.phases:
            print(f"Phase: {phase.name}")
            print(f"Description: {phase.description}\n")
            
            print("Tasks:")
            for task in phase.tasks:
                print(f"- {task.name}")
                print(f"  Description: {task.description}")
                print(f"  Owner: {task.owner}")
                print(f"  Duration: {task.duration_days} days")
                print(f"  Status: {task.status.value}")
                if task.start_date and task.end_date:
                    print(f"  Dates: {task.start_date.strftime('%Y-%m-%d')} to {task.end_date.strftime('%Y-%m-%d')}")
                if task.dependencies:
                    print(f"  Depends on: {', '.join(task.dependencies)}")
                print()


def create_rebranding_project_plan():
    """Create a sample rebranding and website migration project plan"""
    
    # Project setup
    start_date = datetime(2023, 11, 1)
    project = ProjectPlan("Company Rebranding & Website Migration", start_date)
    
    # Phase 1: Discovery & Planning
    discovery = ProjectPhase("Discovery & Planning", "Initial research and planning phase")
    
    discovery.add_task(Task(
        "Stakeholder Interviews",
        "Conduct interviews with key stakeholders to understand brand goals",
        "Project Manager",
        5
    ))
    
    discovery.add_task(Task(
        "Competitive Analysis",
        "Analyze competitors and market positioning",
        "Marketing Team",
        7
    ))
    
    discovery.add_task(Task(
        "Project Scope Definition",
        "Define project scope, goals, and deliverables",
        "Project Manager",
        3,
        ["Stakeholder Interviews", "Competitive Analysis"]
    ))
    
    project.add_phase(discovery)
    
    # Phase 2: Brand Development
    brand_dev = ProjectPhase("Brand Development", "Creating new brand identity")
    
    brand_dev.add_task(Task(
        "Brand Strategy Workshop",
        "Conduct workshop to define brand positioning and messaging",
        "Brand Strategist",
        2,
        ["Project Scope Definition"]
    ))
    
    brand_dev.add_task(Task(
        "Logo Design",
        "Create new logo concepts and finalize design",
        "Design Team",
        10,
        ["Brand Strategy Workshop"]
    ))
    
    brand_dev.add_task(Task(
        "Brand Guidelines",
        "Develop comprehensive brand guidelines document",
        "Design Team",
        7,
        ["Logo Design"]
    ))
    
    project.add_phase(brand_dev)
    
    # Phase 3: Website Migration
    website = ProjectPhase("Website Migration", "Rebuild and migrate website")
    
    website.add_task(Task(
        "Content Audit",
        "Audit existing website content and structure",
        "Content Team",
        5,
        ["Project Scope Definition"]
    ))
    
    website.add_task(Task(
        "Information Architecture",
        "Define new site structure and navigation",
        "UX Team",
        7,
        ["Content Audit"]
    ))
    
    website.add_task(Task(
        "UI Design",
        "Create new UI designs based on brand guidelines",
        "Design Team",
        14,
        ["Brand Guidelines", "Information Architecture"]
    ))
    
    website.add_task(Task(
        "Frontend Development",
        "Develop new website frontend",
        "Development Team",
        21,
        ["UI Design"]
    ))
    
    website.add_task(Task(
        "Backend Development",
        "Develop new website backend and CMS integration",
        "Development Team",
        21,
        ["UI Design"]
    ))
    
    website.add_task(Task(
        "Content Migration",
        "Migrate and rewrite content for new site",
        "Content Team",
        14,
        ["Frontend Development", "Backend Development"]
    ))
    
    website.add_task(Task(
        "QA Testing",
        "Conduct quality assurance testing",
        "QA Team",
        7,
        ["Content Migration"]
    ))
    
    project.add_phase(website)
    
    # Phase 4: Launch & Transition
    launch = ProjectPhase("Launch & Transition", "Final preparations and launch")
    
    launch.add_task(Task(
        "Soft Launch",
        "Launch to limited audience for final testing",
        "Project Manager",
        2,
        ["QA Testing"]
    ))
    
    launch.add_task(Task(
        "Full Launch",
        "Public launch of new brand and website",
        "Project Manager",
        1,
        ["Soft Launch"]
    ))
    
    launch.add_task(Task(
        "Post-Launch Review",
        "Review launch metrics and address any issues",
        "Project Team",
        5,
        ["Full Launch"]
    ))
    
    project.add_phase(launch)
    
    # Generate timeline
    project.generate_timeline()
    
    return project


if __name__ == "__main__":
    # Create and print the project plan
    rebranding_project = create_rebranding_project_plan()
    rebranding_project.print_plan()
```
