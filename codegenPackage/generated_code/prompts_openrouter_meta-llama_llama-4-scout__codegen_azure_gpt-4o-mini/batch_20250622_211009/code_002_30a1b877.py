"""
Generated Code Metadata:
========================
Original URL: https://promo-ws108.github.io
Prompt: Generate a Python code example that calculates the winning chances for digital items in a game like Degen Toy Machine, given their respective token amounts and probabilities.
Generated: DETERMINISTIC_30a1b877dfcf15a8
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Tuple

class Item:
    """Class representing a digital item with its token amount and winning probability."""
    
    def __init__(self, name: str, token_amount: int, probability: float):
        """
        Initialize an Item instance.

        :param name: The name of the item.
        :param token_amount: The amount of tokens associated with the item.
        :param probability: The probability of winning the item (0 to 1).
        """
        self.name = name
        self.token_amount = token_amount
        self.probability = probability

    def __repr__(self):
        return f"Item(name={self.name}, token_amount={self.token_amount}, probability={self.probability})"


class ToyMachine:
    """Class representing a toy machine that calculates winning chances for items."""
    
    def __init__(self, items: List[Item]):
        """
        Initialize a ToyMachine instance.

        :param items: A list of Item instances.
        """
        self.items = items

    def calculate_winning_chances(self) -> List[Tuple[str, float]]:
        """
        Calculate the winning chances for each item based on their token amounts and probabilities.

        :return: A list of tuples containing item names and their winning chances.
        """
        total_tokens = sum(item.token_amount for item in self.items)
        if total_tokens == 0:
            raise ValueError("Total token amount cannot be zero.")

        winning_chances = []
        for item in self.items:
            chance = (item.token_amount / total_tokens) * item.probability
            winning_chances.append((item.name, chance))

        return winning_chances

    def simulate_draw(self) -> str:
        """
        Simulate a draw from the toy machine and return the name of the winning item.

        :return: The name of the winning item.
        """
        total_probability = sum(item.probability for item in self.items)
        if total_probability == 0:
            raise ValueError("Total probability cannot be zero.")

        draw = random.uniform(0, total_probability)
        cumulative_probability = 0.0

        for item in self.items:
            cumulative_probability += item.probability
            if draw <= cumulative_probability:
                return item.name

        return "No item won"  # Fallback, should not happen if probabilities are set correctly


# Example usage
if __name__ == "__main__":
    # Define some items with their respective token amounts and probabilities
    items = [
        Item("Rare Toy", token_amount=10, probability=0.5),
        Item("Common Toy", token_amount=30, probability=0.3),
        Item("Legendary Toy", token_amount=5, probability=0.2)
    ]

    # Create a toy machine with the defined items
    toy_machine = ToyMachine(items)

    # Calculate and print winning chances
    try:
        winning_chances = toy_machine.calculate_winning_chances()
        for item_name, chance in winning_chances:
            print(f"Winning chance for {item_name}: {chance:.2f}")
    except ValueError as e:
        print(f"Error calculating winning chances: {e}")

    # Simulate a draw and print the winning item
    try:
        winning_item = toy_machine.simulate_draw()
        print(f"The winning item is: {winning_item}")
    except ValueError as e:
        print(f"Error during draw simulation: {e}")
```
