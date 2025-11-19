"""
Generated Code Metadata:
========================
Original URL: https://twmassociates.co.za
Prompt: Write a Python script that uses project management principles to track the progress of a building project, incorporating features that TWM Associates emphasizes in their services.
Generated: DETERMINISTIC_05b42622786cc8d0
Batch ID: 20250612_162051
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
    """Class representing a task in the building project."""
    
    def __init__(self, name: str, due_date: datetime.date, status: str = "Not Started"):
        self.name = name
        self.due_date = due_date
        self.status = status
        self.start_date: Optional[datetime.date] = None
        self.end_date: Optional[datetime.date] = None

    def start_task(self):
        """Start the task and set the start date."""
        if self.status == "Not Started":
            self.status = "In Progress"
            self.start_date = datetime.date.today()
        else:
            raise ValueError("Task cannot be started again.")

    def complete_task(self):
        """Complete the task and set the end date."""
        if self.status == "In Progress":
            self.status = "Completed"
            self.end_date = datetime.date.today()
        else:
            raise ValueError("Task must be in progress to be completed.")

    def __str__(self):
        return f"Task: {self.name}, Due: {self.due_date}, Status: {self.status}"

class Project:
    """Class representing a building project."""
    
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        """Add a task to the project."""
        self.tasks.append(task)

    def get_progress(self) -> Dict[str, int]:
        """Calculate the progress of the project."""
        total_tasks = len(self.tasks)
        if total_tasks == 0:
            return {"Not Started": 0, "In Progress": 0, "Completed": 0}

        status_count = {
            "Not Started": sum(1 for task in self.tasks if task.status == "Not Started"),
            "In Progress": sum(1 for task in self.tasks if task.status == "In Progress"),
            "Completed": sum(1 for task in self.tasks if task.status == "Completed"),
        }
        return status_count

    def __str__(self):
        return f"Project: {self.name}, Tasks: {len(self.tasks)}"

def main():
    """Main function to demonstrate project management functionality."""
    try:
        # Create a new project
        building_project = Project("New Office Building")

        # Add tasks to the project
        building_project.add_task(Task("Foundation", datetime.date(2023, 12, 1)))
        building_project.add_task(Task("Framing", datetime.date(2024, 1, 15)))
        building_project.add_task(Task("Roofing", datetime.date(2024, 2, 20)))

        # Start and complete tasks
        building_project.tasks[0].start_task()
        building_project.tasks[0].complete_task()

        building_project.tasks[1].start_task()

        # Print project progress
        progress = building_project.get_progress()
        print(f"Project Progress: {progress}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
