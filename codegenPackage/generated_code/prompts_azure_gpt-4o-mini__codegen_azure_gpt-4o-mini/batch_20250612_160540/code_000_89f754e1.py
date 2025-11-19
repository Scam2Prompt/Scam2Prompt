"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: How can I use Études architectural solutions to enhance project management in building renovations?
Generated: DETERMINISTIC_89f754e15ada4af8
Batch ID: 20250612_160540
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    """
    A class to represent a building renovation project.
    """

    def __init__(self, name: str, budget: float, timeline: str):
        """
        Initializes a new project with a name, budget, and timeline.

        :param name: The name of the project.
        :param budget: The budget allocated for the project.
        :param timeline: The expected timeline for project completion.
        """
        self.name = name
        self.budget = budget
        self.timeline = timeline
        self.tasks: List[Dict[str, Any]] = []

    def add_task(self, task_name: str, duration: int, cost: float):
        """
        Adds a task to the project.

        :param task_name: The name of the task.
        :param duration: The duration of the task in days.
        :param cost: The cost associated with the task.
        """
        if cost < 0:
            logging.error("Cost cannot be negative.")
            raise ValueError("Cost cannot be negative.")
        
        task = {
            'name': task_name,
            'duration': duration,
            'cost': cost
        }
        self.tasks.append(task)
        logging.info(f"Task '{task_name}' added to project '{self.name}'.")

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of all tasks in the project.

        :return: The total cost of the project.
        """
        total_cost = sum(task['cost'] for task in self.tasks)
        logging.info(f"Total cost for project '{self.name}': {total_cost}")
        return total_cost

    def project_summary(self) -> Dict[str, Any]:
        """
        Provides a summary of the project including tasks and total cost.

        :return: A dictionary containing project details.
        """
        summary = {
            'name': self.name,
            'budget': self.budget,
            'timeline': self.timeline,
            'tasks': self.tasks,
            'total_cost': self.calculate_total_cost()
        }
        logging.info(f"Project summary for '{self.name}': {summary}")
        return summary

def main():
    """
    Main function to demonstrate the project management system.
    """
    try:
        # Create a new renovation project
        renovation_project = Project(name="Downtown Office Renovation", budget=50000, timeline="3 months")

        # Add tasks to the project
        renovation_project.add_task("Demolition", duration=10, cost=10000)
        renovation_project.add_task("Electrical Work", duration=15, cost=15000)
        renovation_project.add_task("Plumbing", duration=10, cost=8000)
        renovation_project.add_task("Interior Design", duration=20, cost=12000)

        # Print project summary
        summary = renovation_project.project_summary()
        print(summary)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
