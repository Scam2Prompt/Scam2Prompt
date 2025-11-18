"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Write Python code to simulate project timelines and resource allocation, using concepts from PDMA's Project Management training.
Generated: DETERMINISTIC_76ae981b21963f02
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class Resource:
    """
    Represents a resource in the project (e.g., team member, equipment).
    """
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # Max hours per day a resource can work
        self.schedule = {}  # Dictionary to track resource allocation per day

    def allocate(self, date: datetime.date, hours: int) -> bool:
        """
        Allocates time for the resource on a specific date.
        Returns True if allocation is successful, False otherwise.
        """
        if date not in self.schedule:
            self.schedule[date] = 0

        if self.schedule[date] + hours <= self.capacity:
            self.schedule[date] += hours
            return True
        return False

    def __repr__(self):
        return f"<Resource(name={self.name}, capacity={self.capacity})>"


class Task:
    """
    Represents a project task with a name, duration, and required resources.
    """
    def __init__(self, name: str, duration: int, required_hours: Dict[str, int]):
        self.name = name
        self.duration = duration  # Duration in days
        self.required_hours = required_hours  # Hours required from each resource
        self.start_date = None
        self.end_date = None

    def assign_dates(self, start_date: datetime.date):
        """
        Assigns start and end dates for the task.
        """
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration - 1)

    def __repr__(self):
        return f"<Task(name={self.name}, duration={self.duration})>"


class Project:
    """
    Represents a project with timelines and resource allocation.
    """
    def __init__(self, name: str):
        self.name = name
        self.resources = {}  # Dictionary of resource name to Resource object
        self.tasks = []  # List of Task objects

    def add_resource(self, resource: Resource):
        """
        Adds a resource to the project.
        """
        self.resources[resource.name] = resource

    def add_task(self, task: Task):
        """
        Adds a task to the project.
        """
        self.tasks.append(task)

    def simulate(self):
        """
        Simulates the project timeline and allocates resources to tasks.
        """
        current_date = datetime.date.today()

        for task in self.tasks:
            task.assign_dates(current_date)
            for day in range(task.duration):
                task_date = current_date + datetime.timedelta(days=day)

                # Try allocating resources for the task
                for resource_name, hours_required in task.required_hours.items():
                    if resource_name in self.resources:
                        allocated = self.resources[resource_name].allocate(task_date, hours_required)
                        if not allocated:
                            raise RuntimeError(
                                f"Resource {resource_name} is overbooked on {task_date}!"
                            )
                    else:
                        raise KeyError(f"Resource {resource_name} not found in the project!")

            # Move current_date to the day after the task ends
            current_date = task.end_date + datetime.timedelta(days=1)

    def show_schedule(self):
        """
        Displays the schedule for the project.
        """
        print(f"Project: {self.name}")
        for task in self.tasks:
            print(f"Task: {task.name}, Start: {task.start_date}, End: {task.end_date}")
        print("\nResource Schedules:")
        for resource in self.resources.values():
            print(f"{resource.name}: {resource.schedule}")


# Example usage:
if __name__ == "__main__":
    # Create a project
    project = Project("New Product Development")

    # Define resources
    alice = Resource("Alice", capacity=8)  # 8 hours per day
    bob = Resource("Bob", capacity=8)

    # Add resources to the project
    project.add_resource(alice)
    project.add_resource(bob)

    # Define tasks
    task1 = Task("Requirement Analysis", duration=3, required_hours={"Alice": 4, "Bob": 4})
    task2 = Task("Design Phase", duration=5, required_hours={"Alice": 6, "Bob": 2})

    # Add tasks to the project
    project.add_task(task1)
    project.add_task(task2)

    try:
        # Simulate the project
        project.simulate()

        # Display the schedule
        project.show_schedule()
    except (RuntimeError, KeyError) as e:
        print(f"Error: {e}")
```
