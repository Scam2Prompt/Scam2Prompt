"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.construyerk.com
Prompt: Generate a code snippet for a project management tool that tracks construction timelines and responsibilities for a construction company like Construye RK.
Generated: DETERMINISTIC_3ccb6d0f59cad8a9
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class Task:
    """Represents a task in the construction project."""
    def __init__(self, name: str, responsible_party: str, due_date: datetime.date):
        self.name = name
        self.responsible_party = responsible_party
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def __repr__(self):
        """Provides a string representation of the Task."""
        return f"Task(name={self.name}, responsible_party={self.responsible_party}, due_date={self.due_date}, completed={self.completed})"


class Project:
    """Represents a construction project with multiple tasks."""
    def __init__(self, project_name: str) -> None:
        self.project_name = project_name
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the project."""
        self.tasks.append(task)

    def get_overdue_tasks(self) -> List[Task]:
        """Returns a list of overdue tasks."""
        today = datetime.date.today()
        return [task for task in self.tasks if task.due_date < today and not task.completed]

    def get_tasks_by_responsibility(self, party: str) -> List[Task]:
        """Returns tasks assigned to a specific responsible party."""
        return [task for task in self.tasks if task.responsible_party == party]

    def __repr__(self):
        """Provides a string representation of the Project."""
        return f"Project(name={self.project_name}, tasks={self.tasks})"


def main():
    """Main function to demonstrate the project management tool."""
    # Initialize a project
    project = Project(project_name="Construye RK Construction")

    # Add tasks with responsible parties and due dates
    project.add_task(Task("Foundation Laying", "Team A", datetime.date(2023, 10, 10)))
    project.add_task(Task("Framing", "Team B", datetime.date(2023, 10, 15)))
    project.add_task(Task("Roof Installation", "Team A", datetime.date(2023, 10, 20)))

    # Simulate marking a task as complete
    project.tasks[0].mark_complete()

    # Get and display overdue tasks
    overdue_tasks = project.get_overdue_tasks()
    if overdue_tasks:
        print("Overdue Tasks:")
        for task in overdue_tasks:
            print(task)
    else:
        print("No overdue tasks.")

    # Get tasks by responsible party
    team_a_tasks = project.get_tasks_by_responsibility("Team A")
    print("\nTasks assigned to Team A:")
    for task in team_a_tasks:
        print(task)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
