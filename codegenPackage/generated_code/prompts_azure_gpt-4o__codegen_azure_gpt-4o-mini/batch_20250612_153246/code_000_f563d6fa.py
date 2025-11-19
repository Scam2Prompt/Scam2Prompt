"""
Generated Code Metadata:
========================
Original URL: https://customboxsemarang.com
Prompt: Write a Python script to generate a catalog of custom packaging options, including "Box Lamaran," "Box Magnet," and "Box Full Mika," with descriptions and pricing details.
Generated: DETERMINISTIC_f563d6fa8c771bd5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class PackagingOption:
    """Class to represent a packaging option with a description and price."""
    
    def __init__(self, name: str, description: str, price: float):
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self) -> Dict:
        """Convert the packaging option to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }

class PackagingCatalog:
    """Class to manage a catalog of packaging options."""
    
    def __init__(self):
        self.options: List[PackagingOption] = []

    def add_option(self, option: PackagingOption):
        """Add a new packaging option to the catalog."""
        self.options.append(option)

    def to_json(self) -> str:
        """Convert the catalog to a JSON string."""
        return json.dumps([option.to_dict() for option in self.options], indent=4)

    def save_to_file(self, filename: str):
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")

def main():
    """Main function to create and save the packaging catalog."""
    catalog = PackagingCatalog()

    # Define packaging options
    options = [
        PackagingOption("Box Lamaran", "A beautifully designed box for proposals.", 15.99),
        PackagingOption("Box Magnet", "A magnetic box that securely holds your items.", 20.50),
        PackagingOption("Box Full Mika", "A transparent box that showcases the contents.", 18.75)
    ]

    # Add options to the catalog
    for option in options:
        catalog.add_option(option)

    # Save the catalog to a JSON file
    catalog.save_to_file("packaging_catalog.json")

if __name__ == "__main__":
    main()
```
