"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Describe a software solution for construction project management that could be used by a company like INARO S.A.S., including features for planning, team management, and client relations."
Generated: DETERMINISTIC_9985b627572992c3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management.py

from datetime import datetime
from typing import List, Dict

class TeamMember:
    """Represents a team member with their role and contact information."""

    def __init__(self, name: str, role: str, email: str, phone: str):
        """
        Initializes a TeamMember.

        Args:
            name (str): The team member's name.
            role (str): The team member's role.
            email (str): The team member's email.
            phone (str): The team member's phone number.
        """
        self.name = name
        self.role = role
        self.email = email
        self.phone = phone

class Task:
    """Represents a task with its description, deadline, and assigned team members."""

    def __init__(self, description: str, deadline: datetime, team_members: List[TeamMember]):
        """
        Initializes a Task.

        Args:
            description (str): The task's description.
            deadline (datetime): The task's deadline.
            team_members (List[TeamMember]): The team members assigned to the task.
        """
        self.description = description
        self.deadline = deadline
        self.team_members = team_members

class Client:
    """Represents a client with their contact information and project details."""

    def __init__(self, name: str, email: str, phone: str, project_name: str):
        """
        Initializes a Client.

        Args:
            name (str): The client's name.
            email (str): The client's email.
            phone (str): The client's phone number.
            project_name (str): The client's project name.
        """
        self.name = name
        self.email = email
        self.phone = phone
        self.project_name = project_name

class ConstructionProject:
    """Represents a construction project with its tasks, team members, and clients."""

    def __init__(self, name: str):
        """
        Initializes a ConstructionProject.

        Args:
            name (str): The project's name.
        """
        self.name = name
        self.tasks: List[Task] = []
        self.team_members: List[TeamMember] = []
        self.clients: List[Client] = []

    def add_task(self, task: Task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def add_team_member(self, team_member: TeamMember):
        """Adds a team member to the project."""
        self.team_members.append(team_member)

    def add_client(self, client: Client):
        """Adds a client to the project."""
        self.clients.append(client)

    def get_project_details(self) -> Dict:
        """Returns the project's details."""
        project_details = {
            "name": self.name,
            "tasks": [task.description for task in self.tasks],
            "team_members": [team_member.name for team_member in self.team_members],
            "clients": [client.name for client in self.clients],
        }
        return project_details

def main():
    try:
        # Create team members
        team_member1 = TeamMember("John Doe", "Project Manager", "john.doe@example.com", "1234567890")
        team_member2 = TeamMember("Jane Doe", "Engineer", "jane.doe@example.com", "0987654321")

        # Create tasks
        task1 = Task("Design project layout", datetime(2024, 9, 20), [team_member1, team_member2])
        task2 = Task("Conduct site analysis", datetime(2024, 9, 25), [team_member1])

        # Create clients
        client1 = Client("Client1", "client1@example.com", "1111111111", "Project1")
        client2 = Client("Client2", "client2@example.com", "2222222222", "Project2")

        # Create construction project
        project = ConstructionProject("INARO S.A.S. Project")
        project.add_task(task1)
        project.add_task(task2)
        project.add_team_member(team_member1)
        project.add_team_member(team_member2)
        project.add_client(client1)
        project.add_client(client2)

        # Get project details
        project_details = project.get_project_details()
        print(project_details)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
