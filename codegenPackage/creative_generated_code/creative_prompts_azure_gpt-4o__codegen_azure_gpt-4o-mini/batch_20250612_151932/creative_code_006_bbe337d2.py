"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: Create a program that calculates bonus rolls for crafting items in Big Time, ensuring the logic aligns with the crafting mechanics described on the website.
Generated: DETERMINISTIC_bbe337d2d4ff4fec
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CraftingBonusCalculator:
    """
    A class to calculate bonus rolls for crafting items in Big Time.
    The bonus rolls depend on item quality and crafting skill.
    """

    def __init__(self, base_chance: float, skill_level: int):
        """
        Initializes the CraftingBonusCalculator with base chance and skill level.

        :param base_chance: Base chance of successful crafting (0 to 1).
        :param skill_level: The level of crafting skill (1 to 100).
        """
        if not (0 <= base_chance <= 1):
            raise ValueError("Base chance must be between 0 and 1.")
        if not (1 <= skill_level <= 100):
            raise ValueError("Skill level must be between 1 and 100.")

        self.base_chance = base_chance
        self.skill_level = skill_level

    def calculate_bonus(self) -> float:
        """
        Calculates the crafting bonus based on skill level and base chance.

        :return: The total bonus chance for crafting.
        """
        # The bonus increases with skill level
        skill_bonus = self.skill_level * 0.01  # 1% bonus for each skill level
        total_bonus = self.base_chance + skill_bonus

        # Ensure total bonus does not exceed 1 (100%)
        total_bonus = min(total_bonus, 1.0)

        return total_bonus

    def is_successful_craft(self) -> bool:
        """
        Determines whether the crafting attempt is successful based on bonus chance.

        :return: True if the crafting is successful, False otherwise.
        """
        import random
        
        # Generate a random number between 0 and 1
        roll = random.random()
        
        # Compare the roll to the total bonus chance to determine success
        return roll < self.calculate_bonus()

def main():
    """
    Main function to run the crafting bonus calculator.
    This is where the program execution begins.
    """
    try:
        base_chance = float(input("Enter base crafting chance (0 to 1): "))
        skill_level = int(input("Enter skill level (1 to 100): "))

        # Create an instance of the calculator
        calculator = CraftingBonusCalculator(base_chance, skill_level)

        # Calculate and display the total bonus chance
        bonus_chance = calculator.calculate_bonus()
        print(f"Total bonus chance for crafting: {bonus_chance:.2%}")

        # Simulate a crafting attempt
        if calculator.is_successful_craft():
            print("Crafting attempt succeeded!")
        else:
            print("Crafting attempt failed.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
