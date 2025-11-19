"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Generate a step-by-step guide in code for assembling IKEA furniture, ensuring durability and long-lasting quality, as highlighted by شركة آل البيت نجار ايكيا services.
Generated: DETERMINISTIC_ed576acd524b7751
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# IKEA Furniture Assembly Guide

class IKAEAFurniture:
    def __init__(self, name, parts, instructions):
        """
        Initialize an IKEA furniture object.

        Args:
            name (str): Name of the furniture.
            parts (list): List of parts required for assembly.
            instructions (list): List of instructions for assembly.
        """
        self.name = name
        self.parts = parts
        self.instructions = instructions

    def display_assembly_guide(self):
        """
        Display the step-by-step assembly guide.
        """
        print(f"Assembly Guide for {self.name}:")
        for i, instruction in enumerate(self.instructions, start=1):
            print(f"Step {i}: {instruction}")


class IkeaAssemblyService:
    def __init__(self):
        """
        Initialize the IKEA assembly service.
        """
        self.furniture_catalog = {}

    def add_furniture(self, furniture):
        """
        Add furniture to the catalog.

        Args:
            furniture (IKAEAFurniture): IKEA furniture object.
        """
        self.furniture_catalog[furniture.name] = furniture

    def get_assembly_guide(self, furniture_name):
        """
        Get the assembly guide for a specific furniture.

        Args:
            furniture_name (str): Name of the furniture.

        Returns:
            IKAEAFurniture: IKEA furniture object with assembly guide.

        Raises:
            ValueError: If furniture not found in catalog.
        """
        if furniture_name in self.furniture_catalog:
            return self.furniture_catalog[furniture_name]
        else:
            raise ValueError("Furniture not found in catalog.")


def main():
    # Create IKEA assembly service
    ikea_service = IkeaAssemblyService()

    # Create furniture objects
    malm_dresser_parts = ["Frame", "Drawers", "Screws", "Handles"]
    malm_dresser_instructions = [
        "Assemble frame using screws.",
        "Attach drawers to frame.",
        "Add handles to drawers.",
        "Tighten all screws."
    ]
    malm_dresser = IKAEAFurniture("MALM Dresser", malm_dresser_parts, malm_dresser_instructions)

    # Add furniture to catalog
    ikea_service.add_furniture(malm_dresser)

    # Get and display assembly guide
    try:
        furniture_name = "MALM Dresser"
        assembly_guide = ikea_service.get_assembly_guide(furniture_name)
        assembly_guide.display_assembly_guide()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
