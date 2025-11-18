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
    A class to manage an inventory system for machinery parts from multiple brands.
    """
    
    def __init__(self, inventory_file='inventory.json'):
        """
        Initialize the inventory manager with a file to store inventory data.
        
        :param inventory_file: File to store inventory data, defaults to 'inventory.json'
        """
        self.inventory_file = inventory_file
        self.brands = ["FIATALLIS", "CATERPILLAR", "JOHN DEERE", "KOMATSU", "IVECO"]
        self.inventory = self._load_inventory()
    
    def _load_inventory(self):
        """
        Load inventory data from the JSON file. If it doesn't exist, initialize an empty inventory.
        
        :return: Dictionary representing the inventory data
        """
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading inventory file. Initializing empty inventory.")
        return {brand: {} for brand in self.brands}
    
    def save_inventory(self):
        """
        Save inventory data to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory file: {e}")
    
    def add_part(self, brand, part_name, quantity):
        """
        Add a part to the inventory for a specific brand.
        
        :param brand: The brand of the part
        :param part_name: The name of the part
        :param quantity: Quantity of the part to add
        """
        if brand not in self.brands:
            print(f"Error: Brand '{brand}' is not recognized.")
            return
        
        if part_name in self.inventory[brand]:
            self.inventory[brand][part_name] += quantity
        else:
            self.inventory[brand][part_name] = quantity
        
        print(f"Added {quantity} '{part_name}' to {brand}.")
        self.save_inventory()
    
    def remove_part(self, brand, part_name, quantity):
        """
        Remove a part from the inventory for a specific brand.
        
        :param brand: The brand of the part
        :param part_name: The name of the part
        :param quantity: Quantity of the part to remove
        """
        if brand not in self.brands:
            print(f"Error: Brand '{brand}' is not recognized.")
            return
        
        if part_name not in self.inventory[brand]:
            print(f"Error: Part '{part_name}' not found in {brand} inventory.")
            return
        
        if self.inventory[brand][part_name] < quantity:
            print(f"Error: Cannot remove {quantity}. Only {self.inventory[brand][part_name]} in inventory.")
            return
        
        self.inventory[brand][part_name] -= quantity
        if self.inventory[brand][part_name] == 0:
            del self.inventory[brand][part_name]
        
        print(f"Removed {quantity} '{part_name}' from {brand}.")
        self.save_inventory()
    
    def view_inventory(self):
        """
        Display the current inventory in a readable format.
        """
        print("Current Inventory:")
        for brand, parts in self.inventory.items():
            print(f"{brand}:")
            if not parts:
                print("  No parts available.")
            for part_name, quantity in parts.items():
                print(f"  {part_name}: {quantity}")
    
    def search_part(self, part_name):
        """
        Search for a part across all brands.
        
        :param part_name: The name of the part to search for
        """
        print(f"Searching for '{part_name}' in inventory:")
        found = False
        for brand, parts in self.inventory.items():
            if part_name in parts:
                print(f"{brand}: {parts[part_name]} available")
                found = True
        if not found:
            print(f"Part '{part_name}' not found in inventory.")


# Main script execution
if __name__ == "__main__":
    manager = InventoryManager()

    # Example usage
    manager.add_part("FIATALLIS", "Engine", 10)
    manager.add_part("CATERPILLAR", "Hydraulic Pump", 5)
    manager.view_inventory()
    manager.remove_part("FIATALLIS", "Engine", 3)
    manager.view_inventory()
    manager.search_part("Hydraulic Pump")
    manager.search_part("Tires")
```
