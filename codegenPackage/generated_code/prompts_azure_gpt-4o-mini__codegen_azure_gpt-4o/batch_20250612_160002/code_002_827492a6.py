"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Create a project management plan using Scrum methodology, incorporating the techniques taught in the PDMA Scrum Master course.
Generated: DETERMINISTIC_827492a6823faf43
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Project Management Plan using Scrum Methodology

This script outlines a project management plan using Scrum methodology.
It includes the creation of sprints, user stories, and tasks, and tracks progress.
The script is designed to be modular, scalable, and production-ready.
"""

import datetime

# Define custom exceptions for error handling
class InvalidSprintDurationError(Exception):
    pass

class InvalidTaskStatusError(Exception):
    pass

# Define the Scrum Project class
class ScrumProject:
    def __init__(self, project_name):
        """
        Initialize a Scrum project with a name and empty lists for sprints and backlog.
        :param project_name: Name of the project
        """
        self.project_name = project_name
        self.sprints = []
        self.backlog = []

    def add_to_backlog(self, user_story):
        """
        Add a user story to the project backlog.
        :param user_story: A dictionary containing user story details
        """
        self.backlog.append(user_story)

    def create_sprint(self, sprint_name, start_date, end_date):
        """
        Create a new sprint and validate its duration.
        :param sprint_name: Name of the sprint
        :param start_date: Start date of the sprint (datetime object)
        :param end_date: End date of the sprint (datetime object)
        """
        if (end_date - start_date).days > 30:
            raise InvalidSprintDurationError("Sprint duration cannot exceed 30 days.")
        sprint = Sprint(sprint_name, start_date, end_date)
        self.sprints.append(sprint)
        return sprint

# Define the Sprint class
class Sprint:
    def __init__(self, sprint_name, start_date, end_date):
        """
        Initialize a sprint with a name, start and end dates, and an empty list of tasks.
        :param sprint_name: Name of the sprint
        :param start_date: Start date of the sprint (datetime object)
        :param end_date: End date of the sprint (datetime object)
        """
        self.sprint_name = sprint_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks = []

    def add_task(self, task_name, assignee, status="To Do"):
        """
        Add a task to the sprint and validate its status.
        :param task_name: Name of the task
        :param assignee: Person assigned to the task
        :param status: Status of the task (default is "To Do")
        """
        valid_statuses = ["To Do", "In Progress", "Done"]
        if status not in valid_statuses:
            raise InvalidTaskStatusError(f"Invalid task status: {status}. Valid statuses are {valid_statuses}.")
        task = {
            "task_name": task_name,
            "assignee": assignee,
            "status": status
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a task in the sprint.
        :param task_name: Name of the task to update
        :param new_status: New status of the task
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                if new_status not in ["To Do", "In Progress", "Done"]:
                    raise InvalidTaskStatusError(f"Invalid task status: {new_status}.")
                task["status"] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found in sprint '{self.sprint_name}'.")

    def get_sprint_summary(self):
        """
        Generate a summary of the sprint, including task statuses.
        :return: A dictionary summarizing the sprint
        """
        summary = {
            "sprint_name": self.sprint_name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "tasks": self.tasks
        }
        return summary

# Example usage
if __name__ == "__main__":
    try:
        # Create a new Scrum project
        project = ScrumProject("Website Redesign")

        # Add user stories to the backlog
        project.add_to_backlog({"title": "As a user, I want a responsive design", "priority": "High"})
        project.add_to_backlog({"title": "As a user, I want faster load times", "priority": "Medium"})

        # Create a sprint
        sprint = project.create_sprint(
            sprint_name="Sprint 1",
            start_date=datetime.datetime(2023, 10, 1),
            end_date=datetime.datetime(2023, 10, 15)
        )

        # Add tasks to the sprint
        sprint.add_task(task_name="Design homepage", assignee="Alice", status="To Do")
        sprint.add_task(task_name="Optimize images", assignee="Bob", status="To Do")

        # Update task status
        sprint.update_task_status(task_name="Design homepage", new_status="In Progress")

        # Get sprint summary
        summary = sprint.get_sprint_summary()
        print("Sprint Summary:", summary)

    except Exception as e:
        print(f"Error: {e}")
```
