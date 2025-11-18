"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtimecodes.pages.dev
Prompt: Develop a program to manage and visualize the crafting economy in Big Time, including tracking $BIGTIME token usage, materials, and item upgrades.
Generated: DETERMINISTIC_de4aafc41e04cff1
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import matplotlib.pyplot as plt

class CraftingEconomyManager:
    """
    A class to manage and visualize the crafting economy in Big Time.
    It tracks $BIGTIME token usage, materials, and item upgrades.
    """

    def __init__(self):
        """Initialize the crafting economy manager with empty data."""
        self.token_usage = []
        self.materials = {}
        self.item_upgrades = {}

    def add_token_usage(self, amount):
        """
        Add an amount of $BIGTIME tokens used in crafting.

        Args:
            amount (float): The amount of $BIGTIME tokens to add.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Token usage cannot be negative.")
        self.token_usage.append(amount)

    def add_material(self, material, quantity):
        """
        Add materials to the tracking system.

        Args:
            material (str): The name of the material.
            quantity (int): The quantity of the material.
        
        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Material quantity cannot be negative.")
        if material in self.materials:
            self.materials[material] += quantity
        else:
            self.materials[material] = quantity

    def upgrade_item(self, item_name, cost, materials_required):
        """
        Upgrade an item and track its requirements.

        Args:
            item_name (str): The name of the item to upgrade.
            cost (float): The cost in $BIGTIME tokens for the upgrade.
            materials_required (dict): A dictionary of materials required for the upgrade.
        
        Raises:
            ValueError: If the cost is negative or materials are insufficient.
        """
        if cost < 0:
            raise ValueError("Upgrade cost cannot be negative.")
        
        # Check if materials are sufficient
        for material, required_quantity in materials_required.items():
            if material not in self.materials or self.materials[material] < required_quantity:
                raise ValueError(f"Insufficient materials for {material}.")

        # Process the upgrade
        self.add_token_usage(cost)
        for material, required_quantity in materials_required.items():
            self.materials[material] -= required_quantity

        # Record the item upgrade
        self.item_upgrades[item_name] = self.item_upgrades.get(item_name, 0) + 1

    def visualize_data(self):
        """Visualize the data for token usage and materials."""
        try:
            # Visualize token usage
            plt.figure(figsize=(12, 6))
            
            plt.subplot(1, 2, 1)
            plt.plot(self.token_usage, marker='o')
            plt.title("$BIGTIME Token Usage Over Time")
            plt.xlabel("Crafting Sessions")
            plt.ylabel("Tokens Used")
            
            # Visualize materials
            plt.subplot(1, 2, 2)
            materials_names = list(self.materials.keys())
            materials_quantities = list(self.materials.values())
            plt.bar(materials_names, materials_quantities)
            plt.title("Materials Inventory")
            plt.xlabel("Materials")
            plt.ylabel("Quantity")

            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred during visualization: {e}")

    def export_data(self, file_path):
        """
        Export the current data to a JSON file.

        Args:
            file_path (str): The path to the file where data should be saved.
        
        Raises:
            IOError: If the file cannot be created or written to.
        """
        data = {
            'token_usage': self.token_usage,
            'materials': self.materials,
            'item_upgrades': self.item_upgrades
        }
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

# Example usage
if __name__ == "__main__":
    manager = CraftingEconomyManager()
    
    # Adding some sample data
    manager.add_token_usage(10.5)
    manager.add_material('Wood', 20)
    manager.add_material('Iron', 15)
    
    # Upgrading an item
    manager.upgrade_item('Sword', 5.0, {'Wood': 2, 'Iron': 1})
    
    # Visualize the current crafting economy state
    manager.visualize_data()

    # Export the data to a JSON file
    manager.export_data('crafting_economy_data.json')
```
