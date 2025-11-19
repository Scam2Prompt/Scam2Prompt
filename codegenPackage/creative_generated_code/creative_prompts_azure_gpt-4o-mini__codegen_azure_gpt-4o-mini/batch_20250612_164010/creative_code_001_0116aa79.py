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
from typing import List, Optional

class Task:
    """Class representing a maintenance task."""

    def __init__(self, title: str, description: str, due_date: datetime.date):
        """
        Initialize a new Task.

        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date for task completion
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'Pending'  # Task status: Pending, In Progress, Completed
        self.created_at = datetime.date.today()  # Task creation date

    def mark_in_progress(self):
        """Mark the task as in progress."""
        if self.status == 'Pending':
            self.status = 'In Progress'

    def mark_completed(self):
        """Mark the task as completed."""
        if self.status == 'In Progress':
            self.status = 'Completed'

    def __str__(self):
        """Return a string representation of the task."""
        return f"Task(title='{self.title}', status='{self.status}', due_date='{self.due_date}')"

class ProjectManagementTool:
    """Class to manage civil maintenance tasks."""

    def __init__(self):
        """Initialize the project management tool with an empty task list."""
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, due_date: datetime.date) -> None:
        """
        Add a new task to the project.

        :param title: Title of the task
        :param description: Description of the task
        :param due_date: Due date for task completion
        """
        # Validate due date
        if due_date < datetime.date.today():
            raise ValueError("Due date cannot be in the past.")
        
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)

    def get_task_list(self) -> List[str]:
        """Get a list of all tasks in string format."""
        return [str(task) for task in self.tasks]

    def update_task_status(self, title: str, status: str) -> None:
        """
        Update the status of a task by title.

        :param title: Title of the task to update
        :param status: New status of the task (In Progress or Completed)
        :raises ValueError: If the task is not found or invalid status is given
        """
        task = self.find_task(title)
        
        if not task:
            raise ValueError(f"Task with title '{title}' not found.")
        
        if status == 'In Progress':
            task.mark_in_progress()
        elif status == 'Completed':
            task.mark_completed()
        else:
            raise ValueError("Invalid status. Use 'In Progress' or 'Completed'.")

    def find_task(self, title: str) -> Optional[Task]:
        """
        Find a task by its title.

        :param title: Title of the task to find
        :return: The Task object if found, otherwise None
        """
        for task in self.tasks:
            if task.title == title:
                return task
        return None

# Example usage
if __name__ == "__main__":
    tool = ProjectManagementTool()
    
    try:
        tool.add_task("Repair Road", "Fix potholes on Main St.", datetime.date(2023, 12, 1))
        tool.add_task("Clean Park", "Remove debris from Central Park.", datetime.date(2023, 11, 15))
        
        print("Current Tasks:")
        print(tool.get_task_list())

        tool.update_task_status("Repair Road", "In Progress")
        print("\nUpdated Task:")
        print(tool.get_task_list())
        
        tool.update_task_status("Repair Road", "Completed")
        print("\nFinal Task Status:")
        print(tool.get_task_list())

    except ValueError as e:
        print(f"An error occurred: {e}")
```
