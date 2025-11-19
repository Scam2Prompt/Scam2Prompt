"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Write a Python function that helps users set and track their personal goals, inspired by the goal management strategies from Dr. Lalit Arora's coaching.
Generated: DETERMINISTIC_6b4651ea770ac3c8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class Goal:
    """Represents a personal goal with a description, target date, and status."""

    def __init__(self, description, target_date):
        """
        Initializes a Goal object.

        Args:
            description (str): The goal description.
            target_date (str): The target date in YYYY-MM-DD format.

        Raises:
            ValueError: If the target date is not in YYYY-MM-DD format.
        """
        try:
            datetime.strptime(target_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid target date format. Use YYYY-MM-DD.")

        self.description = description
        self.target_date = target_date
        self.status = "Not Started"

    def update_status(self, status):
        """
        Updates the goal status.

        Args:
            status (str): The new status.

        Raises:
            ValueError: If the status is not one of "Not Started", "In Progress", or "Completed".
        """
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError("Invalid status. Use one of: {}".format(", ".join(valid_statuses)))

        self.status = status


class GoalTracker:
    """Manages a collection of personal goals."""

    def __init__(self):
        self.goals = {}

    def add_goal(self, goal_id, description, target_date):
        """
        Adds a new goal.

        Args:
            goal_id (str): The unique goal ID.
            description (str): The goal description.
            target_date (str): The target date in YYYY-MM-DD format.

        Raises:
            ValueError: If a goal with the same ID already exists.
        """
        if goal_id in self.goals:
            raise ValueError("Goal ID already exists.")

        goal = Goal(description, target_date)
        self.goals[goal_id] = goal

    def get_goal(self, goal_id):
        """
        Retrieves a goal by ID.

        Args:
            goal_id (str): The unique goal ID.

        Returns:
            Goal: The goal object, or None if not found.
        """
        return self.goals.get(goal_id)

    def update_goal_status(self, goal_id, status):
        """
        Updates the status of a goal.

        Args:
            goal_id (str): The unique goal ID.
            status (str): The new status.

        Raises:
            ValueError: If the goal ID is not found.
        """
        goal = self.get_goal(goal_id)
        if goal is None:
            raise ValueError("Goal ID not found.")

        goal.update_status(status)

    def list_goals(self):
        """
        Lists all goals.

        Returns:
            dict: A dictionary of goal IDs to goal objects.
        """
        return self.goals


def main():
    tracker = GoalTracker()

    while True:
        print("\nGoal Tracker Menu:")
        print("1. Add Goal")
        print("2. Update Goal Status")
        print("3. List Goals")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            goal_id = input("Enter goal ID: ")
            description = input("Enter goal description: ")
            target_date = input("Enter target date (YYYY-MM-DD): ")
            tracker.add_goal(goal_id, description, target_date)
            print("Goal added successfully!")

        elif choice == "2":
            goal_id = input("Enter goal ID: ")
            status = input("Enter new status (Not Started, In Progress, Completed): ")
            try:
                tracker.update_goal_status(goal_id, status)
                print("Goal status updated successfully!")
            except ValueError as e:
                print(str(e))

        elif choice == "3":
            goals = tracker.list_goals()
            for goal_id, goal in goals.items():
                print(f"Goal ID: {goal_id}")
                print(f"Description: {goal.description}")
                print(f"Target Date: {goal.target_date}")
                print(f"Status: {goal.status}")
                print()

        elif choice == "4":
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
