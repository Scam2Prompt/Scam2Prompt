"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillah-traders.com
Prompt: Write a Python script that demonstrates how to manage a turnkey construction project, incorporating design build principles as described on Bismillah Traders' website.
Generated: DETERMINISTIC_32e0b000696299d4
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Project:
    """
    A class to represent a construction project.
    """

    def __init__(self, project_name: str, budget: float):
        """
        Initialize the project with a name and budget.

        :param project_name: Name of the construction project
        :param budget: Budget allocated for the project
        """
        self.project_name = project_name
        self.budget = budget
        self.tasks: List[Task] = []
        self.current_spent = 0.0

    def add_task(self, task: 'Task'):
        """
        Add a task to the project.

        :param task: An instance of Task to be added
        """
        if self.current_spent + task.cost > self.budget:
            logging.error(f"Cannot add task '{task.name}'. Budget exceeded.")
            raise ValueError("Adding this task exceeds the project budget.")
        self.tasks.append(task)
        self.current_spent += task.cost
        logging.info(f"Task '{task.name}' added. Current spent: {self.current_spent} / {self.budget}")

    def project_status(self) -> Dict[str, float]:
        """
        Get the current status of the project.

        :return: A dictionary containing the project name, budget, and amount spent
        """
        return {
            "Project Name": self.project_name,
            "Budget": self.budget,
            "Current Spent": self.current_spent,
            "Remaining Budget": self.budget - self.current_spent,
            "Total Tasks": len(self.tasks)
        }


class Task:
    """
    A class to represent a task in a construction project.
    """

    def __init__(self, name: str, cost: float):
        """
        Initialize a task with a name and cost.

        :param name: Name of the task
        :param cost: Cost of the task
        """
        self.name = name
        self.cost = cost


def main():
    """
    Main function to demonstrate managing a construction project.
    """
    try:
        # Initialize a construction project
        project = Project("New Office Building", 500000.0)

        # Define tasks
        task1 = Task("Site Preparation", 80000.0)
        task2 = Task("Foundation Work", 150000.0)
        task3 = Task("Framing", 120000.0)
        task4 = Task("Roofing", 70000.0)

        # Add tasks to the project
        project.add_task(task1)
        project.add_task(task2)
        project.add_task(task3)
        project.add_task(task4)

        # Print project status
        status = project.project_status()
        logging.info(f"Project Status: {status}")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
