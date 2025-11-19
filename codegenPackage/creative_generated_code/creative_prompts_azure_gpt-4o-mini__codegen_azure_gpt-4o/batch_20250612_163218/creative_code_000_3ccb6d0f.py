"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Generate a code snippet for a project management tool that tracks construction timelines and responsibilities for a construction company like Construye RK.
Generated: DETERMINISTIC_3ccb6d0f59cad8a9
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# project_management_tool.py
# A simple project management tool for tracking construction timelines and responsibilities.

import datetime


class Task:
    """
    Represents a task in a construction project.
    """

    def __init__(self, name, assigned_to, start_date, end_date):
        """
        Initialize a Task instance.
        :param name: Name of the task
        :param assigned_to: Person responsible for the task
        :param start_date: Task start date (datetime.date object)
        :param end_date: Task end date (datetime.date object)
        """
        self.name = name
        self.assigned_to = assigned_to
        self.start_date = start_date
        self.end_date = end_date
        self.status = "Pending"  # Status can be "Pending", "In Progress", or "Completed"

    def update_status(self, status):
        """
        Update the task's status.
        :param status: New status of the task
        """
        if status not in ["Pending", "In Progress", "Completed"]:
            raise ValueError("Invalid status. Allowed values are 'Pending', 'In Progress', or 'Completed'.")
        self.status = status

    def __str__(self):
        """
        Return a string representation of the task.
        """
        return f"Task: {self.name}, Assigned To: {self.assigned_to}, Start Date: {self.start_date}, End Date: {self.end_date}, Status: {self.status}"


class Project:
    """
    Represents a construction project.
    """

    def __init__(self, name):
        """
        Initialize a Project instance.
        :param name: Name of the project
        """
        self.name = name
        self.tasks = []  # List of tasks in the project

    def add_task(self, task):
        """
        Add a task to the project.
        :param task: Task instance to add
        """
        if not isinstance(task, Task):
            raise TypeError("task must be an instance of Task.")
        self.tasks.append(task)

    def get_pending_tasks(self):
        """
        Retrieve all pending tasks in the project.
        :return: List of tasks with status "Pending"
        """
        return [task for task in self.tasks if task.status == "Pending"]

    def __str__(self):
        """
        Return a string representation of the project.
        """
        task_details = "\n".join(str(task) for task in self.tasks)
        return f"Project: {self.name}\nTasks:\n{task_details}"


# Example usage:
if __name__ == "__main__":
    try:
        # Create a project
        project = Project("Construye RK Headquarters")

        # Add tasks to the project
        task1 = Task("Foundation Work", "John Doe", datetime.date(2023, 10, 1), datetime.date(2023, 10, 15))
        task2 = Task("Roof Installation", "Jane Smith", datetime.date(2023, 10, 16), datetime.date(2023, 10, 25))
        project.add_task(task1)
        project.add_task(task2)

        # Update task status
        task1.update_status("In Progress")

        # Print project details
        print(project)

        # Retrieve and display pending tasks
        print("\nPending Tasks:")
        pending_tasks = project.get_pending_tasks()
        for task in pending_tasks:
            print(task)

    except Exception as e:
        print(f"An error occurred: {e}")
```
