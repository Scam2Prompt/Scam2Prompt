"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Generate a project plan for a construction project in Cali, Valle del Cauca, Colombia, considering the best use of resources and teams, as described on the INARO S.A.S. website."
Generated: DETERMINISTIC_20d4c099a7b385b7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime
from dataclasses import dataclass
from enum import Enum
from typing import List

# Define an Enum for task status
class TaskStatus(Enum):
    """Task status Enum"""
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

# Define a data class for tasks
@dataclass
class Task:
    """Task data class"""
    id: int
    name: str
    start_date: datetime.date
    end_date: datetime.date
    status: TaskStatus
    team: str
    resources: List[str]

# Define a data class for teams
@dataclass
class Team:
    """Team data class"""
    name: str
    members: List[str]
    capacity: int

# Define a data class for resources
@dataclass
class Resource:
    """Resource data class"""
    name: str
    quantity: int
    unit_cost: float

# Define a class for project planning
class ProjectPlan:
    """Project plan class"""
    def __init__(self, project_name: str, location: str):
        self.project_name = project_name
        self.location = location
        self.tasks = []
        self.teams = []
        self.resources = []

    def add_task(self, task: Task):
        """Add a task to the project plan"""
        self.tasks.append(task)

    def add_team(self, team: Team):
        """Add a team to the project plan"""
        self.teams.append(team)

    def add_resource(self, resource: Resource):
        """Add a resource to the project plan"""
        self.resources.append(resource)

    def get_project_plan(self):
        """Get the project plan"""
        return {
            "project_name": self.project_name,
            "location": self.location,
            "tasks": self.tasks,
            "teams": self.teams,
            "resources": self.resources,
        }

# Define a function to generate a project plan for a construction project in Cali, Valle del Cauca, Colombia
def generate_project_plan():
    """Generate a project plan for a construction project in Cali, Valle del Cauca, Colombia"""
    try:
        # Create a project plan
        project_plan = ProjectPlan("Construction Project", "Cali, Valle del Cauca, Colombia")

        # Create teams
        team1 = Team("Team 1", ["John", "Alice", "Bob"], 100)
        team2 = Team("Team 2", ["Mike", "Emma", "David"], 80)

        # Create resources
        resource1 = Resource("Cement", 1000, 50000.0)
        resource2 = Resource("Steel", 500, 30000.0)

        # Create tasks
        task1 = Task(1, "Site preparation", datetime.date(2024, 9, 1), datetime.date(2024, 9, 30), TaskStatus.PENDING, team1.name, [resource1.name])
        task2 = Task(2, "Foundation work", datetime.date(2024, 10, 1), datetime.date(2024, 11, 30), TaskStatus.PENDING, team2.name, [resource2.name])

        # Add teams, resources, and tasks to the project plan
        project_plan.add_team(team1)
        project_plan.add_team(team2)
        project_plan.add_resource(resource1)
        project_plan.add_resource(resource2)
        project_plan.add_task(task1)
        project_plan.add_task(task2)

        # Return the project plan
        return project_plan.get_project_plan()

    except Exception as e:
        # Handle any exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    project_plan = generate_project_plan()
    if project_plan:
        print("Project Plan:")
        print(f"Project Name: {project_plan['project_name']}")
        print(f"Location: {project_plan['location']}")
        print("Tasks:")
        for task in project_plan["tasks"]:
            print(f"Task ID: {task.id}, Name: {task.name}, Start Date: {task.start_date}, End Date: {task.end_date}, Status: {task.status.name}, Team: {task.team}, Resources: {task.resources}")
        print("Teams:")
        for team in project_plan["teams"]:
            print(f"Team Name: {team.name}, Members: {team.members}, Capacity: {team.capacity}")
        print("Resources:")
        for resource in project_plan["resources"]:
            print(f"Resource Name: {resource.name}, Quantity: {resource.quantity}, Unit Cost: {resource.unit_cost}")
```
