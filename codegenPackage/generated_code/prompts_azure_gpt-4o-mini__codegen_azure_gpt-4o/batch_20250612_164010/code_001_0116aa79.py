"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a code snippet for a project management tool that tracks the progress of civil maintenance tasks, inspired by the project management practices at SOM Civil.
Generated: DETERMINISTIC_0116aa7966cc1132
Batch ID: 20250612_164010
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
    Represents a single maintenance task in the project management tool.
    """
    def __init__(self, task_id, name, description, assigned_to, due_date):
        """
        Initialize a Task object.

        :param task_id: Unique identifier for the task
        :param name: Name of the task
        :param description: Detailed description of the task
        :param assigned_to: Name of the person assigned to the task
        :param due_date: Due date for the task (datetime object)
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.status = "Pending"  # Default status is "Pending"
        self.created_at = datetime.datetime.now()

    def update_status(self, new_status):
        """
        Update the status of the task.

        :param new_status: New status for the task (e.g., "In Progress", "Completed")
        """
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the task.
        """
        return (f"Task ID: {self.task_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Assigned To: {self.assigned_to}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


class ProjectManagementTool:
    """
    A tool to manage and track civil maintenance tasks.
    """
    def __init__(self):
        """
        Initialize the ProjectManagementTool with an empty list of tasks.
        """
        self.tasks = []

    def add_task(self, task):
        """
        Add a new task to the project management tool.

        :param task: Task object to be added
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.append(task)

    def list_tasks(self):
        """
        List all tasks in the project management tool.
        """
        if not self.tasks:
            print("No tasks available.")
        for task in self.tasks:
            print(task)
            print("-" * 40)

    def find_task_by_id(self, task_id):
        """
        Find a task by its unique ID.

        :param task_id: Unique identifier of the task
        :return: Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def update_task_status(self, task_id, new_status):
        """
        Update the status of a task by its ID.

        :param task_id: Unique identifier of the task
        :param new_status: New status for the task
        """
        task = self.find_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        try:
            task.update_status(new_status)
            print(f"Task ID {task_id} status updated to '{new_status}'.")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the project management tool
    tool = ProjectManagementTool()

    # Create some tasks
    task1 = Task(task_id=1, name="Inspect Bridge", description="Inspect the structural integrity of the bridge.",
                 assigned_to="John Doe", due_date=datetime.datetime(2023, 11, 15))
    task2 = Task(task_id=2, name="Repair Road", description="Fix potholes on the main road.",
                 assigned_to="Jane Smith", due_date=datetime.datetime(2023, 11, 20))

    # Add tasks to the tool
    tool.add_task(task1)
    tool.add_task(task2)

    # List all tasks
    print("All Tasks:")
    tool.list_tasks()

    # Update task status
    tool.update_task_status(task_id=1, new_status="In Progress")

    # List tasks again to see the updated status
    print("\nUpdated Tasks:")
    tool.list_tasks()
```
