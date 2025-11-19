"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Write a Python code snippet to manage and track industrial projects, including designing and manufacturing machinery, similar to Multiservicios 3L's services.
Generated: DETERMINISTIC_e217881d103a2cb7
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Industrial Project Management System for Machinery Design and Manufacturing

This module provides functionalities to manage and track industrial projects,
including machinery design and manufacturing processes similar to Multiservicios 3L's services.
"""

from datetime import datetime
from enum import Enum, auto
from typing import List, Dict, Optional
import json
import os


class ProjectStatus(Enum):
    """Enumeration for project status."""
    PLANNING = auto()
    DESIGN = auto()
    MANUFACTURING = auto()
    TESTING = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class Task:
    """Represents a task in a project."""
    
    def __init__(self, name: str, description: str, assigned_to: str, due_date: datetime):
        """
        Initialize a task.
        
        Args:
            name: Name of the task
            description: Description of the task
            assigned_to: Person/team assigned to the task
            due_date: Due date for the task
        """
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.completed = False
        self.completion_date = None

    def mark_completed(self) -> None:
        """Mark the task as completed with current date."""
        self.completed = True
        self.completion_date = datetime.now()

    def to_dict(self) -> Dict:
        """Convert task to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'assigned_to': self.assigned_to,
            'due_date': self.due_date.isoformat(),
            'completed': self.completed,
            'completion_date': self.completion_date.isoformat() if self.completion_date else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create task from dictionary."""
        task = cls(
            name=data['name'],
            description=data['description'],
            assigned_to=data['assigned_to'],
            due_date=datetime.fromisoformat(data['due_date'])
        )
        task.completed = data['completed']
        if data['completion_date']:
            task.completion_date = datetime.fromisoformat(data['completion_date'])
        return task


class Project:
    """Represents an industrial project."""
    
    def __init__(self, name: str, description: str, client: str, start_date: datetime, end_date: datetime):
        """
        Initialize a project.
        
        Args:
            name: Name of the project
            description: Description of the project
            client: Client name
            start_date: Project start date
            end_date: Project end date
        """
        self.name = name
        self.description = description
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.status = ProjectStatus.PLANNING
        self.tasks: List[Task] = []
        self.machinery_specs: Dict = {}
        self.budget: float = 0.0
        self.actual_cost: float = 0.0

    def add_task(self, task: Task) -> None:
        """Add a task to the project."""
        self.tasks.append(task)

    def update_status(self, new_status: ProjectStatus) -> None:
        """Update project status."""
        self.status = new_status

    def update_budget(self, amount: float) -> None:
        """Update project budget."""
        self.budget = amount

    def add_cost(self, amount: float) -> None:
        """Add actual cost to the project."""
        self.actual_cost += amount

    def add_machinery_spec(self, spec_name: str, spec_value: str) -> None:
        """Add machinery specification."""
        self.machinery_specs[spec_name] = spec_value

    def get_completion_percentage(self) -> float:
        """Calculate project completion percentage based on tasks."""
        if not self.tasks:
            return 0.0
        completed = sum(1 for task in self.tasks if task.completed)
        return (completed / len(self.tasks)) * 100

    def to_dict(self) -> Dict:
        """Convert project to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'client': self.client,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'status': self.status.name,
            'tasks': [task.to_dict() for task in self.tasks],
            'machinery_specs': self.machinery_specs,
            'budget': self.budget,
            'actual_cost': self.actual_cost
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Project':
        """Create project from dictionary."""
        project = cls(
            name=data['name'],
            description=data['description'],
            client=data['client'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        project.status = ProjectStatus[data['status']]
        project.tasks = [Task.from_dict(task_data) for task_data in data['tasks']]
        project.machinery_specs = data['machinery_specs']
        project.budget = data['budget']
        project.actual_cost = data['actual_cost']
        return project


class ProjectManager:
    """Manages multiple industrial projects."""
    
    def __init__(self, data_file: str = 'projects.json'):
        """
        Initialize project manager.
        
        Args:
            data_file: File to store project data
        """
        self.data_file = data_file
        self.projects: Dict[str, Project] = {}
        self.load_projects()

    def add_project(self, project: Project) -> None:
        """Add a project to the manager."""
        if project.name in self.projects:
            raise ValueError(f"Project '{project.name}' already exists")
        self.projects[project.name] = project
        self.save_projects()

    def get_project(self, name: str) -> Optional[Project]:
        """Get a project by name."""
        return self.projects.get(name)

    def update_project(self, name: str, updated_project: Project) -> None:
        """Update an existing project."""
        if name not in self.projects:
            raise ValueError(f"Project '{name}' not found")
        self.projects[name] = updated_project
        self.save_projects()

    def delete_project(self, name: str) -> None:
        """Delete a project."""
        if name not in self.projects:
            raise ValueError(f"Project '{name}' not found")
        del self.projects[name]
        self.save_projects()

    def list_projects(self) -> List[Project]:
        """List all projects."""
        return list(self.projects.values())

    def save_projects(self) -> None:
        """Save projects to file."""
        data = {
            'projects': {
                name: project.to_dict() for name, project in self.projects.items()
            }
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_projects(self) -> None:
        """Load projects from file."""
        if not os.path.exists(self.data_file):
            return
            
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.projects = {
                    name: Project.from_dict(project_data)
                    for name, project_data in data['projects'].items()
                }
        except (json.JSONDecodeError, FileNotFoundError) as e:
            raise RuntimeError(f"Error loading projects: {str(e)}")


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()
    
    # Create a new project
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 6, 30)
    project = Project(
        name="Industrial Mixer Design",
        description="Design and manufacture of a custom industrial mixer",
        client="FoodTech Inc.",
        start_date=start_date,
        end_date=end_date
    )
    
    # Add tasks
    design_task = Task(
        name="Initial Design",
        description="Create initial design concepts",
        assigned_to="Design Team",
        due_date=datetime(2023, 1, 15)
    )
    project.add_task(design_task)
    
    manufacturing_task = Task(
        name="Prototype Manufacturing",
        description="Manufacture prototype based on approved design",
        assigned_to="Manufacturing Team",
        due_date=datetime(2023, 3, 1)
    )
    project.add_task(manufacturing_task)
    
    # Add project to manager
    manager.add_project(project)
    
    # Print all projects
    for proj in manager.list_projects():
        print(f"Project: {proj.name}, Status: {proj.status.name}, Completion: {proj.get_completion_percentage():.2f}%")
```
