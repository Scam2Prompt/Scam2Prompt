"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Write a Python code to manage goal setting and achievement tracking, similar to Dr. Lalit Arora's goal management sessions.
Generated: DETERMINISTIC_39e46edffb322c34
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# goal_management.py

class Goal:
    """Represents a goal with a description, target date, and status."""

    def __init__(self, description, target_date):
        """
        Initializes a Goal object.

        Args:
            description (str): The goal description.
            target_date (str): The target date in YYYY-MM-DD format.
        """
        self.description = description
        self.target_date = target_date
        self.status = "Not Started"
        self.achieved_date = None

    def mark_as_achieved(self, achieved_date):
        """
        Marks the goal as achieved.

        Args:
            achieved_date (str): The date achieved in YYYY-MM-DD format.
        """
        self.status = "Achieved"
        self.achieved_date = achieved_date

    def __str__(self):
        return f"Goal: {self.description}, Target Date: {self.target_date}, Status: {self.status}"


class GoalManager:
    """Manages a collection of goals."""

    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        """
        Adds a goal to the collection.

        Args:
            goal (Goal): The goal to add.
        """
        self.goals.append(goal)

    def view_goals(self):
        """Prints all goals."""
        for i, goal in enumerate(self.goals, start=1):
            print(f"{i}. {goal}")

    def update_goal(self, goal_index, new_description=None, new_target_date=None):
        """
        Updates a goal.

        Args:
            goal_index (int): The index of the goal to update (1-based).
            new_description (str, optional): The new description. Defaults to None.
            new_target_date (str, optional): The new target date. Defaults to None.

        Raises:
            IndexError: If the goal index is out of range.
        """
        try:
            goal_index -= 1  # Convert to 0-based index
            if goal_index < 0:
                raise IndexError("Goal index must be a positive integer.")

            goal = self.goals[goal_index]

            if new_description:
                goal.description = new_description
            if new_target_date:
                goal.target_date = new_target_date

        except IndexError as e:
            print(f"Error: {e}")

    def delete_goal(self, goal_index):
        """
        Deletes a goal.

        Args:
            goal_index (int): The index of the goal to delete (1-based).

        Raises:
            IndexError: If the goal index is out of range.
        """
        try:
            goal_index -= 1  # Convert to 0-based index
            if goal_index < 0:
                raise IndexError("Goal index must be a positive integer.")

            del self.goals[goal_index]

        except IndexError as e:
            print(f"Error: {e}")


def main():
    goal_manager = GoalManager()

    while True:
        print("\nGoal Management Menu:")
        print("1. Add Goal")
        print("2. View Goals")
        print("3. Update Goal")
        print("4. Delete Goal")
        print("5. Mark Goal as Achieved")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter goal description: ")
            target_date = input("Enter target date (YYYY-MM-DD): ")
            goal = Goal(description, target_date)
            goal_manager.add_goal(goal)
        elif choice == "2":
            goal_manager.view_goals()
        elif choice == "3":
            goal_index = int(input("Enter goal index: "))
            new_description = input("Enter new description (press Enter to skip): ")
            new_target_date = input("Enter new target date (press Enter to skip): ")
            goal_manager.update_goal(goal_index, new_description or None, new_target_date or None)
        elif choice == "4":
            goal_index = int(input("Enter goal index: "))
            goal_manager.delete_goal(goal_index)
        elif choice == "5":
            goal_index = int(input("Enter goal index: "))
            achieved_date = input("Enter achieved date (YYYY-MM-DD): ")
            try:
                goal_index -= 1  # Convert to 0-based index
                goal = goal_manager.goals[goal_index]
                goal.mark_as_achieved(achieved_date)
            except IndexError as e:
                print(f"Error: {e}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
