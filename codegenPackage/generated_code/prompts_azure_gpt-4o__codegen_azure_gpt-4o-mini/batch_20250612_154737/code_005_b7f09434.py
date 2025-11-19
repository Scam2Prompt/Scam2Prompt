"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Provide a Python script to automate the selection of fasteners like "Parafuso Cabeça de Martelo" and "Porcas" based on the material type of the roof structure in a solar energy project.
Generated: DETERMINISTIC_b7f09434b602123d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class FastenerSelector:
    """
    A class to select fasteners based on the material type of the roof structure.
    """

    def __init__(self):
        # Define fasteners based on material types
        self.fasteners = {
            "metal": ["Parafuso Cabeça de Martelo", "Porcas"],
            "wood": ["Parafuso de Madeira", "Porcas de Madeira"],
            "concrete": ["Parafuso de Concreto", "Porcas de Concreto"],
            "composite": ["Parafuso de Composto", "Porcas de Composto"]
        }

    def select_fasteners(self, material_type):
        """
        Select fasteners based on the given material type.

        :param material_type: str - The type of material for the roof structure.
        :return: list - A list of suitable fasteners.
        :raises ValueError: If the material type is not recognized.
        """
        if material_type not in self.fasteners:
            raise ValueError(f"Material type '{material_type}' is not recognized. "
                             f"Available types: {', '.join(self.fasteners.keys())}")

        return self.fasteners[material_type]

def main():
    """
    Main function to execute the fastener selection process.
    """
    selector = FastenerSelector()

    # Example material types to test
    material_types = ["metal", "wood", "concrete", "composite", "unknown"]

    for material in material_types:
        try:
            fasteners = selector.select_fasteners(material)
            print(f"Selected fasteners for '{material}': {fasteners}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
