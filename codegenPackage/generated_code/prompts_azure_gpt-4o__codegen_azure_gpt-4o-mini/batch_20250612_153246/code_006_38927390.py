"""
Generated Code Metadata:
========================
Original URL: https://jauconsulting.com
Prompt: Create a function to model and simulate the commissioning phase of an engineering project, using Jau Consulting's described workflow as a reference.
Generated: DETERMINISTIC_389273905cb415c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Any

class CommissioningPhase:
    """
    A class to model and simulate the commissioning phase of an engineering project.
    """

    def __init__(self, project_name: str):
        """
        Initializes the CommissioningPhase with a project name.

        :param project_name: The name of the engineering project.
        """
        self.project_name = project_name
        self.tasks: List[Dict[str, Any]] = []
        self.completed_tasks: List[Dict[str, Any]] = []

    def add_task(self, task_name: str, duration: int) -> None:
        """
        Adds a task to the commissioning phase.

        :param task_name: The name of the task to be added.
        :param duration: The estimated duration of the task in days.
        """
        task = {
            'name': task_name,
            'duration': duration,
            'status': 'pending'
        }
        self.tasks.append(task)

    def simulate_task(self, task: Dict[str, Any]) -> None:
        """
        Simulates the execution of a task.

        :param task: The task to be simulated.
        """
        # Simulate task completion with a random success or failure
        success = random.choice([True, False])
        if success:
            task['status'] = 'completed'
            self.completed_tasks.append(task)
        else:
            task['status'] = 'failed'

    def run_simulation(self) -> None:
        """
        Runs the simulation for all tasks in the commissioning phase.
        """
        for task in self.tasks:
            self.simulate_task(task)

    def report(self) -> None:
        """
        Generates a report of the commissioning phase, including task statuses.
        """
        print(f"Commissioning Phase Report for Project: {self.project_name}")
        print("Tasks Summary:")
        for task in self.tasks:
            print(f" - Task: {task['name']}, Duration: {task['duration']} days, Status: {task['status']}")

# Example usage
if __name__ == "__main__":
    try:
        commissioning = CommissioningPhase("New Engineering Project")
        commissioning.add_task("Initial Setup", 5)
        commissioning.add_task("System Testing", 10)
        commissioning.add_task("Final Review", 3)

        commissioning.run_simulation()
        commissioning.report()
    except Exception as e:
        print(f"An error occurred: {e}")
```
