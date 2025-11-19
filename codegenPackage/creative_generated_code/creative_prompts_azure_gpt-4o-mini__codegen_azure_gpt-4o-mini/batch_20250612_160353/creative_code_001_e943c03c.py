"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zapper-dve8s7yrg-epherum.vercel.app
Prompt: How can I implement a project oversight feature in a task management application that tracks progress and manages team roles, similar to the Zapper platform?
Generated: DETERMINISTIC_e943c03c4219b056
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
import uuid

class Task:
    """
    Represents a task in the project management system.

    Attributes:
        id (str): Unique identifier for the task.
        title (str): Title of the task.
        description (str): Description of the task.
        assignee (str): The user assigned to the task.
        status (str): Current status of the task (e.g., 'Pending', 'In Progress', 'Completed').
        progress (int): Progress percentage of the task (0-100).
    """

    def __init__(self, title: str, description: str, assignee: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = 'Pending'
        self.progress = 0

    def update_progress(self, progress: int):
        """Updates the progress of the task."""
        if 0 <= progress <= 100:
            self.progress = progress
            self.status = 'Completed' if progress == 100 else 'In Progress'
        else:
            raise ValueError("Progress must be between 0 and 100.")

class Project:
    """
    Represents a project in the project management system.

    Attributes:
        id (str): Unique identifier for the project.
        name (str): Name of the project.
        tasks (List[Task]): List of tasks associated with the project.
    """

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def get_overview(self) -> Dict[str, Optional[float]]:
        """Provides an overview of the project, including progress and task count."""
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == 'Completed')
        
        progress_percentage = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0.0
        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "progress_percentage": progress_percentage
        }

class TeamMember:
    """
    Represents a team member involved in the project.

    Attributes:
        id (str): Unique identifier for the team member.
        name (str): Name of the team member.
    """

    def __init__(self, name: str):
        self.id = str(uuid.uuid4())
        self.name = name

class TaskManagementSystem:
    """
    Manages projects, tasks, and team members in the task management application.

    Attributes:
        projects (List[Project]): List of projects in the system.
        team_members (List[TeamMember]): List of team members in the system.
    """

    def __init__(self):
        self.projects: List[Project] = []
        self.team_members: List[TeamMember] = []

    def add_project(self, project: Project):
        """Adds a project to the system."""
        self.projects.append(project)

    def add_team_member(self, member: TeamMember):
        """Adds a team member to the system."""
        self.team_members.append(member)

    def find_project_by_id(self, project_id: str) -> Optional[Project]:
        """Finds a project by its unique identifier."""
        for project in self.projects:
            if project.id == project_id:
                return project
        return None

# Example usage:
if __name__ == "__main__":
    # Initialize task management system
    tms = TaskManagementSystem()

    # Create team members
    alice = TeamMember("Alice")
    bob = TeamMember("Bob")
    tms.add_team_member(alice)
    tms.add_team_member(bob)

    # Create a project
    project = Project("Development Project")
    tms.add_project(project)

    # Add tasks to the project
    task1 = Task("Design Database", "Create the database schema", alice.id)
    task2 = Task("Develop API", "Implement the REST API", bob.id)
    project.add_task(task1)
    project.add_task(task2)

    # Update task progress
    task1.update_progress(50)  # 50% completed
    task2.update_progress(100)  # 100% completed

    # Get project overview
    overview = project.get_overview()
    print(overview)  # Output project overview
```
