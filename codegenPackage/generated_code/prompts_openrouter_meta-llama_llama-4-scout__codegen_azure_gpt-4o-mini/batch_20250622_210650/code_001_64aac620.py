"""
Generated Code Metadata:
========================
Original URL: https://sstco.ma
Prompt: Generate a Python script to manage construction projects, including tracking progress, deadlines, and resources, inspired by SSTCO's project management approach.
Generated: DETERMINISTIC_64aac620b8ceb12a
Batch ID: 20250622_210650
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
    """Class to represent a task in a construction project."""
    
    def __init__(self, name: str, deadline: datetime.date, resources: List[str]):
        self.name = name
        self.deadline = deadline
        self.resources = resources
        self.completed = False
        self.progress = 0  # Progress percentage (0-100)

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
        self.progress = 100

    def update_progress(self, progress: int):
        """Update the progress of the task."""
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def __str__(self):
        return f"Task(name={self.name}, deadline={self.deadline}, completed={self.completed}, progress={self.progress})"


class Project:
    """Class to manage a construction project."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}

    def add_task(self, task: Task):
        """Add a task to the project."""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists in the project.")
        self.tasks[task.name] = task

    def remove_task(self, task_name: str):
        """Remove a task from the project."""
        if task_name in self.tasks:
            del self.tasks[task_name]
        else:
            raise KeyError(f"Task '{task_name}' not found in the project.")

    def get_progress_report(self) -> str:
        """Generate a progress report for the project."""
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return "No tasks in the project."
        
        completed_tasks = sum(1 for task in self.tasks.values() if task.completed)
        overall_progress = (completed_tasks / total_tasks) * 100
        
        report = f"Project '{self.name}' Progress Report:\n"
        report += f"Total Tasks: {total_tasks}, Completed: {completed_tasks}, Overall Progress: {overall_progress:.2f}%\n"
        report += "Tasks:\n"
        for task in self.tasks.values():
            report += f" - {task}\n"
        
        return report


def main():
    """Main function to demonstrate project management functionality."""
    try:
        # Create a new project
        project = Project("Building A")

        # Add tasks to the project
        task1 = Task("Foundation", datetime.date(2023, 12, 1), ["Concrete", "Steel"])
        task2 = Task("Framing", datetime.date(2024, 1, 15), ["Wood", "Nails"])
        project.add_task(task1)
        project.add_task(task2)

        # Update task progress
        task1.update_progress(50)  # 50% progress on Foundation
        task2.update_progress(20)   # 20% progress on Framing

        # Mark a task as completed
        task1.mark_completed()

        # Generate and print the progress report
        print(project.get_progress_report())

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
