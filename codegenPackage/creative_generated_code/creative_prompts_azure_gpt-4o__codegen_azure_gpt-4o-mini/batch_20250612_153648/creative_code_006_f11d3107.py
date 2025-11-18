"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorealm.vercel.app
Prompt: Write a CLI-based workflow for envisioning and achieving app development goals using Gorealm's tools.
Generated: DETERMINISTIC_f11d3107f4d78353
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse
import json
import os
import sys

class Goal:
    """Class to represent a development goal."""
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        """Mark this goal as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the goal to a dictionary for saving."""
        return {
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

class GoalManager:
    """Class to manage a list of development goals."""
    
    def __init__(self, goals_file):
        self.goals_file = goals_file
        self.goals = self.load_goals()

    def load_goals(self):
        """Load goals from a JSON file."""
        if os.path.exists(self.goals_file):
            with open(self.goals_file, 'r') as file:
                try:
                    return [Goal(**goal) for goal in json.load(file)]
                except (json.JSONDecodeError, TypeError) as e:
                    print(f"Error loading goals: {e}")
                    return []
        return []

    def save_goals(self):
        """Save the current goals to a JSON file."""
        with open(self.goals_file, 'w') as file:
            json.dump([goal.to_dict() for goal in self.goals], file)

    def add_goal(self, title, description):
        """Add a new goal to the list."""
        self.goals.append(Goal(title, description))
        self.save_goals()

    def complete_goal(self, title):
        """Mark a goal as completed."""
        for goal in self.goals:
            if goal.title == title:
                goal.mark_completed()
                self.save_goals()
                return
        print(f"Goal '{title}' not found.")

    def list_goals(self):
        """List all goals with their status."""
        for goal in self.goals:
            status = "✔️" if goal.completed else "❌"
            print(f"{status} {goal.title}: {goal.description}")

def main():
    """Main CLI function to handle user input and commands."""
    parser = argparse.ArgumentParser(description="Manage your app development goals.")
    parser.add_argument('--add', nargs=2, metavar=('TITLE', 'DESCRIPTION'),
                        help='Add a new goal with TITLE and DESCRIPTION')
    parser.add_argument('--complete', metavar='TITLE',
                        help='Mark a goal as completed by TITLE')
    parser.add_argument('--list', action='store_true',
                        help='List all goals')
    parser.add_argument('--file', default='goals.json',
                        help='File to store goals (default: goals.json)')

    args = parser.parse_args()

    # Create a GoalManager instance
    goal_manager = GoalManager(args.file)

    # Handle the different command line arguments
    if args.add:
        title, description = args.add
        goal_manager.add_goal(title, description)
        print(f"Added goal: {title}")
    elif args.complete:
        title = args.complete
        goal_manager.complete_goal(title)
        print(f"Marked goal as completed: {title}")
    elif args.list:
        goal_manager.list_goals()
    else:
        parser.print_help()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```

This code provides a CLI-based workflow for managing app development goals using a simple JSON-based storage system. It allows users to add, complete, and list goals, with proper error handling and documentation.
