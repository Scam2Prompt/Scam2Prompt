"""
Generated Code Metadata:
========================
Original URL: https://rdmerakyat.com
Prompt: Generate a code snippet for a project management app that integrates architectural solutions and allows collaboration among architects.
Generated: DETERMINISTIC_448df0c69e840e3b
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_app.py
from typing import List, Dict, Optional
from datetime import datetime
import uuid
from enum import Enum, auto


class ProjectStatus(Enum):
    """Enum representing the status of a project."""
    DRAFT = auto()
    ACTIVE = auto()
    ON_HOLD = auto()
    COMPLETED = auto()
    ARCHIVED = auto()


class UserRole(Enum):
    """Enum representing user roles in a project."""
    ADMIN = auto()
    ARCHITECT = auto()
    ENGINEER = auto()
    CLIENT = auto()


class User:
    """Class representing a user in the system."""
    
    def __init__(self, user_id: str, name: str, email: str, role: UserRole):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role


class ArchitecturalSolution:
    """Class representing an architectural solution in a project."""
    
    def __init__(self, solution_id: str, name: str, description: str, created_by: User):
        self.solution_id = solution_id
        self.name = name
        self.description = description
        self.created_by = created_by
        self.created_at = datetime.now()
        self.versions: List['ArchitecturalSolutionVersion'] = []
        self.comments: List['Comment'] = []


class ArchitecturalSolutionVersion:
    """Class representing a version of an architectural solution."""
    
    def __init__(self, version_id: str, solution: ArchitecturalSolution, 
                 description: str, created_by: User):
        self.version_id = version_id
        self.solution = solution
        self.description = description
        self.created_by = created_by
        self.created_at = datetime.now()
        self.files: List[str] = []


class Comment:
    """Class representing a comment on an architectural solution."""
    
    def __init__(self, comment_id: str, content: str, created_by: User, 
                 solution: ArchitecturalSolution):
        self.comment_id = comment_id
        self.content = content
        self.created_by = created_by
        self.solution = solution
        self.created_at = datetime.now()
        self.replies: List['Comment'] = []


class Project:
    """Class representing a project in the system."""
    
    def __init__(self, project_id: str, name: str, description: str, created_by: User):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.created_by = created_by
        self.created_at = datetime.now()
        self.status = ProjectStatus.DRAFT
        self.members: List[User] = [created_by]
        self.solutions: List[ArchitecturalSolution] = []
        self.tasks: List['Task'] = []


class Task:
    """Class representing a task in a project."""
    
    def __init__(self, task_id: str, title: str, description: str, 
                 assigned_to: User, project: Project):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.project = project
        self.created_at = datetime.now()
        self.due_date: Optional[datetime] = None
        self.completed = False


class ProjectManagementApp:
    """Main class for the project management application."""
    
    def __init__(self):
        self.projects: Dict[str, Project] = {}
        self.users: Dict[str, User] = {}
    
    def create_user(self, name: str, email: str, role: UserRole) -> User:
        """Create a new user."""
        if not name or not email:
            raise ValueError("Name and email are required")
        
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email, role)
        self.users[user_id] = user
        return user
    
    def create_project(self, name: str, description: str, created_by: User) -> Project:
        """Create a new project."""
        if not name:
            raise ValueError("Project name is required")
        
        project_id = str(uuid.uuid4())
        project = Project(project_id, name, description, created_by)
        self.projects[project_id] = project
        return project
    
    def add_project_member(self, project_id: str, user: User) -> None:
        """Add a member to a project."""
        project = self.projects.get(project_id)
        if not project:
            raise ValueError("Project not found")
        
        if user not in project.members:
            project.members.append(user)
    
    def create_architectural_solution(self, project_id: str, name: str, 
                                    description: str, created_by: User) -> ArchitecturalSolution:
        """Create a new architectural solution in a project."""
        project = self.projects.get(project_id)
        if not project:
            raise ValueError("Project not found")
        
        if created_by not in project.members:
            raise ValueError("User is not a member of this project")
        
        solution_id = str(uuid.uuid4())
        solution = ArchitecturalSolution(solution_id, name, description, created_by)
        project.solutions.append(solution)
        return solution
    
    def add_solution_version(self, solution_id: str, description: str, 
                           created_by: User) -> ArchitecturalSolutionVersion:
        """Add a new version to an architectural solution."""
        solution = None
        for project in self.projects.values():
            for sol in project.solutions:
                if sol.solution_id == solution_id:
                    solution = sol
                    break
            if solution:
                break
        
        if not solution:
            raise ValueError("Solution not found")
        
        version_id = str(uuid.uuid4())
        version = ArchitecturalSolutionVersion(version_id, solution, description, created_by)
        solution.versions.append(version)
        return version
    
    def add_comment_to_solution(self, solution_id: str, content: str, 
                              created_by: User) -> Comment:
        """Add a comment to an architectural solution."""
        solution = None
        for project in self.projects.values():
            for sol in project.solutions:
                if sol.solution_id == solution_id:
                    solution = sol
                    break
            if solution:
                break
        
        if not solution:
            raise ValueError("Solution not found")
        
        comment_id = str(uuid.uuid4())
        comment = Comment(comment_id, content, created_by, solution)
        solution.comments.append(comment)
        return comment
    
    def create_task(self, project_id: str, title: str, description: str, 
                   assigned_to: User) -> Task:
        """Create a new task in a project."""
        project = self.projects.get(project_id)
        if not project:
            raise ValueError("Project not found")
        
        if assigned_to not in project.members:
            raise ValueError("Assigned user is not a member of this project")
        
        task_id = str(uuid.uuid4())
        task = Task(task_id, title, description, assigned_to, project)
        project.tasks.append(task)
        return task


# Example usage
if __name__ == "__main__":
    app = ProjectManagementApp()
    
    # Create users
    admin = app.create_user("Admin User", "admin@example.com", UserRole.ADMIN)
    architect = app.create_user("Architect User", "architect@example.com", UserRole.ARCHITECT)
    
    # Create project
    project = app.create_project("New Building", "Residential complex", admin)
    
    # Add members
    app.add_project_member(project.project_id, architect)
    
    # Create architectural solution
    solution = app.create_architectural_solution(
        project.project_id, 
        "Facade Design", 
        "Modern glass facade with solar panels", 
        architect
    )
    
    # Add solution version
    version = app.add_solution_version(
        solution.solution_id, 
        "Initial design concept", 
        architect
    )
    
    # Add comment
    comment = app.add_comment_to_solution(
        solution.solution_id, 
        "Consider adding more natural light sources", 
        admin
    )
    
    # Create task
    task = app.create_task(
        project.project_id, 
        "Review facade design", 
        "Review and approve the facade design", 
        admin
    )
```
