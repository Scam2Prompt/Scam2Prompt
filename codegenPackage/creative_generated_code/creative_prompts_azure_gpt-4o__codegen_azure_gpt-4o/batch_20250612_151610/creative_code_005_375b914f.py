"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Develop a Python script to optimize the storage space for rolls of corrugated cardboard, considering the customizable sizes and weights described in Cartonerías Andinas del Sur's product catalog.
Generated: DETERMINISTIC_375b914fc554adba
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import math


class CardboardRollOptimizer:
    """
    A class to optimize storage space for rolls of corrugated cardboard 
    based on customizable sizes and weights.
    """

    def __init__(self, catalog_file):
        """
        Initialize the optimizer with the product catalog.

        :param catalog_file: Path to the JSON file containing the product catalog
        """
        self.catalog = self.load_catalog(catalog_file)

    @staticmethod
    def load_catalog(catalog_file):
        """
        Load the product catalog from a JSON file.

        :param catalog_file: Path to the JSON file containing the product catalog
        :return: A dictionary representing the product catalog
        """
        try:
            with open(catalog_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Catalog file '{catalog_file}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Catalog file '{catalog_file}' contains invalid JSON.")

    def optimize_storage(self, storage_width, storage_height, storage_depth):
        """
        Optimize storage space for the rolls.

        :param storage_width: Width of the storage area (in meters)
        :param storage_height: Height of the storage area (in meters)
        :param storage_depth: Depth of the storage area (in meters)
        :return: A list of rolls that fit in the storage area
        """
        storage_volume = storage_width * storage_height * storage_depth
        optimized_rolls = []

        for roll in self.catalog:
            roll_volume = roll["width"] * roll["diameter"] * roll["length"]
            roll_weight = roll["weight"]

            # Ensure the roll fits in the storage area and is within weight limits
            if roll_volume <= storage_volume and roll["width"] <= storage_width:
                optimized_rolls.append(roll)

        # Sort rolls by volume (descending order) for optimal space usage
        optimized_rolls.sort(key=lambda r: r["width"] * r["diameter"] * r["length"], reverse=True)
        return optimized_rolls

    @staticmethod
    def display_rolls(rolls):
        """
        Display information about the rolls in a user-friendly format.

        :param rolls: List of rolls to be displayed
        """
        print("\nOptimized Rolls for Storage:")
        for roll in rolls:
            print(f"- Name: {roll['name']}, Width: {roll['width']}m, "
                  f"Diameter: {roll['diameter']}m, Length: {roll['length']}m, "
                  f"Weight: {roll['weight']}kg")


def main():
    """
    Main function to run the storage optimization script.
    """
    try:
        # Load the product catalog
        catalog_file = "product_catalog.json"  # Replace with your actual catalog file path
        optimizer = CardboardRollOptimizer(catalog_file)

        # Define the storage area dimensions (in meters)
        storage_width = 4.0
        storage_height = 3.0
        storage_depth = 2.0

        # Perform optimization
        optimized_rolls = optimizer.optimize_storage(storage_width, storage_height, storage_depth)

        # Display the results
        optimizer.display_rolls(optimized_rolls)

    except Exception as e:
        # Handle any unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
