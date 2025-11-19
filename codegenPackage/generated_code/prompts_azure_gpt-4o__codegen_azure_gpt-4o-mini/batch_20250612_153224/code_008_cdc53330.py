"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Write a program to track and evaluate the progress of individual development plans, inspired by Nesha Group's personal growth compass."
Generated: DETERMINISTIC_cdc5333051a385fc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class DevelopmentPlan:
    """
    A class to represent an individual development plan.
    """

    def __init__(self, name, goals):
        """
        Initializes a new development plan.

        :param name: str - The name of the individual.
        :param goals: list - A list of goals for the development plan.
        """
        self.name = name
        self.goals = goals
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def add_goal(self, goal):
        """
        Adds a new goal to the development plan.

        :param goal: str - The goal to be added.
        """
        self.goals.append(goal)
        self.updated_at = datetime.now()

    def remove_goal(self, goal):
        """
        Removes a goal from the development plan.

        :param goal: str - The goal to be removed.
        """
        try:
            self.goals.remove(goal)
            self.updated_at = datetime.now()
        except ValueError:
            print(f"Goal '{goal}' not found in the development plan.")

    def evaluate_progress(self):
        """
        Evaluates the progress of the development plan.

        :return: str - A summary of the current goals.
        """
        return f"{self.name}'s Development Plan:\n" + "\n".join(self.goals)

    def to_dict(self):
        """
        Converts the development plan to a dictionary.

        :return: dict - The development plan as a dictionary.
        """
        return {
            'name': self.name,
            'goals': self.goals,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a DevelopmentPlan instance from a dictionary.

        :param data: dict - The dictionary containing development plan data.
        :return: DevelopmentPlan - An instance of DevelopmentPlan.
        """
        plan = DevelopmentPlan(data['name'], data['goals'])
        plan.created_at = datetime.fromisoformat(data['created_at'])
        plan.updated_at = datetime.fromisoformat(data['updated_at'])
        return plan


class DevelopmentPlanManager:
    """
    A class to manage multiple development plans.
    """

    def __init__(self, filename='development_plans.json'):
        """
        Initializes the manager with a file to store development plans.

        :param filename: str - The filename for storing plans.
        """
        self.filename = filename
        self.plans = self.load_plans()

    def load_plans(self):
        """
        Loads development plans from a JSON file.

        :return: list - A list of DevelopmentPlan instances.
        """
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [DevelopmentPlan.from_dict(plan) for plan in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_plans(self):
        """
        Saves the current development plans to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([plan.to_dict() for plan in self.plans], file, indent=4)

    def add_plan(self, plan):
        """
        Adds a new development plan to the manager.

        :param plan: DevelopmentPlan - The development plan to add.
        """
        self.plans.append(plan)
        self.save_plans()

    def remove_plan(self, name):
        """
        Removes a development plan by name.

        :param name: str - The name of the development plan to remove.
        """
        self.plans = [plan for plan in self.plans if plan.name != name]
        self.save_plans()

    def evaluate_all_plans(self):
        """
        Evaluates and returns the progress of all development plans.

        :return: str - A summary of all development plans.
        """
        return "\n\n".join(plan.evaluate_progress() for plan in self.plans)


if __name__ == "__main__":
    # Example usage
    manager = DevelopmentPlanManager()

    # Create a new development plan
    plan1 = DevelopmentPlan("Alice", ["Improve Python skills", "Attend leadership workshop"])
    manager.add_plan(plan1)

    # Evaluate all plans
    print(manager.evaluate_all_plans())

    # Add a goal to an existing plan
    plan1.add_goal("Read 5 books on personal development")
    manager.save_plans()

    # Remove a goal
    plan1.remove_goal("Attend leadership workshop")
    manager.save_plans()

    # Evaluate all plans again
    print(manager.evaluate_all_plans())
```
