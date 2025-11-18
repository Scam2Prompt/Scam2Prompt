"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerswiss.com
Prompt: Write a Python script to simulate the "coin collection" feature described in the TG WebApp Khaby Lame Coin game, where tapping the screen increases the user's balance. Include functionality for upgrades that multiply coin earnings.
Generated: DETERMINISTIC_75dcc2da08241c4c
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import sys


class CoinGame:
    """
    A class to simulate the coin collection feature in a game.
    Users tap to earn coins, and can purchase upgrades to multiply earnings.
    """

    def __init__(self):
        # Initialize the user balance and multiplier
        self.balance = 0  # Total coins collected by the user
        self.coin_multiplier = 1  # Multiplier for coin earnings
        self.upgrade_cost = 10  # Initial cost for upgrades

    def tap_to_collect(self):
        """
        Called when the user taps the screen to collect coins.
        Increases the balance based on the current multiplier.
        """
        self.balance += self.coin_multiplier
        print(f"Coins Collected! Current Balance: {self.balance}")

    def purchase_upgrade(self):
        """
        Allows the user to purchase an upgrade to increase the multiplier.
        Deducts the upgrade cost from the balance and increases the multiplier.
        """
        if self.balance >= self.upgrade_cost:
            self.balance -= self.upgrade_cost
            self.coin_multiplier += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)  # Upgrade cost increases
            print(
                f"Upgrade Purchased! New Multiplier: {self.coin_multiplier}, "
                f"New Balance: {self.balance}, Next Upgrade Cost: {self.upgrade_cost}"
            )
        else:
            print(
                f"Not enough coins to purchase an upgrade. "
                f"Current Balance: {self.balance}, Upgrade Cost: {self.upgrade_cost}"
            )

    def display_menu(self):
        """
        Displays the main menu with options for the user.
        """
        print("\n=== Coin Game Menu ===")
        print("1. Tap to Collect Coins")
        print("2. Purchase Upgrade")
        print("3. Show Balance and Multiplier")
        print("4. Exit Game")

    def display_status(self):
        """
        Displays the current balance and multiplier.
        """
        print(f"Current Balance: {self.balance}, Multiplier: {self.coin_multiplier}")

    def run(self):
        """
        Main game loop. Continuously displays the menu and processes user input.
        """
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1:
                    self.tap_to_collect()
                elif choice == 2:
                    self.purchase_upgrade()
                elif choice == 3:
                    self.display_status()
                elif choice == 4:
                    print("Exiting the game. Thanks for playing!")
                    break
                else:
                    print("Invalid choice. Please select an option between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                sys.exit(1)


if __name__ == "__main__":
    # Create an instance of the CoinGame and run the game
    print("Welcome to the Coin Collection Game!")
    game = CoinGame()
    game.run()
```
