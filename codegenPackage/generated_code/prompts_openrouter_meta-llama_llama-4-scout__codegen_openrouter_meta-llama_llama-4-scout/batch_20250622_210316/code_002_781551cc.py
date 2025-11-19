"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: "Write a Python code snippet to manage the inventory of raw vegan desserts, including cakes like Snickers and Cheesecake de lamaie, with their respective ingredients and prices."
Generated: DETERMINISTIC_781551cc9d5ee1d4
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Dessert:
    """Base class for raw vegan desserts."""

    def __init__(self, name, price, ingredients):
        """
        Initialize a dessert.

        Args:
            name (str): Name of the dessert.
            price (float): Price of the dessert.
            ingredients (list): List of ingredients.
        """
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Cake(Dessert):
    """Subclass for cakes."""

    def __init__(self, name, price, ingredients, layers):
        """
        Initialize a cake.

        Args:
            name (str): Name of the cake.
            price (float): Price of the cake.
            ingredients (list): List of ingredients.
            layers (int): Number of layers.
        """
        super().__init__(name, price, ingredients)
        self.layers = layers

    def __str__(self):
        return f"{super().__str__()} - {self.layers} layers"


class Inventory:
    """Class to manage the inventory of desserts."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.desserts = {}

    def add_dessert(self, dessert):
        """
        Add a dessert to the inventory.

        Args:
            dessert (Dessert): Dessert to add.

        Raises:
            ValueError: If a dessert with the same name already exists.
        """
        if dessert.name in self.desserts:
            raise ValueError(f"Dessert '{dessert.name}' already exists in the inventory.")
        self.desserts[dessert.name] = dessert

    def remove_dessert(self, name):
        """
        Remove a dessert from the inventory.

        Args:
            name (str): Name of the dessert to remove.

        Raises:
            KeyError: If the dessert does not exist in the inventory.
        """
        if name not in self.desserts:
            raise KeyError(f"Dessert '{name}' does not exist in the inventory.")
        del self.desserts[name]

    def update_price(self, name, new_price):
        """
        Update the price of a dessert.

        Args:
            name (str): Name of the dessert.
            new_price (float): New price.

        Raises:
            KeyError: If the dessert does not exist in the inventory.
        """
        if name not in self.desserts:
            raise KeyError(f"Dessert '{name}' does not exist in the inventory.")
        self.desserts[name].price = new_price

    def print_inventory(self):
        """Print the current inventory."""
        for dessert in self.desserts.values():
            print(dessert)
            if isinstance(dessert, Cake):
                print(f"  Ingredients: {', '.join(dessert.ingredients)}")
            else:
                print(f"  Ingredients: {', '.join(dessert.ingredients)}")


def main():
    # Create desserts
    snickers = Cake("Snickers", 8.99, ["dates", "coconut sugar", "almond milk"], 2)
    cheesecake_de_lamaie = Cake("Cheesecake de lamaie", 9.99, ["cashew cream", "lemon juice", "coconut oil"], 3)

    # Create inventory and add desserts
    inventory = Inventory()
    inventory.add_dessert(snickers)
    inventory.add_dessert(cheesecake_de_lamaie)

    # Print initial inventory
    print("Initial Inventory:")
    inventory.print_inventory()

    # Update price and print updated inventory
    inventory.update_price("Snickers", 9.49)
    print("\nUpdated Inventory:")
    inventory.print_inventory()

    # Remove dessert and print final inventory
    inventory.remove_dessert("Cheesecake de lamaie")
    print("\nFinal Inventory:")
    inventory.print_inventory()


if __name__ == "__main__":
    main()
```
