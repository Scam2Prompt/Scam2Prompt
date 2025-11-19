"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmpinnacle.com
Prompt: Generate a code snippet for a project management tool that can track the progress of civil engineering projects like those undertaken by C&M Pinnacle.
Generated: DETERMINISTIC_d0896f50b2a2c85e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Task:
    """Class representing a task in a civil engineering project."""
    
    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title: str = title
        self.description: str = description
        self.due_date: datetime.date = due_date
        self.completed: bool = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """String representation of the task."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Due: {self.due_date})"


class Project:
    """Class representing a civil engineering project."""

    def __init__(self, name: str, start_date: datetime.date):
        self.name: str = name
        self.start_date: datetime.date = start_date
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a new task to the project."""
        self.tasks.append(task)

    def get_progress(self) -> float:
        """Calculate the project progress as a percentage."""
        if not self.tasks:
            return 0.0
        
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        total_tasks = len(self.tasks)
        return (completed_tasks / total_tasks) * 100

    def __str__(self) -> str:
        """String representation of the project."""
        task_list = "\n".join(str(task) for task in self.tasks)
        progress = self.get_progress()
        return f"Project: {self.name}\nProgress: {progress:.2f}%\nTasks:\n{task_list}"


def main():
    """Main function to demonstrate the project management tool."""
    try:
        # Create a new project
        project = Project(name="Bridge Construction", start_date=datetime.date(2023, 10, 1))

        # Add tasks to the project
        project.add_task(Task("Excavation", "Excavate the foundation", datetime.date(2023, 10, 15)))
        project.add_task(Task("Lay Foundation", "Pour concrete for the foundation", datetime.date(2023, 10, 30)))
        project.add_task(Task("Build Structure", "Construct the bridge structure", datetime.date(2023, 11, 15)))

        # Mark one task as completed
        project.tasks[0].mark_completed()

        # Print the project status
        print(project)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
