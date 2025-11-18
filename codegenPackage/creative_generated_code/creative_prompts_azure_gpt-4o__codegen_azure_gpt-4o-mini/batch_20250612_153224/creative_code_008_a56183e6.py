"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Create a project plan template for IT project management that ensures timelines and budgets are met, inspired by ARP Group Corporation's methodology.
Generated: DETERMINISTIC_a56183e65b95474c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class ProjectPlan:
    """
    A class to represent a project plan for IT project management.
    Ensures timelines and budgets are tracked and managed effectively.
    """

    def __init__(self, project_name: str, start_date: str, end_date: str, budget: float):
        """
        Initializes the project plan with necessary parameters.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            end_date (str): The end date of the project in 'YYYY-MM-DD' format.
            budget (float): The total budget allocated for the project.

        Raises:
            ValueError: If the end_date is before the start_date.
            ValueError: If the budget is negative.
        """
        self.project_name = project_name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        self.budget = budget
        self.tasks: List[Dict[str, Any]] = []
        
        if self.end_date < self.start_date:
            raise ValueError("End date cannot be before start date.")
        if self.budget < 0:
            raise ValueError("Budget cannot be negative.")

    def add_task(self, task_name: str, assignee: str, duration_days: int, cost: float):
        """
        Adds a task to the project plan.

        Args:
            task_name (str): The name of the task.
            assignee (str): The person responsible for the task.
            duration_days (int): The duration for which the task is expected to take (in days).
            cost (float): The cost associated with the task.

        Raises:
            ValueError: If the cost exceeds the remaining budget.
        """
        remaining_budget = self.budget - self.get_total_cost()
        if cost > remaining_budget:
            raise ValueError("Task cost exceeds remaining budget.")
        
        task = {
            'task_name': task_name,
            'assignee': assignee,
            'duration_days': duration_days,
            'cost': cost,
            'status': 'Pending'
        }
        self.tasks.append(task)

    def get_total_cost(self) -> float:
        """
        Calculates the total cost of all tasks in the project plan.

        Returns:
            float: The total cost of the project tasks.
        """
        return sum(task['cost'] for task in self.tasks)

    def get_project_summary(self) -> Dict[str, Any]:
        """
        Summarizes the project information including budget status and task details.

        Returns:
            dict: A summary of the project plan.
        """
        return {
            'project_name': self.project_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'budget': self.budget,
            'total_cost': self.get_total_cost(),
            'remaining_budget': self.budget - self.get_total_cost(),
            'tasks': self.tasks
        }

# Example usage
if __name__ == "__main__":
    try:
        project = ProjectPlan("New IT System", "2023-10-01", "2024-01-01", 50000.00)
        project.add_task("Requirement Gathering", "Alice", 10, 5000.00)
        project.add_task("System Design", "Bob", 15, 10000.00)

        # Fetching project summary
        summary = project.get_project_summary()
        print(summary)
        
    except ValueError as e:
        print(f"Error: {e}")
```
