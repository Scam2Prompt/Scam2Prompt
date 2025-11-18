"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amamam-ble.pages.dev
Prompt: Write a Python script to simulate the coin-clicking mechanism in the Hamster Kombat game, where each click adds one coin to the balance. Include functionality for tracking the total number of coins earned.
Generated: DETERMINISTIC_6d82d15f61458bc3
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time


class HamsterKombatCoinClicker:
    """
    A class to simulate the coin-clicking mechanism in the Hamster Kombat game.
    Each click adds one coin to the balance, and the total number of coins earned
    is tracked.
    """

    def __init__(self):
        """
        Initializes the coin-clicker with a starting balance of 0 coins.
        """
        self.balance = 0  # Current balance
        self.total_coins_earned = 0  # Total coins ever earned

    def click_coin(self):
        """
        Simulates clicking a coin. Increases the balance and updates the total coins earned.
        """
        self.balance += 1
        self.total_coins_earned += 1

    def get_balance(self):
        """
        Returns the current coin balance.

        :return: Integer representing the current coin balance.
        """
        return self.balance

    def get_total_coins_earned(self):
        """
        Returns the total number of coins ever earned.

        :return: Integer representing the total coins earned.
        """
        return self.total_coins_earned

    def reset_balance(self):
        """
        Resets the current coin balance to 0. The total coins earned remains unchanged.
        """
        self.balance = 0


def main():
    """
    Main function to simulate the Hamster Kombat coin-clicker mechanism.
    """
    print("Welcome to Hamster Kombat Coin Clicker!")
    print("Press ENTER to click a coin, or type 'exit' to quit the game.")
    print("Type 'stats' to check your balance and total coins earned.")
    print("Type 'reset' to reset your current balance (total coins earned will remain unchanged).")

    # Instantiate the coin-clicker game
    clicker = HamsterKombatCoinClicker()

    while True:
        try:
            user_input = input("\nYour action: ").strip().lower()

            if user_input == "exit":
                print("Thanks for playing! Goodbye!")
                break
            elif user_input == "stats":
                print(f"Current Balance: {clicker.get_balance()} coins")
                print(f"Total Coins Earned: {clicker.get_total_coins_earned()} coins")
            elif user_input == "reset":
                clicker.reset_balance()
                print("Your current balance has been reset to 0.")
            elif user_input == "":
                clicker.click_coin()
                print(f"Coin clicked! Current Balance: {clicker.get_balance()} coins")
            else:
                print("Invalid input. Please press ENTER to click a coin, or type 'exit', 'stats', or 'reset'.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
