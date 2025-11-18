"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Write a script to calculate bonus rolls during item crafting in Big Time, displaying probabilities and potential rewards.
Generated: DETERMINISTIC_009c6944c719aac3
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftingBonusRoll:
    def __init__(self, base_chance: float, bonus_multiplier: float, attempts: int):
        """
        Initializes the CraftingBonusRoll instance.

        :param base_chance: Base probability of success (0 to 1).
        :param bonus_multiplier: Multiplier applied to successful rolls.
        :param attempts: Number of attempts to roll for bonuses.
        """
        self.base_chance = base_chance
        self.bonus_multiplier = bonus_multiplier
        self.attempts = attempts

    def roll_for_bonus(self) -> float:
        """
        Simulates rolling for a bonus based on the base chance.

        :return: The total bonus earned from the rolls.
        """
        total_bonus = 0.0
        
        for attempt in range(self.attempts):
            if random.random() < self.base_chance:
                # Successful roll
                bonus = self.bonus_multiplier * (attempt + 1)
                total_bonus += bonus
                print(f"Attempt {attempt + 1}: Success! Bonus earned: {bonus}")
            else:
                print(f"Attempt {attempt + 1}: Failed.")

        return total_bonus

    def run(self):
        """
        Executes the bonus roll simulation and displays results.

        :return: None
        """
        try:
            total_bonus = self.roll_for_bonus()
            print(f"\nTotal bonus earned after {self.attempts} attempts: {total_bonus:.2f}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Configuration for crafting bonus rolls
    BASE_CHANCE = 0.3  # 30% chance of success
    BONUS_MULTIPLIER = 5.0  # Each successful roll gives 5 times the attempt number
    ATTEMPTS = 10  # Total number of attempts to roll

    # Create a CraftingBonusRoll instance and run the simulation
    crafting_bonus_roll = CraftingBonusRoll(BASE_CHANCE, BONUS_MULTIPLIER, ATTEMPTS)
    crafting_bonus_roll.run()
```
