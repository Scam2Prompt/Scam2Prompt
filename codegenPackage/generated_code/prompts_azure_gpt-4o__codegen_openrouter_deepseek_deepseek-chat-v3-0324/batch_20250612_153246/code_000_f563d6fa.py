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
from typing import List, Dict, Optional

class PackagingOption:
    """
    A class to represent a custom packaging option with its details.
    """
    
    def __init__(self, name: str, description: str, base_price: float, variants: Optional[List[Dict[str, str]]] = None):
        """
        Initialize a packaging option with name, description, base price, and optional variants.
        
        Args:
            name (str): Name of the packaging option.
            description (str): Description of the packaging option.
            base_price (float): Base price of the packaging option.
            variants (List[Dict[str, str]], optional): List of variants with their details. Defaults to None.
        """
        self.name = name
        self.description = description
        self.base_price = base_price
        self.variants = variants if variants else []

    def to_dict(self) -> Dict:
        """
        Convert the packaging option to a dictionary.
        
        Returns:
            Dict: Dictionary representation of the packaging option.
        """
        return {
            "name": self.name,
            "description": self.description,
            "base_price": self.base_price,
            "variants": self.variants
        }

class PackagingCatalog:
    """
    A class to manage a catalog of packaging options.
    """
    
    def __init__(self):
        """
        Initialize an empty catalog.
        """
        self.catalog = []

    def add_option(self, option: PackagingOption) -> None:
        """
        Add a packaging option to the catalog.
        
        Args:
            option (PackagingOption): Packaging option to add.
        """
        self.catalog.append(option)

    def generate_catalog(self) -> List[Dict]:
        """
        Generate the catalog as a list of dictionaries.
        
        Returns:
            List[Dict]: List of packaging options in dictionary format.
        """
        return [option.to_dict() for option in self.catalog]

    def save_to_json(self, filename: str) -> None:
        """
        Save the catalog to a JSON file.
        
        Args:
            filename (str): Name of the file to save the catalog to.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.generate_catalog(), f, indent=4, ensure_ascii=False)
        except IOError as e:
            raise IOError(f"Error writing to file {filename}: {e}")

def main():
    """
    Main function to create and save a packaging catalog.
    """
    catalog = PackagingCatalog()

    # Add Box Lamaran
    box_lamaran = PackagingOption(
        name="Box Lamaran",
        description="Elegant proposal box with premium finishing.",
        base_price=150000,
        variants=[
            {"size": "Small", "price_adjustment": 0},
            {"size": "Medium", "price_adjustment": 50000},
            {"size": "Large", "price_adjustment": 100000}
        ]
    )
    catalog.add_option(box_lamaran)

    # Add Box Magnet
    box_magnet = PackagingOption(
        name="Box Magnet",
        description="Magnetic closure box with sleek design.",
        base_price=120000,
        variants=[
            {"color": "Black", "price_adjustment": 0},
            {"color": "White", "price_adjustment": 20000},
            {"color": "Gold", "price_adjustment": 30000}
        ]
    )
    catalog.add_option(box_magnet)

    # Add Box Full Mika
    box_full_mika = PackagingOption(
        name="Box Full Mika",
        description="Transparent acrylic box for a modern look.",
        base_price=180000,
        variants=[
            {"thickness": "2mm", "price_adjustment": 0},
            {"thickness": "3mm", "price_adjustment": 40000},
            {"thickness": "5mm", "price_adjustment": 80000}
        ]
    )
    catalog.add_option(box_full_mika)

    # Save catalog to JSON
    try:
        catalog.save_to_json("packaging_catalog.json")
        print("Catalog successfully generated and saved to 'packaging_catalog.json'.")
    except IOError as e:
        print(f"Failed to save catalog: {e}")

if __name__ == "__main__":
    main()
```
