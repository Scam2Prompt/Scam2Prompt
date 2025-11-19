"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: "Write a Python script to manage an inventory of medicinal plants, including tracking plant species, quantities, and uses, inspired by Oromaticas' agroecological approach."
Generated: DETERMINISTIC_ecd5ac87d04f56bc
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class MedicinalPlantInventory:
    """
    A class to manage an inventory of medicinal plants.
    Tracks plant species, quantities, and uses.
    """

    def __init__(self):
        """
        Initializes an empty inventory.
        """
        self.inventory = {}

    def add_plant(self, species, quantity, uses):
        """
        Adds a new plant species to the inventory or updates an existing one.

        Args:
            species (str): The name of the plant species.
            quantity (int): The quantity of the plant.
            uses (list): A list of uses for the plant.
        """
        if species in self.inventory:
            self.inventory[species]['quantity'] += quantity
            self.inventory[species]['uses'] = list(set(self.inventory[species]['uses'] + uses))
        else:
            self.inventory[species] = {
                'quantity': quantity,
                'uses': uses
            }

    def remove_plant(self, species, quantity):
        """
        Removes a specified quantity of a plant species from the inventory.

        Args:
            species (str): The name of the plant species.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If the species does not exist or the quantity to remove exceeds the available quantity.
        """
        if species not in self.inventory:
            raise ValueError(f"Plant species '{species}' not found in inventory.")
        if self.inventory[species]['quantity'] < quantity:
            raise ValueError(f"Cannot remove {quantity} units. Only {self.inventory[species]['quantity']} available.")
        
        self.inventory[species]['quantity'] -= quantity
        if self.inventory[species]['quantity'] == 0:
            del self.inventory[species]

    def get_inventory(self):
        """
        Returns the current inventory.

        Returns:
            dict: The inventory of medicinal plants.
        """
        return self.inventory

    def save_inventory(self, file_path):
        """
        Saves the inventory to a JSON file.

        Args:
            file_path (str): The path to the file where the inventory will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to file: {e}")

    def load_inventory(self, file_path):
        """
        Loads the inventory from a JSON file.

        Args:
            file_path (str): The path to the file from which the inventory will be loaded.

        Raises:
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    raise ValueError("Invalid inventory data in file.")
                self.inventory = data
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from file: {e}")

# Example usage
if __name__ == "__main__":
    inventory = MedicinalPlantInventory()

    # Add plants to the inventory
    inventory.add_plant("Chamomile", 50, ["Relaxation", "Digestive Aid"])
    inventory.add_plant("Lavender", 30, ["Stress Relief", "Sleep Aid"])
    inventory.add_plant("Echinacea", 20, ["Immune Support"])

    # Remove plants from the inventory
    try:
        inventory.remove_plant("Chamomile", 10)
    except ValueError as e:
        print(e)

    # Display the inventory
    print("Current Inventory:")
    print(json.dumps(inventory.get_inventory(), indent=4))

    # Save the inventory to a file
    inventory.save_inventory("medicinal_plants.json")

    # Load the inventory from a file
    try:
        inventory.load_inventory("medicinal_plants.json")
        print("Loaded Inventory:")
        print(json.dumps(inventory.get_inventory(), indent=4))
    except ValueError as e:
        print(e)
```
