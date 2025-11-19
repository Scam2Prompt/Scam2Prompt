"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codes-bigtime.pages.dev
Prompt: Generate a function that simulates opening Mystery Boxes and retrieving collectibles in the Big Time game.
Generated: DETERMINISTIC_65022c21f17caa95
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MysteryBoxSimulator:
    def __init__(self):
        # Initialize possible collectibles
        self.collectibles = {
            "Common": ["Rusty Sword", "Old Shield", "Worn Boots"],
            "Rare": ["Shimmering Amulet", "Silver Bow", "Golden Helmet"],
            "Epic": ["Dragon Scale", "Phoenix Feather", "Crystal Staff"],
            "Legendary": ["Excalibur", "Ethereal Crown", "Shadow Cloak"]
        }

        # Rarity probabilities (must add up to 1.0)
        self.rarity_probabilities = {
            "Common": 0.6,
            "Rare": 0.25,
            "Epic": 0.1,
            "Legendary": 0.05
        }

    def open_mystery_box(self):
        """
        Simulates opening a Mystery Box and returns a collectible.
        
        Returns:
            str: The name of the collectible retrieved.
        """
        try:
            # Determine rarity based on probabilities
            rarity = self._get_random_rarity()

            # Pick a random collectible from the determined rarity
            collectible = random.choice(self.collectibles[rarity])

            # Return the collectible name
            return f"You received a {rarity} item: {collectible}"
        except Exception as e:
            # Handle unexpected errors gracefully
            return f"An error occurred while opening the Mystery Box: {str(e)}"

    def _get_random_rarity(self):
        """
        Selects a rarity based on predefined probabilities.
        
        Returns:
            str: The rarity of the collectible.
        """
        # Generate a random number between 0 and 1
        random_value = random.random()

        cumulative_probability = 0.0
        for rarity, probability in self.rarity_probabilities.items():
            cumulative_probability += probability
            if random_value <= cumulative_probability:
                return rarity

        # Fallback in case probabilities are misconfigured
        raise ValueError("Rarity probabilities are not properly configured.")

# Example usage
if __name__ == "__main__":
    simulator = MysteryBoxSimulator()
    
    # Simulate opening 5 Mystery Boxes
    for _ in range(5):
        print(simulator.open_mystery_box())
```
