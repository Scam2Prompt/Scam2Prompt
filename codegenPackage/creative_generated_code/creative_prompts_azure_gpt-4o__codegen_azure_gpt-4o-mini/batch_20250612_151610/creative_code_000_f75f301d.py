"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Write a Python script to manage an inventory system for machinery parts, specifically for brands like FIATALLIS, CATERPILLAR, JOHN DEERE, KOMATSU, and IVECO, as described by Track Diesel Peru.
Generated: DETERMINISTIC_f75f301d3dbfca46
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class InventoryManager:
    """
    A class to manage an inventory of machinery parts for specific brands.
    Supports adding, updating, deleting, and retrieving parts information.
    """

    def __init__(self, filename='inventory.json'):
        """
        Initializes the InventoryManager with a specified JSON file to store inventory data.
        
        Args:
            filename (str): The name of the JSON file. Default is 'inventory.json'.
        """
        self.filename = filename
        self.inventory = self.load_inventory()

    def load_inventory(self):
        """
        Loads the inventory from the JSON file.

        Returns:
            dict: The loaded inventory data.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_inventory(self):
        """
        Saves the current inventory to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def add_part(self, brand, part_number, quantity, description):
        """
        Adds a new part to the inventory.
        
        Args:
            brand (str): The brand of the machinery part.
            part_number (str): The part number.
            quantity (int): The quantity of the part.
            description (str): A description of the part.
        """
        if brand not in ['FIATALLIS', 'CATERPILLAR', 'JOHN DEERE', 'KOMATSU', 'IVECO']:
            raise ValueError("Brand not supported")

        if part_number in self.inventory:
            raise ValueError("Part number already exists")

        self.inventory[part_number] = {
            'brand': brand,
            'quantity': quantity,
            'description': description
        }
        self.save_inventory()

    def update_part(self, part_number, quantity=None, description=None):
        """
        Updates the information of an existing part in the inventory.
        
        Args:
            part_number (str): The part number to update.
            quantity (int, optional): New quantity of the part.
            description (str, optional): New description of the part.
        
        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.inventory:
            raise KeyError("Part number not found")
        
        if quantity is not None:
            self.inventory[part_number]['quantity'] = quantity

        if description is not None:
            self.inventory[part_number]['description'] = description
        
        self.save_inventory()

    def delete_part(self, part_number):
        """
        Deletes a part from the inventory.
        
        Args:
            part_number (str): The part number to delete.
        
        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.inventory:
            raise KeyError("Part number not found")
        
        del self.inventory[part_number]
        self.save_inventory()

    def get_part(self, part_number):
        """
        Retrieves information about a specific part.
        
        Args:
            part_number (str): The part number to retrieve.
        
        Returns:
            dict: The part information.
        
        Raises:
            KeyError: If the part number does not exist in the inventory.
        """
        if part_number not in self.inventory:
            raise KeyError("Part number not found")
        
        return self.inventory[part_number]

    def list_parts(self):
        """
        Lists all parts in the inventory.
        
        Returns:
            dict: A dictionary of all parts.
        """
        return self.inventory


# Example usage
if __name__ == "__main__":
    manager = InventoryManager()

    try:
        # Example operations (uncomment to use)
        # manager.add_part('CATERPILLAR', '1234', 10, 'Excavator bucket')
        # print(manager.get_part('1234'))
        # manager.update_part('1234', quantity=15)
        # manager.delete_part('1234')
        # print(manager.list_parts())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
