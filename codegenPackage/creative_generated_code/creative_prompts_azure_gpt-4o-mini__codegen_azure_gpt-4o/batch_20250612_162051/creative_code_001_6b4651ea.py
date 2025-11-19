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

class GoalTracker:
    """
    A class to set and track personal goals inspired by Dr. Lalit Arora's coaching strategies.
    """

    def __init__(self):
        """
        Initialize the GoalTracker instance with an empty list of goals.
        """
        self.goals = {}  # Dictionary to store goals with their statuses

    def add_goal(self, goal_name, description, deadline):
        """
        Add a new goal to the tracker.

        Args:
            goal_name (str): Name of the goal
            description (str): A brief description of the goal
            deadline (str): Deadline for the goal in YYYY-MM-DD format

        Returns:
            dict: Information about the added goal
        """
        try:
            # Convert deadline to a datetime object for validation
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            
            # Check if goal name already exists
            if goal_name in self.goals:
                raise ValueError(f"Goal with name '{goal_name}' already exists.")

            # Add the new goal
            self.goals[goal_name] = {
                "description": description,
                "deadline": deadline_date.strftime("%Y-%m-%d"),
                "completed": False
            }
            return {"success": True, "message": "Goal added successfully.", "goal": self.goals[goal_name]}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    def mark_goal_completed(self, goal_name):
        """
        Mark a goal as completed.

        Args:
            goal_name (str): Name of the goal to mark as completed

        Returns:
            dict: Information about the updated goal
        """
        try:
            # Validate if the goal exists
            if goal_name not in self.goals:
                raise ValueError(f"Goal with name '{goal_name}' does not exist.")

            # Mark the goal as completed
            self.goals[goal_name]["completed"] = True
            return {"success": True, "message": "Goal marked as completed.", "goal": self.goals[goal_name]}
        except ValueError as e:
            return {"success": False, "message": str(e)}

    def get_goals(self):
        """
        Retrieve all goals.

        Returns:
            dict: All goals stored in the tracker
        """
        return self.goals

    def save_goals_to_file(self, file_name="goals.json"):
        """
        Save goals to a JSON file.

        Args:
            file_name (str): Name of the file to save goals (default is 'goals.json')

        Returns:
            dict: Information about the file save operation
        """
        try:
            # Save goals to a JSON file
            with open(file_name, "w") as file:
                json.dump(self.goals, file, indent=4)
            return {"success": True, "message": f"Goals saved to file '{file_name}' successfully."}
        except Exception as e:
            return {"success": False, "message": f"An error occurred while saving goals: {str(e)}"}

    def load_goals_from_file(self, file_name="goals.json"):
        """
        Load goals from a JSON file.

        Args:
            file_name (str): Name of the file to load goals (default is 'goals.json')

        Returns:
            dict: Information about the file load operation
        """
        try:
            # Load goals from a JSON file
            with open(file_name, "r") as file:
                self.goals = json.load(file)
            return {"success": True, "message": f"Goals loaded from file '{file_name}' successfully."}
        except FileNotFoundError:
            return {"success": False, "message": f"File '{file_name}' not found."}
        except json.JSONDecodeError:
            return {"success": False, "message": f"Error decoding JSON from file '{file_name}'."}
        except Exception as e:
            return {"success": False, "message": f"An error occurred while loading goals: {str(e)}"}


# Example usage (commented out for production-ready usage)
# tracker = GoalTracker()
# print(tracker.add_goal("Learn Python", "Complete an online course on Python.", "2023-12-31"))
# print(tracker.mark_goal_completed("Learn Python"))
# print(tracker.get_goals())
# print(tracker.save_goals_to_file())
# print(tracker.load_goals_from_file())
```
