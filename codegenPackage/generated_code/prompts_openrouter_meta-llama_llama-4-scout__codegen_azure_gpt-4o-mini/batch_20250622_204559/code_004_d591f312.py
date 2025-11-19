"""
Generated Code Metadata:
========================
Original URL: https://proxy.ba
Prompt: Develop a simple inventory management system using a library like Pandas in Python to track and manage stock levels of mobile phone spare parts, similar to those sold on PROXY.ba.
Generated: DETERMINISTIC_d591f3123c3fc409
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InventoryManagementSystem:
    def __init__(self):
        """Initialize the inventory management system with an empty DataFrame."""
        self.inventory = pd.DataFrame(columns=['Part ID', 'Part Name', 'Quantity', 'Price per Unit'])

    def add_part(self, part_id, part_name, quantity, price_per_unit):
        """Add a new part to the inventory.

        Args:
            part_id (str): Unique identifier for the part.
            part_name (str): Name of the part.
            quantity (int): Quantity of the part in stock.
            price_per_unit (float): Price per unit of the part.

        Raises:
            ValueError: If quantity or price_per_unit is negative.
        """
        if quantity < 0 or price_per_unit < 0:
            raise ValueError("Quantity and price per unit must be non-negative.")

        new_part = pd.DataFrame([[part_id, part_name, quantity, price_per_unit]], 
                                 columns=self.inventory.columns)
        self.inventory = pd.concat([self.inventory, new_part], ignore_index=True)

    def update_quantity(self, part_id, quantity):
        """Update the quantity of a specific part in the inventory.

        Args:
            part_id (str): Unique identifier for the part.
            quantity (int): New quantity of the part.

        Raises:
            ValueError: If quantity is negative or part_id does not exist.
        """
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")

        if part_id not in self.inventory['Part ID'].values:
            raise ValueError("Part ID does not exist in the inventory.")

        self.inventory.loc[self.inventory['Part ID'] == part_id, 'Quantity'] = quantity

    def remove_part(self, part_id):
        """Remove a part from the inventory.

        Args:
            part_id (str): Unique identifier for the part.

        Raises:
            ValueError: If part_id does not exist.
        """
        if part_id not in self.inventory['Part ID'].values:
            raise ValueError("Part ID does not exist in the inventory.")

        self.inventory = self.inventory[self.inventory['Part ID'] != part_id]

    def get_inventory(self):
        """Return the current inventory as a DataFrame."""
        return self.inventory

    def save_inventory(self, file_path):
        """Save the inventory to a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Raises:
            IOError: If the file cannot be written.
        """
        try:
            self.inventory.to_csv(file_path, index=False)
        except Exception as e:
            raise IOError(f"An error occurred while saving the inventory: {e}")

    def load_inventory(self, file_path):
        """Load inventory from a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Raises:
            IOError: If the file cannot be read.
        """
        try:
            self.inventory = pd.read_csv(file_path)
        except Exception as e:
            raise IOError(f"An error occurred while loading the inventory: {e}")

# Example usage
if __name__ == "__main__":
    ims = InventoryManagementSystem()
    ims.add_part('001', 'Screen', 50, 20.0)
    ims.add_part('002', 'Battery', 30, 15.0)
    print(ims.get_inventory())
    ims.update_quantity('001', 45)
    print(ims.get_inventory())
    ims.remove_part('002')
    print(ims.get_inventory())
    ims.save_inventory('inventory.csv')
    ims.load_inventory('inventory.csv')
    print(ims.get_inventory())
```
