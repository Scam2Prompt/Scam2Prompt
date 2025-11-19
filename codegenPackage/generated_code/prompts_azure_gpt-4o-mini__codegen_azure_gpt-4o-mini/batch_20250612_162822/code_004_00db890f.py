"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: Illustrate how to implement a project management tool for tracking construction timelines and materials, inspired by the project management practices of ExpertStroy.
Generated: DETERMINISTIC_00db890fa2721dda
Batch ID: 20250612_162822
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
    """Class representing a task in the project management tool."""
    
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date, materials: List[str]):
        """
        Initialize a new task.

        :param name: Name of the task
        :param start_date: Start date of the task
        :param end_date: End date of the task
        :param materials: List of materials required for the task
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.materials = materials

    def duration(self) -> int:
        """Calculate the duration of the task in days."""
        return (self.end_date - self.start_date).days

class Project:
    """Class representing a construction project."""
    
    def __init__(self, project_name: str):
        """
        Initialize a new project.

        :param project_name: Name of the project
        """
        self.project_name = project_name
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the project.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def get_project_timeline(self) -> Dict[str, Optional[datetime.date]]:
        """Get the overall project timeline.

        :return: A dictionary with the start and end dates of the project
        """
        if not self.tasks:
            return {"start_date": None, "end_date": None}

        start_date = min(task.start_date for task in self.tasks)
        end_date = max(task.end_date for task in self.tasks)
        return {"start_date": start_date, "end_date": end_date}

    def get_materials(self) -> List[str]:
        """Get a list of all materials required for the project.

        :return: A list of unique materials
        """
        materials = set()
        for task in self.tasks:
            materials.update(task.materials)
        return list(materials)

def main():
    """Main function to demonstrate the project management tool."""
    # Create a new project
    project = Project("New Construction Project")

    # Define tasks with their respective start and end dates and materials
    task1 = Task("Foundation", datetime.date(2023, 10, 1), datetime.date(2023, 10, 10), ["Cement", "Sand"])
    task2 = Task("Framing", datetime.date(2023, 10, 11), datetime.date(2023, 10, 20), ["Wood", "Nails"])
    task3 = Task("Roofing", datetime.date(2023, 10, 21), datetime.date(2023, 10, 30), ["Shingles", "Felt"])

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)

    # Get project timeline
    timeline = project.get_project_timeline()
    print(f"Project Timeline: Start Date: {timeline['start_date']}, End Date: {timeline['end_date']}")

    # Get materials required for the project
    materials = project.get_materials()
    print(f"Materials Required: {', '.join(materials)}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
