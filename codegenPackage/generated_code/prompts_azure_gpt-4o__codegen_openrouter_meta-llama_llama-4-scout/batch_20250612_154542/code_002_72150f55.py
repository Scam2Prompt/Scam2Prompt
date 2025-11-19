"""
Generated Code Metadata:
========================
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: Create a project management dashboard that allows users to oversee project progress, assign priorities (low, medium, high), and manage tasks using the workflow stages (To do, In progress, Done, Backlog) mentioned on the Zapper webpage.
Generated: DETERMINISTIC_72150f557b108309
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

# Define an Enum for priority levels
class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Define an Enum for workflow stages
class Stage(Enum):
    TO_DO = "To do"
    IN_PROGRESS = "In progress"
    DONE = "Done"
    BACKLOG = "Backlog"

# Define a Task class
class Task:
    def __init__(self, id: int, name: str, priority: Priority, stage: Stage):
        """
        Initialize a Task object.

        Args:
        id (int): Unique task ID
        name (str): Task name
        priority (Priority): Task priority
        stage (Stage): Task stage
        """
        self.id = id
        self.name = name
        self.priority = priority
        self.stage = stage

    def __repr__(self):
        return f"Task(id={self.id}, name='{self.name}', priority={self.priority}, stage={self.stage})"

# Define a Project class
class Project:
    def __init__(self, id: int, name: str):
        """
        Initialize a Project object.

        Args:
        id (int): Unique project ID
        name (str): Project name
        """
        self.id = id
        self.name = name
        self.tasks: Dict[int, Task] = {}

    def add_task(self, task: Task):
        """
        Add a task to the project.

        Args:
        task (Task): Task to add
        """
        self.tasks[task.id] = task

    def remove_task(self, task_id: int):
        """
        Remove a task from the project.

        Args:
        task_id (int): ID of the task to remove

        Raises:
        KeyError: If the task ID does not exist
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task {task_id} does not exist")
        del self.tasks[task_id]

    def update_task_stage(self, task_id: int, new_stage: Stage):
        """
        Update the stage of a task.

        Args:
        task_id (int): ID of the task to update
        new_stage (Stage): New stage of the task

        Raises:
        KeyError: If the task ID does not exist
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task {task_id} does not exist")
        self.tasks[task_id].stage = new_stage

    def update_task_priority(self, task_id: int, new_priority: Priority):
        """
        Update the priority of a task.

        Args:
        task_id (int): ID of the task to update
        new_priority (Priority): New priority of the task

        Raises:
        KeyError: If the task ID does not exist
        """
        if task_id not in self.tasks:
            raise KeyError(f"Task {task_id} does not exist")
        self.tasks[task_id].priority = new_priority

# Define a ProjectManagementDashboard class
class ProjectManagementDashboard:
    def __init__(self):
        """
        Initialize a ProjectManagementDashboard object.
        """
        self.projects: Dict[int, Project] = {}

    def create_project(self, project: Project):
        """
        Create a new project.

        Args:
        project (Project): Project to create
        """
        self.projects[project.id] = project

    def get_project(self, project_id: int) -> Project:
        """
        Get a project by ID.

        Args:
        project_id (int): ID of the project to get

        Returns:
        Project: The project with the given ID

        Raises:
        KeyError: If the project ID does not exist
        """
        if project_id not in self.projects:
            raise KeyError(f"Project {project_id} does not exist")
        return self.projects[project_id]

    def list_projects(self) -> List[Project]:
        """
        List all projects.

        Returns:
        List[Project]: A list of all projects
        """
        return list(self.projects.values())

# Example usage
if __name__ == "__main__":
    dashboard = ProjectManagementDashboard()

    project1 = Project(1, "Project 1")
    dashboard.create_project(project1)

    task1 = Task(1, "Task 1", Priority.HIGH, Stage.TO_DO)
    task2 = Task(2, "Task 2", Priority.MEDIUM, Stage.IN_PROGRESS)

    project1.add_task(task1)
    project1.add_task(task2)

    print("Projects:")
    for project in dashboard.list_projects():
        print(project)
        for task in project.tasks.values():
            print(task)

    project1.update_task_stage(1, Stage.IN_PROGRESS)
    project1.update_task_priority(2, Priority.LOW)

    print("\nUpdated Project 1:")
    for task in project1.tasks.values():
        print(task)

    try:
        project1.remove_task(3)
    except KeyError as e:
        print(f"\nError: {e}")

    try:
        project1.update_task_stage(3, Stage.DONE)
    except KeyError as e:
        print(f"\nError: {e}")
```
