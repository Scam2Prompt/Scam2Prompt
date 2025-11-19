"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notocoin.pages.dev
Prompt: Generate a code snippet that simulates the daily bonus collection process in NotCoin, including features like rocket activation and energy restoration.
Generated: DETERMINISTIC_b5225c1f06474e86
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class NotCoinGame:
    def __init__(self):
        """Initialize the game with default values."""
        self.daily_bonus_collected = False
        self.energy = 100  # Max energy is 100
        self.rocket_activated = False

    def collect_daily_bonus(self):
        """
        Simulate daily bonus collection.
        If the bonus is already collected, inform the user.
        """
        if self.daily_bonus_collected:
            print("Daily bonus already collected!")
            return
        print("Collecting daily bonus...")
        self.daily_bonus_collected = True
        self.energy = min(self.energy + 10, 100)  # Restore energy by 10, capped at 100
        print("Daily bonus collected! Energy restored by 10.")

    def activate_rocket(self):
        """
        Simulate rocket activation.
        Rocket activation is only possible if the daily bonus has been collected.
        """
        if not self.daily_bonus_collected:
            print("Cannot activate rocket - daily bonus not yet collected!")
            return
        if self.rocket_activated:
            print("Rocket already activated!")
            return
        print("Activating rocket...")
        self.rocket_activated = True
        print("Rocket activated successfully!")

    def restore_energy(self, amount):
        """
        Restore energy by a specified amount.
        Ensure energy does not exceed the maximum value.
        """
        if amount <= 0:
            print("Invalid energy restoration amount!")
            return
        self.energy = min(self.energy + amount, 100)
        print(f"Energy restored by {amount}. Current energy: {self.energy}")

    def daily_reset(self):
        """
        Reset the daily bonus and rocket activation status.
        This simulates the reset that happens at the start of a new day.
        """
        print("Resetting daily status...")
        self.daily_bonus_collected = False
        self.rocket_activated = False
        print("Daily status reset successfully.")

# Example usage
if __name__ == "__main__":
    try:
        game = NotCoinGame()

        # Simulate daily bonus collection
        game.collect_daily_bonus()

        # Attempt to activate the rocket
        game.activate_rocket()

        # Restore energy manually
        game.restore_energy(20)

        # Simulate end of the day and reset
        time.sleep(1)  # Simulating passage of time (e.g., end of the day)
        game.daily_reset()
    except Exception as e:
        print(f"An error occurred: {e}")
```
