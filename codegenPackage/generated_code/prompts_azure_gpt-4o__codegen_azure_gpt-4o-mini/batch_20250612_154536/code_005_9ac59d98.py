"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: Write code to simulate the production of EVA masterbatches with special effects, referencing Ray Colors' product descriptions.
Generated: DETERMINISTIC_9ac59d98b0584d6f
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict

class Masterbatch:
    """
    A class to represent a masterbatch with special effects.
    """

    def __init__(self, name: str, color: str, effect: str, quantity: int):
        """
        Initializes a new Masterbatch instance.

        :param name: The name of the masterbatch.
        :param color: The color of the masterbatch.
        :param effect: The special effect of the masterbatch.
        :param quantity: The quantity produced in grams.
        """
        self.name = name
        self.color = color
        self.effect = effect
        self.quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the Masterbatch instance.
        """
        return f"{self.name} - Color: {self.color}, Effect: {self.effect}, Quantity: {self.quantity}g"


class MasterbatchProduction:
    """
    A class to simulate the production of EVA masterbatches with special effects.
    """

    def __init__(self):
        """
        Initializes the production simulator with predefined masterbatch specifications.
        """
        self.masterbatches: List[Masterbatch] = []
        self.product_descriptions = [
            {"name": "EVA Glitter", "color": "Transparent", "effect": "Glitter"},
            {"name": "EVA Fluorescent", "color": "Yellow", "effect": "Fluorescent"},
            {"name": "EVA Metallic", "color": "Silver", "effect": "Metallic"},
            {"name": "EVA Glow-in-the-Dark", "color": "Green", "effect": "Glow-in-the-Dark"},
            {"name": "EVA Color-Changing", "color": "Red", "effect": "Color-Changing"},
        ]

    def produce_masterbatch(self, quantity: int) -> None:
        """
        Produces a random masterbatch based on predefined specifications.

        :param quantity: The quantity to produce in grams.
        :raises ValueError: If the quantity is not a positive integer.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        # Select a random product description
        product = random.choice(self.product_descriptions)
        masterbatch = Masterbatch(
            name=product["name"],
            color=product["color"],
            effect=product["effect"],
            quantity=quantity
        )
        self.masterbatches.append(masterbatch)
        print(f"Produced: {masterbatch}")

    def produce_batch(self, batch_size: int, quantity_per_masterbatch: int) -> None:
        """
        Produces a batch of masterbatches.

        :param batch_size: The number of masterbatches to produce.
        :param quantity_per_masterbatch: The quantity of each masterbatch in grams.
        :raises ValueError: If batch_size or quantity_per_masterbatch is not a positive integer.
        """
        if batch_size <= 0 or quantity_per_masterbatch <= 0:
            raise ValueError("Both batch size and quantity per masterbatch must be positive integers.")

        for _ in range(batch_size):
            self.produce_masterbatch(quantity_per_masterbatch)

    def get_produced_masterbatches(self) -> List[Masterbatch]:
        """
        Returns the list of produced masterbatches.

        :return: A list of Masterbatch instances.
        """
        return self.masterbatches


if __name__ == "__main__":
    try:
        # Create a production simulator instance
        production_simulator = MasterbatchProduction()

        # Produce a batch of 5 masterbatches, each with a quantity of 100 grams
        production_simulator.produce_batch(batch_size=5, quantity_per_masterbatch=100)

        # Retrieve and display all produced masterbatches
        produced_masterbatches = production_simulator.get_produced_masterbatches()
        print("\nAll Produced Masterbatches:")
        for mb in produced_masterbatches:
            print(mb)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
