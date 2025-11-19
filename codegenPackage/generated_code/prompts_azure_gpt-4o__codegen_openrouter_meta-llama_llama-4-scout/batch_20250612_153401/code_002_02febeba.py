"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Generate code using a project management library (e.g., `ProjectLibre` or similar) to simulate the planning phase of a construction project, incorporating milestones and dependencies as described by INARO S.A.S.
Generated: DETERMINISTIC_02febebaac4b6c32
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta

class Task:
    """Represents a task in the project."""
    
    def __init__(self, id, name, start_date, end_date):
        """
        Initializes a Task object.

        Args:
            id (int): Unique task identifier.
            name (str): Task name.
            start_date (datetime): Task start date.
            end_date (datetime): Task end date.
        """
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.dependencies = []

    def add_dependency(self, task):
        """Adds a dependency to the task."""
        self.dependencies.append(task)


class Project:
    """Represents a construction project."""
    
    def __init__(self, name):
        """
        Initializes a Project object.

        Args:
            name (str): Project name.
        """
        self.name = name
        self.tasks = []
        self.milestones = []

    def add_task(self, task):
        """Adds a task to the project."""
        self.tasks.append(task)

    def add_milestone(self, milestone):
        """Adds a milestone to the project."""
        self.milestones.append(milestone)

    def simulate_planning_phase(self):
        """Simulates the planning phase of the construction project."""
        # Sort tasks by start date
        self.tasks.sort(key=lambda task: task.start_date)

        # Print project timeline
        print(f"Project: {self.name}")
        print("Tasks:")
        for task in self.tasks:
            print(f"  - {task.name} ({task.start_date} - {task.end_date})")

        # Print milestones
        print("\nMilestones:")
        for milestone in self.milestones:
            print(f"  - {milestone.name} ({milestone.end_date})")

        # Print task dependencies
        print("\nTask Dependencies:")
        for task in self.tasks:
            if task.dependencies:
                print(f"  - {task.name} depends on:")
                for dependency in task.dependencies:
                    print(f"    - {dependency.name}")


def main():
    try:
        # Create a project
        project = Project("Construction of a new building")

        # Create tasks
        task1 = Task(1, "Site preparation", datetime(2024, 9, 1), datetime(2024, 9, 15))
        task2 = Task(2, "Foundation work", datetime(2024, 9, 16), datetime(2024, 10, 15))
        task3 = Task(3, "Structural work", datetime(2024, 10, 16), datetime(2024, 11, 15))

        # Add task dependencies
        task2.add_dependency(task1)
        task3.add_dependency(task2)

        # Create milestones
        milestone1 = Task(4, "Completion of site preparation", datetime(2024, 9, 15), datetime(2024, 9, 15))
        milestone2 = Task(5, "Completion of foundation work", datetime(2024, 10, 15), datetime(2024, 10, 15))
        milestone3 = Task(6, "Completion of structural work", datetime(2024, 11, 15), datetime(2024, 11, 15))

        # Add tasks and milestones to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)
        project.add_milestone(milestone1)
        project.add_milestone(milestone2)
        project.add_milestone(milestone3)

        # Simulate planning phase
        project.simulate_planning_phase()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
