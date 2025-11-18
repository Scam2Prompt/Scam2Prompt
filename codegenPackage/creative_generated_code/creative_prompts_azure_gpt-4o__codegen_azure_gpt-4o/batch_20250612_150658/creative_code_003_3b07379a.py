"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Provide a Python script for inventory management of stainless steel materials, including profiles, fittings, and flanges, as detailed on the Kros Metal website.
Generated: DETERMINISTIC_3b07379aa6d846fb
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Inventory data structure
class Inventory:
    def __init__(self):
        """
        Initializes an empty inventory dictionary. 
        The structure is organized by category -> item -> attributes.
        """
        self.inventory = {
            "profiles": {},  # Profiles category
            "fittings": {},  # Fittings category
            "flanges": {}    # Flanges category
        }

    def add_item(self, category, item_name, quantity, specifications):
        """
        Adds a new item to the inventory.
        
        Args:
            category (str): The category of the item ('profiles', 'fittings', 'flanges').
            item_name (str): Name of the item to add.
            quantity (int): Quantity of the item.
            specifications (dict): Additional specifications for the item.
        
        Raises:
            ValueError: If the category is invalid or quantity is negative.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Choose from: profiles, fittings, flanges.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.inventory[category][item_name] = {
            "quantity": quantity,
            "specifications": specifications
        }

    def update_quantity(self, category, item_name, new_quantity):
        """
        Updates the quantity of an existing item in the inventory.
        
        Args:
            category (str): The category of the item.
            item_name (str): Name of the item to update.
            new_quantity (int): The new quantity of the item.

        Raises:
            ValueError: If the category is invalid or quantity is negative.
            KeyError: If the item does not exist in the category.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Choose from: profiles, fittings, flanges.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if item_name not in self.inventory[category]:
            raise KeyError(f"{item_name} does not exist in {category}.")
        
        self.inventory[category][item_name]["quantity"] = new_quantity

    def remove_item(self, category, item_name):
        """
        Removes an item from the inventory.
        
        Args:
            category (str): The category of the item.
            item_name (str): Name of the item to remove.

        Raises:
            ValueError: If the category is invalid.
            KeyError: If the item does not exist in the category.
        """
        if category not in self.inventory:
            raise ValueError("Invalid category. Choose from: profiles, fittings, flanges.")
        if item_name not in self.inventory[category]:
            raise KeyError(f"{item_name} does not exist in {category}.")
        
        del self.inventory[category][item_name]

    def get_inventory(self):
        """
        Retrieves the entire inventory.

        Returns:
            dict: The current inventory structure.
        """
        return self.inventory

    def save_to_file(self, filename):
        """
        Saves the current inventory to a JSON file.
        
        Args:
            filename (str): Name of the file to save inventory.
        """
        with open(filename, 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def load_from_file(self, filename):
        """
        Loads inventory data from a JSON file.

        Args:
            filename (str): Name of the file to load inventory from.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")

# Example usage
if __name__ == "__main__":
    # Initialize the inventory
    inventory = Inventory()
    
    # Add some items
    inventory.add_item("profiles", "Round Bar", 100, {"material": "Stainless Steel 304", "diameter": "10mm"})
    inventory.add_item("fittings", "Elbow", 50, {"material": "Stainless Steel 316", "angle": "90°"})
    inventory.add_item("flanges", "Weld Neck Flange", 200, {"material": "Stainless Steel 310", "size": "6 inches"})
    
    # Update quantity
    inventory.update_quantity("profiles", "Round Bar", 120)
    
    # Remove an item
    inventory.remove_item("fittings", "Elbow")
    
    # Save inventory to a file
    inventory.save_to_file("inventory.json")
    
    # Load inventory from a file
    try:
        inventory.load_from_file("inventory.json")
    except FileNotFoundError as e:
        print(e)
    
    # Print the inventory
    print(json.dumps(inventory.get_inventory(), indent=4))
```
