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
import datetime

class Goal:
    """
    A class to represent a goal with a title, description, deadline, and status.
    """
    def __init__(self, title, description, deadline):
        """
        Initialize a Goal object.

        :param title: Title of the goal
        :param description: Description of the goal
        :param deadline: Deadline for the goal (datetime object)
        """
        self.title = title
        self.description = description
        self.deadline = deadline
        self.status = "Pending"  # Status can be "Pending", "Completed", or "Overdue"

    def mark_completed(self):
        """
        Mark the goal as completed.
        """
        self.status = "Completed"

    def check_status(self):
        """
        Check and update the status of the goal based on the current date.
        """
        if self.status != "Completed" and datetime.datetime.now() > self.deadline:
            self.status = "Overdue"

    def __str__(self):
        """
        Return a string representation of the goal.
        """
        return f"Goal: {self.title}\nDescription: {self.description}\nDeadline: {self.deadline}\nStatus: {self.status}"


class GoalManager:
    """
    A class to manage multiple goals.
    """
    def __init__(self):
        """
        Initialize a GoalManager object.
        """
        self.goals = []

    def add_goal(self, title, description, deadline):
        """
        Add a new goal to the manager.

        :param title: Title of the goal
        :param description: Description of the goal
        :param deadline: Deadline for the goal (datetime object)
        """
        try:
            if not isinstance(deadline, datetime.datetime):
                raise ValueError("Deadline must be a datetime object.")
            new_goal = Goal(title, description, deadline)
            self.goals.append(new_goal)
            print(f"Goal '{title}' added successfully.")
        except Exception as e:
            print(f"Error adding goal: {e}")

    def list_goals(self):
        """
        List all goals with their details.
        """
        if not self.goals:
            print("No goals found.")
        else:
            for idx, goal in enumerate(self.goals, start=1):
                print(f"\nGoal {idx}:\n{goal}")

    def mark_goal_completed(self, title):
        """
        Mark a goal as completed by its title.

        :param title: Title of the goal to mark as completed
        """
        for goal in self.goals:
            if goal.title == title:
                goal.mark_completed()
                print(f"Goal '{title}' marked as completed.")
                return
        print(f"Goal '{title}' not found.")

    def check_all_statuses(self):
        """
        Check and update the status of all goals.
        """
        for goal in self.goals:
            goal.check_status()

    def remove_goal(self, title):
        """
        Remove a goal by its title.

        :param title: Title of the goal to remove
        """
        for goal in self.goals:
            if goal.title == title:
                self.goals.remove(goal)
                print(f"Goal '{title}' removed successfully.")
                return
        print(f"Goal '{title}' not found.")


# Example usage
if __name__ == "__main__":
    manager = GoalManager()

    # Adding goals
    manager.add_goal("Learn Python", "Complete Python tutorials", datetime.datetime(2023, 12, 31))
    manager.add_goal("Fitness", "Exercise daily for 30 minutes", datetime.datetime(2023, 11, 30))

    # Listing goals
    manager.list_goals()

    # Marking a goal as completed
    manager.mark_goal_completed("Learn Python")

    # Checking statuses
    manager.check_all_statuses()

    # Listing goals again to see updated statuses
    manager.list_goals()

    # Removing a goal
    manager.remove_goal("Fitness")

    # Listing goals after removal
    manager.list_goals()
```
