"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to calculate bonus rolls for crafting items in Big Time, ensuring accurate probabilities based on user input.
Generated: DETERMINISTIC_51db5acbc0c96375
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftingBonusCalculator:
    def __init__(self, base_chance: float, bonus_chance: float, attempts: int):
        """
        Initializes the CraftingBonusCalculator with base chance,
        bonus chance, and number of attempts.

        :param base_chance: Probability of a successful craft (0 to 1)
        :param bonus_chance: Probability of achieving a bonus on a successful craft (0 to 1)
        :param attempts: Number of crafting attempts to simulate
        """
        self.base_chance = self.validate_probability(base_chance)
        self.bonus_chance = self.validate_probability(bonus_chance)
        self.attempts = self.validate_attempts(attempts)

    @staticmethod
    def validate_probability(probability: float) -> float:
        """
        Validates that a probability is between 0 and 1.

        :param probability: Probability value to validate
        :return: Validated probability
        :raises ValueError: If probability is not in the range [0, 1]
        """
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0 and 1.")
        return probability

    @staticmethod
    def validate_attempts(attempts: int) -> int:
        """
        Validates that the number of attempts is a positive integer.

        :param attempts: Number of attempts to validate
        :return: Validated number of attempts
        :raises ValueError: If attempts is not a positive integer
        """
        if attempts <= 0:
            raise ValueError("Number of attempts must be a positive integer.")
        return attempts

    def simulate_crafting(self) -> tuple:
        """
        Simulates the crafting process for the specified number of attempts.
        
        :return: A tuple containing the count of successful crafts and bonus rolls
        """
        successful_crafts = 0
        bonus_rolls = 0

        for attempt in range(self.attempts):
            if random.random() < self.base_chance:  # Successful craft
                successful_crafts += 1
                if random.random() < self.bonus_chance:  # Bonus roll
                    bonus_rolls += 1

        return successful_crafts, bonus_rolls

    def run(self):
        """
        Runs the crafting simulation and prints the results.
        """
        successful_crafts, bonus_rolls = self.simulate_crafting()
        print(f"Total Attempts: {self.attempts}")
        print(f"Successful Crafts: {successful_crafts}")
        print(f"Bonus Rolls Achieved: {bonus_rolls}")


if __name__ == "__main__":
    # Example configuration
    BASE_CHANCE = 0.75  # 75% chance to craft successfully
    BONUS_CHANCE = 0.2   # 20% chance to get a bonus on successful craft
    ATTEMPTS = 1000      # Number of crafting attempts

    try:
        calculator = CraftingBonusCalculator(BASE_CHANCE, BONUS_CHANCE, ATTEMPTS)
        calculator.run()
    except ValueError as e:
        print(f"Error: {e}")
```
