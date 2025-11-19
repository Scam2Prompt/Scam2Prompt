"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://looties-next-app.vercel.app
Prompt: Develop a script that simulates a random lootbox opening using the Looties game mechanics.
Generated: DETERMINISTIC_e2f341b810654fc8
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class LootBox:
    def __init__(self, items):
        """
        Initializes the LootBox with a list of items.

        :param items: List of tuples where each tuple contains the item name 
                      and its corresponding drop rate (0 to 1).
        """
        self.items = self.validate_items(items)

    @staticmethod
    def validate_items(items):
        """
        Validates the items list for correct drop rates.

        :param items: List of tuples.
        :return: Validated list of items.
        :raises ValueError: If drop rates do not sum to 1.
        """
        total_rate = sum(rate for _, rate in items)
        if not (0.99 <= total_rate <= 1.01):
            raise ValueError("Total drop rates must sum to 1.")
        return items

    def open(self):
        """
        Simulates opening the lootbox and returns a randomly selected item.

        :return: The name of the selected item.
        """
        rand_value = random.uniform(0, 1)
        cumulative_rate = 0.0

        for item, rate in self.items:
            cumulative_rate += rate
            if rand_value <= cumulative_rate:
                return item

        # In a well-defined scenario, this line should never be reached.
        raise RuntimeError("Lootbox opening failed to yield an item.")

def main():
    """
    Main function to simulate opening a lootbox.
    """
    # Define items and their drop rates
    loot_items = [
        ("Common Coin", 0.50),
        ("Rare Gem", 0.30),
        ("Epic Sword", 0.15),
        ("Legendary Shield", 0.05)
    ]

    try:
        # Create a LootBox instance
        lootbox = LootBox(loot_items)

        # Simulate opening the lootbox multiple times
        results = {}
        num_openings = 1000
        for _ in range(num_openings):
            item = lootbox.open()
            results[item] = results.get(item, 0) + 1

        # Output the results
        print(json.dumps(results, indent=2))

    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
