"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Create a code snippet that implements a customizable tracking template, like the Action Tracker Google Sheets template offered by the Action Accelerator Academy, to monitor progress toward goals.
Generated: DETERMINISTIC_365a6d11c84e2b70
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime

class GoalTracker:
    """
    A class to track progress toward goals using a customizable tracking template.
    """

    def __init__(self, filename='goal_tracker.xlsx'):
        """
        Initializes the GoalTracker with a specified Excel filename.

        :param filename: The name of the Excel file to save the tracker.
        """
        self.filename = filename
        self.goals_df = pd.DataFrame(columns=['Goal', 'Start Date', 'End Date', 'Progress', 'Status'])

    def add_goal(self, goal, start_date, end_date):
        """
        Adds a new goal to the tracker.

        :param goal: The goal description.
        :param start_date: The start date of the goal (YYYY-MM-DD).
        :param end_date: The end date of the goal (YYYY-MM-DD).
        """
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
            if end_date < start_date:
                raise ValueError("End date must be after start date.")
            new_goal = {
                'Goal': goal,
                'Start Date': start_date,
                'End Date': end_date,
                'Progress': 0,
                'Status': 'Not Started'
            }
            self.goals_df = self.goals_df.append(new_goal, ignore_index=True)
        except Exception as e:
            print(f"Error adding goal: {e}")

    def update_progress(self, goal_index, progress):
        """
        Updates the progress of a specified goal.

        :param goal_index: The index of the goal to update.
        :param progress: The progress percentage (0-100).
        """
        try:
            if goal_index < 0 or goal_index >= len(self.goals_df):
                raise IndexError("Goal index out of range.")
            if not (0 <= progress <= 100):
                raise ValueError("Progress must be between 0 and 100.")
            self.goals_df.at[goal_index, 'Progress'] = progress
            self.goals_df.at[goal_index, 'Status'] = 'In Progress' if progress > 0 else 'Not Started'
        except Exception as e:
            print(f"Error updating progress: {e}")

    def save_to_excel(self):
        """
        Saves the current goals and their progress to an Excel file.
        """
        try:
            self.goals_df.to_excel(self.filename, index=False)
            print(f"Goals saved to {self.filename}")
        except Exception as e:
            print(f"Error saving to Excel: {e}")

    def load_from_excel(self):
        """
        Loads goals and their progress from an Excel file.
        """
        try:
            self.goals_df = pd.read_excel(self.filename)
            print(f"Goals loaded from {self.filename}")
        except Exception as e:
            print(f"Error loading from Excel: {e}")

# Example usage
if __name__ == "__main__":
    tracker = GoalTracker()
    tracker.add_goal("Learn Python", "2023-01-01", "2023-12-31")
    tracker.update_progress(0, 50)
    tracker.save_to_excel()
```
