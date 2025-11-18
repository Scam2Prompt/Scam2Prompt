"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Write Python code to track daily steps and convert them into in-game energy for a "move-to-earn" NFT game like Genopets. Include functionality for banking steps and calculating rewards.
Generated: DETERMINISTIC_9d5b89f107fc516c
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class StepTracker:
    """
    A class to track daily steps and convert them into in-game energy for a move-to-earn game.
    """

    def __init__(self, conversion_rate=10):
        """
        Initialize the StepTracker object.

        Args:
            conversion_rate (int): Number of steps required for 1 unit of in-game energy.
        """
        self.steps_today = 0  # Steps logged for the current day
        self.bank = 0  # Banked steps that can be converted to in-game energy later
        self.conversion_rate = conversion_rate  # Steps-to-energy conversion rate
        self.last_updated_date = datetime.date.today()  # Track the last update date

    def log_steps(self, steps):
        """
        Log steps for the current day. If a new day has started, reset steps_today.

        Args:
            steps (int): Number of steps to log for the current day.
        """
        if steps < 0:
            raise ValueError("Steps cannot be negative.")

        # Check if the date has changed since the last update
        current_date = datetime.date.today()
        if current_date != self.last_updated_date:
            self._reset_daily_steps()
            self.last_updated_date = current_date

        self.steps_today += steps
        print(f"Logged {steps} steps. Total steps today: {self.steps_today}")

    def _reset_daily_steps(self):
        """
        Reset the daily steps and add them to the bank.
        """
        self.bank += self.steps_today
        self.steps_today = 0
        print(f"New day detected. Daily steps reset. Banked steps: {self.bank}")

    def bank_steps(self):
        """
        Bank the current day's steps without resetting them.

        This allows the user to store unconverted steps for later use.
        """
        self.bank += self.steps_today
        self.steps_today = 0
        print(f"Steps banked. Total banked steps: {self.bank}")

    def calculate_energy(self):
        """
        Calculate in-game energy from banked steps.

        Returns:
            int: Amount of in-game energy that can be earned based on banked steps.
        """
        energy = self.bank // self.conversion_rate
        remainder_steps = self.bank % self.conversion_rate
        print(
            f"Calculated energy: {energy}. Remaining steps in bank: {remainder_steps}"
        )
        return energy

    def convert_steps_to_energy(self):
        """
        Convert banked steps into in-game energy and reset the bank.

        Returns:
            int: Amount of in-game energy earned from the conversion.
        """
        energy = self.calculate_energy()
        self.bank %= self.conversion_rate  # Keep only remaining steps that weren't converted
        print(f"Converted steps to energy. Earned {energy} energy units.")
        return energy


if __name__ == "__main__":
    # Example usage
    tracker = StepTracker(conversion_rate=10)  # 10 steps = 1 energy unit

    # Log some steps for today
    try:
        tracker.log_steps(5000)
        tracker.log_steps(2000)

        # Bank today's steps
        tracker.bank_steps()

        # Convert banked steps to energy
        energy = tracker.convert_steps_to_energy()
        print(f"Total energy earned: {energy}")

    except Exception as e:
        print(f"Error: {e}")
```
