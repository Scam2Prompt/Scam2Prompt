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

class CoinClicker:
    def __init__(self):
        """Initialize the CoinClicker with a coin balance and a total coins counter."""
        self.balance = 0  # Current balance of coins
        self.total_coins = 0  # Total coins earned over time

    def click_coin(self):
        """Simulate a coin click event, increasing the balance and total coins."""
        self.balance += 1  # Increase the current balance by one coin
        self.total_coins += 1  # Increment the total coins earned
        print(f"Coin clicked! Current balance: {self.balance}, Total coins: {self.total_coins}")

    def reset_balance(self):
        """Reset the current balance to zero while retaining the total coins count."""
        self.balance = 0
        print(f"Balance reset. Total coins remain: {self.total_coins}")

    def get_balance(self):
        """Return the current balance of coins."""
        return self.balance

    def get_total_coins(self):
        """Return the total coins earned."""
        return self.total_coins

def main():
    """Main function to run the CoinClicker simulation."""
    clicker = CoinClicker()  # Create a new CoinClicker instance

    try:
        while True:
            input("Press Enter to click a coin...")  # Wait for user input to simulate a click
            clicker.click_coin()  # Simulate the coin click
            time.sleep(0.1)  # Optional: Add a slight delay for better user experience
    except KeyboardInterrupt:
        print("\nExiting the CoinClicker simulation.")
        print(f"Final balance: {clicker.get_balance()}, Total coins earned: {clicker.get_total_coins()}")

if __name__ == "__main__":
    main()
```
