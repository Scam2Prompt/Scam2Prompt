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

class CoinGame:
    def __init__(self):
        """Initialize the game with a balance and upgrade level."""
        self.balance = 0      # User's current coin balance
        self.upgrade_level = 1  # Current level of upgrade for coin multiplier
        self.coin_multiplier = 1  # Multiplier effect of upgrades

    def tap(self):
        """Simulate a tap on the screen to collect coins."""
        # Increase the balance based on the current coin multiplier
        coins_collected = 1 * self.coin_multiplier
        self.balance += coins_collected
        print(f"Tapped! You collected {coins_collected} coins. Current balance: {self.balance}")

    def upgrade(self):
        """Upgrade the coin multiplier for increased earnings."""
        # Check if an upgrade can be purchased
        upgrade_cost = self.calculate_upgrade_cost()
        if self.balance >= upgrade_cost:
            self.balance -= upgrade_cost
            self.upgrade_level += 1
            self.coin_multiplier = self.upgrade_level  # Increase the multiplier
            print(f"Upgrade successful! New upgrade level: {self.upgrade_level}, Coin multiplier: {self.coin_multiplier}")
        else:
            print(f"Not enough coins to upgrade. Current balance: {self.balance}, Required: {upgrade_cost}")

    def calculate_upgrade_cost(self):
        """Calculate the cost of the next upgrade based on the current level."""
        return self.upgrade_level * 10  # Example cost formula

    def display_status(self):
        """Display the current game status."""
        print(f"Balance: {self.balance}, Upgrade Level: {self.upgrade_level}, Coin Multiplier: {self.coin_multiplier}")

def main():
    """Main function to run the CoinCollection game."""
    game = CoinGame()
    
    while True:
        # Display status of the game
        game.display_status()
        
        action = input("Enter 'tap' to collect coins, 'upgrade' to upgrade, or 'exit' to quit: ").strip().lower()
        
        if action == 'tap':
            game.tap()
        elif action == 'upgrade':
            game.upgrade()
        elif action == 'exit':
            print("Exiting game. Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'tap', 'upgrade', or 'exit'.")
        
        time.sleep(1)  # Add a slight delay for user experience

if __name__ == "__main__":
    main()
```
