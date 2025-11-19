"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lalitarora.in
Prompt: Write a Python function that helps users set and track their personal goals, inspired by the goal management strategies from Dr. Lalit Arora's coaching.
Generated: DETERMINISTIC_6b4651ea770ac3c8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class Goal:
    """Class to represent a personal goal."""

    def __init__(self, title, description, target_date):
        """
        Initializes a new Goal instance.

        Args:
            title (str): The title of the goal.
            description (str): A detailed description of the goal.
            target_date (str): The target date for achieving the goal in 'YYYY-MM-DD' format.
        """
        self.title = title
        self.description = description
        self.target_date = datetime.strptime(target_date, '%Y-%m-%d')
        self.creation_date = datetime.now()
        self.completed = False

    def complete_goal(self):
        """Marks the goal as completed."""
        self.completed = True

    def __repr__(self):
        """Returns a string representation of the Goal instance."""
        return (f"Goal(title={self.title}, description={self.description}, "
                f"target_date={self.target_date.date()}, completed={self.completed})")


class GoalTracker:
    """Class to manage a collection of personal goals."""

    def __init__(self, filename='goals.json'):
        """
        Initializes a new GoalTracker instance.

        Args:
            filename (str): The filename to store goals data.
        """
        self.goals = []
        self.filename = filename
        self.load_goals()

    def add_goal(self, title, description, target_date):
        """
        Adds a new goal to the tracker.

        Args:
            title (str): The title of the goal.
            description (str): A detailed description of the goal.
            target_date (str): The target date for achieving the goal.

        Raises:
            ValueError: If the target date is in the past.
        """
        if datetime.strptime(target_date, '%Y-%m-%d') < datetime.now():
            raise ValueError("Target date must be in the future.")
        
        new_goal = Goal(title, description, target_date)
        self.goals.append(new_goal)
        self.save_goals()

    def complete_goal(self, title):
        """
        Marks a goal as completed.

        Args:
            title (str): The title of the goal to mark as completed.

        Raises:
            ValueError: If the goal with the given title does not exist.
        """
        for goal in self.goals:
            if goal.title == title and not goal.completed:
                goal.complete_goal()
                self.save_goals()
                return
        raise ValueError("Goal not found or already completed.")

    def save_goals(self):
        """Saves the current goals to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([goal.__dict__ for goal in self.goals], file)

    def load_goals(self):
        """Loads goals from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                goals_data = json.load(file)
                self.goals = [Goal(**goal) for goal in goals_data]
        except FileNotFoundError:
            # If the file does not exist, start with an empty goal list
            self.goals = []
        except json.JSONDecodeError:
            # If the file is corrupted, reset the goal list
            self.goals = []

    def get_goals(self):
        """Returns a list of all goals."""
        return self.goals


if __name__ == "__main__":
    tracker = GoalTracker()

    # Example usage
    try:
        tracker.add_goal("Run a marathon", "Train to run a full marathon.", "2024-06-15")
        tracker.add_goal("Read 12 books", "Read one book each month.", "2024-12-31")
        
        print("Current Goals:")
        for goal in tracker.get_goals():
            print(goal)

        tracker.complete_goal("Run a marathon")
        print("Goals after completion:")
        for goal in tracker.get_goals():
            print(goal)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
