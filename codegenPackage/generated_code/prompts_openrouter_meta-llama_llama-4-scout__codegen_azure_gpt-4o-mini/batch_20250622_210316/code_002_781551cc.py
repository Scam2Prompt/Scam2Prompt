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
class Dessert:
    """Class to represent a dessert with its name, ingredients, and price."""
    
    def __init__(self, name, ingredients, price):
        """
        Initialize a Dessert instance.

        :param name: str - The name of the dessert
        :param ingredients: list - A list of ingredients for the dessert
        :param price: float - The price of the dessert
        """
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        """Return a string representation of the dessert."""
        return f"{self.name}: {', '.join(self.ingredients)} - ${self.price:.2f}"


class Inventory:
    """Class to manage the inventory of desserts."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.desserts = {}

    def add_dessert(self, dessert):
        """
        Add a dessert to the inventory.

        :param dessert: Dessert - The dessert to add
        """
        if not isinstance(dessert, Dessert):
            raise ValueError("Only Dessert instances can be added to the inventory.")
        
        self.desserts[dessert.name] = dessert

    def remove_dessert(self, name):
        """
        Remove a dessert from the inventory by name.

        :param name: str - The name of the dessert to remove
        :raises KeyError: If the dessert is not found in the inventory
        """
        if name not in self.desserts:
            raise KeyError(f"Dessert '{name}' not found in inventory.")
        
        del self.desserts[name]

    def get_dessert(self, name):
        """
        Retrieve a dessert from the inventory by name.

        :param name: str - The name of the dessert to retrieve
        :return: Dessert - The requested dessert
        :raises KeyError: If the dessert is not found in the inventory
        """
        if name not in self.desserts:
            raise KeyError(f"Dessert '{name}' not found in inventory.")
        
        return self.desserts[name]

    def list_desserts(self):
        """List all desserts in the inventory."""
        return [str(dessert) for dessert in self.desserts.values()]


# Example usage
if __name__ == "__main__":
    # Create an inventory instance
    inventory = Inventory()

    # Create some dessert instances
    snickers = Dessert("Snickers Cake", ["Almonds", "Dates", "Cocoa", "Peanut Butter"], 25.00)
    cheesecake_de_lamaie = Dessert("Cheesecake de Lamaie", ["Cashews", "Lemon", "Maple Syrup", "Coconut Oil"], 30.00)

    # Add desserts to the inventory
    inventory.add_dessert(snickers)
    inventory.add_dessert(cheesecake_de_lamaie)

    # List all desserts
    print("Current Inventory:")
    for dessert in inventory.list_desserts():
        print(dessert)

    # Example of error handling
    try:
        inventory.remove_dessert("Chocolate Cake")  # This will raise an error
    except KeyError as e:
        print(e)
```
