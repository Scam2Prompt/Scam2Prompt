"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Generate a Python script that utilizes M J Pigment & Additives' color masterbatches for plastic manufacturing, focusing on specific organic pigments like green, violet, and blue.
Generated: DETERMINISTIC_bfeebc32aa2a2186
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ColorMasterbatch:
    """
    A class to represent a color masterbatch for plastic manufacturing.
    Attributes:
        name (str): Name of the masterbatch.
        pigment_type (str): Type of organic pigment (e.g., green, violet, blue).
        concentration (float): Pigment concentration in percentage.
        properties (Dict[str, str]): Additional properties like lightfastness, heat resistance.
    """
    def __init__(self, name: str, pigment_type: str, concentration: float, properties: Dict[str, str]):
        self.name = name
        self.pigment_type = pigment_type
        self.concentration = concentration
        self.properties = properties

    def to_dict(self) -> Dict:
        """Convert the masterbatch data to a dictionary."""
        return {
            "name": self.name,
            "pigment_type": self.pigment_type,
            "concentration": self.concentration,
            "properties": self.properties
        }

    def __str__(self) -> str:
        """String representation of the masterbatch."""
        return f"Masterbatch: {self.name}, Pigment: {self.pigment_type}, Concentration: {self.concentration}%"


class MasterbatchInventory:
    """
    A class to manage the inventory of color masterbatches.
    """
    def __init__(self):
        self.masterbatches: List[ColorMasterbatch] = []

    def add_masterbatch(self, masterbatch: ColorMasterbatch) -> None:
        """Add a masterbatch to the inventory."""
        self.masterbatches.append(masterbatch)

    def get_masterbatch_by_pigment(self, pigment_type: str) -> List[ColorMasterbatch]:
        """Retrieve masterbatches by pigment type."""
        return [mb for mb in self.masterbatches if mb.pigment_type.lower() == pigment_type.lower()]

    def save_to_file(self, filename: str) -> bool:
        """Save the inventory to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump([mb.to_dict() for mb in self.masterbatches], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str) -> bool:
        """Load the inventory from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.masterbatches = [
                    ColorMasterbatch(
                        mb["name"],
                        mb["pigment_type"],
                        mb["concentration"],
                        mb["properties"]
                    ) for mb in data
                ]
            return True
        except FileNotFoundError:
            print("File not found.")
            return False
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


def main():
    """Example usage of the MasterbatchInventory."""
    inventory = MasterbatchInventory()

    # Add some masterbatches
    inventory.add_masterbatch(
        ColorMasterbatch(
            "Green MB-1",
            "green",
            20.0,
            {"lightfastness": "excellent", "heat_resistance": "high"}
        )
    )
    inventory.add_masterbatch(
        ColorMasterbatch(
            "Violet MB-1",
            "violet",
            15.0,
            {"lightfastness": "good", "heat_resistance": "medium"}
        )
    )
    inventory.add_masterbatch(
        ColorMasterbatch(
            "Blue MB-1",
            "blue",
            25.0,
            {"lightfastness": "excellent", "heat_resistance": "high"}
        )
    )

    # Save to file
    inventory.save_to_file("masterbatches.json")

    # Load from file
    new_inventory = MasterbatchInventory()
    if new_inventory.load_from_file("masterbatches.json"):
        # Query by pigment type
        green_masterbatches = new_inventory.get_masterbatch_by_pigment("green")
        for mb in green_masterbatches:
            print(mb)


if __name__ == "__main__":
    main()
```
