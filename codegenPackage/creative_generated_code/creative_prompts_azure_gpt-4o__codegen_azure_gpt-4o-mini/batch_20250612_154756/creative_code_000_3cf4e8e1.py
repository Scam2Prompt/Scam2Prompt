"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Write a Python script to calculate the cost of leveling up in STEPN based on the recommended point distribution provided in the blog.
Generated: DETERMINISTIC_3cf4e8e1942f9ff6
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class LevelUpCostCalculator:
    """
    A class to calculate the cost of leveling up in the STEPN game based on
    the recommended point distribution provided in a blog.
    """

    def __init__(self, base_cost=100, cost_increase_factor=1.2):
        """
        Initializes the LevelUpCostCalculator.
        
        :param base_cost: The base cost for the first level up.
        :param cost_increase_factor: The factor by which the cost increases per level.
        """
        self.base_cost = base_cost
        self.cost_increase_factor = cost_increase_factor

    def calculate_cost(self, levels):
        """
        Calculates the total cost of leveling up for a given number of levels.
        
        :param levels: The number of levels to level up.
        :return: The total cost for leveling up.
        """
        total_cost = 0

        for level in range(levels):
            level_cost = self.base_cost * (self.cost_increase_factor ** level)
            total_cost += level_cost

        return total_cost

    def display_cost(self, levels):
        """
        Displays the calculated cost in a user-friendly format.
        
        :param levels: The number of levels to level up.
        """
        try:
            total_cost = self.calculate_cost(levels)
            print(f"Total cost to level up {levels} levels: {total_cost:.2f} in-game currency.")
        except Exception as e:
            print(f"An error occurred while calculating the cost: {e}")

def main():
    """
    Main function to execute the level-up cost calculation.
    """
    # Define the number of levels to level up
    levels_to_level_up = 5

    # Create an instance of the calculator
    calculator = LevelUpCostCalculator()

    # Display the cost
    calculator.display_cost(levels_to_level_up)

if __name__ == "__main__":
    main()
```
