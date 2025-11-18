"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Generate a Python script to manage inventory for digital products like "5300 جم زپتو" and "35000 جم کلش رویال," ensuring stock updates based on user purchases.
Generated: DETERMINISTIC_e2e2d71d1cf2058c
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InventoryManager:
    """
    A class to manage inventory for digital products.
    """

    def __init__(self, inventory_file="inventory.json"):
        """
        Initialize the inventory manager.

        Args:
            inventory_file (str): Path to the JSON file containing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self._load_inventory()

    def _load_inventory(self):
        """
        Load inventory data from a JSON file.

        Returns:
            dict: Inventory data.
        """
        try:
            with open(self.inventory_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            # If the file does not exist, return an empty inventory
            return {}
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in inventory file.")

    def _save_inventory(self):
        """
        Save the current inventory data to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w', encoding='utf-8') as file:
                json.dump(self.inventory, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save inventory: {str(e)}")

    def add_product(self, product_name, stock):
        """
        Add a new product to the inventory.

        Args:
            product_name (str): Name of the product.
            stock (int): Initial stock for the product.
        """
        if product_name in self.inventory:
            raise ValueError(f"Product '{product_name}' already exists in inventory.")
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

        self.inventory[product_name] = stock
        self._save_inventory()

    def update_stock(self, product_name, stock_change):
        """
        Update the stock of a product based on user purchases.

        Args:
            product_name (str): Name of the product.
            stock_change (int): Change in stock (negative for purchases).

        Raises:
            ValueError: If the product does not exist or stock would become negative.
        """
        if product_name not in self.inventory:
            raise ValueError(f"Product '{product_name}' does not exist in inventory.")
        if self.inventory[product_name] + stock_change < 0:
            raise ValueError("Stock cannot be negative after the update.")

        self.inventory[product_name] += stock_change
        self._save_inventory()

    def display_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for product, stock in self.inventory.items():
            print(f"{product}: {stock} units")


# Example usage of the InventoryManager class
if __name__ == "__main__":
    try:
        # Initialize inventory manager
        manager = InventoryManager()

        # Add products to inventory
        manager.add_product("5300 جم زپتو", 100)
        manager.add_product("35000 جم کلش رویال", 50)

        # Display inventory
        manager.display_inventory()

        # Update stock based on user purchases
        manager.update_stock("5300 جم زپتو", -10)  # User purchased 10 units
        manager.update_stock("35000 جم کلش رویال", -5)  # User purchased 5 units

        # Display updated inventory
        manager.display_inventory()

    except Exception as e:
        print(f"Error: {str(e)}")
```
