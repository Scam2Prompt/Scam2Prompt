"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memecoindrop.pages.dev
Prompt: Generate a script that tracks the number of coins a user has earned in a game for $meme redemption.
Generated: DETERMINISTIC_b511b6fc5a4fe83c
Batch ID: 20250612_163807
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

class CoinTracker:
    """A class to track the number of coins a user has earned."""

    def __init__(self, user_id):
        """Initialize the CoinTracker with a user ID."""
        self.user_id = user_id
        self.coins_file = f"{user_id}_coins.json"
        self.coins = self.load_coins()

    def load_coins(self):
        """Load the number of coins from a JSON file. If the file does not exist, initialize with 0 coins."""
        if os.path.exists(self.coins_file):
            try:
                with open(self.coins_file, 'r') as file:
                    data = json.load(file)
                    return data.get("coins", 0)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading coins: {e}")
                return 0
        return 0

    def save_coins(self):
        """Save the current number of coins to a JSON file."""
        try:
            with open(self.coins_file, 'w') as file:
                json.dump({"coins": self.coins}, file)
        except IOError as e:
            print(f"Error saving coins: {e}")

    def add_coins(self, amount):
        """Add a specified amount of coins to the user's total."""
        if amount < 0:
            print("Amount to add must be non-negative.")
            return
        self.coins += amount
        self.save_coins()

    def redeem_coins(self, amount):
        """Redeem a specified amount of coins. Returns True if successful, False otherwise."""
        if amount < 0:
            print("Amount to redeem must be non-negative.")
            return False
        if amount > self.coins:
            print("Not enough coins to redeem.")
            return False
        self.coins -= amount
        self.save_coins()
        return True

    def get_coins(self):
        """Return the current number of coins."""
        return self.coins


if __name__ == "__main__":
    # Example usage of the CoinTracker class
    user_id = "user123"
    tracker = CoinTracker(user_id)

    # Adding coins
    tracker.add_coins(50)
    print(f"Current coins: {tracker.get_coins()}")  # Expected output: 50

    # Redeeming coins
    success = tracker.redeem_coins(30)
    print(f"Redemption successful: {success}")
    print(f"Current coins after redemption: {tracker.get_coins()}")  # Expected output: 20

    # Attempt to redeem more coins than available
    success = tracker.redeem_coins(25)
    print(f"Redemption successful: {success}")  # Expected output: False
```
