"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Write code to automate warehousing operations with customized storage solutions, referencing Bin Qutab Logistics' flexible options for dedicated storage facilities.
Generated: DETERMINISTIC_03f6608c05c527a9
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Warehouse:
    """
    A class to represent a warehouse with customizable storage solutions.
    """

    def __init__(self, name: str, capacity: int):
        """
        Initializes a Warehouse instance with a name and capacity.

        :param name: The name of the warehouse.
        :param capacity: The maximum capacity of items the warehouse can hold.
        """
        self.name = name
        self.capacity = capacity
        self.current_stock = {}
    
    def add_item(self, item_name: str, quantity: int):
        """
        Adds items to the warehouse stock.

        :param item_name: The name of the item to add.
        :param quantity: The quantity of the item to add.
        :raises ValueError: If the quantity exceeds the available capacity.
        """
        if self.total_stock() + quantity > self.capacity:
            raise ValueError("Cannot add items: Exceeds warehouse capacity.")
        
        if item_name in self.current_stock:
            self.current_stock[item_name] += quantity
        else:
            self.current_stock[item_name] = quantity

    def remove_item(self, item_name: str, quantity: int):
        """
        Removes items from the warehouse stock.

        :param item_name: The name of the item to remove.
        :param quantity: The quantity of the item to remove.
        :raises ValueError: If the item does not exist or quantity is insufficient.
        """
        if item_name not in self.current_stock:
            raise ValueError("Cannot remove items: Item does not exist.")
        
        if self.current_stock[item_name] < quantity:
            raise ValueError("Cannot remove items: Insufficient quantity in stock.")
        
        self.current_stock[item_name] -= quantity
        if self.current_stock[item_name] == 0:
            del self.current_stock[item_name]

    def total_stock(self) -> int:
        """
        Calculates the total number of items in the warehouse.

        :return: Total number of items in stock.
        """
        return sum(self.current_stock.values())

    def get_stock(self) -> dict:
        """
        Returns the current stock of items in the warehouse.

        :return: A dictionary of item names and their quantities.
        """
        return self.current_stock

    def __str__(self):
        """
        Returns a string representation of the warehouse's current state.
        
        :return: A string description of the warehouse name, capacity, and current stock.
        """
        return f"Warehouse '{self.name}' - Capacity: {self.capacity}, Current Stock: {self.current_stock}"


# Example usage
if __name__ == "__main__":
    try:
        warehouse = Warehouse("Bin Qutab Logistics", 1000)
        warehouse.add_item("Widgets", 250)
        warehouse.add_item("Gadgets", 500)
        print(warehouse)

        warehouse.remove_item("Widgets", 100)
        print(warehouse)

        # Attempting to exceed capacity
        warehouse.add_item("Doodads", 900)  # This should raise an error
    except ValueError as e:
        print(f"Error: {e}")
```
