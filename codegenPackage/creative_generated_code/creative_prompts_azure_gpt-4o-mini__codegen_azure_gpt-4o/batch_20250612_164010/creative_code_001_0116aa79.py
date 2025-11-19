"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Generate a code snippet for a project management tool that tracks the progress of civil maintenance tasks, inspired by the project management practices at SOM Civil.
Generated: DETERMINISTIC_0116aa7966cc1132
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Task:
    """
    Represents a single maintenance task.
    Attributes:
        name (str): The name of the task.
        description (str): A detailed description of the task.
        assigned_to (str): The person responsible for the task.
        deadline (datetime.date): The deadline for task completion.
        status (str): Current status of the task ('Pending', 'In Progress', 'Completed').
    """
    def __init__(self, name, description, assigned_to, deadline):
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.status = 'Pending'  # Initial status is 'Pending'

    def update_status(self, new_status):
        """
        Updates the status of the task.
        Args:
            new_status (str): The new status ('Pending', 'In Progress', 'Completed').
        Raises:
            ValueError: If the new_status is not one of the allowed values.
        """
        valid_statuses = ['Pending', 'In Progress', 'Completed']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")
        self.status = new_status

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"Task: {self.name}\nDescription: {self.description}\nAssigned To: {self.assigned_to}\nDeadline: {self.deadline}\nStatus: {self.status}"


class Project:
    """
    Represents a project containing multiple tasks.
    Attributes:
        name (str): The name of the project.
        tasks (list): A list of tasks associated with the project.
    """
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the project.
        Args:
            task (Task): The task to be added.
        """
        if not isinstance(task, Task):
            raise TypeError("Expected a Task object.")
        self.tasks.append(task)

    def track_progress(self):
        """
        Tracks the progress of tasks in the project.
        Returns:
            dict: A summary of task statuses.
        """
        status_summary = {'Pending': 0, 'In Progress': 0, 'Completed': 0}
        for task in self.tasks:
            status_summary[task.status] += 1
        return status_summary

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        task_details = "\n\n".join(str(task) for task in self.tasks)
        return f"Project: {self.name}\n\nTasks:\n{task_details}"


# Example Usage
if __name__ == "__main__":
    try:
        # Create a project
        project = Project("Civil Maintenance - Downtown Road Repairs")

        # Create tasks
        task1 = Task("Repair Potholes", "Fix all potholes on Main Street.", "John Doe", datetime.date(2023, 10, 15))
        task2 = Task("Inspect Bridges", "Conduct safety inspections for all bridges.", "Jane Smith", datetime.date(2023, 10, 20))

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)

        # Update task statuses
        task1.update_status("In Progress")
        task2.update_status("Completed")

        # Track progress
        progress = project.track_progress()
        print(project)
        print("\nProgress Summary:", progress)
    except Exception as e:
        print(f"Error: {e}")
```
