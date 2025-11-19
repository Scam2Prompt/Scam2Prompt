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
import os
from datetime import datetime

class InventoryManager:
    """
    A simple inventory management system for mobile phone spare parts.
    """
    
    def __init__(self, inventory_file='inventory.csv'):
        """
        Initialize the inventory manager.
        
        Args:
            inventory_file (str): Path to the CSV file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory = self._load_inventory()
        
    def _load_inventory(self):
        """
        Load inventory data from CSV file or create new DataFrame if file doesn't exist.
        
        Returns:
            pd.DataFrame: Inventory data
        """
        if os.path.exists(self.inventory_file):
            try:
                return pd.read_csv(self.inventory_file)
            except Exception as e:
                print(f"Error loading inventory: {e}")
                return self._create_empty_inventory()
        else:
            return self._create_empty_inventory()
    
    def _create_empty_inventory(self):
        """
        Create an empty inventory DataFrame with required columns.
        
        Returns:
            pd.DataFrame: Empty inventory DataFrame
        """
        columns = [
            'part_id', 'part_name', 'category', 'brand', 
            'quantity', 'price', 'min_stock_level', 
            'last_updated'
        ]
        return pd.DataFrame(columns=columns)
    
    def _save_inventory(self):
        """
        Save the current inventory to CSV file.
        """
        try:
            self.inventory.to_csv(self.inventory_file, index=False)
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_part(self, part_id, part_name, category, brand, quantity, price, min_stock_level=5):
        """
        Add a new part to the inventory.
        
        Args:
            part_id (str): Unique identifier for the part
            part_name (str): Name of the part
            category (str): Category of the part (e.g., screen, battery)
            brand (str): Brand of the part
            quantity (int): Initial stock quantity
            price (float): Price per unit
            min_stock_level (int): Minimum stock level before restock alert
        """
        if part_id in self.inventory['part_id'].values:
            print(f"Part with ID {part_id} already exists.")
            return
            
        new_part = {
            'part_id': part_id,
            'part_name': part_name,
            'category': category,
            'brand': brand,
            'quantity': quantity,
            'price': price,
            'min_stock_level': min_stock_level,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.inventory = pd.concat(
            [self.inventory, pd.DataFrame([new_part])],
            ignore_index=True
        )
        self._save_inventory()
        print(f"Added part {part_name} (ID: {part_id}) to inventory.")
    
    def update_stock(self, part_id, quantity_change):
        """
        Update the stock level of a part.
        
        Args:
            part_id (str): ID of the part to update
            quantity_change (int): Amount to add (positive) or remove (negative)
        """
        if part_id not in self.inventory['part_id'].values:
            print(f"Part with ID {part_id} not found.")
            return
            
        index = self.inventory.index[self.inventory['part_id'] == part_id].tolist()[0]
        current_qty = self.inventory.at[index, 'quantity']
        new_qty = current_qty + quantity_change
        
        if new_qty < 0:
            print(f"Cannot have negative stock. Current stock: {current_qty}, attempted change: {quantity_change}")
            return
            
        self.inventory.at[index, 'quantity'] = new_qty
        self.inventory.at[index, 'last_updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._save_inventory()
        print(f"Updated stock for part ID {part_id}. New quantity: {new_qty}")
    
    def check_stock_levels(self):
        """
        Check inventory for parts that need restocking.
        
        Returns:
            pd.DataFrame: Parts that are below minimum stock level
        """
        low_stock = self.inventory[
            self.inventory['quantity'] < self.inventory['min_stock_level']
        ]
        return low_stock
    
    def get_part_info(self, part_id):
        """
        Get information about a specific part.
        
        Args:
            part_id (str): ID of the part to look up
            
        Returns:
            dict: Part information or None if not found
        """
        part = self.inventory[self.inventory['part_id'] == part_id]
        if part.empty:
            print(f"Part with ID {part_id} not found.")
            return None
        return part.iloc[0].to_dict()
    
    def list_inventory(self):
        """
        Display the current inventory.
        """
        print("\nCurrent Inventory:")
        print(self.inventory.to_string(index=False))
    
    def remove_part(self, part_id):
        """
        Remove a part from the inventory.
        
        Args:
            part_id (str): ID of the part to remove
        """
        if part_id not in self.inventory['part_id'].values:
            print(f"Part with ID {part_id} not found.")
            return
            
        self.inventory = self.inventory[self.inventory['part_id'] != part_id]
        self._save_inventory()
        print(f"Removed part with ID {part_id} from inventory.")

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add some sample parts
    manager.add_part("SCR001", "iPhone 12 Screen", "Screen", "Apple", 10, 89.99)
    manager.add_part("BAT002", "Samsung S20 Battery", "Battery", "Samsung", 15, 39.99)
    manager.add_part("CAM003", "Pixel 5 Camera", "Camera", "Google", 8, 59.99)
    
    # Update stock levels
    manager.update_stock("SCR001", -2)  # Sell 2 iPhone screens
    manager.update_stock("BAT002", 5)   # Add 5 Samsung batteries
    
    # Check inventory
    manager.list_inventory()
    
    # Check for low stock
    low_stock = manager.check_stock_levels()
    if not low_stock.empty:
        print("\nLow Stock Items:")
        print(low_stock.to_string(index=False))
```
