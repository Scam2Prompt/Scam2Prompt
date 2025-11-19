"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: "Write a Python code snippet to manage inventory for a wire mesh fence manufacturing company, including columns for product name, quantity, and supplier information."
Generated: DETERMINISTIC_ab653c2de53f2ad5
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class InventoryManager:
    """
    A class to manage the inventory of a wire mesh fence manufacturing company.
    """

    def __init__(self):
        """
        Initializes the InventoryManager with an empty DataFrame.
        """
        self.inventory = pd.DataFrame(columns=['Product Name', 'Quantity', 'Supplier'])

    def add_product(self, product_name: str, quantity: int, supplier: str):
        """
        Adds a new product to the inventory.

        :param product_name: Name of the product
        :param quantity: Quantity of the product
        :param supplier: Supplier information
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        new_product = {'Product Name': product_name, 'Quantity': quantity, 'Supplier': supplier}
        self.inventory = self.inventory.append(new_product, ignore_index=True)

    def update_quantity(self, product_name: str, quantity: int):
        """
        Updates the quantity of an existing product in the inventory.

        :param product_name: Name of the product to update
        :param quantity: New quantity of the product
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_name not in self.inventory['Product Name'].values:
            raise ValueError("Product not found in inventory.")
        
        self.inventory.loc[self.inventory['Product Name'] == product_name, 'Quantity'] = quantity

    def remove_product(self, product_name: str):
        """
        Removes a product from the inventory.

        :param product_name: Name of the product to remove
        """
        if product_name not in self.inventory['Product Name'].values:
            raise ValueError("Product not found in inventory.")
        
        self.inventory = self.inventory[self.inventory['Product Name'] != product_name]

    def get_inventory(self):
        """
        Returns the current inventory as a DataFrame.

        :return: DataFrame containing the inventory
        """
        return self.inventory

    def save_inventory(self, file_path: str):
        """
        Saves the current inventory to a CSV file.

        :param file_path: Path to the CSV file
        """
        try:
            self.inventory.to_csv(file_path, index=False)
        except Exception as e:
            raise IOError(f"An error occurred while saving the inventory: {e}")

    def load_inventory(self, file_path: str):
        """
        Loads inventory from a CSV file.

        :param file_path: Path to the CSV file
        """
        try:
            self.inventory = pd.read_csv(file_path)
        except FileNotFoundError:
            raise FileNotFoundError("The specified file was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise IOError(f"An error occurred while loading the inventory: {e}")

# Example usage:
if __name__ == "__main__":
    manager = InventoryManager()
    manager.add_product("Wire Mesh", 100, "Supplier A")
    manager.update_quantity("Wire Mesh", 150)
    print(manager.get_inventory())
    manager.save_inventory("inventory.csv")
```
