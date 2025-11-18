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
import datetime

class PersonalDevelopmentPlan:
    """
    A class to represent and track the progress of an individual's development plan.
    Inspired by Nesha Group's personal growth compass.
    """

    def __init__(self, name, goals):
        """
        Constructor to initialize the development plan.

        Args:
        - name (str): Name of the individual.
        - goals (list): List of goals in the format {"description": str, "target_date": str, "status": str}.
        """
        self.name = name
        self.goals = goals
        self.start_date = datetime.date.today()

    def add_goal(self, description, target_date):
        """
        Add a new goal to the plan.

        Args:
        - description (str): Description of the goal.
        - target_date (str): Target completion date in 'YYYY-MM-DD' format.

        Raises:
        - ValueError: If the target date is invalid or in the past.
        """
        try:
            target_date_obj = datetime.datetime.strptime(target_date, '%Y-%m-%d').date()
            if target_date_obj < datetime.date.today():
                raise ValueError("Target date cannot be in the past.")
            self.goals.append({"description": description, "target_date": target_date, "status": "Not Started"})
        except ValueError as e:
            print(f"Error adding goal: {str(e)}")

    def update_goal_status(self, description, status):
        """
        Update the status of a specific goal.

        Args:
        - description (str): Description of the goal to be updated.
        - status (str): New status for the goal (e.g., "In Progress", "Completed").

        Raises:
        - ValueError: If the goal is not found.
        """
        for goal in self.goals:
            if goal["description"] == description:
                goal["status"] = status
                return
        raise ValueError(f"Goal with description '{description}' not found.")

    def evaluate_progress(self):
        """
        Evaluate and print the progress of all goals.

        Prints:
        - List of goals with their status and whether the target date has been exceeded.
        """
        print(f"Progress Report for {self.name}:")
        for goal in self.goals:
            target_date_obj = datetime.datetime.strptime(goal["target_date"], '%Y-%m-%d').date()
            overdue = "Overdue" if target_date_obj < datetime.date.today() and goal["status"] != "Completed" else "On Track"
            print(f"Goal: {goal['description']}, Status: {goal['status']}, Due: {goal['target_date']} ({overdue})")

    def remove_goal(self, description):
        """
        Remove a specific goal from the plan.

        Args:
        - description (str): Description of the goal to be removed.

        Raises:
        - ValueError: If the goal is not found.
        """
        for goal in self.goals:
            if goal["description"] == description:
                self.goals.remove(goal)
                print(f"Goal '{description}' removed successfully.")
                return
        raise ValueError(f"Goal with description '{description}' not found.")


# Example usage:
if __name__ == "__main__":
    # Initialize a development plan
    plan = PersonalDevelopmentPlan("John Doe", [
        {"description": "Learn Python", "target_date": "2023-12-31", "status": "In Progress"},
        {"description": "Read 10 books", "target_date": "2024-06-30", "status": "Not Started"}
    ])

    # Add a new goal
    plan.add_goal("Exercise regularly", "2024-01-01")

    # Update the status of a goal
    try:
        plan.update_goal_status("Learn Python", "Completed")
    except ValueError as e:
        print(e)

    # Evaluate progress
    plan.evaluate_progress()

    # Remove a goal
    try:
        plan.remove_goal("Read 10 books")
    except ValueError as e:
        print(e)

    # Evaluate progress after changes
    plan.evaluate_progress()
```
