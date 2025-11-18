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
"""
Team Collaboration Workflow in Scrum Framework
================================================

This script is a high-level implementation of a workflow for managing team collaboration 
in a Scrum framework. The workflow incorporates the responsibilities of the Scrum Master 
as referenced by PDMA's Scrum Master certification guidelines.

The script demonstrates:
- Sprint planning
- Daily standups
- Sprint reviews and retrospectives
- Task tracking and role management

Dependencies:
- Python 3.9+
- `tabulate` library for pretty-printing task tables. Install via `pip install tabulate`.

"""

from datetime import datetime, timedelta
from tabulate import tabulate


class Task:
    """Represents a task in the Scrum workflow."""
    def __init__(self, title, assignee, status="To Do"):
        self.title = title
        self.assignee = assignee
        self.status = status
        self.created_at = datetime.now()

    def update_status(self, new_status):
        """Update the status of the task."""
        if new_status not in ["To Do", "In Progress", "Done"]:
            raise ValueError("Invalid status. Use 'To Do', 'In Progress', or 'Done'.")
        self.status = new_status


class ScrumTeam:
    """Manages the Scrum team, tasks, and ceremonies."""
    def __init__(self, team_name, members):
        self.team_name = team_name
        self.members = members
        self.backlog = []
        self.sprint_tasks = []
        self.sprint_start_date = None
        self.sprint_end_date = None

    def add_task_to_backlog(self, task):
        """Add a task to the product backlog."""
        if not isinstance(task, Task):
            raise TypeError("Invalid task. Must be an instance of the Task class.")
        self.backlog.append(task)

    def start_sprint(self, duration_in_days=14):
        """Start a new sprint with a given duration."""
        if self.sprint_start_date:
            raise RuntimeError("Cannot start a new sprint. Current sprint is still active.")
        self.sprint_start_date = datetime.now()
        self.sprint_end_date = self.sprint_start_date + timedelta(days=duration_in_days)
        self.sprint_tasks = self.backlog[:]
        self.backlog = []

    def daily_standup(self):
        """Simulate a daily standup meeting."""
        print(f"Daily Standup - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Team: {self.team_name}")
        print(tabulate(
            [[task.title, task.assignee, task.status] for task in self.sprint_tasks],
            headers=["Task", "Assignee", "Status"],
            tablefmt="grid",
        ))

    def complete_sprint(self):
        """Complete the sprint and move pending tasks back to the backlog."""
        if not self.sprint_start_date:
            raise RuntimeError("No active sprint to complete.")
        print("Sprint completed. Reviewing tasks...")
        pending_tasks = [task for task in self.sprint_tasks if task.status != "Done"]
        self.backlog.extend(pending_tasks)
        self.sprint_tasks = []
        self.sprint_start_date = None
        self.sprint_end_date = None

    def show_backlog(self):
        """Display the product backlog."""
        print("Product Backlog:")
        print(tabulate(
            [[task.title, task.assignee, task.status, task.created_at.strftime('%Y-%m-%d %H:%M:%S')] for task in self.backlog],
            headers=["Task", "Assignee", "Status", "Created At"],
            tablefmt="grid",
        ))


# Example Execution
if __name__ == "__main__":
    # Initialize Scrum team
    team = ScrumTeam("Agile Avengers", ["Alice", "Bob", "Charlie", "Diana"])

    # Add tasks to backlog
    team.add_task_to_backlog(Task("Setup project repository", "Alice"))
    team.add_task_to_backlog(Task("Define user stories", "Bob"))
    team.add_task_to_backlog(Task("Create CI/CD pipeline", "Charlie"))

    # Display backlog
    team.show_backlog()

    # Start a new sprint
    team.start_sprint(duration_in_days=14)
    
    # Run a daily standup
    team.daily_standup()

    # Progress tasks
    team.sprint_tasks[0].update_status("In Progress")
    team.sprint_tasks[1].update_status("Done")
    
    # Run another daily standup
    team.daily_standup()

    # Complete the sprint
    team.complete_sprint()

    # Show backlog after sprint completion
    team.show_backlog()
```
