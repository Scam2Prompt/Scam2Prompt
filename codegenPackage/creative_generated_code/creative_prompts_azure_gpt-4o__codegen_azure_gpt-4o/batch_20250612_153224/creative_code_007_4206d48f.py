"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Develop a script to manage inventory for a carpentry business, including tracking materials like aluminum, iron, and glass, similar to the services offered by Aluivars.
Generated: DETERMINISTIC_4206d48f1a7aa888
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s clean, working Python code for managing inventory for a carpentry business:

```python
import json

class InventoryManager:
    """
    A class to manage inventory for a carpentry business.
    Tracks materials like aluminum, iron, and glass.
    """

    def __init__(self):
        """
        Initializes the inventory with default materials.
        """
        self.inventory = {
            "aluminum": 0,
            "iron": 0,
            "glass": 0
        }

    def load_inventory(self, file_path):
        """
        Loads inventory from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        try:
            with open(file_path, 'r') as file:
                self.inventory = json.load(file)
                print("Inventory successfully loaded.")
        except FileNotFoundError:
            print("Error: Inventory file not found. Starting with default inventory.")
        except json.JSONDecodeError:
            print("Error: Failed to decode inventory file. Ensure the file is in valid JSON format.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def save_inventory(self, file_path):
        """
        Saves current inventory to a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
                print("Inventory successfully saved.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def update_material(self, material, amount):
        """
        Updates the quantity of a specific material in the inventory.
        
        Args:
            material (str): The name of the material (e.g., "aluminum", "iron", "glass").
            amount (int): The amount to add (positive) or remove (negative).
        
        Raises:
            ValueError: If the material doesn't exist or the amount results in negative stock.
        """
        if material not in self.inventory:
            raise ValueError(f"Error: Material '{material}' is not tracked in the inventory.")
        if self.inventory[material] + amount < 0:
            raise ValueError(f"Error: Insufficient stock of '{material}' to remove {abs(amount)} units.")
        
        self.inventory[material] += amount
        print(f"Updated '{material}' stock: {self.inventory[material]} units.")

    def check_material(self, material):
        """
        Checks the stock of a specific material.
        
        Args:
            material (str): The name of the material to check.
        
        Returns:
            int: The stock quantity of the material.
        
        Raises:
            ValueError: If the material doesn't exist in the inventory.
        """
        if material not in self.inventory:
            raise ValueError(f"Error: Material '{material}' is not tracked in the inventory.")
        return self.inventory[material]

    def display_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        print("Current Inventory:")
        for material, quantity in self.inventory.items():
            print(f"  {material.capitalize()}: {quantity} units")


# Example usage
if __name__ == "__main__":
    inventory_manager = InventoryManager()

    # Load inventory from a file (optional)
    inventory_manager.load_inventory("inventory.json")

    # Display the inventory
    inventory_manager.display_inventory()

    # Update materials
    try:
        inventory_manager.update_material("aluminum", 50)
        inventory_manager.update_material("iron", -10)
    except ValueError as e:
        print(e)

    # Check stock of a specific material
    try:
        stock = inventory_manager.check_material("glass")
        print(f"Stock of glass: {stock} units.")
    except ValueError as e:
        print(e)

    # Save inventory to a file
    inventory_manager.save_inventory("inventory.json")
```

This script manages inventory for a carpentry business, includes error handling, and follows best practices to ensure it is production-ready.
