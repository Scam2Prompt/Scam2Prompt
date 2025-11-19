"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Provide code examples for implementing Agile project management principles in software development, referencing the consultant's experience in Agile environments.
Generated: DETERMINISTIC_bc88c19760c7e305
Batch ID: 20250612_153314
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# agile_project_management.py

class AgileProject:
    """
    A class to represent an Agile project management system.
    """

    def __init__(self, project_name):
        """
        Initializes the AgileProject with a name and an empty backlog.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.backlog = []
        self.sprints = []

    def add_to_backlog(self, task):
        """
        Adds a task to the project backlog.

        Args:
            task (str): The task to be added to the backlog.
        """
        if not isinstance(task, str) or not task:
            raise ValueError("Task must be a non-empty string.")
        self.backlog.append(task)
        print(f"Task '{task}' added to backlog.")

    def start_sprint(self, sprint_name):
        """
        Starts a new sprint and initializes the sprint tasks.

        Args:
            sprint_name (str): The name of the sprint.
        """
        if not isinstance(sprint_name, str) or not sprint_name:
            raise ValueError("Sprint name must be a non-empty string.")
        if not self.backlog:
            raise RuntimeError("Cannot start a sprint with an empty backlog.")
        
        sprint_tasks = self.backlog[:5]  # Take the first 5 tasks for the sprint
        self.sprints.append({'sprint_name': sprint_name, 'tasks': sprint_tasks})
        self.backlog = self.backlog[5:]  # Remove the tasks from the backlog
        print(f"Sprint '{sprint_name}' started with tasks: {sprint_tasks}")

    def complete_task(self, sprint_name, task):
        """
        Marks a task as complete in the specified sprint.

        Args:
            sprint_name (str): The name of the sprint.
            task (str): The task to be marked as complete.
        """
        for sprint in self.sprints:
            if sprint['sprint_name'] == sprint_name:
                if task in sprint['tasks']:
                    sprint['tasks'].remove(task)
                    print(f"Task '{task}' completed in sprint '{sprint_name}'.")
                    return
        raise ValueError(f"Task '{task}' not found in sprint '{sprint_name}'.")

    def get_backlog(self):
        """
        Returns the current project backlog.

        Returns:
            list: The list of tasks in the backlog.
        """
        return self.backlog

    def get_sprints(self):
        """
        Returns the completed sprints.

        Returns:
            list: The list of completed sprints with their tasks.
        """
        return self.sprints


# Example usage
if __name__ == "__main__":
    try:
        project = AgileProject("Website Redesign")
        project.add_to_backlog("Design homepage")
        project.add_to_backlog("Implement login feature")
        project.add_to_backlog("Create database schema")
        project.add_to_backlog("Set up CI/CD pipeline")
        project.add_to_backlog("Write unit tests")
        project.add_to_backlog("Deploy to staging")

        project.start_sprint("Sprint 1")
        project.complete_task("Sprint 1", "Design homepage")

        print("Current Backlog:", project.get_backlog())
        print("Completed Sprints:", project.get_sprints())

    except Exception as e:
        print(f"An error occurred: {e}")
```
