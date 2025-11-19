"""
Generated Code Metadata:
========================
Original URL: https://sitechgt.com
Prompt: "Write a code snippet to implement a project management tool inspired by Études Architectural Solutions' approach."
Generated: DETERMINISTIC_d65e464ac55676c1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Tool inspired by Études Architectural Solutions' approach.

This tool allows users to manage projects, tasks, and team members. It includes functionality
to create projects, add tasks, assign team members, and track task completion.

Language: Python
"""

import uuid
from datetime import datetime


class ProjectManagementTool:
    def __init__(self):
        # Initialize the tool with empty lists for projects and team members
        self.projects = {}
        self.team_members = {}

    # ------------------ Project Management ------------------
    def create_project(self, name, description):
        """
        Create a new project.
        :param name: Name of the project
        :param description: Description of the project
        :return: Project ID
        """
        project_id = str(uuid.uuid4())
        self.projects[project_id] = {
            "name": name,
            "description": description,
            "tasks": [],
            "created_at": datetime.now(),
        }
        return project_id

    def list_projects(self):
        """
        List all projects.
        :return: List of projects
        """
        return [
            {"id": project_id, **details}
            for project_id, details in self.projects.items()
        ]

    # ------------------ Task Management ------------------
    def add_task(self, project_id, title, description, due_date):
        """
        Add a task to a project.
        :param project_id: ID of the project
        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date of the task (YYYY-MM-DD)
        :return: Task ID
        """
        if project_id not in self.projects:
            raise ValueError("Invalid project ID")

        task_id = str(uuid.uuid4())
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False,
            "assigned_to": None,
        }
        self.projects[project_id]["tasks"].append(task)
        return task_id

    def mark_task_completed(self, project_id, task_id):
        """
        Mark a task as completed.
        :param project_id: ID of the project
        :param task_id: ID of the task
        """
        if project_id not in self.projects:
            raise ValueError("Invalid project ID")

        for task in self.projects[project_id]["tasks"]:
            if task["id"] == task_id:
                task["completed"] = True
                return
        raise ValueError("Invalid task ID")

    # ------------------ Team Management ------------------
    def add_team_member(self, name, email):
        """
        Add a team member.
        :param name: Name of the team member
        :param email: Email of the team member
        :return: Team Member ID
        """
        member_id = str(uuid.uuid4())
        self.team_members[member_id] = {"name": name, "email": email}
        return member_id

    def assign_task(self, project_id, task_id, member_id):
        """
        Assign a task to a team member.
        :param project_id: ID of the project
        :param task_id: ID of the task
        :param member_id: ID of the team member
        """
        if project_id not in self.projects:
            raise ValueError("Invalid project ID")
        if member_id not in self.team_members:
            raise ValueError("Invalid team member ID")

        for task in self.projects[project_id]["tasks"]:
            if task["id"] == task_id:
                task["assigned_to"] = member_id
                return
        raise ValueError("Invalid task ID")


# ------------------ Example Usage ------------------
if __name__ == "__main__":
    # Initialize the tool
    tool = ProjectManagementTool()

    # Create a project
    project_id = tool.create_project(
        name="Website Redesign",
        description="Redesign the company website to improve user experience.",
    )

    # Add a team member
    member_id = tool.add_team_member(name="Alice Johnson", email="alice@example.com")

    # Add a task to the project
    task_id = tool.add_task(
        project_id=project_id,
        title="Create Wireframes",
        description="Design wireframes for the new website layout.",
        due_date="2023-12-01",
    )

    # Assign the task to the team member
    tool.assign_task(project_id=project_id, task_id=task_id, member_id=member_id)

    # Mark the task as completed
    tool.mark_task_completed(project_id=project_id, task_id=task_id)

    # List all projects
    print(tool.list_projects())
```
