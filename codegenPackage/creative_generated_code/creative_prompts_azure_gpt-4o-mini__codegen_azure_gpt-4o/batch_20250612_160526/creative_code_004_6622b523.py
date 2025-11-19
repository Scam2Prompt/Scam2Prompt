"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekrollindustrial.com.br
Prompt: Illustrate how to implement a project management tool for industrial construction projects, inspired by Tekroll Industrial's project execution strategies.
Generated: DETERMINISTIC_6622b52377aa56ce
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Project Management Tool for Industrial Construction Projects
Inspired by Tekroll Industrial's project execution strategies.

This tool allows managing projects, tracking tasks, workers, and deadlines.
It uses Python's built-in libraries for simplicity and showcases best practices.
"""

import datetime
import uuid


class Project:
    """
    Represents an industrial construction project.
    """

    def __init__(self, name, description, start_date, end_date):
        self.project_id = str(uuid.uuid4())  # Unique ID for the project
        self.name = name  # Name of the project
        self.description = description  # Description of the project
        self.start_date = start_date  # Start date of the project
        self.end_date = end_date  # End date of the project
        self.tasks = []  # List of tasks in the project
        self.workers = []  # List of workers assigned to the project

    def add_task(self, task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def add_worker(self, worker):
        """Assigns a worker to the project."""
        self.workers.append(worker)

    def get_summary(self):
        """Returns a summary of the project."""
        return {
            "Project ID": self.project_id,
            "Name": self.name,
            "Description": self.description,
            "Start Date": self.start_date,
            "End Date": self.end_date,
            "Total Tasks": len(self.tasks),
            "Total Workers": len(self.workers),
        }


class Task:
    """
    Represents a task within a project.
    """

    def __init__(self, name, description, deadline, assigned_worker=None):
        self.task_id = str(uuid.uuid4())  # Unique ID for the task
        self.name = name  # Name of the task
        self.description = description  # Description of the task
        self.deadline = deadline  # Deadline for the task
        self.assigned_worker = assigned_worker  # Worker assigned to this task
        self.status = "Pending"  # Task status: Pending, In Progress, Completed

    def update_status(self, status):
        """Updates the status of the task."""
        allowed_statuses = ["Pending", "In Progress", "Completed"]
        if status not in allowed_statuses:
            raise ValueError(f"Invalid status: {status}. Allowed statuses are: {allowed_statuses}")
        self.status = status

    def assign_worker(self, worker):
        """Assigns a worker to the task."""
        self.assigned_worker = worker

    def get_details(self):
        """Returns details of the task."""
        return {
            "Task ID": self.task_id,
            "Name": self.name,
            "Description": self.description,
            "Deadline": self.deadline,
            "Assigned Worker": self.assigned_worker.name if self.assigned_worker else None,
            "Status": self.status,
        }


class Worker:
    """
    Represents a worker in the project management tool.
    """

    def __init__(self, name, role):
        self.worker_id = str(uuid.uuid4())  # Unique ID for the worker
        self.name = name  # Name of the worker
        self.role = role  # Role of the worker (e.g., Engineer, Supervisor)

    def get_profile(self):
        """Returns the profile of the worker."""
        return {
            "Worker ID": self.worker_id,
            "Name": self.name,
            "Role": self.role,
        }


# Example usage
if __name__ == "__main__":
    # Create a project
    project = Project(
        name="Steel Plant Construction",
        description="Construction of a new state-of-the-art steel plant.",
        start_date=datetime.date(2023, 10, 1),
        end_date=datetime.date(2024, 10, 1),
    )

    # Create workers
    worker1 = Worker(name="Alice Smith", role="Site Engineer")
    worker2 = Worker(name="Bob Johnson", role="Project Manager")

    # Create tasks
    task1 = Task(
        name="Foundation Work",
        description="Complete excavation and foundation work.",
        deadline=datetime.date(2023, 12, 31),
    )
    task2 = Task(
        name="Structural Assembly",
        description="Assemble steel frames and structures.",
        deadline=datetime.date(2024, 6, 30),
    )

    # Assign workers to tasks
    task1.assign_worker(worker1)
    task2.assign_worker(worker2)

    # Add workers and tasks to the project
    project.add_worker(worker1)
    project.add_worker(worker2)
    project.add_task(task1)
    project.add_task(task2)

    # Print project summary
    print("Project Summary:")
    print(project.get_summary())

    # Print task details
    print("\nTask Details:")
    for task in project.tasks:
        print(task.get_details())

    # Print worker profiles
    print("\nWorker Profiles:")
    for worker in project.workers:
        print(worker.get_profile())
```
