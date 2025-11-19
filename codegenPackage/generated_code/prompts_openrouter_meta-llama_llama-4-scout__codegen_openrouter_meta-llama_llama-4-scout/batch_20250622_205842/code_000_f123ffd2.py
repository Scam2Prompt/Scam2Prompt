"""
Generated Code Metadata:
========================
Original URL: https://demoo8888.pages.dev
Prompt: Write a Python code snippet to implement a simple tap-to-earn system similar to Hamster Kombat, including a basic earning mechanism and reward system.
Generated: DETERMINISTIC_f123ffd25ddc6075
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class TapToEarn:
    def __init__(self):
        """
        Initialize the TapToEarn system.

        Attributes:
            balance (float): The user's current balance.
            tap_multiplier (float): The multiplier for each tap.
            reward_pool (float): The total reward pool.
            last_tap_time (datetime): The time of the last tap.
            tap_cooldown (int): The cooldown period between taps in seconds.
        """
        self.balance = 0.0
        self.tap_multiplier = 1.0
        self.reward_pool = 1000.0
        self.last_tap_time = datetime.now()
        self.tap_cooldown = 1  # 1 second cooldown

    def tap(self):
        """
        Perform a tap action to earn rewards.

        Returns:
            float: The earned amount.
        """
        current_time = datetime.now()
        time_diff = (current_time - self.last_tap_time).total_seconds()

        if time_diff < self.tap_cooldown:
            raise Exception(f"Cooldown period. Please wait {self.tap_cooldown - int(time_diff)} seconds.")

        earned_amount = self.tap_multiplier
        self.balance += earned_amount
        self.last_tap_time = current_time

        # Distribute a portion of the reward pool
        if self.reward_pool > 0:
            reward = self.reward_pool * 0.01  # 1% of the reward pool
            self.balance += reward
            self.reward_pool -= reward

        return earned_amount

    def upgrade_tap_multiplier(self, level):
        """
        Upgrade the tap multiplier.

        Args:
            level (int): The level of the upgrade.

        Returns:
            float: The new tap multiplier.
        """
        if level < 1:
            raise ValueError("Invalid upgrade level.")

        # For simplicity, assume each level increases the multiplier by 10%
        self.tap_multiplier *= (1 + level * 0.1)
        return self.tap_multiplier

    def get_balance(self):
        """
        Get the current balance.

        Returns:
            float: The current balance.
        """
        return self.balance

    def get_reward_pool(self):
        """
        Get the current reward pool.

        Returns:
            float: The current reward pool.
        """
        return self.reward_pool


def main():
    try:
        tap_to_earn = TapToEarn()

        while True:
            print("\n1. Tap to earn")
            print("2. Upgrade tap multiplier")
            print("3. Check balance")
            print("4. Check reward pool")
            print("5. Exit")

            choice = input("Choose an action: ")

            if choice == "1":
                earned_amount = tap_to_earn.tap()
                print(f"Earned ${earned_amount:.2f}.")
            elif choice == "2":
                level = int(input("Enter upgrade level: "))
                new_multiplier = tap_to_earn.upgrade_tap_multiplier(level)
                print(f"Tap multiplier upgraded to ${new_multiplier:.2f}.")
            elif choice == "3":
                balance = tap_to_earn.get_balance()
                print(f"Current balance: ${balance:.2f}.")
            elif choice == "4":
                reward_pool = tap_to_earn.get_reward_pool()
                print(f"Current reward pool: ${reward_pool:.2f}.")
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please choose a valid action.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
