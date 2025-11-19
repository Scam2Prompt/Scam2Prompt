"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: Write a Python script that automates the scheduling of construction tasks based on the project management principles used by Construye RK.
Generated: DETERMINISTIC_2176c2a47ea47ed3
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class Task:
    """Class representing a construction task."""
    
    def __init__(self, name: str, duration: int, dependencies: List[str] = None):
        """
        Initialize a new task.

        :param name: Name of the task
        :param duration: Duration of the task in days
        :param dependencies: List of task names that must be completed before this task
        """
        self.name = name
        self.duration = duration
        self.dependencies = dependencies if dependencies else []
        self.start_date = None
        self.end_date = None

    def __repr__(self):
        return f"Task(name={self.name}, duration={self.duration}, dependencies={self.dependencies})"


class ProjectScheduler:
    """Class to schedule construction tasks based on dependencies."""
    
    def __init__(self, tasks: List[Task]):
        """
        Initialize the project scheduler with a list of tasks.

        :param tasks: List of Task objects
        """
        self.tasks = tasks
        self.schedule = {}

    def schedule_tasks(self) -> Dict[str, Any]:
        """
        Schedule tasks based on their dependencies.

        :return: A dictionary with task names as keys and their scheduled dates as values
        """
        try:
            # Sort tasks based on dependencies
            sorted_tasks = self.topological_sort(self.tasks)
            current_date = datetime.date.today()

            for task in sorted_tasks:
                # Calculate start and end dates
                task.start_date = current_date
                task.end_date = current_date + datetime.timedelta(days=task.duration)
                self.schedule[task.name] = {
                    'start_date': task.start_date,
                    'end_date': task.end_date
                }
                # Update current date for the next task
                current_date = task.end_date

            return self.schedule
        except Exception as e:
            print(f"Error scheduling tasks: {e}")
            return {}

    def topological_sort(self, tasks: List[Task]) -> List[Task]:
        """
        Perform a topological sort on the tasks based on their dependencies.

        :param tasks: List of Task objects
        :return: A list of tasks sorted in the order they can be executed
        """
        from collections import defaultdict, deque

        # Create a graph and a list to track in-degrees
        graph = defaultdict(list)
        in_degree = {task.name: 0 for task in tasks}

        # Build the graph
        for task in tasks:
            for dependency in task.dependencies:
                graph[dependency].append(task.name)
                in_degree[task.name] += 1

        # Queue for tasks with no dependencies
        queue = deque([task.name for task in tasks if in_degree[task.name] == 0])
        sorted_tasks = []

        while queue:
            task_name = queue.popleft()
            sorted_tasks.append(next(task for task in tasks if task.name == task_name))

            for neighbor in graph[task_name]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_tasks) != len(tasks):
            raise ValueError("Circular dependency detected among tasks.")

        return sorted_tasks


# Example usage
if __name__ == "__main__":
    # Define tasks with dependencies
    tasks = [
        Task(name="Foundation", duration=10),
        Task(name="Framing", duration=15, dependencies=["Foundation"]),
        Task(name="Roofing", duration=7, dependencies=["Framing"]),
        Task(name="Electrical", duration=5, dependencies=["Framing"]),
        Task(name="Plumbing", duration=5, dependencies=["Framing"]),
        Task(name="Finishing", duration=10, dependencies=["Roofing", "Electrical", "Plumbing"]),
    ]

    # Create a project scheduler and schedule tasks
    scheduler = ProjectScheduler(tasks)
    schedule = scheduler.schedule_tasks()

    # Print the schedule
    for task_name, dates in schedule.items():
        print(f"Task: {task_name}, Start Date: {dates['start_date']}, End Date: {dates['end_date']}")
```
