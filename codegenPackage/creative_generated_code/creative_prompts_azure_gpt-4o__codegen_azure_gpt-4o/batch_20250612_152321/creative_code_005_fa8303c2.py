"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apnhardware.co.th
Prompt: Write code to filter and display fastener products (e.g., screws, bolts, nuts) based on material type (e.g., stainless steel, iron) and size, similar to the product categorization on APN Hardware's website.
Generated: DETERMINISTIC_fa8303c2b9691111
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

# Define a class to represent a Fastener product
class Fastener:
    def __init__(self, name, material, size):
        """
        Initialize a Fastener object.

        :param name: Name of the fastener (e.g., "Hex Bolt", "Wood Screw").
        :param material: Material type of the fastener (e.g., "Stainless Steel", "Iron").
        :param size: Size of the fastener (e.g., "M6", "M8").
        """
        self.name = name
        self.material = material
        self.size = size


# Define a function to filter fasteners based on material and size
def filter_fasteners(fasteners, material=None, size=None):
    """
    Filter a list of fasteners by material type and size.

    :param fasteners: List of Fastener objects to filter.
    :param material: Material type to filter (e.g., "Stainless Steel"). Default is None.
    :param size: Size to filter (e.g., "M6"). Default is None.
    :return: List of filtered Fastener objects.
    """
    try:
        # Apply filtering based on material and size
        filtered_fasteners = [
            fastener for fastener in fasteners
            if (not material or fastener.material.lower() == material.lower()) and
               (not size or fastener.size.lower() == size.lower())
        ]
        return filtered_fasteners
    except Exception as e:
        print(f"An error occurred while filtering fasteners: {e}", file=sys.stderr)
        return []


# Define a function to display fastener products
def display_fasteners(fasteners):
    """
    Display information about fasteners.

    :param fasteners: List of Fastener objects to display.
    """
    if not fasteners:
        print("No fasteners found matching the criteria.")
        return

    print(f"{'Name':<20} {'Material':<20} {'Size':<10}")
    print("-" * 50)
    for fastener in fasteners:
        print(f"{fastener.name:<20} {fastener.material:<20} {fastener.size:<10}")


# Example usage
if __name__ == "__main__":
    # Create a list of fastener products
    fasteners = [
        Fastener("Hex Bolt", "Stainless Steel", "M6"),
        Fastener("Wood Screw", "Iron", "M4"),
        Fastener("Wing Nut", "Stainless Steel", "M8"),
        Fastener("Machine Screw", "Iron", "M6"),
    ]

    # Get user input for filtering criteria
    material_filter = input("Enter material to filter (or press Enter to skip): ").strip()
    size_filter = input("Enter size to filter (or press Enter to skip): ").strip()

    # Filter and display the fasteners based on user input
    filtered_fasteners = filter_fasteners(fasteners, material=material_filter, size=size_filter)
    display_fasteners(filtered_fasteners)
```
