"""
Generated Code Metadata:
========================
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: "Write a Python code snippet to manage construction projects using design-build and turnkey construction services, considering factors like project planning, client requirements, and team collaboration."
Generated: DETERMINISTIC_bae6003ff7810109
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class Project:
    def __init__(self, name: str, client: str, start_date: datetime.date, end_date: datetime.date):
        """
        Initialize a new construction project.

        :param name: Name of the project
        :param client: Client's name
        :param start_date: Project start date
        :param end_date: Project end date
        """
        self.name = name
        self.client = client
        self.start_date = start_date
        self.end_date = end_date
        self.tasks: List[Dict[str, Any]] = []
        self.team_members: List[str] = []

    def add_task(self, task_name: str, assigned_to: str, due_date: datetime.date):
        """
        Add a task to the project.

        :param task_name: Name of the task
        :param assigned_to: Team member assigned to the task
        :param due_date: Due date for the task
        """
        task = {
            'task_name': task_name,
            'assigned_to': assigned_to,
            'due_date': due_date,
            'status': 'Pending'
        }
        self.tasks.append(task)

    def add_team_member(self, member_name: str):
        """
        Add a team member to the project.

        :param member_name: Name of the team member
        """
        if member_name not in self.team_members:
            self.team_members.append(member_name)
        else:
            raise ValueError(f"Team member '{member_name}' is already added.")

    def update_task_status(self, task_name: str, status: str):
        """
        Update the status of a task.

        :param task_name: Name of the task to update
        :param status: New status of the task (e.g., 'Completed', 'In Progress')
        """
        for task in self.tasks:
            if task['task_name'] == task_name:
                task['status'] = status
                return
        raise ValueError(f"Task '{task_name}' not found.")

    def project_summary(self) -> Dict[str, Any]:
        """
        Generate a summary of the project.

        :return: A dictionary containing project details
        """
        return {
            'project_name': self.name,
            'client': self.client,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'tasks': self.tasks,
            'team_members': self.team_members
        }

def main():
    # Example usage of the Project class
    try:
        project = Project("New Office Building", "ABC Corp", datetime.date(2023, 10, 1), datetime.date(2024, 10, 1))
        project.add_team_member("Alice")
        project.add_team_member("Bob")
        project.add_task("Foundation Work", "Alice", datetime.date(2023, 11, 1))
        project.add_task("Framing", "Bob", datetime.date(2023, 12, 1))
        
        project.update_task_status("Foundation Work", "Completed")
        
        summary = project.project_summary()
        print(summary)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
