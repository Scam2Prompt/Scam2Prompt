"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neshagroup.ir
Prompt: "Write a program to track and evaluate the progress of individual development plans, inspired by Nesha Group's personal growth compass."
Generated: DETERMINISTIC_cdc5333051a385fc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DevelopmentPlan:
    """
    A class to represent an individual development plan (IDP).
    """

    def __init__(self, employee_name):
        """
        Initializes a new DevelopmentPlan instance.

        :param employee_name: Name of the employee for whom the plan is created.
        """
        self.employee_name = employee_name
        self.goals = []
        self.progress = {}

    def add_goal(self, goal):
        """
        Adds a new goal to the development plan.

        :param goal: A string representing the goal.
        """
        if not goal:
            raise ValueError("Goal cannot be empty.")
        self.goals.append(goal)
        self.progress[goal] = 0  # Initialize progress to 0%
        print(f"Goal '{goal}' added for {self.employee_name}.")

    def update_progress(self, goal, progress):
        """
        Updates the progress of a specific goal.

        :param goal: A string representing the goal to update.
        :param progress: An integer representing the new progress percentage (0-100).
        """
        if goal not in self.goals:
            raise ValueError(f"Goal '{goal}' not found in the development plan.")
        if not (0 <= progress <= 100):
            raise ValueError("Progress must be between 0 and 100.")

        self.progress[goal] = progress
        print(f"Progress for '{goal}' updated to {progress}%.")

    def evaluate_progress(self):
        """
        Evaluates and returns the overall progress of the development plan.

        :return: A float representing the average progress of all goals.
        """
        if not self.goals:
            return 0.0

        total_progress = sum(self.progress[goal] for goal in self.goals)
        average_progress = total_progress / len(self.goals)
        return average_progress


def main():
    """
    Main function to demonstrate the functionality of the DevelopmentPlan class.
    """
    try:
        # Create a development plan for an employee
        employee_plan = DevelopmentPlan("John Doe")

        # Add goals to the development plan
        employee_plan.add_goal("Improve communication skills")
        employee_plan.add_goal("Complete project management certification")

        # Update progress on goals
        employee_plan.update_progress("Improve communication skills", 50)
        employee_plan.update_progress("Complete project management certification", 20)

        # Evaluate overall progress
        overall_progress = employee_plan.evaluate_progress()
        print(f"Overall progress for {employee_plan.employee_name}: {overall_progress:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
