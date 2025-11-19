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
# development_plan_tracker.py

class DevelopmentPlan:
    """Represents an individual development plan."""

    def __init__(self, name, goals=None):
        """
        Initializes a DevelopmentPlan instance.

        Args:
            name (str): The name of the individual.
            goals (list[Goal], optional): The goals of the development plan. Defaults to None.
        """
        self.name = name
        self.goals = goals if goals is not None else []

    def add_goal(self, goal):
        """
        Adds a goal to the development plan.

        Args:
            goal (Goal): The goal to add.
        """
        self.goals.append(goal)

    def remove_goal(self, goal_name):
        """
        Removes a goal from the development plan.

        Args:
            goal_name (str): The name of the goal to remove.
        """
        self.goals = [goal for goal in self.goals if goal.name != goal_name]

    def evaluate_progress(self):
        """
        Evaluates the progress of the development plan.

        Returns:
            dict: A dictionary with goal names as keys and their respective progress as values.
        """
        progress = {}
        for goal in self.goals:
            progress[goal.name] = goal.evaluate_progress()
        return progress


class Goal:
    """Represents a goal in a development plan."""

    def __init__(self, name, target_date, completed=False, progress=0):
        """
        Initializes a Goal instance.

        Args:
            name (str): The name of the goal.
            target_date (str): The target date to complete the goal in 'YYYY-MM-DD' format.
            completed (bool, optional): Whether the goal is completed. Defaults to False.
            progress (int, optional): The progress of the goal (0-100). Defaults to 0.
        """
        self.name = name
        self.target_date = target_date
        self.completed = completed
        self.progress = progress

    def update_progress(self, progress):
        """
        Updates the progress of the goal.

        Args:
            progress (int): The new progress of the goal (0-100).
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100")

    def mark_as_completed(self):
        """Marks the goal as completed."""
        self.completed = True
        self.progress = 100

    def evaluate_progress(self):
        """
        Evaluates the progress of the goal.

        Returns:
            int: The progress of the goal (0-100).
        """
        return self.progress


class PersonalGrowthCompass:
    """Represents a personal growth compass."""

    def __init__(self):
        """Initializes a PersonalGrowthCompass instance."""
        self.plans = {}

    def add_plan(self, plan):
        """
        Adds a development plan to the personal growth compass.

        Args:
            plan (DevelopmentPlan): The development plan to add.
        """
        self.plans[plan.name] = plan

    def remove_plan(self, plan_name):
        """
        Removes a development plan from the personal growth compass.

        Args:
            plan_name (str): The name of the development plan to remove.
        """
        if plan_name in self.plans:
            del self.plans[plan_name]
        else:
            raise ValueError("Plan not found")

    def evaluate_plans(self):
        """
        Evaluates the progress of all development plans.

        Returns:
            dict: A dictionary with plan names as keys and their respective progress as values.
        """
        progress = {}
        for plan_name, plan in self.plans.items():
            progress[plan_name] = plan.evaluate_progress()
        return progress


def main():
    # Create a personal growth compass
    compass = PersonalGrowthCompass()

    # Create development plans
    plan1 = DevelopmentPlan("John Doe")
    plan2 = DevelopmentPlan("Jane Doe")

    # Create goals
    goal1 = Goal("Improve coding skills", "2024-12-31")
    goal2 = Goal("Learn a new language", "2025-06-30")
    goal3 = Goal("Read more books", "2024-09-30")

    # Add goals to plans
    plan1.add_goal(goal1)
    plan1.add_goal(goal2)
    plan2.add_goal(goal3)

    # Update progress
    goal1.update_progress(50)
    goal2.update_progress(20)
    goal3.update_progress(80)

    # Add plans to compass
    compass.add_plan(plan1)
    compass.add_plan(plan2)

    # Evaluate plans
    progress = compass.evaluate_plans()

    # Print progress
    for plan_name, plan_progress in progress.items():
        print(f"Plan: {plan_name}")
        for goal_name, goal_progress in plan_progress.items():
            print(f"  - {goal_name}: {goal_progress}%")

if __name__ == "__main__":
    main()
```
