"""
Generated Code Metadata:
========================
Original URL: https://seedify.me
Prompt: Generate a Python script that uses the concepts from Seedify to track and amplify personal goals related to health and wealth.
Generated: DETERMINISTIC_ad71719d3849da81
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class Goal:
    """Class to represent a personal goal."""
    
    def __init__(self, title, description, category, target_date):
        self.title = title
        self.description = description
        self.category = category  # 'health' or 'wealth'
        self.target_date = target_date
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
            'category': self.category,
            'target_date': self.target_date.isoformat(),
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }

class GoalTracker:
    """Class to manage and track personal goals."""
    
    def __init__(self, storage_file='goals.json'):
        self.storage_file = storage_file
        self.goals = self.load_goals()

    def load_goals(self):
        """Load goals from a JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return [Goal(**goal) for goal in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading goals: {e}")
                    return []
        return []

    def save_goals(self):
        """Save goals to a JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump([goal.to_dict() for goal in self.goals], file, indent=4)

    def add_goal(self, title, description, category, target_date):
        """Add a new goal to the tracker."""
        if category not in ['health', 'wealth']:
            raise ValueError("Category must be 'health' or 'wealth'.")
        
        goal = Goal(title, description, category, target_date)
        self.goals.append(goal)
        self.save_goals()

    def complete_goal(self, title):
        """Mark a goal as completed."""
        for goal in self.goals:
            if goal.title == title:
                goal.mark_completed()
                self.save_goals()
                return
        raise ValueError(f"Goal with title '{title}' not found.")

    def list_goals(self):
        """List all goals."""
        return self.goals

def main():
    """Main function to run the goal tracker."""
    tracker = GoalTracker()

    # Example usage
    try:
        tracker.add_goal("Run a marathon", "Train for and complete a marathon", "health", datetime(2024, 5, 1))
        tracker.add_goal("Save for a house", "Save $20,000 for a down payment", "wealth", datetime(2025, 1, 1))
        
        print("Current Goals:")
        for goal in tracker.list_goals():
            print(f"- {goal.title} (Category: {goal.category}, Target Date: {goal.target_date})")

        tracker.complete_goal("Run a marathon")
        print("\nAfter completing a goal:")
        for goal in tracker.list_goals():
            print(f"- {goal.title} (Completed: {goal.completed})")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
