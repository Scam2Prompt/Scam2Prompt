"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://actionacceleratoracademy.com
Prompt: Generate a Python script that utilizes AI-powered tools for personal development, similar to those offered in the Action Accelerator Academy, to help users track their progress and set actionable goals.
Generated: DETERMINISTIC_52e801295de742e1
Batch ID: 20250612_160946
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
    def __init__(self, title, description, deadline):
        """
        Initialize a new goal.

        :param title: Title of the goal
        :param description: Description of the goal
        :param deadline: Deadline for achieving the goal
        """
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now()
        self.progress = 0  # Progress percentage, from 0 to 100

    def update_progress(self, progress):
        """
        Update the progress of the goal.

        :param progress: Progress percentage to set
        """
        if 0 <= progress <= 100:
            self.progress = progress
        else:
            raise ValueError("Progress must be between 0 and 100.")

    def to_dict(self):
        """
        Convert the goal to a dictionary for easy JSON serialization.

        :return: Dictionary representation of the goal
        """
        return {
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline.isoformat(),
            'created_at': self.created_at.isoformat(),
            'progress': self.progress
        }


class GoalTracker:
    def __init__(self, filename='goals.json'):
        """
        Initialize the goal tracker.

        :param filename: Path to the JSON file for storing goals
        """
        self.filename = filename
        self.goals = self.load_goals()

    def load_goals(self):
        """
        Load goals from a JSON file.

        :return: List of Goal objects
        """
        try:
            with open(self.filename, 'r') as file:
                goals_data = json.load(file)
                return [Goal(**goal) for goal in goals_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Warning: JSON file is corrupted. Starting with an empty goal list.")
            return []

    def save_goals(self):
        """
        Save the current goals to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([goal.to_dict() for goal in self.goals], file, indent=4)

    def add_goal(self, title, description, deadline):
        """
        Add a new goal to the tracker.

        :param title: Title of the goal
        :param description: Description of the goal
        :param deadline: Deadline for achieving the goal
        """
        new_goal = Goal(title, description, deadline)
        self.goals.append(new_goal)
        self.save_goals()

    def update_goal_progress(self, title, progress):
        """
        Update the progress of an existing goal.

        :param title: Title of the goal to update
        :param progress: New progress percentage
        """
        for goal in self.goals:
            if goal.title == title:
                goal.update_progress(progress)
                self.save_goals()
                return
        raise ValueError("Goal not found.")

    def display_goals(self):
        """
        Display all goals and their progress.
        """
        for goal in self.goals:
            print(f"Title: {goal.title}, Description: {goal.description}, "
                  f"Deadline: {goal.deadline}, Progress: {goal.progress}%")


def main():
    tracker = GoalTracker()

    # Example usage
    tracker.add_goal("Learn Python", "Complete the Python course", datetime(2023, 12, 31))
    tracker.display_goals()
    
    # Updating progress
    tracker.update_goal_progress("Learn Python", 50)
    tracker.display_goals()

if __name__ == "__main__":
    main()
```
