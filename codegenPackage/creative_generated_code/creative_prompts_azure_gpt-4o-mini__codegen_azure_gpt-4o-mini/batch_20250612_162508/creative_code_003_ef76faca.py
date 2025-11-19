"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Generate a function that calculates the probability of winning for different items in the Degen Toy Machine inventory.
Generated: DETERMINISTIC_ef76faca17b60913
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class DegenToyMachine:
    def __init__(self, inventory):
        """
        Initializes the Degen Toy Machine with a given inventory.

        :param inventory: A dictionary where keys are item names and values are their respective quantities.
        """
        self.inventory = inventory
        self.total_items = sum(inventory.values())

    def calculate_probability(self, item):
        """
        Calculates the probability of winning a specific item from the toy machine.

        :param item: The name of the item for which the probability will be calculated.
        :return: The probability of winning the item as a float. Returns None if the item does not exist.
        """
        try:
            if self.total_items == 0:
                raise ValueError("The inventory is empty. Cannot calculate probabilities.")

            item_quantity = self.inventory.get(item, 0)

            if item_quantity == 0:
                print(f"Item '{item}' not found in inventory.")
                return None

            probability = item_quantity / self.total_items
            return probability

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def calculate_all_probabilities(self):
        """
        Calculates the winning probabilities for all items in the inventory.

        :return: A dictionary with items as keys and their winning probabilities as values.
        """
        probabilities = {}
        for item in self.inventory.keys():
            probabilities[item] = self.calculate_probability(item)
        return probabilities


# Example usage:
if __name__ == "__main__":
    # Define the toy machine inventory
    toy_machine_inventory = {
        "Teddy Bear": 10,
        "Action Figure": 5,
        "Rubber Duck": 20
    }

    # Create an instance of the DegenToyMachine
    toy_machine = DegenToyMachine(toy_machine_inventory)

    # Calculate probabilities for specific items
    print("Probability of winning a Teddy Bear:", toy_machine.calculate_probability("Teddy Bear"))
    print("Probability of winning a Rubber Duck:", toy_machine.calculate_probability("Rubber Duck"))

    # Calculate probabilities for all items
    all_probabilities = toy_machine.calculate_all_probabilities()
    print("All item probabilities:", all_probabilities)
```
