"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Write code to filter and display fastener products (e.g., screws, bolts, nuts) based on material type (e.g., stainless steel, iron) and size, similar to the product categorization on APN Hardware's website.
Generated: DETERMINISTIC_fa8303c2b9691111
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class Fastener:
    """Class representing a fastener product."""
    
    def __init__(self, name, material, size):
        """
        Initialize a Fastener instance.

        Args:
            name (str): The name of the fastener.
            material (str): The material type of the fastener.
            size (str): The size of the fastener.
        """
        self.name = name
        self.material = material
        self.size = size

    def __repr__(self):
        """Return a string representation of the Fastener."""
        return f"{self.name} ({self.material}, {self.size})"


class FastenerCatalog:
    """Class to manage a catalog of fasteners."""
    
    def __init__(self):
        """Initialize an empty fastener catalog."""
        self.fasteners = []

    def add_fastener(self, fastener):
        """
        Add a fastener to the catalog.

        Args:
            fastener (Fastener): The fastener to add.
        """
        if not isinstance(fastener, Fastener):
            raise ValueError("Only Fastener instances can be added.")
        self.fasteners.append(fastener)

    def filter_fasteners(self, material=None, size=None):
        """
        Filter fasteners based on material and size.

        Args:
            material (str, optional): The material type to filter by.
            size (str, optional): The size to filter by.

        Returns:
            list: A list of filtered fasteners.
        """
        filtered = self.fasteners
        if material:
            filtered = [f for f in filtered if f.material.lower() == material.lower()]
        if size:
            filtered = [f for f in filtered if f.size.lower() == size.lower()]
        return filtered


def load_fasteners_from_json(file_path):
    """
    Load fasteners from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        FastenerCatalog: A catalog populated with fasteners.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            catalog = FastenerCatalog()
            for item in data:
                fastener = Fastener(item['name'], item['material'], item['size'])
                catalog.add_fastener(fastener)
            return catalog
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise


def display_fasteners(fasteners):
    """
    Display a list of fasteners.

    Args:
        fasteners (list): The list of fasteners to display.
    """
    if not fasteners:
        print("No fasteners found.")
    else:
        for fastener in fasteners:
            print(fastener)


if __name__ == "__main__":
    # Load fasteners from a JSON file
    catalog = load_fasteners_from_json('fasteners.json')

    # Filter fasteners by material and size
    material_filter = input("Enter material type to filter (or leave blank): ")
    size_filter = input("Enter size to filter (or leave blank): ")

    filtered_fasteners = catalog.filter_fasteners(material=material_filter, size=size_filter)

    # Display the filtered fasteners
    display_fasteners(filtered_fasteners)
```

**Note:** Ensure that the `fasteners.json` file exists in the same directory as this script and contains valid JSON data structured as follows:

```json
[
    {"name": "Screw A", "material": "Stainless Steel", "size": "M5"},
    {"name": "Bolt B", "material": "Iron", "size": "M6"},
    {"name": "Nut C", "material": "Stainless Steel", "size": "M5"}
]
```
