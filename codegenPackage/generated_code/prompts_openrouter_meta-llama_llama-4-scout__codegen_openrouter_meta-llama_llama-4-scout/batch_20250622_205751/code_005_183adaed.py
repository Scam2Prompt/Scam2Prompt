"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Develop a solution brief for implementing OpSense's remote monitoring system in a convenience store to reduce perishable inventory loss and ensure equipment operates at peak efficiency.
Generated: DETERMINISTIC_183adaed18f16ea6
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
OpSense Remote Monitoring System Implementation

This script provides a basic implementation of OpSense's remote monitoring system 
for a convenience store. It includes features to monitor perishable inventory levels 
and ensure equipment operates at peak efficiency.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import time
from datetime import datetime
import random

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Equipment:
    """Represents a store equipment with a name and operating status."""
    
    def __init__(self, name):
        """
        Initializes an Equipment object.

        Args:
            name (str): The name of the equipment.
        """
        self.name = name
        self.is_operating = True  # Assume equipment is operating by default

    def update_status(self, status):
        """
        Updates the operating status of the equipment.

        Args:
            status (bool): The new operating status.
        """
        self.is_operating = status

class Inventory:
    """Represents a store inventory with a list of perishable items."""
    
    def __init__(self):
        """
        Initializes an Inventory object.
        """
        self.items = {}

    def add_item(self, name, quantity, expiration_date):
        """
        Adds a perishable item to the inventory.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            expiration_date (str): The expiration date of the item (YYYY-MM-DD).
        """
        self.items[name] = {
            'quantity': quantity,
            'expiration_date': expiration_date
        }

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a perishable item.

        Args:
            name (str): The name of the item.
            quantity (int): The new quantity of the item.
        """
        if name in self.items:
            self.items[name]['quantity'] = quantity
        else:
            logging.warning(f"Item '{name}' not found in inventory.")

class RemoteMonitoringSystem:
    """Represents the OpSense remote monitoring system."""
    
    def __init__(self):
        """
        Initializes a RemoteMonitoringSystem object.
        """
        self.equipment = []
        self.inventory = Inventory()

    def add_equipment(self, equipment):
        """
        Adds equipment to the monitoring system.

        Args:
            equipment (Equipment): The equipment to add.
        """
        self.equipment.append(equipment)

    def monitor_equipment(self):
        """
        Monitors the operating status of all equipment.

        Returns:
            list: A list of equipment with their operating status.
        """
        equipment_status = []
        for equipment in self.equipment:
            equipment_status.append({
                'name': equipment.name,
                'is_operating': equipment.is_operating
            })
        return equipment_status

    def monitor_inventory(self):
        """
        Monitors the perishable inventory levels.

        Returns:
            dict: A dictionary of perishable items with their quantity and expiration date.
        """
        return self.inventory.items

def main():
    # Create a remote monitoring system
    rms = RemoteMonitoringSystem()

    # Create equipment
    fridge = Equipment('Fridge')
    freezer = Equipment('Freezer')

    # Add equipment to the monitoring system
    rms.add_equipment(fridge)
    rms.add_equipment(freezer)

    # Simulate equipment status updates
    fridge.update_status(False)  # Fridge is not operating
    freezer.update_status(True)   # Freezer is operating

    # Create perishable inventory
    rms.inventory.add_item('Milk', 10, '2024-09-20')
    rms.inventory.add_item('Eggs', 20, '2024-09-25')

    # Simulate inventory quantity updates
    rms.inventory.update_quantity('Milk', 5)

    # Monitor equipment and inventory
    equipment_status = rms.monitor_equipment()
    inventory_levels = rms.monitor_inventory()

    # Log monitoring results
    logging.info('Equipment Status:')
    for status in equipment_status:
        logging.info(f"{status['name']}: {'Operating' if status['is_operating'] else 'Not Operating'}")

    logging.info('\nInventory Levels:')
    for item, details in inventory_levels.items():
        logging.info(f"{item}: {details['quantity']} (Expires: {details['expiration_date']})")

if __name__ == '__main__':
    main()
```
