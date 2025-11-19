"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Generate a Python function that calculates the drop rate for different rarities of Meowgon NFTs based on the provided percentages.
Generated: DETERMINISTIC_bf9fc871e874d195
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class NFTDropRateCalculator:
    def __init__(self, rarity_percentages):
        """
        Initializes the NFTDropRateCalculator with the given rarity percentages.

        :param rarity_percentages: A dictionary where keys are rarity names (str)
                                   and values are their respective drop rates (float).
        """
        if not isinstance(rarity_percentages, dict):
            raise ValueError("rarity_percentages must be a dictionary.")
        
        total_percentage = sum(rarity_percentages.values())
        if total_percentage != 100.0:
            raise ValueError("Total percentage of rarities must equal 100.")

        self.rarity_percentages = rarity_percentages

    def calculate_drop(self):
        """
        Simulates an NFT drop based on the defined rarity percentages.

        :return: The rarity of the dropped NFT (str).
        """
        # Generate a random number between 0 and 100
        random_value = random.uniform(0, 100)
        cumulative_percentage = 0.0

        # Determine the rarity based on the random value
        for rarity, percentage in self.rarity_percentages.items():
            cumulative_percentage += percentage
            if random_value <= cumulative_percentage:
                return rarity
        
        # This point should never be reached if the inputs are valid
        raise RuntimeError("Drop calculation failed, check rarity percentages.")

# Example usage:
if __name__ == "__main__":
    try:
        # Define rarity percentages for Meowgon NFTs
        rarity_percentages = {
            "Common": 50.0,
            "Rare": 30.0,
            "Epic": 15.0,
            "Legendary": 5.0
        }

        # Create the drop rate calculator
        calculator = NFTDropRateCalculator(rarity_percentages)

        # Simulate a drop
        dropped_rarity = calculator.calculate_drop()
        print(f"Dropped NFT rarity: {dropped_rarity}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
