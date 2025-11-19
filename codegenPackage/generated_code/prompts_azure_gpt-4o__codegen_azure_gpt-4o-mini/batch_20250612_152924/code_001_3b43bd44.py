"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: Generate a script to simulate the construction process of sanitary networks, ensuring adherence to budget and timelines, as highlighted by Espinel y Cia's services.
Generated: DETERMINISTIC_3b43bd4454aae71f
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from datetime import datetime, timedelta

class SanitaryNetworkConstruction:
    def __init__(self, budget, timeline_days):
        """
        Initialize the construction simulation with a budget and timeline.

        :param budget: Total budget allocated for the construction.
        :param timeline_days: Total number of days allocated for the construction.
        """
        self.budget = budget
        self.timeline = timedelta(days=timeline_days)
        self.start_date = datetime.now()
        self.end_date = self.start_date + self.timeline
        self.costs = []
        self.completed_tasks = []

    def simulate_task(self, task_name, task_cost, task_duration):
        """
        Simulate the execution of a construction task.

        :param task_name: Name of the task to be simulated.
        :param task_cost: Cost associated with the task.
        :param task_duration: Duration of the task in days.
        :return: None
        """
        if self.budget < task_cost:
            raise ValueError(f"Insufficient budget for task '{task_name}'. Required: {task_cost}, Available: {self.budget}")

        if datetime.now() + timedelta(days=task_duration) > self.end_date:
            raise ValueError(f"Task '{task_name}' cannot be completed within the timeline. Required: {task_duration} days.")

        # Simulate task execution
        print(f"Starting task: {task_name} (Cost: {task_cost}, Duration: {task_duration} days)")
        time.sleep(1)  # Simulate time taken for the task
        self.budget -= task_cost
        self.costs.append(task_cost)
        self.completed_tasks.append(task_name)
        print(f"Completed task: {task_name}. Remaining budget: {self.budget}")

    def run_simulation(self):
        """
        Run the construction simulation with predefined tasks.

        :return: None
        """
        tasks = [
            {"name": "Excavation", "cost": 5000, "duration": 5},
            {"name": "Pipe Installation", "cost": 7000, "duration": 10},
            {"name": "Backfilling", "cost": 3000, "duration": 3},
            {"name": "Testing and Inspection", "cost": 2000, "duration": 2},
        ]

        for task in tasks:
            try:
                self.simulate_task(task["name"], task["cost"], task["duration"])
            except ValueError as e:
                print(f"Error: {e}")
                break

        self.final_report()

    def final_report(self):
        """
        Generate a final report of the construction simulation.

        :return: None
        """
        print("\n--- Final Report ---")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Total Budget: {self.budget + sum(self.costs)}")
        print(f"Remaining Budget: {self.budget}")
        print(f"Completed Tasks: {', '.join(self.completed_tasks)}")
        print(f"Total Costs: {sum(self.costs)}")
        print("--------------------")

if __name__ == "__main__":
    # Example usage
    try:
        construction_simulation = SanitaryNetworkConstruction(budget=20000, timeline_days=30)
        construction_simulation.run_simulation()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
