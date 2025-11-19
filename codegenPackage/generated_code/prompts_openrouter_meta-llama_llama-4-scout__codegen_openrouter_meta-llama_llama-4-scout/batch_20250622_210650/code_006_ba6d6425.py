"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: "Create a template for a project management plan using agile methodologies, incorporating Matter's approach to project development and monitoring."
Generated: DETERMINISTIC_ba6d64257576327d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management_plan.py

class ProjectManagementPlan:
    """
    A template for a project management plan using agile methodologies,
    incorporating Matter's approach to project development and monitoring.
    """

    def __init__(self, project_name, team_members, project_description):
        """
        Initialize a project management plan.

        Args:
            project_name (str): The name of the project.
            team_members (list): A list of team members.
            project_description (str): A brief description of the project.
        """
        self.project_name = project_name
        self.team_members = team_members
        self.project_description = project_description
        self.sprint_backlog = []
        self.tasks = {}

    def add_sprint(self, sprint_name, sprint_duration):
        """
        Add a sprint to the project management plan.

        Args:
            sprint_name (str): The name of the sprint.
            sprint_duration (int): The duration of the sprint in days.

        Returns:
            dict: The sprint details.
        """
        sprint = {
            "name": sprint_name,
            "duration": sprint_duration,
            "tasks": []
        }
        self.sprint_backlog.append(sprint)
        return sprint

    def add_task(self, sprint_name, task_name, task_description, task_assignee):
        """
        Add a task to a sprint.

        Args:
            sprint_name (str): The name of the sprint.
            task_name (str): The name of the task.
            task_description (str): A brief description of the task.
            task_assignee (str): The team member assigned to the task.

        Returns:
            dict: The task details.
        """
        for sprint in self.sprint_backlog:
            if sprint["name"] == sprint_name:
                task = {
                    "name": task_name,
                    "description": task_description,
                    "assignee": task_assignee,
                    "status": "To-Do"
                }
                sprint["tasks"].append(task)
                self.tasks[task_name] = task
                return task
        raise ValueError("Sprint not found")

    def update_task_status(self, task_name, status):
        """
        Update the status of a task.

        Args:
            task_name (str): The name of the task.
            status (str): The new status of the task.

        Raises:
            ValueError: If the task is not found.
        """
        if task_name in self.tasks:
            self.tasks[task_name]["status"] = status
        else:
            raise ValueError("Task not found")

    def print_project_plan(self):
        """
        Print the project management plan.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Team Members: {', '.join(self.team_members)}")
        print(f"Project Description: {self.project_description}")
        print("Sprint Backlog:")
        for sprint in self.sprint_backlog:
            print(f"  - {sprint['name']} ({sprint['duration']} days)")
            for task in sprint["tasks"]:
                print(f"    - {task['name']} (Assignee: {task['assignee']}, Status: {task['status']})")


def main():
    try:
        project_name = "Example Project"
        team_members = ["John Doe", "Jane Doe", "Bob Smith"]
        project_description = "This is an example project."

        project_plan = ProjectManagementPlan(project_name, team_members, project_description)

        sprint1 = project_plan.add_sprint("Sprint 1", 14)
        sprint2 = project_plan.add_sprint("Sprint 2", 14)

        project_plan.add_task("Sprint 1", "Task 1", "This is task 1.", "John Doe")
        project_plan.add_task("Sprint 1", "Task 2", "This is task 2.", "Jane Doe")
        project_plan.add_task("Sprint 2", "Task 3", "This is task 3.", "Bob Smith")

        project_plan.update_task_status("Task 1", "In Progress")

        project_plan.print_project_plan()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
