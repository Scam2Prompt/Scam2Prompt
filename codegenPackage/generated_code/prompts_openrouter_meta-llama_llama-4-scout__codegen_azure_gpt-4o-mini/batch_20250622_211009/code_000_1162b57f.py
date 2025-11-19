"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a Python script to manage inventory of golf grips, including rubber, TPE, and PU grips, with different styles and customization options.
Generated: DETERMINISTIC_1162b57fe7274c67
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class GolfGrip:
    """Class to represent a golf grip with its properties."""
    
    def __init__(self, material: str, style: str, customization: Dict[str, Any]):
        """
        Initialize a GolfGrip instance.

        :param material: Material of the grip (e.g., rubber, TPE, PU).
        :param style: Style of the grip.
        :param customization: Customization options for the grip.
        """
        self.material = material
        self.style = style
        self.customization = customization

    def to_dict(self) -> Dict[str, Any]:
        """Convert the GolfGrip instance to a dictionary."""
        return {
            'material': self.material,
            'style': self.style,
            'customization': self.customization
        }

class Inventory:
    """Class to manage the inventory of golf grips."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.grips: List[GolfGrip] = []

    def add_grip(self, grip: GolfGrip) -> None:
        """Add a new grip to the inventory.

        :param grip: An instance of GolfGrip to add.
        """
        self.grips.append(grip)

    def remove_grip(self, grip: GolfGrip) -> bool:
        """Remove a grip from the inventory.

        :param grip: An instance of GolfGrip to remove.
        :return: True if the grip was removed, False otherwise.
        """
        try:
            self.grips.remove(grip)
            return True
        except ValueError:
            return False

    def list_grips(self) -> List[Dict[str, Any]]:
        """List all grips in the inventory.

        :return: A list of dictionaries representing each grip.
        """
        return [grip.to_dict() for grip in self.grips]

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file.

        :param filename: The name of the file to save the inventory.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_grips(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file.

        :param filename: The name of the file to load the inventory from.
        """
        try:
            with open(filename, 'r') as file:
                grips_data = json.load(file)
                self.grips = [GolfGrip(**grip) for grip in grips_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory: {e}")

def main():
    """Main function to manage the inventory."""
    inventory = Inventory()

    # Example usage
    grip1 = GolfGrip(material='rubber', style='standard', customization={'color': 'black', 'size': 'medium'})
    grip2 = GolfGrip(material='TPE', style='tapered', customization={'color': 'red', 'size': 'large'})

    inventory.add_grip(grip1)
    inventory.add_grip(grip2)

    print("Current Inventory:")
    print(inventory.list_grips())

    # Save inventory to a file
    inventory.save_inventory('inventory.json')

    # Load inventory from a file
    new_inventory = Inventory()
    new_inventory.load_inventory('inventory.json')
    print("Loaded Inventory:")
    print(new_inventory.list_grips())

if __name__ == "__main__":
    main()
```
