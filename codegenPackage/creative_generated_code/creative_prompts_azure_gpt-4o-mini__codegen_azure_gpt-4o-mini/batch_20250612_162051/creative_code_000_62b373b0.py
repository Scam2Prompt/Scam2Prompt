"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shop.isabelreinachic.com
Prompt: Generate a code snippet for a sewing machine inventory management system that includes features for tracking mechanical and electronic sewing machines, overlockers, and accessories available at Isabel Reina Chic.
Generated: DETERMINISTIC_62b373b07e4a7c28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class SewingMachine:
    """
    A class to represent a sewing machine or accessory.
    """
    
    def __init__(self, machine_type: str, brand: str, model: str, quantity: int):
        """
        Initializes a SewingMachine instance.

        :param machine_type: Type of the machine (e.g., 'mechanical', 'electronic', 'overlocker', 'accessory').
        :param brand: Brand of the machine.
        :param model: Model name or number of the machine.
        :param quantity: Available quantity of the machine.
        """
        self.machine_type = machine_type
        self.brand = brand
        self.model = model
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Converts the SewingMachine instance to a dictionary."""
        return {
            'machine_type': self.machine_type,
            'brand': self.brand,
            'model': self.model,
            'quantity': self.quantity
        }

class Inventory:
    """
    A class to manage the inventory of sewing machines.
    """
    
    def __init__(self):
        """Initializes an empty inventory."""
        self.items: List[SewingMachine] = []

    def add_machine(self, machine: SewingMachine):
        """
        Adds a sewing machine to the inventory.

        :param machine: An instance of SewingMachine to add.
        """
        self.items.append(machine)

    def remove_machine(self, model: str):
        """
        Removes a sewing machine from the inventory by model.

        :param model: Model name of the machine to remove.
        :raises ValueError: If the machine is not found in the inventory.
        """
        for item in self.items:
            if item.model == model:
                self.items.remove(item)
                return
        raise ValueError(f"Machine with model {model} not found in inventory.")

    def get_inventory(self) -> List[Dict[str, Any]]:
        """Returns the current inventory as a list of dictionaries."""
        return [item.to_dict() for item in self.items]

    def save_to_file(self, filename: str):
        """
        Saves the inventory to a JSON file.

        :param filename: The name of the file to save the inventory.
        :raises IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            raise IOError("An error occurred while saving to file.") from e

    def load_from_file(self, filename: str):
        """
        Loads the inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        :raises IOError: If there is an issue reading the file.
        :raises ValueError: If the data is not valid.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.add_machine(SewingMachine(item['machine_type'], item['brand'], item['model'], item['quantity']))
        except IOError as e:
            raise IOError("An error occurred while loading from file.") from e
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError("Loaded data is not valid.") from e

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding machines to the inventory
    inventory.add_machine(SewingMachine('mechanical', 'Singer', '1234', 10))
    inventory.add_machine(SewingMachine('electronic', 'Brother', '5678', 5))
    inventory.add_machine(SewingMachine('overlocker', 'Janome', '91011', 3))
    
    # Saving inventory to a file
    inventory.save_to_file('inventory.json')

    # Loading inventory from a file
    new_inventory = Inventory()
    new_inventory.load_from_file('inventory.json')
    
    # Displaying the loaded inventory
    print(new_inventory.get_inventory())
```
