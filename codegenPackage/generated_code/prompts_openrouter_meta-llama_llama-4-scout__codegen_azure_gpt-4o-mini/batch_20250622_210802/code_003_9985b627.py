"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: "Describe a software solution for construction project management that could be used by a company like INARO S.A.S., including features for planning, team management, and client relations."
Generated: DETERMINISTIC_9985b627572992c3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_project_management.py

class Project:
    """
    Represents a construction project with attributes for planning, team management, and client relations.
    """

    def __init__(self, name, client_name, budget):
        """
        Initializes a new project with the given name, client name, and budget.

        :param name: Name of the project
        :param client_name: Name of the client
        :param budget: Budget allocated for the project
        """
        self.name = name
        self.client_name = client_name
        self.budget = budget
        self.team_members = []
        self.tasks = []
        self.status = 'Planning'

    def add_team_member(self, member_name):
        """
        Adds a team member to the project.

        :param member_name: Name of the team member to add
        """
        self.team_members.append(member_name)

    def add_task(self, task_name, assigned_to, deadline):
        """
        Adds a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Name of the team member assigned to the task
        :param deadline: Deadline for the task
        """
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'deadline': deadline,
            'completed': False
        }
        self.tasks.append(task)

    def complete_task(self, task_name):
        """
        Marks a task as completed.

        :param task_name: Name of the task to complete
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['completed'] = True
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def get_project_summary(self):
        """
        Returns a summary of the project including team members, tasks, and status.

        :return: Dictionary containing project summary
        """
        return {
            'project_name': self.name,
            'client_name': self.client_name,
            'budget': self.budget,
            'team_members': self.team_members,
            'tasks': self.tasks,
            'status': self.status
        }

    def update_status(self, new_status):
        """
        Updates the status of the project.

        :param new_status: New status to set for the project
        """
        self.status = new_status


def main():
    """
    Main function to demonstrate the functionality of the Project management system.
    """
    try:
        # Create a new project
        project = Project(name="New Building", client_name="INARO S.A.S.", budget=500000)

        # Add team members
        project.add_team_member("Alice")
        project.add_team_member("Bob")

        # Add tasks
        project.add_task("Foundation", "Alice", "2023-12-01")
        project.add_task("Framing", "Bob", "2024-01-15")

        # Complete a task
        project.complete_task("Foundation")

        # Update project status
        project.update_status("In Progress")

        # Print project summary
        summary = project.get_project_summary()
        print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
