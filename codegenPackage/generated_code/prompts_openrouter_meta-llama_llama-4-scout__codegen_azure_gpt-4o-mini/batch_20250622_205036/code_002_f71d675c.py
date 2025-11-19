"""
Generated Code Metadata:
========================
Original URL: https://poocoinswasopnet.blogspot.com
Prompt: Generate a Python code snippet to manage inventory for a shoe store with different types of shoes, including chuteira infantil and sapato social.
Generated: DETERMINISTIC_f71d675c2c1cb9fb
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Shoe:
    """Class to represent a shoe in the inventory."""
    
    def __init__(self, shoe_type, size, quantity):
        """
        Initialize a new shoe instance.

        :param shoe_type: str - Type of the shoe (e.g., 'chuteira infantil', 'sapato social')
        :param size: float - Size of the shoe
        :param quantity: int - Quantity of the shoe in stock
        """
        self.shoe_type = shoe_type
        self.size = size
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the shoe."""
        return f"{self.shoe_type} (Size: {self.size}) - Quantity: {self.quantity}"


class Inventory:
    """Class to manage the shoe inventory."""
    
    def __init__(self):
        """Initialize the inventory with an empty dictionary."""
        self.shoes = {}

    def add_shoe(self, shoe):
        """
        Add a shoe to the inventory.

        :param shoe: Shoe - The shoe object to add
        """
        if not isinstance(shoe, Shoe):
            raise ValueError("Only Shoe instances can be added to the inventory.")
        
        key = (shoe.shoe_type, shoe.size)
        if key in self.shoes:
            self.shoes[key].quantity += shoe.quantity
        else:
            self.shoes[key] = shoe

    def remove_shoe(self, shoe_type, size, quantity):
        """
        Remove a specified quantity of a shoe from the inventory.

        :param shoe_type: str - Type of the shoe to remove
        :param size: float - Size of the shoe to remove
        :param quantity: int - Quantity of the shoe to remove
        :raises ValueError: If the shoe is not found or quantity exceeds available stock
        """
        key = (shoe_type, size)
        if key not in self.shoes:
            raise ValueError("Shoe not found in inventory.")
        
        if self.shoes[key].quantity < quantity:
            raise ValueError("Not enough stock to remove the specified quantity.")
        
        self.shoes[key].quantity -= quantity
        if self.shoes[key].quantity == 0:
            del self.shoes[key]

    def get_inventory(self):
        """
        Get a list of all shoes in the inventory.

        :return: list - List of shoe objects in the inventory
        """
        return list(self.shoes.values())

    def __str__(self):
        """Return a string representation of the entire inventory."""
        return "\n".join(str(shoe) for shoe in self.get_inventory())


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()
        
        # Adding shoes to the inventory
        inventory.add_shoe(Shoe("chuteira infantil", 30, 10))
        inventory.add_shoe(Shoe("sapato social", 42, 5))
        
        print("Current Inventory:")
        print(inventory)
        
        # Removing shoes from the inventory
        inventory.remove_shoe("chuteira infantil", 30, 2)
        
        print("\nUpdated Inventory after removal:")
        print(inventory)
        
    except ValueError as e:
        print(f"Error: {e}")
```
