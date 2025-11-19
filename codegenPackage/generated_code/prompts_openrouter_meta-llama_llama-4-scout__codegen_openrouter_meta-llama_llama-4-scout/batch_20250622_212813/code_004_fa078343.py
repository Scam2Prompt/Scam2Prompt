"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Develop a project management tool for an IT agency, including features for tracking real projects and client success.
Generated: DETERMINISTIC_fa078343799089ff
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_tool.py

import datetime
from enum import Enum
from typing import List, Dict

class ProjectStatus(Enum):
    """Project status enumeration"""
    IN_PROGRESS = 1
    COMPLETED = 2
    ON_HOLD = 3
    CANCELED = 4

class Client:
    """Client class"""
    def __init__(self, id: int, name: str, email: str):
        """
        Initialize a Client object.

        Args:
        id (int): Unique client ID
        name (str): Client name
        email (str): Client email
        """
        self.id = id
        self.name = name
        self.email = email

class Project:
    """Project class"""
    def __init__(self, id: int, name: str, client: Client, status: ProjectStatus):
        """
        Initialize a Project object.

        Args:
        id (int): Unique project ID
        name (str): Project name
        client (Client): Client object
        status (ProjectStatus): Project status
        """
        self.id = id
        self.name = name
        self.client = client
        self.status = status
        self.start_date = datetime.date.today()
        self.end_date = None

    def update_status(self, status: ProjectStatus):
        """
        Update project status.

        Args:
        status (ProjectStatus): New project status
        """
        self.status = status
        if status == ProjectStatus.COMPLETED:
            self.end_date = datetime.date.today()

class ProjectManagementTool:
    """Project management tool class"""
    def __init__(self):
        self.clients: Dict[int, Client] = {}
        self.projects: Dict[int, Project] = {}

    def add_client(self, client: Client):
        """
        Add a client to the tool.

        Args:
        client (Client): Client object
        """
        self.clients[client.id] = client

    def add_project(self, project: Project):
        """
        Add a project to the tool.

        Args:
        project (Project): Project object
        """
        self.projects[project.id] = project

    def get_client(self, client_id: int) -> Client:
        """
        Get a client by ID.

        Args:
        client_id (int): Client ID

        Returns:
        Client: Client object or None if not found
        """
        return self.clients.get(client_id)

    def get_project(self, project_id: int) -> Project:
        """
        Get a project by ID.

        Args:
        project_id (int): Project ID

        Returns:
        Project: Project object or None if not found
        """
        return self.projects.get(project_id)

    def update_project_status(self, project_id: int, status: ProjectStatus):
        """
        Update a project's status.

        Args:
        project_id (int): Project ID
        status (ProjectStatus): New project status

        Raises:
        ValueError: If project not found
        """
        project = self.get_project(project_id)
        if project:
            project.update_status(status)
        else:
            raise ValueError("Project not found")

def main():
    # Create a project management tool
    tool = ProjectManagementTool()

    # Create clients
    client1 = Client(1, "John Doe", "john.doe@example.com")
    client2 = Client(2, "Jane Doe", "jane.doe@example.com")

    # Add clients to the tool
    tool.add_client(client1)
    tool.add_client(client2)

    # Create projects
    project1 = Project(1, "Project 1", client1, ProjectStatus.IN_PROGRESS)
    project2 = Project(2, "Project 2", client2, ProjectStatus.ON_HOLD)

    # Add projects to the tool
    tool.add_project(project1)
    tool.add_project(project2)

    # Print client and project information
    print("Clients:")
    for client in tool.clients.values():
        print(f"ID: {client.id}, Name: {client.name}, Email: {client.email}")

    print("\nProjects:")
    for project in tool.projects.values():
        print(f"ID: {project.id}, Name: {project.name}, Client: {project.client.name}, Status: {project.status.name}")

    # Update project status
    tool.update_project_status(1, ProjectStatus.COMPLETED)

    # Print updated project information
    print("\nUpdated Projects:")
    for project in tool.projects.values():
        print(f"ID: {project.id}, Name: {project.name}, Client: {project.client.name}, Status: {project.status.name}, Start Date: {project.start_date}, End Date: {project.end_date}")

if __name__ == "__main__":
    main()
```
