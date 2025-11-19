"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Develop a plan for implementing a project management system for a civil engineering company like SOM Civil Engineers, including features like task assignment, progress tracking, and team collaboration."
Generated: DETERMINISTIC_545925434b424a13
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

import datetime

class Task:
    """
    Represents a task in the project management system.
    """
    def __init__(self, title, description, assigned_to, due_date):
        self.title = title
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = "Pending"  # Default status
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status):
        """
        Updates the status of the task.
        """
        if new_status not in ["Pending", "In Progress", "Completed"]:
            raise ValueError("Invalid status. Choose from 'Pending', 'In Progress', or 'Completed'.")
        self.status = new_status
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"Task: {self.title}, Assigned to: {self.assigned_to}, Status: {self.status}, Due: {self.due_date}"


class Project:
    """
    Represents a project in the project management system.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []  # List to store tasks
        self.created_at = datetime.datetime.now()

    def add_task(self, task):
        """
        Adds a task to the project.
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task object.")
        self.tasks.append(task)

    def get_progress(self):
        """
        Calculates and returns the progress of the project based on task statuses.
        """
        if not self.tasks:
            return "No tasks available."
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.status == "Completed")
        progress_percentage = (completed_tasks / total_tasks) * 100
        return f"Project Progress: {progress_percentage:.2f}%"

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        return f"Project: {self.name}, Description: {self.description}, Tasks: {len(self.tasks)}"


class TeamMember:
    """
    Represents a team member in the project management system.
    """
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        """
        Returns a string representation of the team member.
        """
        return f"Team Member: {self.name}, Role: {self.role}"


class ProjectManagementSystem:
    """
    Main class for the project management system.
    """
    def __init__(self):
        self.projects = []  # List to store projects
        self.team_members = []  # List to store team members

    def add_project(self, project):
        """
        Adds a project to the system.
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project object.")
        self.projects.append(project)

    def add_team_member(self, team_member):
        """
        Adds a team member to the system.
        """
        if not isinstance(team_member, TeamMember):
            raise TypeError("Expected a TeamMember object.")
        self.team_members.append(team_member)

    def assign_task(self, project_name, task_title, team_member_name):
        """
        Assigns a task to a team member within a specific project.
        """
        project = next((p for p in self.projects if p.name == project_name), None)
        if not project:
            raise ValueError(f"Project '{project_name}' not found.")
        
        task = next((t for t in project.tasks if t.title == task_title), None)
        if not task:
            raise ValueError(f"Task '{task_title}' not found in project '{project_name}'.")
        
        team_member = next((tm for tm in self.team_members if tm.name == team_member_name), None)
        if not team_member:
            raise ValueError(f"Team member '{team_member_name}' not found.")
        
        task.assigned_to = team_member.name

    def __str__(self):
        """
        Returns a string representation of the system.
        """
        return f"Project Management System: {len(self.projects)} Projects, {len(self.team_members)} Team Members"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the system
        system = ProjectManagementSystem()

        # Create team members
        member1 = TeamMember("Alice", "Engineer")
        member2 = TeamMember("Bob", "Project Manager")
        system.add_team_member(member1)
        system.add_team_member(member2)

        # Create a project
        project = Project("Bridge Construction", "Build a new bridge over the river.")
        system.add_project(project)

        # Create tasks
        task1 = Task("Foundation Work", "Complete the foundation of the bridge.", None, "2023-12-01")
        task2 = Task("Structural Design", "Design the structure of the bridge.", None, "2023-11-15")
        project.add_task(task1)
        project.add_task(task2)

        # Assign tasks
        system.assign_task("Bridge Construction", "Foundation Work", "Alice")
        system.assign_task("Bridge Construction", "Structural Design", "Bob")

        # Update task status
        task1.update_status("In Progress")
        task2.update_status("Completed")

        # Display project progress
        print(project.get_progress())

        # Display system details
        print(system)

    except Exception as e:
        print(f"Error: {e}")
```
