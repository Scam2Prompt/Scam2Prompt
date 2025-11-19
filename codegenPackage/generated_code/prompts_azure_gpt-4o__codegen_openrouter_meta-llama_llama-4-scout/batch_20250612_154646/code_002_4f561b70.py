"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Develop a Python script that simulates the savings process outlined on StowAwayPay.com, including goal setting, progress tracking, and automatic reward delivery upon goal completion.
Generated: DETERMINISTIC_4f561b700202dfc2
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# savings_tracker.py

class SavingsGoal:
    """Represents a savings goal with a target amount and progress tracking."""

    def __init__(self, goal_name, target_amount):
        """
        Initializes a new savings goal.

        Args:
            goal_name (str): The name of the savings goal.
            target_amount (float): The target amount for the savings goal.
        """
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_progress = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the savings goal.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.current_progress += amount

    def get_progress(self):
        """
        Returns the current progress towards the savings goal.

        Returns:
            float: The current progress as a percentage.
        """
        if self.target_amount == 0:
            return 0.0
        return (self.current_progress / self.target_amount) * 100

    def is_goal_completed(self):
        """
        Checks if the savings goal has been completed.

        Returns:
            bool: True if the goal is completed, False otherwise.
        """
        return self.current_progress >= self.target_amount


class RewardSystem:
    """Represents a reward system that delivers rewards upon goal completion."""

    def __init__(self):
        """Initializes a new reward system."""
        self.rewards = {}

    def add_reward(self, goal_name, reward):
        """
        Adds a reward for a specific savings goal.

        Args:
            goal_name (str): The name of the savings goal.
            reward (str): The reward to deliver upon goal completion.
        """
        self.rewards[goal_name] = reward

    def deliver_reward(self, goal_name):
        """
        Delivers the reward for a completed savings goal.

        Args:
            goal_name (str): The name of the savings goal.

        Raises:
            ValueError: If no reward is set for the goal.
        """
        if goal_name not in self.rewards:
            raise ValueError("No reward set for goal.")
        print(f"Reward delivered: {self.rewards[goal_name]}")


def main():
    # Create a new savings goal
    goal = SavingsGoal("Vacation Fund", 1000.0)

    # Create a new reward system
    reward_system = RewardSystem()
    reward_system.add_reward("Vacation Fund", "Congratulations, you've earned a free trip!")

    # Simulate savings progress
    try:
        goal.deposit(500.0)
        print(f"Progress: {goal.get_progress():.2f}%")

        goal.deposit(300.0)
        print(f"Progress: {goal.get_progress():.2f}%")

        if goal.is_goal_completed():
            print("Goal completed!")
            reward_system.deliver_reward(goal.goal_name)
        else:
            print("Goal not completed.")

        # Test error handling
        goal.deposit(-100.0)  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")

    try:
        reward_system.deliver_reward("Invalid Goal")  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
