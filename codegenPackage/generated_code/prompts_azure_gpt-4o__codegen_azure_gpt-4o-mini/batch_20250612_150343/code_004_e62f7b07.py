"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: Write a script to manage inventory for a glass installation company, tracking glass types (tempered, laminated), thickness, and associated hardware like roldanas and stainless steel fittings.
Generated: DETERMINISTIC_e62f7b073ca77245
Batch ID: 20250612_150343
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

class GlassType:
    """Class to represent a type of glass."""
    def __init__(self, name: str, thickness: float):
        self.name = name
        self.thickness = thickness

    def to_dict(self) -> Dict[str, Any]:
        """Convert the glass type to a dictionary."""
        return {"name": self.name, "thickness": self.thickness}

class Hardware:
    """Class to represent hardware associated with glass installation."""
    def __init__(self, type: str, quantity: int):
        self.type = type
        self.quantity = quantity

    def to_dict(self) -> Dict[str, Any]:
        """Convert the hardware to a dictionary."""
        return {"type": self.type, "quantity": self.quantity}

class Inventory:
    """Class to manage the inventory of glass and hardware."""
    def __init__(self):
        self.glass_types: List[GlassType] = []
        self.hardware: List[Hardware] = []

    def add_glass_type(self, glass_type: GlassType) -> None:
        """Add a new type of glass to the inventory."""
        self.glass_types.append(glass_type)

    def add_hardware(self, hardware: Hardware) -> None:
        """Add hardware to the inventory."""
        self.hardware.append(hardware)

    def remove_glass_type(self, name: str) -> None:
        """Remove a type of glass from the inventory by name."""
        self.glass_types = [g for g in self.glass_types if g.name != name]

    def remove_hardware(self, type: str) -> None:
        """Remove hardware from the inventory by type."""
        self.hardware = [h for h in self.hardware if h.type != type]

    def get_inventory(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get the current inventory as a dictionary."""
        return {
            "glass_types": [g.to_dict() for g in self.glass_types],
            "hardware": [h.to_dict() for h in self.hardware]
        }

    def save_inventory(self, filename: str) -> None:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_inventory(), file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.glass_types = [GlassType(**g) for g in data.get("glass_types", [])]
                self.hardware = [Hardware(**h) for h in data.get("hardware", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding glass types
    inventory.add_glass_type(GlassType("Tempered", 10.0))
    inventory.add_glass_type(GlassType("Laminated", 8.0))
    
    # Adding hardware
    inventory.add_hardware(Hardware("Roldana", 50))
    inventory.add_hardware(Hardware("Stainless Steel Fitting", 100))
    
    # Saving inventory to a file
    inventory.save_inventory("inventory.json")
    
    # Loading inventory from a file
    inventory.load_inventory("inventory.json")
    
    # Displaying current inventory
    print(json.dumps(inventory.get_inventory(), indent=4))
```
