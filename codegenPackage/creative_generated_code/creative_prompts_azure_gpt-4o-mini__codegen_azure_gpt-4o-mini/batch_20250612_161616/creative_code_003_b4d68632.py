"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplebr.com
Prompt: Create a function that simulates the rollingan bonus calculation for an online betting platform, inspired by DewaTogel's bonus structure.
Generated: DETERMINISTIC_b4d68632716d46e4
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class BonusCalculator:
    """
    A class to simulate the rolling bonus calculation for an online betting platform.
    Inspired by DewaTogel's bonus structure.
    """

    def __init__(self, base_bonus: float, bonus_multiplier: float):
        """
        Initializes the BonusCalculator with base bonus and multiplier.

        :param base_bonus: The initial bonus amount.
        :param bonus_multiplier: The multiplier for the bonus calculation.
        """
        if base_bonus < 0 or bonus_multiplier <= 0:
            raise ValueError("Base bonus must be non-negative and multiplier must be positive.")
        self.base_bonus = base_bonus
        self.bonus_multiplier = bonus_multiplier

    def roll_bonus(self, rolls: int) -> float:
        """
        Simulates rolling the bonus calculation.

        :param rolls: The number of rolls to perform.
        :return: The total calculated bonus.
        """
        if rolls <= 0:
            raise ValueError("Number of rolls must be a positive integer.")
        
        total_bonus = 0.0
        
        for roll in range(rolls):
            # Simulate a random outcome for the roll
            outcome = random.random()  # Generate a random float between 0 and 1
            if outcome < 0.5:
                # 50% chance to take the base bonus
                total_bonus += self.base_bonus
            else:
                # 50% chance to apply the multiplier
                total_bonus += self.base_bonus * self.bonus_multiplier
            
            # Log the result for each roll (optional)
            print(f"Roll {roll + 1}: Outcome = {outcome}, Total Bonus = {total_bonus}")

        return total_bonus

# Example usage
if __name__ == "__main__":
    try:
        # Create a BonusCalculator instance with a base bonus of 10 and a multiplier of 2
        calculator = BonusCalculator(base_bonus=10.0, bonus_multiplier=2.0)
        # Simulate the bonus calculation for 5 rolls
        total_bonus = calculator.roll_bonus(rolls=5)
        print(f"Total calculated bonus after 5 rolls: {total_bonus:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
