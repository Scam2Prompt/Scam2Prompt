"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://customboxsemarang.com
Prompt: Write a Python script to generate a catalog of custom packaging options, including "Box Lamaran," "Box Magnet," and "Box Full Mika," with descriptions and pricing details.
Generated: DETERMINISTIC_f563d6fa8c771bd5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class PackagingOption:
    """
    A class to represent a custom packaging option.
    """

    def __init__(self, name: str, description: str, price: float):
        """
        Initialize a new packaging option.

        :param name: Name of the packaging option.
        :param description: Description of the packaging option.
        :param price: Price of the packaging option.
        """
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the packaging option to a dictionary.

        :return: A dictionary representation of the packaging option.
        """
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price
        }


class PackagingCatalog:
    """
    A class to manage a catalog of packaging options.
    """

    def __init__(self):
        """
        Initialize an empty packaging catalog.
        """
        self.options: List[PackagingOption] = []

    def add_option(self, option: PackagingOption):
        """
        Add a new packaging option to the catalog.

        :param option: An instance of PackagingOption to add to the catalog.
        """
        self.options.append(option)

    def to_json(self) -> str:
        """
        Convert the catalog to a JSON string.

        :return: A JSON string representation of the catalog.
        """
        return json.dumps([option.to_dict() for option in self.options], indent=4)

    def save_to_file(self, filename: str):
        """
        Save the catalog to a JSON file.

        :param filename: The name of the file to save the catalog.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
            print(f"Catalog saved to {filename}.")
        except IOError as e:
            print(f"Error saving catalog to file: {e}")


def main():
    """
    Main function to create and save a packaging catalog.
    """
    catalog = PackagingCatalog()

    # Adding packaging options to the catalog
    catalog.add_option(PackagingOption(
        name="Box Lamaran",
        description="A decorative box for engagement gifts.",
        price=15.99
    ))
    catalog.add_option(PackagingOption(
        name="Box Magnet",
        description="A magnetic box for secure and elegant packaging.",
        price=25.50
    ))
    catalog.add_option(PackagingOption(
        name="Box Full Mika",
        description="A clear box made of mika, perfect for showcasing contents.",
        price=20.00
    ))

    # Save the catalog to a JSON file
    catalog.save_to_file("packaging_catalog.json")


if __name__ == "__main__":
    main()
```
