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


class SavingsGoal:
    """
    A class to represent a savings goal.
    """

    def __init__(self, name, target_amount, reward):
        """
        Initialize a SavingsGoal object.

        :param name: Name of the savings goal (e.g., 'Vacation Fund')
        :param target_amount: Total amount required for the goal
        :param reward: Reward to be delivered upon goal completion
        """
        self.name = name
        self.target_amount = target_amount
        self.current_amount = 0.0
        self.reward = reward
        self.completed = False

    def add_progress(self, amount):
        """
        Add savings to the current amount. Check if the goal is completed.

        :param amount: The amount to add to the savings
        :raises ValueError: If the amount is negative
        """
        if amount < 0:
            raise ValueError("Progress amount cannot be negative.")
        self.current_amount += amount
        if self.current_amount >= self.target_amount:
            self.current_amount = self.target_amount
            self.completed = True
            self.deliver_reward()

    def deliver_reward(self):
        """
        Deliver the reward upon completing the goal.
        """
        print(f"Congratulations! You have completed the savings goal: {self.name}")
        print(f"Reward: {self.reward}")

    def get_progress(self):
        """
        Get the progress percentage of the savings goal.

        :return: Progress percentage (0-100)
        """
        return (self.current_amount / self.target_amount) * 100

    def __str__(self):
        """
        Return a user-friendly string representation of the savings goal.
        """
        return (
            f"Savings Goal: {self.name}\n"
            f"Target Amount: ${self.target_amount:.2f}\n"
            f"Current Amount: ${self.current_amount:.2f}\n"
            f"Progress: {self.get_progress():.2f}%\n"
            f"Reward: {self.reward}\n"
            f"Completed: {'Yes' if self.completed else 'No'}"
        )


class SavingsTracker:
    """
    A class to manage multiple savings goals.
    """

    def __init__(self, storage_file="savings_data.json"):
        """
        Initialize a SavingsTracker object.

        :param storage_file: File to save and load goals
        """
        self.goals = {}
        self.storage_file = storage_file
        self.load_goals()

    def add_goal(self, name, target_amount, reward):
        """
        Add a new savings goal.

        :param name: Name of the savings goal
        :param target_amount: Total amount required for the goal
        :param reward: Reward to be delivered upon goal completion
        :raises ValueError: If a goal with the same name already exists
        """
        if name in self.goals:
            raise ValueError(f"A savings goal with the name '{name}' already exists.")
        self.goals[name] = SavingsGoal(name, target_amount, reward)
        self.save_goals()

    def add_progress_to_goal(self, name, amount):
        """
        Add progress to a specific savings goal.

        :param name: Name of the savings goal
        :param amount: The amount to add to the savings
        :raises KeyError: If the goal does not exist
        :raises ValueError: If the amount is negative
        """
        if name not in self.goals:
            raise KeyError(f"No savings goal found with the name '{name}'.")
        self.goals[name].add_progress(amount)
        self.save_goals()

    def list_goals(self):
        """
        List all savings goals.

        :return: A list of string representations of all goals
        """
        return [str(goal) for goal in self.goals.values()]

    def save_goals(self):
        """
        Save all goals to the storage file.
        """
        try:
            with open(self.storage_file, "w") as file:
                serialized_goals = {
                    name: {
                        "name": goal.name,
                        "target_amount": goal.target_amount,
                        "current_amount": goal.current_amount,
                        "reward": goal.reward,
                        "completed": goal.completed,
                    }
                    for name, goal in self.goals.items()
                }
                json.dump(serialized_goals, file, indent=4)
        except IOError as e:
            print(f"Error saving goals: {e}")

    def load_goals(self):
        """
        Load all goals from the storage file.
        """
        if not os.path.exists(self.storage_file):
            return
        try:
            with open(self.storage_file, "r") as file:
                serialized_goals = json.load(file)
                for name, data in serialized_goals.items():
                    goal = SavingsGoal(
                        name=data["name"],
                        target_amount=data["target_amount"],
                        reward=data["reward"],
                    )
                    goal.current_amount = data["current_amount"]
                    goal.completed = data["completed"]
                    self.goals[name] = goal
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading goals: {e}")


# Example usage
if __name__ == "__main__":
    tracker = SavingsTracker()

    try:
        # Add a new savings goal
        tracker.add_goal("Vacation Fund", 5000, "Plane tickets and hotel stay")
        tracker.add_goal("Emergency Fund", 10000, "Financial peace of mind")

        # Add progress
        tracker.add_progress_to_goal("Vacation Fund", 1500)
        tracker.add_progress_to_goal("Vacation Fund", 3500)  # Completes the goal
        tracker.add_progress_to_goal("Emergency Fund", 2000)

        # List all goals
        for goal_info in tracker.list_goals():
            print(goal_info)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
