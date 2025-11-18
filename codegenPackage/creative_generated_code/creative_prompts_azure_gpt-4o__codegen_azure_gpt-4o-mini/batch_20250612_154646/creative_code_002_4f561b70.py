"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Develop a Python script that simulates the savings process outlined on StowAwayPay.com, including goal setting, progress tracking, and automatic reward delivery upon goal completion.
Generated: DETERMINISTIC_4f561b700202dfc2
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class SavingsGoal:
    """Class to represent a savings goal."""

    def __init__(self, name, target_amount, current_amount=0):
        """
        Initialize a new savings goal.

        :param name: Name of the savings goal
        :param target_amount: Total amount desired for the goal
        :param current_amount: Current amount saved towards the goal
        """
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.creation_date = datetime.now()

    def add_savings(self, amount):
        """
        Add savings to the current amount.

        :param amount: Amount to add to the savings
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self.current_amount += amount
        print(f"Added {amount} to {self.name}. Current savings: {self.current_amount}.")

    def is_goal_reached(self):
        """
        Check if the savings goal has been reached.

        :return: Boolean indicating whether the goal is reached
        """
        return self.current_amount >= self.target_amount

    def reward(self):
        """
        Deliver a reward if the goal is reached.

        :return: Reward message if goal is reached, else None
        """
        if self.is_goal_reached():
            return f"Congratulations! You've reached your savings goal of {self.target_amount} for {self.name}!"
        return None

    def progress(self):
        """
        Get the current progress towards the savings goal.

        :return: Progress percentage
        """
        return (self.current_amount / self.target_amount) * 100

class SavingsTracker:
    """Class to track multiple savings goals."""

    def __init__(self, filename='savings_goals.json'):
        """
        Initialize the savings tracker.

        :param filename: File to save the goals
        """
        self.goals = []
        self.filename = filename
        self.load_goals()

    def add_goal(self, goal):
        """
        Add a new savings goal to the tracker.

        :param goal: SavingsGoal instance
        """
        self.goals.append(goal)
        self.save_goals()

    def save_goals(self):
        """
        Save the current goals to a JSON file.
        """
        with open(self.filename, 'w') as f:
            json.dump([goal.__dict__ for goal in self.goals], f)

    def load_goals(self):
        """
        Load goals from a JSON file if it exists.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                goals_data = json.load(f)
                self.goals = [SavingsGoal(**data) for data in goals_data]

    def display_goals(self):
        """
        Display all the savings goals and their progress.
        """
        for goal in self.goals:
            progress = goal.progress()
            print(f"Goal: {goal.name}, Target: {goal.target_amount}, Current: {goal.current_amount}, Progress: {progress:.2f}%")
            reward_message = goal.reward()
            if reward_message:
                print(reward_message)

def main():
    """Main function to run the savings simulator."""
    tracker = SavingsTracker()

    # Example of adding savings goals
    try:
        vacation_goal = SavingsGoal(name="Vacation", target_amount=2000)
        tracker.add_goal(vacation_goal)

        tracker.display_goals()

        # Simulating adding savings
        vacation_goal.add_savings(500)
        vacation_goal.add_savings(1500)  # Completing the goal
        tracker.display_goals()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
