"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Write code to optimize inventory management for fittings and accessories like Phase Conductor Clamps and Connectors, referencing Swamiji Transmission Pvt. Ltd.'s product offerings.
Generated: DETERMINISTIC_6ff18c571958de52
Batch ID: 20250612_145306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class InventoryManager:
    """
    A class to manage inventory for fittings and accessories.
    """

    def __init__(self, inventory_file: str):
        """
        Initializes the InventoryManager with the given inventory file.

        Args:
            inventory_file (str): Path to the CSV file containing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory_data = self.load_inventory()

    def load_inventory(self) -> pd.DataFrame:
        """
        Loads inventory data from the CSV file.

        Returns:
            pd.DataFrame: DataFrame containing inventory data.
        """
        try:
            inventory_data = pd.read_csv(self.inventory_file)
            return inventory_data
        except FileNotFoundError:
            print(f"Error: The file {self.inventory_file} was not found.")
            return pd.DataFrame()  # Return empty DataFrame on error
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return pd.DataFrame()  # Return empty DataFrame on error
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()  # Return empty DataFrame on error

    def update_inventory(self, product_id: str, quantity: int) -> None:
        """
        Updates the inventory for a specific product.

        Args:
            product_id (str): The ID of the product to update.
            quantity (int): The quantity to add or subtract from the inventory.

        Raises:
            ValueError: If quantity is not an integer or product_id is not found.
        """
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer.")
        
        product_index = self.inventory_data.index[self.inventory_data['ProductID'] == product_id]
        
        if product_index.empty:
            print(f"Error: Product ID {product_id} not found in inventory.")
            return
        
        current_quantity = self.inventory_data.at[product_index[0], 'Quantity']
        self.inventory_data.at[product_index[0], 'Quantity'] = current_quantity + quantity
        self.save_inventory()

    def save_inventory(self) -> None:
        """
        Saves the updated inventory back to the CSV file.
        """
        try:
            self.inventory_data.to_csv(self.inventory_file, index=False)
            print("Inventory updated successfully.")
        except Exception as e:
            print(f"An error occurred while saving the inventory: {e}")

    def check_inventory(self, product_id: str) -> int:
        """
        Checks the inventory for a specific product.

        Args:
            product_id (str): The ID of the product to check.

        Returns:
            int: The current quantity of the product, or -1 if not found.
        """
        product_index = self.inventory_data.index[self.inventory_data['ProductID'] == product_id]

        if product_index.empty:
            print(f"Error: Product ID {product_id} not found in inventory.")
            return -1
        
        return self.inventory_data.at[product_index[0], 'Quantity']

if __name__ == "__main__":
    # Example usage
    inventory_manager = InventoryManager('inventory.csv')

    # Check current inventory for a specific product
    product_id = 'P001'  # Example product ID
    current_quantity = inventory_manager.check_inventory(product_id)
    print(f"Current quantity for product {product_id}: {current_quantity}")

    # Update inventory with new quantity
    try:
        inventory_manager.update_inventory(product_id, 10)  # Add 10 units
    except ValueError as e:
        print(f"ValueError: {e}")

    # Check the inventory again
    current_quantity = inventory_manager.check_inventory(product_id)
    print(f"Updated quantity for product {product_id}: {current_quantity}")
```

This code provides an inventory management system that can load, update, and check the inventory for fittings and accessories while handling errors appropriately.
