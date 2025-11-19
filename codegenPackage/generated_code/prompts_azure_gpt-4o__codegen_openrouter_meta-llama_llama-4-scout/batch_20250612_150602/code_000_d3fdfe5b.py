"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write Python code to generate a list of FSC-certified materials for a cleaning product inventory system, referencing PDC Brush's focus on sustainability.
Generated: DETERMINISTIC_d3fdfe5bb7272f44
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fsc_certified_materials.py

class FSCMaterial:
    """Represents an FSC-certified material."""

    def __init__(self, name, fsc_code, description):
        """
        Initializes an FSCMaterial instance.

        Args:
            name (str): Material name.
            fsc_code (str): FSC certification code.
            description (str): Material description.
        """
        self.name = name
        self.fsc_code = fsc_code
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.fsc_code}) - {self.description}"


class CleaningProductInventory:
    """Manages a list of FSC-certified materials for a cleaning product inventory system."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.materials = []

    def add_material(self, material):
        """
        Adds an FSC-certified material to the inventory.

        Args:
            material (FSCMaterial): Material to add.

        Raises:
            TypeError: If material is not an FSCMaterial instance.
        """
        if not isinstance(material, FSCMaterial):
            raise TypeError("Material must be an FSCMaterial instance")
        self.materials.append(material)

    def remove_material(self, fsc_code):
        """
        Removes an FSC-certified material from the inventory by FSC code.

        Args:
            fsc_code (str): FSC code of material to remove.

        Raises:
            ValueError: If material not found in inventory.
        """
        for material in self.materials:
            if material.fsc_code == fsc_code:
                self.materials.remove(material)
                return
        raise ValueError("Material not found in inventory")

    def get_materials(self):
        """Returns a list of FSC-certified materials in the inventory."""
        return self.materials


def main():
    # Create an inventory
    inventory = CleaningProductInventory()

    # Add FSC-certified materials (example materials used by PDC Brush)
    materials = [
        FSCMaterial("Bamboo", "FSC-C009876", "Sustainable bamboo handle"),
        FSCMaterial("Recycled Polypropylene", "FSC-C010123", "Recycled plastic bristles"),
        FSCMaterial("Natural Bristles", "FSC-C011456", "Sustainable natural bristles"),
    ]

    for material in materials:
        inventory.add_material(material)

    # Print materials
    print("FSC-certified Materials:")
    for material in inventory.get_materials():
        print(material)

    # Remove a material
    inventory.remove_material("FSC-C010123")

    # Print updated materials
    print("\nUpdated FSC-certified Materials:")
    for material in inventory.get_materials():
        print(material)


if __name__ == "__main__":
    main()
```
