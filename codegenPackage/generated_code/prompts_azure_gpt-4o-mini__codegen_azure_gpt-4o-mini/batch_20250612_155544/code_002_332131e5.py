"""
Generated Code Metadata:
========================
Original URL: https://haseebbaig.me
Prompt: Create a project management strategy for a web development project using Agile methodologies, inspired by the project management expertise highlighted by Enorness.
Generated: DETERMINISTIC_332131e5728b43da
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management.py

class AgileProject:
    """
    A class to represent an Agile project management strategy for web development.
    """

    def __init__(self, project_name, team_members):
        """
        Initializes the AgileProject with a name and a list of team members.

        Args:
            project_name (str): The name of the project.
            team_members (list): A list of team members involved in the project.
        """
        self.project_name = project_name
        self.team_members = team_members
        self.sprints = []
        self.backlog = []
        self.current_sprint = None

    def add_to_backlog(self, task):
        """
        Adds a task to the project backlog.

        Args:
            task (str): The task to be added to the backlog.
        """
        self.backlog.append(task)
        print(f"Task '{task}' added to backlog.")

    def start_sprint(self, sprint_duration):
        """
        Starts a new sprint with a specified duration.

        Args:
            sprint_duration (int): The duration of the sprint in days.
        """
        if self.current_sprint is not None:
            print("A sprint is already in progress. Please complete it before starting a new one.")
            return

        self.current_sprint = {
            'duration': sprint_duration,
            'tasks': [],
            'completed_tasks': []
        }
        print(f"Sprint started with duration of {sprint_duration} days.")

    def add_task_to_sprint(self, task):
        """
        Adds a task from the backlog to the current sprint.

        Args:
            task (str): The task to be added to the current sprint.
        """
        if self.current_sprint is None:
            print("No sprint in progress. Please start a sprint first.")
            return

        if task in self.backlog:
            self.current_sprint['tasks'].append(task)
            self.backlog.remove(task)
            print(f"Task '{task}' added to current sprint.")
        else:
            print(f"Task '{task}' not found in backlog.")

    def complete_task(self, task):
        """
        Marks a task as completed in the current sprint.

        Args:
            task (str): The task to be marked as completed.
        """
        if self.current_sprint is None:
            print("No sprint in progress. Please start a sprint first.")
            return

        if task in self.current_sprint['tasks']:
            self.current_sprint['tasks'].remove(task)
            self.current_sprint['completed_tasks'].append(task)
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found in current sprint.")

    def end_sprint(self):
        """
        Ends the current sprint and summarizes the results.
        """
        if self.current_sprint is None:
            print("No sprint in progress to end.")
            return

        print(f"Sprint ended. Summary:")
        print(f"Duration: {self.current_sprint['duration']} days")
        print(f"Completed tasks: {self.current_sprint['completed_tasks']}")
        print(f"Remaining tasks: {self.current_sprint['tasks']}")
        self.current_sprint = None

    def display_backlog(self):
        """
        Displays the current project backlog.
        """
        print("Current Backlog:")
        for task in self.backlog:
            print(f"- {task}")

# Example usage
if __name__ == "__main__":
    try:
        project = AgileProject("Web Development Project", ["Alice", "Bob", "Charlie"])
        project.add_to_backlog("Design UI")
        project.add_to_backlog("Develop API")
        project.start_sprint(14)
        project.add_task_to_sprint("Design UI")
        project.complete_task("Design UI")
        project.end_sprint()
        project.display_backlog()
    except Exception as e:
        print(f"An error occurred: {e}")
```
