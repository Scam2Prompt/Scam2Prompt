"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Design a system to streamline project management and focus on core tasks for a construction business while using a virtual receptionist service for call handling and appointment scheduling.
Generated: DETERMINISTIC_16d705e86593fd24
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_system.py

from datetime import datetime
from typing import Dict, List

class Project:
    def __init__(self, id: int, name: str, description: str, tasks: List[str]):
        """
        Initialize a Project object.

        Args:
        id (int): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        tasks (List[str]): List of tasks for the project.
        """
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks
        self.status = "Not Started"

    def update_status(self, status: str):
        """
        Update the project status.

        Args:
        status (str): New project status.
        """
        self.status = status

class Task:
    def __init__(self, id: int, project_id: int, name: str, description: str, due_date: str):
        """
        Initialize a Task object.

        Args:
        id (int): Unique task ID.
        project_id (int): Foreign key referencing the Project ID.
        name (str): Task name.
        description (str): Task description.
        due_date (str): Task due date in YYYY-MM-DD format.
        """
        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = "Not Started"

    def update_status(self, status: str):
        """
        Update the task status.

        Args:
        status (str): New task status.
        """
        self.status = status

class VirtualReceptionist:
    def __init__(self):
        """
        Initialize a VirtualReceptionist object.
        """
        self.appointments = {}

    def schedule_appointment(self, date: str, time: str, description: str):
        """
        Schedule an appointment.

        Args:
        date (str): Appointment date in YYYY-MM-DD format.
        time (str): Appointment time in HH:MM format.
        description (str): Appointment description.
        """
        appointment_date = datetime.strptime(date, "%Y-%m-%d")
        appointment_time = datetime.strptime(time, "%H:%M").time()
        self.appointments[appointment_date] = (appointment_time, description)

    def cancel_appointment(self, date: str):
        """
        Cancel an appointment.

        Args:
        date (str): Appointment date in YYYY-MM-DD format.
        """
        appointment_date = datetime.strptime(date, "%Y-%m-%d")
        if appointment_date in self.appointments:
            del self.appointments[appointment_date]
        else:
            raise ValueError("Appointment not found")

class ConstructionBusiness:
    def __init__(self):
        """
        Initialize a ConstructionBusiness object.
        """
        self.projects: Dict[int, Project] = {}
        self.tasks: Dict[int, Task] = {}
        self.virtual_receptionist = VirtualReceptionist()

    def create_project(self, id: int, name: str, description: str, tasks: List[str]):
        """
        Create a new project.

        Args:
        id (int): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        tasks (List[str]): List of tasks for the project.
        """
        project = Project(id, name, description, tasks)
        self.projects[id] = project

    def create_task(self, id: int, project_id: int, name: str, description: str, due_date: str):
        """
        Create a new task.

        Args:
        id (int): Unique task ID.
        project_id (int): Foreign key referencing the Project ID.
        name (str): Task name.
        description (str): Task description.
        due_date (str): Task due date in YYYY-MM-DD format.
        """
        task = Task(id, project_id, name, description, due_date)
        self.tasks[id] = task

    def get_project(self, id: int) -> Project:
        """
        Get a project by ID.

        Args:
        id (int): Unique project ID.

        Returns:
        Project: Project object.

        Raises:
        ValueError: If the project is not found.
        """
        if id in self.projects:
            return self.projects[id]
        else:
            raise ValueError("Project not found")

    def get_task(self, id: int) -> Task:
        """
        Get a task by ID.

        Args:
        id (int): Unique task ID.

        Returns:
        Task: Task object.

        Raises:
        ValueError: If the task is not found.
        """
        if id in self.tasks:
            return self.tasks[id]
        else:
            raise ValueError("Task not found")

def main():
    business = ConstructionBusiness()

    # Create projects
    business.create_project(1, "Project 1", "Description 1", ["Task 1", "Task 2"])
    business.create_project(2, "Project 2", "Description 2", ["Task 3", "Task 4"])

    # Create tasks
    business.create_task(1, 1, "Task 1", "Description 1", "2024-09-20")
    business.create_task(2, 1, "Task 2", "Description 2", "2024-09-25")
    business.create_task(3, 2, "Task 3", "Description 3", "2024-09-15")
    business.create_task(4, 2, "Task 4", "Description 4", "2024-09-30")

    # Schedule appointments
    business.virtual_receptionist.schedule_appointment("2024-09-20", "10:00", "Meeting with client")
    business.virtual_receptionist.schedule_appointment("2024-09-25", "14:00", "Site visit")

    # Get project and task
    project = business.get_project(1)
    task = business.get_task(1)

    # Print project and task details
    print(f"Project {project.id}: {project.name}")
    print(f"Description: {project.description}")
    print(f"Tasks: {project.tasks}")
    print(f"Status: {project.status}")

    print(f"\nTask {task.id}: {task.name}")
    print(f"Project ID: {task.project_id}")
    print(f"Description: {task.description}")
    print(f"Due Date: {task.due_date.strftime('%Y-%m-%d')}")
    print(f"Status: {task.status}")

if __name__ == "__main__":
    main()
```
