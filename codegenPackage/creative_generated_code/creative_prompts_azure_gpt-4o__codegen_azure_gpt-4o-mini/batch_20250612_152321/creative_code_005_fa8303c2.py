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
# fastener_filter.py

import json

class Fastener:
    """
    Class representing a fastener product with attributes for material, size, and type.
    """
    def __init__(self, name, material, size, fastener_type):
        self.name = name
        self.material = material
        self.size = size
        self.fastener_type = fastener_type

    def __repr__(self):
        return f"{self.name} ({self.material}, Size: {self.size}, Type: {self.fastener_type})"


class FastenerFilter:
    """
    Class to filter fasteners based on material type and size.
    """
    def __init__(self, fasteners):
        self.fasteners = fasteners

    def filter_by_material(self, material):
        """
        Filter fasteners by material type.
        
        :param material: The material to filter by.
        :return: A list of filtered fasteners.
        """
        return [fastener for fastener in self.fasteners if fastener.material.lower() == material.lower()]

    def filter_by_size(self, size):
        """
        Filter fasteners by size.
        
        :param size: The size to filter by.
        :return: A list of filtered fasteners.
        """
        return [fastener for fastener in self.fasteners if fastener.size == size]

    def filter_by_material_and_size(self, material, size):
        """
        Filter fasteners by both material type and size.
        
        :param material: The material to filter by.
        :param size: The size to filter by.
        :return: A list of filtered fasteners.
        """
        return [fastener for fastener in self.fasteners if fastener.material.lower() == material.lower() and fastener.size == size]


def load_fasteners_from_json(file_path):
    """
    Load fastener data from a JSON file.
    
    :param file_path: The path to the JSON file.
    :return: A list of Fastener objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            fasteners = [Fastener(**item) for item in data]
            return fasteners
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def display_fasteners(fasteners):
    """
    Display the list of fasteners in a readable format.
    
    :param fasteners: A list of Fastener objects to display.
    """
    if not fasteners:
        print("No fasteners found.")
        return
    for fastener in fasteners:
        print(fastener)


if __name__ == "__main__":
    # Load fasteners from a JSON file
    fasteners_list = load_fasteners_from_json('fasteners.json')

    # Create a filter object
    filter_instance = FastenerFilter(fasteners_list)

    # Example filter criteria
    material_to_filter = "stainless steel"
    size_to_filter = "M5"

    # Filter fasteners based on user criteria
    filtered_fasteners = filter_instance.filter_by_material_and_size(material_to_filter, size_to_filter)

    # Display the filtered fasteners
    display_fasteners(filtered_fasteners)
```

**Note**: The JSON file `fasteners.json` should be structured as a list of dictionaries where each dictionary contains the keys: `name`, `material`, `size`, and `fastener_type`. For example:

```json
[
    {"name": "Screw 1", "material": "Stainless Steel", "size": "M5", "fastener_type": "screw"},
    {"name": "Bolt 1", "material": "Iron", "size": "M8", "fastener_type": "bolt"},
    {"name": "Nut 1", "material": "Stainless Steel", "size": "M5", "fastener_type": "nut"}
]
```
