"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Develop a workflow for managing team collaboration in a Scrum framework, referencing PDMA's Scrum Master certification.
Generated: DETERMINISTIC_64313935866f4df4
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime, timedelta
from typing import List, Dict

class Task:
    """Class to represent a task in the Scrum workflow."""
    def __init__(self, title: str, description: str, assignee: str):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = "To Do"
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_status(self, status: str):
        """Update the status of the task."""
        valid_statuses = ["To Do", "In Progress", "Done"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status: {status}. Valid statuses are {valid_statuses}.")
        self.status = status
        self.updated_at = datetime.now()

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status}, assignee={self.assignee})"


class ScrumTeam:
    """Class to manage a Scrum team and its tasks."""
    def __init__(self, team_name: str):
        self.team_name = team_name
        self.sprint_backlog: List[Task] = []
        self.sprint_start_date = None
        self.sprint_end_date = None

    def start_sprint(self, duration_days: int):
        """Start a new sprint."""
        self.sprint_start_date = datetime.now()
        self.sprint_end_date = self.sprint_start_date + timedelta(days=duration_days)

    def add_task(self, task: Task):
        """Add a new task to the sprint backlog."""
        if self.sprint_start_date is None:
            raise RuntimeError("Sprint has not started. Please start a sprint before adding tasks.")
        self.sprint_backlog.append(task)

    def update_task_status(self, task_title: str, status: str):
        """Update the status of a task by its title."""
        task = self.get_task(task_title)
        if task:
            task.update_status(status)

    def get_task(self, task_title: str) -> Task:
        """Retrieve a task from the sprint backlog by its title."""
        for task in self.sprint_backlog:
            if task.title == task_title:
                return task
        raise ValueError(f"Task with title '{task_title}' not found in the sprint backlog.")

    def get_sprint_summary(self) -> Dict[str, List[Task]]:
        """Get a summary of the current sprint's tasks categorized by their status."""
        summary = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }
        for task in self.sprint_backlog:
            summary[task.status].append(task)
        return summary


# Example usage
if __name__ == "__main__":
    # Create a Scrum Team
    scrum_team = ScrumTeam("Development Team")

    # Start a new sprint of 14 days
    scrum_team.start_sprint(duration_days=14)

    # Add tasks to the sprint
    task1 = Task(title="Implement login feature", description="Create a login feature using OAuth.", assignee="Alice")
    task2 = Task(title="Set up continuous integration", description="Configure CI/CD pipeline with GitHub Actions.", assignee="Bob")
    scrum_team.add_task(task1)
    scrum_team.add_task(task2)

    # Update the status of a task
    scrum_team.update_task_status("Implement login feature", "In Progress")

    # Print sprint summary
    print(scrum_team.get_sprint_summary())
```
