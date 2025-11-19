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
import json
from datetime import datetime

class Goal:
    """Class to represent a personal goal."""
    
    def __init__(self, title, description, target_date):
        """
        Initialize a new goal.

        :param title: Title of the goal
        :param description: Description of the goal
        :param target_date: Target date for achieving the goal (YYYY-MM-DD)
        """
        self.title = title
        self.description = description
        self.target_date = datetime.strptime(target_date, '%Y-%m-%d')
        self.created_at = datetime.now()
        self.completed = False

    def mark_completed(self):
        """Mark the goal as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the goal to a dictionary for easy serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'completed': self.completed
        }

class GoalManager:
    """Class to manage a collection of goals."""
    
    def __init__(self, filename='goals.json'):
        """
        Initialize the goal manager.

        :param filename: The filename to store goals in JSON format
        """
        self.filename = filename
        self.goals = self.load_goals()

    def load_goals(self):
        """Load goals from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                goals_data = json.load(file)
                return [Goal(**goal) for goal in goals_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_goals(self):
        """Save goals to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([goal.to_dict() for goal in self.goals], file, indent=4)

    def add_goal(self, title, description, target_date):
        """Add a new goal to the manager."""
        new_goal = Goal(title, description, target_date)
        self.goals.append(new_goal)
        self.save_goals()

    def complete_goal(self, title):
        """Mark a goal as completed by its title."""
        for goal in self.goals:
            if goal.title == title:
                goal.mark_completed()
                self.save_goals()
                return
        raise ValueError(f"Goal with title '{title}' not found.")

    def list_goals(self):
        """List all goals."""
        return [goal.to_dict() for goal in self.goals]

def main():
    """Main function to demonstrate goal management."""
    manager = GoalManager()

    # Example usage
    try:
        manager.add_goal("Learn Python", "Complete the Python course", "2023-12-31")
        manager.add_goal("Get Fit", "Exercise 3 times a week", "2024-01-15")
        
        print("Current Goals:")
        for goal in manager.list_goals():
            print(goal)

        manager.complete_goal("Learn Python")
        print("\nGoals after completion:")
        for goal in manager.list_goals():
            print(goal)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
