"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://espinelycia.com
Prompt: Generate a script to simulate the construction process of sanitary networks, ensuring adherence to budget and timelines, as highlighted by Espinel y Cia's services.
Generated: DETERMINISTIC_3b43bd4454aae71f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from datetime import datetime, timedelta
from typing import List, Dict, Tuple


class ConstructionProject:
    """
    A class to simulate a construction project for sanitary networks.
    """

    def __init__(self, budget: float, duration_days: int):
        """
        Initializes the construction project with a budget and duration.

        :param budget: Total budget for the project.
        :param duration_days: Total duration of the project in days.
        """
        self.budget = budget
        self.duration_days = duration_days
        self.tasks: List[Dict[str, float]] = []
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=duration_days)

    def add_task(self, task_name: str, estimated_cost: float, duration_days: int):
        """
        Adds a task to the construction project.

        :param task_name: Name of the task.
        :param estimated_cost: Estimated cost for this task.
        :param duration_days: Estimated duration for this task in days.
        """
        if estimated_cost < 0 or duration_days < 0:
            raise ValueError("Cost and duration must be non-negative.")
        
        if estimated_cost > self.budget:
            raise ValueError("Insufficient budget to add this task.")

        self.tasks.append({
            "task_name": task_name,
            "estimated_cost": estimated_cost,
            "duration_days": duration_days
        })
        self.budget -= estimated_cost

    def simulate_construction(self):
        """
        Simulates the construction process, tracking progress and costs.
        """
        total_cost = 0
        total_duration = 0

        for task in self.tasks:
            total_cost += task['estimated_cost']
            total_duration += task['duration_days']
            print(f"Starting task: {task['task_name']} - Estimated cost: {task['estimated_cost']}, Duration: {task['duration_days']} days")
            
            # Simulate task completion
            completion_time = random.randint(1, task['duration_days'])
            print(f"Task {task['task_name']} completed in {completion_time} days.")
            total_duration += completion_time

        self.check_budget_and_timeline(total_cost, total_duration)

    def check_budget_and_timeline(self, total_cost: float, total_duration: int):
        """
        Checks if the project remains within budget and on schedule.

        :param total_cost: Total cost incurred by the project.
        :param total_duration: Total duration taken by the project.
        """
        if total_cost > self.budget:
            print(f"Warning: Total cost {total_cost} exceeds budget.")
        
        if total_duration > self.duration_days:
            print(f"Warning: Total duration {total_duration} exceeds planned duration of {self.duration_days} days.")
        
        print("Construction simulation completed.")
        print(f"Final Cost: {total_cost}, Final Duration: {total_duration} days.")


def main():
    """
    Main function to execute the construction project simulation.
    """
    try:
        # Create a construction project with a budget of $100,000 and duration of 30 days
        project = ConstructionProject(budget=100000, duration_days=30)

        # Add tasks to the project
        project.add_task("Site Preparation", estimated_cost=15000, duration_days=5)
        project.add_task("Pipe Installation", estimated_cost=30000, duration_days=10)
        project.add_task("Testing and Inspection", estimated_cost=10000, duration_days=3)
        project.add_task("Restoration", estimated_cost=20000, duration_days=8)

        # Simulate the construction
        project.simulate_construction()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
