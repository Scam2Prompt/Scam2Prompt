"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Generate a project management workflow in Python for civil engineering tasks, including structural repairs, waterproofing, and painting, inspired by SOM Civil Engineers' project management approach.
Generated: DETERMINISTIC_17feb92a70f58f09
Batch ID: 20250612_151429
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
    Represents a single task in the project workflow.
    """
    def __init__(self, name, category, deadline, priority):
        """
        Initialize a task with name, category, deadline, and priority.

        :param name: Name of the task
        :param category: Category of the task (e.g., Structural Repairs, Waterproofing, Painting)
        :param deadline: Deadline for the task (datetime.date object)
        :param priority: Priority level (integer, lower values = higher priority)
        """
        self.name = name
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.status = "Pending"  # Status can be "Pending", "In Progress", or "Completed"

    def mark_in_progress(self):
        """Marks the task status as 'In Progress'."""
        self.status = "In Progress"

    def mark_completed(self):
        """Marks the task status as 'Completed'."""
        self.status = "Completed"

    def __str__(self):
        """Returns a string representation of the task."""
        return f"{self.name} - {self.category} - {self.status} - Priority: {self.priority} - Deadline: {self.deadline}"


class ProjectWorkflow:
    """
    Represents the workflow for managing multiple civil engineering tasks.
    """
    def __init__(self, project_name):
        """
        Initialize a project workflow with a name and an empty task list.

        :param project_name: Name of the project
        """
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task):
        """
        Adds a new task to the workflow.

        :param task: Task object to add
        """
        if not isinstance(task, Task):
            raise TypeError("Only Task objects can be added.")
        self.tasks.append(task)

    def view_tasks(self):
        """Displays all tasks in the workflow."""
        if not self.tasks:
            print("No tasks found.")
            return
        print(f"Tasks for Project: {self.project_name}")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def get_pending_tasks(self):
        """Returns a list of all pending tasks."""
        return [task for task in self.tasks if task.status == "Pending"]

    def get_in_progress_tasks(self):
        """Returns a list of all in-progress tasks."""
        return [task for task in self.tasks if task.status == "In Progress"]

    def get_completed_tasks(self):
        """Returns a list of all completed tasks."""
        return [task for task in self.tasks if task.status == "Completed"]

    def sort_tasks_by_priority(self):
        """Sorts tasks by priority in ascending order (highest priority first)."""
        self.tasks.sort(key=lambda task: task.priority)

    def sort_tasks_by_deadline(self):
        """Sorts tasks by deadline in ascending order (earliest deadline first)."""
        self.tasks.sort(key=lambda task: task.deadline)


# Example Usage
if __name__ == "__main__":
    try:
        # Create a new project workflow
        workflow = ProjectWorkflow("Civil Engineering Project")

        # Add tasks to the workflow
        workflow.add_task(Task("Repair Column A", "Structural Repairs", datetime.date(2023, 11, 15), 1))
        workflow.add_task(Task("Apply Basement Waterproofing", "Waterproofing", datetime.date(2023, 11, 20), 3))
        workflow.add_task(Task("Paint Exterior Walls", "Painting", datetime.date(2023, 11, 18), 2))

        # View all tasks
        workflow.view_tasks()

        # Mark a task as 'In Progress' and 'Completed'
        workflow.tasks[0].mark_in_progress()
        workflow.tasks[0].mark_completed()

        # Sort tasks by priority and view them
        workflow.sort_tasks_by_priority()
        print("\nSorted Tasks by Priority:")
        workflow.view_tasks()

        # Sort tasks by deadline and view them
        workflow.sort_tasks_by_deadline()
        print("\nSorted Tasks by Deadline:")
        workflow.view_tasks()

    except Exception as e:
        # Catch and display any errors
        print(f"An error occurred: {e}")
```
