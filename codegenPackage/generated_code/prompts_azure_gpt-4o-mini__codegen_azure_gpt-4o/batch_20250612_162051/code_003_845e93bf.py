"""
Generated Code Metadata:
========================
Original URL: https://vivekenterprises.co.in
Prompt: Generate a code example for a project management tool that tracks the progress of interior turnkey contracting tasks, including design and execution phases mentioned by Vivek Enterprises.
Generated: DETERMINISTIC_845e93bfe62b1c55
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime


class Task:
    """
    Represents a single task in the project management tool.
    """

    def __init__(self, name, phase, due_date):
        """
        Initialize a task with a name, phase, and due date.

        :param name: Name of the task
        :param phase: Phase of the task (e.g., 'Design', 'Execution')
        :param due_date: Due date of the task (datetime.date)
        """
        self.name = name
        self.phase = phase
        self.due_date = due_date
        self.completed = False
        self.completed_date = None

    def mark_completed(self):
        """
        Mark the task as completed and set the completion date.
        """
        self.completed = True
        self.completed_date = datetime.date.today()

    def __str__(self):
        """
        String representation of the task.
        """
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.name}, Phase: {self.phase}, Due: {self.due_date}, Status: {status}"


class Project:
    """
    Represents a project with multiple tasks.
    """

    def __init__(self, name, client_name):
        """
        Initialize a project with a name and client name.

        :param name: Name of the project
        :param client_name: Name of the client
        """
        self.name = name
        self.client_name = client_name
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: Task object to be added
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.append(task)

    def get_pending_tasks(self):
        """
        Get a list of all pending tasks.

        :return: List of pending Task objects
        """
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        """
        Get a list of all completed tasks.

        :return: List of completed Task objects
        """
        return [task for task in self.tasks if task.completed]

    def __str__(self):
        """
        String representation of the project.
        """
        return f"Project: {self.name}, Client: {self.client_name}, Total Tasks: {len(self.tasks)}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a project
        project = Project(name="Interior Turnkey Contracting", client_name="Vivek Enterprises")

        # Add tasks to the project
        task1 = Task(name="Create Floor Plan", phase="Design", due_date=datetime.date(2023, 11, 15))
        task2 = Task(name="Install Electrical Wiring", phase="Execution", due_date=datetime.date(2023, 12, 1))
        task3 = Task(name="Paint Walls", phase="Execution", due_date=datetime.date(2023, 12, 10))

        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)

        # Mark a task as completed
        task1.mark_completed()

        # Display project details
        print(project)
        print("\nPending Tasks:")
        for task in project.get_pending_tasks():
            print(task)

        print("\nCompleted Tasks:")
        for task in project.get_completed_tasks():
            print(task)

    except Exception as e:
        print(f"An error occurred: {e}")
```
