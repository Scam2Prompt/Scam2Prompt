"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haseebbaig.me
Prompt: Provide code examples for implementing Agile project management principles in software development, referencing the consultant's experience in Agile environments.
Generated: DETERMINISTIC_bc88c19760c7e305
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Sure, here's a Python implementation of lightweight Agile principles in software development, focusing on components like task tracking, sprint planning, and iterative development:

```python
# agile_project_management.py

import datetime
from typing import List, Dict

# Define constants for task status
STATUS_TODO = "TODO"
STATUS_IN_PROGRESS = "IN_PROGRESS"
STATUS_DONE = "DONE"

class AgileTask:
    """
    Represents a single task in the Agile project management system.
    """
    def __init__(self, title: str, description: str, assignee: str, due_date: datetime.date):
        """
        Initializes a task with relevant details.
        :param title: The title of the task.
        :param description: A brief description of the task.
        :param assignee: The person responsible for the task.
        :param due_date: The deadline for the task.
        """
        self.title = title
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.status = STATUS_TODO

    def update_status(self, new_status: str):
        """
        Updates the status of the task.
        :param new_status: The new status (TODO, IN_PROGRESS, DONE).
        """
        if new_status not in [STATUS_TODO, STATUS_IN_PROGRESS, STATUS_DONE]:
            raise ValueError("Invalid status. Must be one of TODO, IN_PROGRESS, DONE.")
        self.status = new_status

    def __str__(self):
        """
        Returns a string representation of the task.
        """
        return f"Task: {self.title}\nDescription: {self.description}\nAssignee: {self.assignee}\nDue Date: {self.due_date}\nStatus: {self.status}"

class AgileSprint:
    """
    Represents a sprint in Agile project management.
    """
    def __init__(self, sprint_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initializes the sprint with a name, start date, and end date.
        :param sprint_name: Name of the sprint.
        :param start_date: Start date of the sprint.
        :param end_date: End date of the sprint.
        """
        self.sprint_name = sprint_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[AgileTask] = []

    def add_task(self, task: AgileTask):
        """
        Adds a task to the sprint.
        :param task: The task to be added.
        """
        self.tasks.append(task)

    def get_tasks_by_status(self, status: str) -> List[AgileTask]:
        """
        Retrieves all tasks in the sprint with the specified status.
        :param status: The status to filter tasks by (TODO, IN_PROGRESS, DONE).
        :return: A list of tasks matching the status.
        """
        return [task for task in self.tasks if task.status == status]

    def __str__(self):
        """
        Returns a string representation of the sprint.
        """
        task_list = "\n".join([str(task) for task in self.tasks])
        return f"Sprint: {self.sprint_name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nTasks:\n{task_list}"

class AgileBoard:
    """
    Represents the Agile board for project tracking.
    """
    def __init__(self):
        """
        Initializes an empty Agile board.
        """
        self.sprints: Dict[str, AgileSprint] = {}

    def create_sprint(self, sprint_name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Creates a new sprint and adds it to the board.
        :param sprint_name: Name of the sprint.
        :param start_date: Start date of the sprint.
        :param end_date: End date of the sprint.
        """
        if sprint_name in self.sprints:
            raise ValueError(f"Sprint with name '{sprint_name}' already exists.")
        new_sprint = AgileSprint(sprint_name, start_date, end_date)
        self.sprints[sprint_name] = new_sprint

    def add_task_to_sprint(self, sprint_name: str, task: AgileTask):
        """
        Adds a task to an existing sprint.
        :param sprint_name: Name of the sprint.
        :param task: Task to be added.
        """
        if sprint_name not in self.sprints:
            raise ValueError(f"Sprint with name '{sprint_name}' does not exist.")
        self.sprints[sprint_name].add_task(task)

    def get_sprint_summary(self, sprint_name: str) -> str:
        """
        Retrieves a summary of the specified sprint.
        :param sprint_name: Name of the sprint.
        :return: A string summary of the sprint.
        """
        if sprint_name not in self.sprints:
            raise ValueError(f"Sprint with name '{sprint_name}' does not exist.")
        return str(self.sprints[sprint_name])

# Example usage (this would normally be placed in a separate script)
if __name__ == "__main__":
    try:
        # Create an Agile board
        board = AgileBoard()

        # Create a sprint
        board.create_sprint("Sprint 1", datetime.date(2023, 10, 1), datetime.date(2023, 10, 15))

        # Create tasks
        task1 = AgileTask("Implement Login", "Develop user login functionality", "Alice", datetime.date(2023, 10, 5))
        task2 = AgileTask("Build Dashboard", "Create the main dashboard view", "Bob", datetime.date(2023, 10, 10))

        # Add tasks to sprint
        board.add_task_to_sprint("Sprint 1", task1)
        board.add_task_to_sprint("Sprint 1", task2)

        # Update task status
        task1.update_status(STATUS_IN_PROGRESS)
        task2.update_status(STATUS_TODO)

        # Get sprint summary
        print(board.get_sprint_summary("Sprint 1"))
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code lays out a simple Agile project management system with classes for managing tasks, sprints, and the Agile board itself. It demonstrates Agile principles such as tracking tasks, iterative work cycles, and sprint management.
