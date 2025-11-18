"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://generate-digital.com
Prompt: Write Python code to analyze and optimize digital inventory using a configurable catalogue ranked by factors such as partner value and performance, as described on Generate Digital's website.
Generated: DETERMINISTIC_8cd11cfb60b4fb08
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union


class DigitalInventoryOptimizer:
    def __init__(self, catalogue: List[Dict[str, Union[str, int, float]]]):
        """
        Initializes the optimizer with a digital inventory catalogue.

        :param catalogue: List of items in the catalogue. Each item should be a dictionary
                          containing 'name', 'partner_value', 'performance', and 'stock'.
        """
        self.catalogue = catalogue

    def rank_inventory(self) -> List[Dict[str, Union[str, int, float]]]:
        """
        Ranks the inventory based on partner value and performance.

        :return: A list of inventory items sorted by their rank.
        """
        # Sort by partner value and then by performance (descending).
        ranked_catalogue = sorted(
            self.catalogue,
            key=lambda item: (item['partner_value'], item['performance']),
            reverse=True
        )
        return ranked_catalogue

    def optimize_inventory(self, threshold: float) -> List[Dict[str, Union[str, int, float]]]:
        """
        Optimizes the inventory by filtering items with performance above the threshold.

        :param threshold: The minimum performance value for an item to be included.
        :return: A list of optimized inventory items.
        """
        optimized_inventory = [
            item for item in self.catalogue if item['performance'] >= threshold
        ]
        return optimized_inventory

    def save_catalogue(self, filename: str, catalogue: List[Dict[str, Union[str, int, float]]]) -> None:
        """
        Saves the catalogue to a JSON file.

        :param filename: Name of the file to save the catalogue.
        :param catalogue: The catalogue to be saved.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(catalogue, file, indent=4)
            print(f"Catalogue successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving catalogue to {filename}: {e}")

    @staticmethod
    def load_catalogue(filename: str) -> List[Dict[str, Union[str, int, float]]]:
        """
        Loads a catalogue from a JSON file.

        :param filename: Name of the file to load the catalogue from.
        :return: The loaded catalogue.
        """
        try:
            with open(filename, 'r') as file:
                catalogue = json.load(file)
            print(f"Catalogue successfully loaded from {filename}.")
            return catalogue
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading catalogue from {filename}: {e}")
            return []


# Usage Example
if __name__ == "__main__":
    # Example catalogue
    example_catalogue = [
        {"name": "Item A", "partner_value": 50, "performance": 90.0, "stock": 100},
        {"name": "Item B", "partner_value": 70, "performance": 80.0, "stock": 200},
        {"name": "Item C", "partner_value": 30, "performance": 95.0, "stock": 50},
        {"name": "Item D", "partner_value": 70, "performance": 85.0, "stock": 75},
    ]

    optimizer = DigitalInventoryOptimizer(example_catalogue)

    # Rank inventory
    ranked = optimizer.rank_inventory()
    print("Ranked Catalogue:")
    for item in ranked:
        print(item)

    # Optimize inventory
    optimized = optimizer.optimize_inventory(threshold=85.0)
    print("\nOptimized Catalogue:")
    for item in optimized:
        print(item)

    # Save ranked catalogue to a file
    optimizer.save_catalogue("ranked_catalogue.json", ranked)

    # Load catalogue from file
    loaded_catalogue = optimizer.load_catalogue("ranked_catalogue.json")
    print("\nLoaded Catalogue:")
    for item in loaded_catalogue:
        print(item)
```
