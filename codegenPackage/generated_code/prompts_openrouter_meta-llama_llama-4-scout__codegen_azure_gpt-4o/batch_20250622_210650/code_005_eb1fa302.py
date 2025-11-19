"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "What are the benefits of using Scrum and Agile methodologies in software development, and how can they be applied in a real-world project?"
Generated: DETERMINISTIC_eb1fa302def6198a
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is Python code that simulates the application of Scrum and Agile methodologies in a real-world software development project. The code demonstrates how tasks can be managed in sprints, how team members collaborate, and how progress is tracked.

```python
import datetime
from typing import List, Dict

# Define a class to represent a task in the project
class Task:
    def __init__(self, title: str, description: str, assignee: str, status: str = "To Do"):
        """
        Initialize a task with a title, description, assignee, and status.

        :param title: Title of the task
        :param description: Description of the task
        :param assignee: Team member assigned to the task
        :param status: Current status of the task (default: "To Do")
        """
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status

    def update_status(self, new_status: str):
        """
        Update the status of the task.

        :param new_status: New status of the task (e.g., "In Progress", "Completed")
        """
        valid_statuses = ["To Do", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status

    def __str__(self):
        """
        Return a string representation of the task.
        """
        return f"Task: {self.title}, Assignee: {self.assignee}, Status: {self.status}"


# Define a class to represent a sprint in the project
class Sprint:
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a sprint with a name, start date, and end date.

        :param name: Name of the sprint
        :param start_date: Start date of the sprint
        :param end_date: End date of the sprint
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """
        Add a task to the sprint.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def get_progress(self) -> Dict[str, int]:
        """
        Calculate the progress of the sprint based on task statuses.

        :return: A dictionary with counts of tasks by status
        """
        progress = {"To Do": 0, "In Progress": 0, "Completed": 0}
        for task in self.tasks:
            progress[task.status] += 1
        return progress

    def __str__(self):
        """
        Return a string representation of the sprint.
        """
        return f"Sprint: {self.name}, Start: {self.start_date}, End: {self.end_date}, Tasks: {len(self.tasks)}"


# Define a class to represent the Agile project
class AgileProject:
    def __init__(self, name: str):
        """
        Initialize an Agile project with a name.

        :param name: Name of the project
        """
        self.name = name
        self.sprints: List[Sprint] = []

    def add_sprint(self, sprint: Sprint):
        """
        Add a sprint to the project.

        :param sprint: Sprint to be added
        """
        self.sprints.append(sprint)

    def get_project_summary(self):
        """
        Generate a summary of the project's progress.

        :return: A summary string
        """
        summary = f"Project: {self.name}\n"
        for sprint in self.sprints:
            progress = sprint.get_progress()
            summary += f"{sprint.name} - Start: {sprint.start_date}, End: {sprint.end_date}\n"
            summary += f"  Tasks: {len(sprint.tasks)}\n"
            summary += f"  Progress: {progress}\n"
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Create an Agile project
        project = AgileProject("Website Redesign")

        # Create a sprint
        sprint1 = Sprint("Sprint 1", datetime.date(2023, 10, 1), datetime.date(2023, 10, 15))

        # Add tasks to the sprint
        task1 = Task("Design Homepage", "Create a new homepage design", "Alice")
        task2 = Task("Develop Login Feature", "Implement login functionality", "Bob")
        task3 = Task("Write Unit Tests", "Write tests for the login feature", "Charlie")

        sprint1.add_task(task1)
        sprint1.add_task(task2)
        sprint1.add_task(task3)

        # Update task statuses
        task1.update_status("In Progress")
        task2.update_status("Completed")

        # Add the sprint to the project
        project.add_sprint(sprint1)

        # Print project summary
        print(project.get_project_summary())

    except Exception as e:
        print(f"An error occurred: {e}")
```

This code is production-ready, adheres to best practices, and includes error handling. It simulates the Agile methodology by managing tasks within sprints and tracking progress.
