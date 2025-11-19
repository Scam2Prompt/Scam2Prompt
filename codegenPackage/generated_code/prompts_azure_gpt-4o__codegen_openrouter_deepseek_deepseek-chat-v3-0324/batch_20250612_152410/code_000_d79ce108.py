"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: Write Python code to simulate a project management system for housing developments and retirement living, incorporating health and safety guidelines as outlined by Westpoint Construction.
Generated: DETERMINISTIC_d79ce1087e45216f
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management System for Housing Developments and Retirement Living
Incorporating Health and Safety Guidelines by Westpoint Construction

This system manages projects, tasks, and safety compliance for housing and retirement living developments.
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional


class ProjectStatus(Enum):
    """Enum representing the status of a project."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    TODO = auto()
    IN_PROGRESS = auto()
    REVIEW = auto()
    DONE = auto()
    BLOCKED = auto()


class SafetyLevel(Enum):
    """Enum representing the safety level required for a task."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()


class SafetyGuideline:
    """Class representing a safety guideline with description and compliance requirements."""
    
    def __init__(self, guideline_id: str, description: str, compliance_requirements: str):
        self.guideline_id = guideline_id
        self.description = description
        self.compliance_requirements = compliance_requirements
    
    def __str__(self):
        return f"{self.guideline_id}: {self.description}"


class Task:
    """Class representing a task in a project."""
    
    def __init__(
        self,
        task_id: str,
        name: str,
        description: str,
        assigned_to: str,
        due_date: datetime,
        safety_level: SafetyLevel,
        required_guidelines: List[SafetyGuideline]
    ):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.safety_level = safety_level
        self.required_guidelines = required_guidelines
        self.status = TaskStatus.TODO
        self.completion_date: Optional[datetime] = None
    
    def update_status(self, new_status: TaskStatus):
        """Update the status of the task."""
        self.status = new_status
        if new_status == TaskStatus.DONE:
            self.completion_date = datetime.now()
    
    def is_compliant(self) -> bool:
        """Check if all required safety guidelines are met."""
        # In a real implementation, this would verify actual compliance
        return True
    
    def __str__(self):
        return f"Task {self.task_id}: {self.name} ({self.status.name})"


class Project:
    """Class representing a housing or retirement living development project."""
    
    def __init__(
        self,
        project_id: str,
        name: str,
        description: str,
        project_type: str,
        start_date: datetime,
        end_date: datetime,
        manager: str
    ):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.project_type = project_type  # e.g., "Housing Development" or "Retirement Living"
        self.start_date = start_date
        self.end_date = end_date
        self.manager = manager
        self.status = ProjectStatus.NOT_STARTED
        self.tasks: List[Task] = []
        self.safety_guidelines: Dict[str, SafetyGuideline] = {}
    
    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)
        if self.status == ProjectStatus.NOT_STARTED:
            self.status = ProjectStatus.IN_PROGRESS
    
    def update_project_status(self):
        """Update the project status based on task completion."""
        if all(task.status == TaskStatus.DONE for task in self.tasks):
            self.status = ProjectStatus.COMPLETED
        elif any(task.status == TaskStatus.BLOCKED for task in self.tasks):
            self.status = ProjectStatus.ON_HOLD
    
    def add_safety_guideline(self, guideline: SafetyGuideline):
        """Add a safety guideline to the project."""
        self.safety_guidelines[guideline.guideline_id] = guideline
    
    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """Get all tasks with the specified status."""
        return [task for task in self.tasks if task.status == status]
    
    def __str__(self):
        return f"Project {self.project_id}: {self.name} ({self.status.name})"


class ProjectManager:
    """Class to manage multiple projects and provide reporting."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.safety_guidelines: Dict[str, SafetyGuideline] = {}
    
    def create_project(self, project: Project):
        """Add a new project to the manager."""
        if project.project_id in self.projects:
            raise ValueError(f"Project with ID {project.project_id} already exists")
        self.projects[project.project_id] = project
    
    def get_project(self, project_id: str) -> Project:
        """Retrieve a project by its ID."""
        if project_id not in self.projects:
            raise ValueError(f"Project with ID {project_id} not found")
        return self.projects[project_id]
    
    def add_safety_guideline(self, guideline: SafetyGuideline):
        """Add a safety guideline to the global repository."""
        self.safety_guidelines[guideline.guideline_id] = guideline
    
    def get_safety_guideline(self, guideline_id: str) -> SafetyGuideline:
        """Retrieve a safety guideline by its ID."""
        if guideline_id not in self.safety_guidelines:
            raise ValueError(f"Safety guideline with ID {guideline_id} not found")
        return self.safety_guidelines[guideline_id]
    
    def get_projects_by_status(self, status: ProjectStatus) -> List[Project]:
        """Get all projects with the specified status."""
        return [project for project in self.projects.values() if project.status == status]
    
    def generate_safety_compliance_report(self, project_id: str) -> Dict[str, bool]:
        """Generate a report of safety compliance for all tasks in a project."""
        project = self.get_project(project_id)
        return {
            task.task_id: task.is_compliant()
            for task in project.tasks
        }


# Example usage
if __name__ == "__main__":
    # Initialize project manager
    manager = ProjectManager()
    
    # Create safety guidelines
    electrical_safety = SafetyGuideline(
        "ELEC-001",
        "Electrical Safety Protocol",
        "All electrical work must be performed by licensed electricians"
    )
    height_safety = SafetyGuideline(
        "HEIGHT-001",
        "Working at Heights Protocol",
        "Fall protection required for all work above 6 feet"
    )
    
    manager.add_safety_guideline(electrical_safety)
    manager.add_safety_guideline(height_safety)
    
    # Create a project
    retirement_project = Project(
        "RET-2023-001",
        "Sunset Retirement Village",
        "Construction of 50-unit retirement living complex",
        "Retirement Living",
        datetime(2023, 1, 1),
        datetime(2024, 6, 30),
        "John Smith"
    )
    
    # Add safety guidelines to project
    retirement_project.add_safety_guideline(electrical_safety)
    retirement_project.add_safety_guideline(height_safety)
    
    # Create tasks
    foundation_task = Task(
        "TASK-001",
        "Foundation Work",
        "Excavation and pouring of foundations",
        "Construction Team A",
        datetime(2023, 2, 15),
        SafetyLevel.HIGH,
        [height_safety]
    )
    
    electrical_task = Task(
        "TASK-002",
        "Electrical Installation",
        "Installation of electrical systems",
        "Electrical Team B",
        datetime(2023, 5, 1),
        SafetyLevel.CRITICAL,
        [electrical_safety]
    )
    
    # Add tasks to project
    retirement_project.add_task(foundation_task)
    retirement_project.add_task(electrical_task)
    
    # Add project to manager
    manager.create_project(retirement_project)
    
    # Update task status
    foundation_task.update_status(TaskStatus.DONE)
    retirement_project.update_project_status()
    
    # Generate reports
    print(f"Project Status: {retirement_project}")
    print("Tasks:")
    for task in retirement_project.tasks:
        print(f"  - {task}")
    
    compliance_report = manager.generate_safety_compliance_report("RET-2023-001")
    print("\nSafety Compliance Report:")
    for task_id, compliant in compliance_report.items():
        print(f"  - {task_id}: {'Compliant' if compliant else 'Non-Compliant'}")
```
