"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Suggest software tools or libraries for managing vertical storage systems and distribution centers, similar to those offered by PLM.
Generated: DETERMINISTIC_fa90ec4c368a6628
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
InventoryManagement.py

This module provides functionality for managing vertical storage systems
and distribution centers. It includes classes and methods to simulate
the management of storage items, track inventory levels, and handle
error cases appropriately.

Modules Used:
- `pandas`: For data management and manipulation
- `logging`: For logging errors and important information
"""

import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class StorageItem:
    """
    Class representing an item in the vertical storage system.
    
    Attributes:
    - name (str): The name of the storage item.
    - quantity (int): The available quantity of the item.
    - location (str): The storage location identifier.
    """
    
    def __init__(self, name, quantity, location):
        if quantity < 0:
            logging.error("Quantity cannot be negative.")
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.quantity = quantity
        self.location = location

    def update_quantity(self, change):
        """
        Updates the quantity of the storage item.
        
        Parameters:
        - change (int): The amount to add (if positive) or subtract (if negative).
        
        Raises:
        - ValueError: If resulting quantity would be negative.
        """
        if self.quantity + change < 0:
            logging.error("Cannot reduce quantity below zero.")
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += change
        logging.info(f"Updated quantity for {self.name}. New quantity: {self.quantity}")


class StorageSystem:
    """
    Class representing a vertical storage system.
    
    Attributes:
    - items (list): List of StorageItem objects representing items in the storage system.
    """
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds a new storage item to the system.
        
        Parameters:
        - item (StorageItem): The item to be added.
        """
        self.items.append(item)
        logging.info(f"Added item: {item.name}")

    def get_inventory_report(self):
        """
        Generates a report of the current inventory.
        
        Returns:
        - pd.DataFrame: DataFrame containing the inventory report.
        """
        data = [{'Name': item.name, 'Quantity': item.quantity, 'Location': item.location}
                for item in self.items]
        report = pd.DataFrame(data)
        logging.info("Generated inventory report.")
        return report

    def find_item(self, name):
        """
        Finds an item in the storage system by name.
        
        Parameters:
        - name (str): The name of the item to find.
        
        Returns:
        - StorageItem: The found StorageItem object, if it exists.
        
        Raises:
        - ValueError: If the item is not found.
        """
        for item in self.items:
            if item.name == name:
                logging.info(f"Item found: {item.name}")
                return item
        logging.error(f"Item not found: {name}")
        raise ValueError("Item not found.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a storage system instance
        storage_system = StorageSystem()

        # Add items to the storage system
        item1 = StorageItem("Item A", 100, "Location 1")
        storage_system.add_item(item1)

        item2 = StorageItem("Item B", 50, "Location 2")
        storage_system.add_item(item2)

        # Update item quantities
        item1.update_quantity(-20)

        # Generate inventory report
        report = storage_system.get_inventory_report()
        print(report)

        # Find an item
        found_item = storage_system.find_item("Item A")
        print(f"Found: {found_item.name}, Quantity: {found_item.quantity}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
