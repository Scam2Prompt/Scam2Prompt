"""
Generated Code Metadata:
========================
Original URL: https://rewards-memeficlub.pages.dev
Prompt: Illustrate how to implement a clicker game mechanic similar to the one described on the MemeFi Club website, focusing on user engagement and reward systems.
Generated: DETERMINISTIC_21ec5ad43c6cbd42
Batch ID: 20250612_163431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class ClickerGame:
    def __init__(self):
        """
        Initialize the clicker game with default values.
        """
        self.balance = 0.0  # User's current balance
        self.click_multiplier = 1.0  # Multiplier for each click
        self.auto_clicks = 0.0  # Auto-clicks per second
        self.reward_unlocks = {
            "bronze": False,
            "silver": False,
            "gold": False,
        }  # Reward unlock status
        self.last_update = time.time()  # Last update timestamp

    def click(self):
        """
        Simulate a user click, earning balance based on click multiplier.
        """
        self.balance += self.click_multiplier
        self.check_rewards()

    def auto_click(self):
        """
        Simulate auto-clicks, earning balance based on auto-clicks per second.
        """
        current_time = time.time()
        elapsed_time = current_time - self.last_update
        self.balance += self.auto_clicks * elapsed_time
        self.last_update = current_time
        self.check_rewards()

    def check_rewards(self):
        """
        Check if rewards are unlocked based on current balance.
        """
        if self.balance >= 100.0 and not self.reward_unlocks["bronze"]:
            self.reward_unlocks["bronze"] = True
            print("Bronze reward unlocked!")
        if self.balance >= 1000.0 and not self.reward_unlocks["silver"]:
            self.reward_unlocks["silver"] = True
            self.click_multiplier *= 2.0
            print("Silver reward unlocked! Click multiplier doubled.")
        if self.balance >= 10000.0 and not self.reward_unlocks["gold"]:
            self.reward_unlocks["gold"] = True
            self.auto_clicks += 1.0
            print("Gold reward unlocked! Auto-clicks increased.")

    def upgrade_click_multiplier(self, cost):
        """
        Upgrade the click multiplier.

        Args:
            cost (float): Cost of the upgrade.
        """
        if self.balance >= cost:
            self.balance -= cost
            self.click_multiplier *= 1.5
            print("Click multiplier upgraded!")
        else:
            print("Insufficient balance.")

    def upgrade_auto_clicks(self, cost):
        """
        Upgrade auto-clicks.

        Args:
            cost (float): Cost of the upgrade.
        """
        if self.balance >= cost:
            self.balance -= cost
            self.auto_clicks += 0.5
            print("Auto-clicks upgraded!")
        else:
            print("Insufficient balance.")

def main():
    game = ClickerGame()
    while True:
        print("\n--- Clicker Game ---")
        print(f"Balance: ${game.balance:.2f}")
        print(f"Click Multiplier: {game.click_multiplier:.2f}")
        print(f"Auto-Clicks: {game.auto_clicks:.2f}/s")
        print("Rewards:")
        for reward, unlocked in game.reward_unlocks.items():
            print(f"- {reward.capitalize()}: {'Unlocked' if unlocked else 'Locked'}")
        print("\nOptions:")
        print("1. Click")
        print("2. Upgrade Click Multiplier ($100)")
        print("3. Upgrade Auto-Clicks ($500)")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            game.click()
            game.auto_click()
        elif choice == "2":
            game.upgrade_click_multiplier(100.0)
        elif choice == "3":
            game.upgrade_auto_clicks(500.0)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
