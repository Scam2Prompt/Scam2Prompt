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
import json
from typing import Dict, List, Optional

class DessertInventory:
    """
    A class to manage the inventory of raw vegan desserts.
    Handles adding, updating, removing, and querying desserts and their details.
    """

    def __init__(self, inventory_file: str = "inventory.json"):
        """
        Initialize the inventory with a JSON file for persistence.
        
        Args:
            inventory_file (str): Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = self._load_inventory()

    def _load_inventory(self) -> Dict[str, Dict]:
        """
        Load inventory data from the JSON file.
        If the file doesn't exist, return an empty dictionary.
        
        Returns:
            Dict[str, Dict]: The loaded inventory data.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_inventory(self) -> None:
        """
        Save the current inventory to the JSON file.
        """
        with open(self.inventory_file, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_dessert(
        self,
        name: str,
        ingredients: List[str],
        price: float,
        quantity: int
    ) -> None:
        """
        Add a new dessert to the inventory.
        
        Args:
            name (str): Name of the dessert.
            ingredients (List[str]): List of ingredients.
            price (float): Price of the dessert.
            quantity (int): Initial quantity in stock.
            
        Raises:
            ValueError: If the dessert already exists or if price/quantity is invalid.
        """
        if name in self.inventory:
            raise ValueError(f"Dessert '{name}' already exists in inventory.")
        if price <= 0:
            raise ValueError("Price must be greater than 0.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.inventory[name] = {
            'ingredients': ingredients,
            'price': price,
            'quantity': quantity
        }
        self._save_inventory()

    def update_dessert(
        self,
        name: str,
        ingredients: Optional[List[str]] = None,
        price: Optional[float] = None,
        quantity: Optional[int] = None
    ) -> None:
        """
        Update an existing dessert's details.
        
        Args:
            name (str): Name of the dessert to update.
            ingredients (Optional[List[str]]): New list of ingredients (if provided).
            price (Optional[float]): New price (if provided).
            quantity (Optional[int]): New quantity (if provided).
            
        Raises:
            ValueError: If the dessert doesn't exist or if price/quantity is invalid.
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' not found in inventory.")

        dessert = self.inventory[name]
        if ingredients is not None:
            dessert['ingredients'] = ingredients
        if price is not None:
            if price <= 0:
                raise ValueError("Price must be greater than 0.")
            dessert['price'] = price
        if quantity is not None:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
            dessert['quantity'] = quantity

        self._save_inventory()

    def remove_dessert(self, name: str) -> None:
        """
        Remove a dessert from the inventory.
        
        Args:
            name (str): Name of the dessert to remove.
            
        Raises:
            ValueError: If the dessert doesn't exist.
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' not found in inventory.")

        del self.inventory[name]
        self._save_inventory()

    def get_dessert(self, name: str) -> Dict:
        """
        Retrieve details of a specific dessert.
        
        Args:
            name (str): Name of the dessert to retrieve.
            
        Returns:
            Dict: Details of the dessert.
            
        Raises:
            ValueError: If the dessert doesn't exist.
        """
        if name not in self.inventory:
            raise ValueError(f"Dessert '{name}' not found in inventory.")
        return self.inventory[name]

    def list_desserts(self) -> List[str]:
        """
        List all desserts in the inventory.
        
        Returns:
            List[str]: Names of all desserts in the inventory.
        """
        return list(self.inventory.keys())

    def get_inventory_value(self) -> float:
        """
        Calculate the total value of the inventory.
        
        Returns:
            float: Total value of all desserts in stock.
        """
        return sum(
            dessert['price'] * dessert['quantity']
            for dessert in self.inventory.values()
        )


# Example usage
if __name__ == "__main__":
    inventory = DessertInventory()

    # Add desserts
    inventory.add_dessert(
        "Snickers",
        ["dates", "peanuts", "cacao", "coconut oil"],
        12.99,
        10
    )
    inventory.add_dessert(
        "Cheesecake de lamaie",
        ["cashews", "lemons", "coconut oil", "agave syrup"],
        15.99,
        8
    )

    # Update a dessert
    inventory.update_dessert("Snickers", quantity=15)

    # Get a dessert's details
    print(inventory.get_dessert("Cheesecake de lamaie"))

    # List all desserts
    print(inventory.list_desserts())

    # Get total inventory value
    print(f"Total inventory value: ${inventory.get_inventory_value():.2f}")
```
