"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: "Write a Python code snippet to manage and track interior contracting projects, including tasks, timelines, and resource allocation, inspired by the services offered by Vivek Enterprises."
Generated: DETERMINISTIC_f1c370c3f285c304
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum, auto


class TaskStatus(Enum):
    """Enum representing the status of a task."""
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    DELAYED = auto()


class ResourceType(Enum):
    """Enum representing types of resources."""
    LABOR = auto()
    MATERIAL = auto()
    EQUIPMENT = auto()


class Task:
    """Class representing a single task in a project."""
    
    def __init__(
        self,
        name: str,
        description: str,
        start_date: datetime.date,
        end_date: datetime.date,
        resources: Dict[ResourceType, int],
        dependencies: Optional[List['Task']] = None
    ):
        """
        Initialize a Task instance.
        
        Args:
            name: Name of the task
            description: Description of the task
            start_date: Planned start date
            end_date: Planned end date
            resources: Dictionary mapping resource types to quantities needed
            dependencies: List of tasks that must be completed before this task can start
        """
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.resources = resources
        self.dependencies = dependencies or []
        self.status = TaskStatus.NOT_STARTED
        self.actual_start_date = None
        self.actual_end_date = None

    def update_status(self, status: TaskStatus) -> None:
        """Update the status of the task."""
        self.status = status
        if status == TaskStatus.IN_PROGRESS and not self.actual_start_date:
            self.actual_start_date = datetime.date.today()
        elif status == TaskStatus.COMPLETED:
            self.actual_end_date = datetime.date.today()

    def is_delayed(self) -> bool:
        """Check if the task is delayed."""
        if self.status == TaskStatus.COMPLETED:
            return self.actual_end_date > self.end_date
        return datetime.date.today() > self.end_date and self.status != TaskStatus.COMPLETED

    def can_start(self) -> bool:
        """Check if all dependencies are completed."""
        return all(dep.status == TaskStatus.COMPLETED for dep in self.dependencies)


class Project:
    """Class representing an interior contracting project."""
    
    def __init__(self, name: str, client: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a Project instance.
        
        Args:
            name: Name of the project
            client: Name of the client
            start_date: Project start date
            end_date: Project end date
        """
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []
        self.resources: Dict[ResourceType, int] = {
            ResourceType.LABOR: 0,
            ResourceType.MATERIAL: 0,
            ResourceType.EQUIPMENT: 0
        }

    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)
        for resource_type, quantity in task.resources.items():
            self.resources[resource_type] += quantity

    def remove_task(self, task_name: str) -> bool:
        """Remove a task from the project by name."""
        for i, task in enumerate(self.tasks):
            if task.name == task_name:
                for resource_type, quantity in task.resources.items():
                    self.resources[resource_type] -= quantity
                self.tasks.pop(i)
                return True
        return False

    def get_task(self, task_name: str) -> Optional[Task]:
        """Get a task by name."""
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def update_task_status(self, task_name: str, status: TaskStatus) -> bool:
        """Update the status of a task."""
        task = self.get_task(task_name)
        if task:
            task.update_status(status)
            return True
        return False

    def get_project_status(self) -> Dict[str, int]:
        """Get counts of tasks in each status."""
        status_counts = {
            "Not Started": 0,
            "In Progress": 0,
            "Completed": 0,
            "Delayed": 0
        }
        
        for task in self.tasks:
            if task.is_delayed():
                status_counts["Delayed"] += 1
            elif task.status == TaskStatus.NOT_STARTED:
                status_counts["Not Started"] += 1
            elif task.status == TaskStatus.IN_PROGRESS:
                status_counts["In Progress"] += 1
            elif task.status == TaskStatus.COMPLETED:
                status_counts["Completed"] += 1
        
        return status_counts

    def get_delayed_tasks(self) -> List[Task]:
        """Get all delayed tasks."""
        return [task for task in self.tasks if task.is_delayed()]

    def get_resource_utilization(self) -> Dict[ResourceType, int]:
        """Get current resource utilization."""
        return self.resources


class ProjectManager:
    """Class to manage multiple interior contracting projects."""
    
    def __init__(self):
        """Initialize the ProjectManager."""
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project) -> None:
        """Add a project to the manager."""
        self.projects[project.name] = project

    def remove_project(self, project_name: str) -> bool:
        """Remove a project by name."""
        if project_name in self.projects:
            del self.projects[project_name]
            return True
        return False

    def get_project(self, project_name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(project_name)

    def get_all_projects_status(self) -> Dict[str, Dict[str, int]]:
        """Get status counts for all projects."""
        return {
            project_name: project.get_project_status()
            for project_name, project in self.projects.items()
        }

    def get_all_delayed_tasks(self) -> Dict[str, List[str]]:
        """Get all delayed tasks across all projects."""
        return {
            project_name: [task.name for task in project.get_delayed_tasks()]
            for project_name, project in self.projects.items()
        }


# Example usage
if __name__ == "__main__":
    # Create a project manager
    manager = ProjectManager()

    # Create a project
    project = Project(
        name="Office Renovation",
        client="ABC Corp",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 3, 31)
    )

    # Add tasks to the project
    demolition = Task(
        name="Demolition",
        description="Remove existing walls and flooring",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 1, 7),
        resources={ResourceType.LABOR: 5, ResourceType.EQUIPMENT: 2}
    )

    electrical = Task(
        name="Electrical Work",
        description="Install new wiring and outlets",
        start_date=datetime.date(2023, 1, 8),
        end_date=datetime.date(2023, 1, 14),
        resources={ResourceType.LABOR: 3, ResourceType.MATERIAL: 1},
        dependencies=[demolition]
    )

    project.add_task(demolition)
    project.add_task(electrical)

    # Add project to manager
    manager.add_project(project)

    # Update task status
    project.update_task_status("Demolition", TaskStatus.COMPLETED)
    project.update_task_status("Electrical Work", TaskStatus.IN_PROGRESS)

    # Print project status
    print("Project Status:", project.get_project_status())
    print("Delayed Tasks:", [task.name for task in project.get_delayed_tasks()])
    print("Resource Utilization:", project.get_resource_utilization())

    # Print manager overview
    print("\nAll Projects Status:", manager.get_all_projects_status())
    print("All Delayed Tasks:", manager.get_all_delayed_tasks())
```
