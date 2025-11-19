"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Develop a workflow for managing team collaboration in a Scrum framework, referencing PDMA's Scrum Master certification.
Generated: DETERMINISTIC_64313935866f4df4
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Task:
    """Represents a task in the Scrum workflow."""
    
    def __init__(self, title: str, description: str, assignee: str):
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = 'To Do'  # Initial status
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status: str):
        """Update the status of the task."""
        valid_statuses = ['To Do', 'In Progress', 'Done']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.datetime.now()

    def __repr__(self):
        return f"Task(title={self.title}, status={self.status}, assignee={self.assignee})"


class Sprint:
    """Represents a sprint in the Scrum framework."""
    
    def __init__(self, sprint_name: str, duration_days: int):
        self.sprint_name = sprint_name
        self.start_date = datetime.datetime.now()
        self.end_date = self.start_date + datetime.timedelta(days=duration_days)
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the sprint."""
        self.tasks.append(task)

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Retrieve tasks by their status."""
        return [task for task in self.tasks if task.status == status]

    def __repr__(self):
        return f"Sprint(name={self.sprint_name}, tasks={self.tasks})"


class ScrumBoard:
    """Manages the Scrum workflow for team collaboration."""
    
    def __init__(self):
        self.sprints: List[Sprint] = []

    def create_sprint(self, sprint_name: str, duration_days: int) -> Sprint:
        """Create a new sprint."""
        sprint = Sprint(sprint_name, duration_days)
        self.sprints.append(sprint)
        return sprint

    def get_active_sprints(self) -> List[Sprint]:
        """Get all active sprints."""
        return [sprint for sprint in self.sprints if sprint.start_date <= datetime.datetime.now() <= sprint.end_date]

    def __repr__(self):
        return f"ScrumBoard(sprints={self.sprints})"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Scrum board
        scrum_board = ScrumBoard()

        # Create a new sprint
        sprint = scrum_board.create_sprint("Sprint 1", 14)

        # Create tasks
        task1 = Task("Implement login", "Create a login page", "Alice")
        task2 = Task("Set up database", "Configure the database", "Bob")

        # Add tasks to the sprint
        sprint.add_task(task1)
        sprint.add_task(task2)

        # Update task status
        task1.update_status("In Progress")

        # Print active sprints and their tasks
        active_sprints = scrum_board.get_active_sprints()
        for s in active_sprints:
            print(s)

    except Exception as e:
        print(f"An error occurred: {e}")
```
