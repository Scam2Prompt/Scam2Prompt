"""
Generated Code Metadata:
========================
Original URL: https://minerswiss.com
Prompt: Write a Python script to simulate the "coin collection" feature described in the TG WebApp Khaby Lame Coin game, where tapping the screen increases the user's balance. Include functionality for upgrades that multiply coin earnings.
Generated: DETERMINISTIC_75dcc2da08241c4c
Batch ID: 20250612_145712
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

class CoinGame:
    def __init__(self):
        """
        Initialize the CoinGame with a starting balance and no upgrades.
        """
        self.balance = 0
        self.upgrade_level = 1
        self.upgrade_cost = 10
        self.last_update = time.time()

    def tap(self):
        """
        Simulate a tap on the screen, increasing the user's balance based on the current upgrade level.
        """
        current_time = time.time()
        if current_time - self.last_update < 0.1:  # prevent tapping too fast
            print("Please wait a bit before tapping again.")
            return
        self.last_update = current_time
        earnings = self.upgrade_level
        self.balance += earnings
        print(f"You tapped and earned {earnings} coins. Your new balance is {self.balance}.")

    def upgrade(self):
        """
        Upgrade the coin earnings multiplier if the user has enough balance.
        """
        cost = self.upgrade_cost
        if self.balance < cost:
            print(f"You need {cost} coins to upgrade. Your current balance is {self.balance}.")
            return
        self.balance -= cost
        self.upgrade_level += 1
        self.upgrade_cost = int(self.upgrade_cost * 1.1)  # increase the cost by 10%
        print(f"You upgraded! Your new earnings multiplier is {self.upgrade_level}.")

    def display_status(self):
        """
        Display the user's current balance and upgrade level.
        """
        print(f"Balance: {self.balance}, Upgrade Level: {self.upgrade_level}, Upgrade Cost: {self.upgrade_cost}")


def main():
    game = CoinGame()
    while True:
        print("\n1. Tap\n2. Upgrade\n3. Status\n4. Exit")
        try:
            choice = int(input("Choose an action: "))
            if choice == 1:
                game.tap()
            elif choice == 2:
                game.upgrade()
            elif choice == 3:
                game.display_status()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please choose a valid action.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
```
