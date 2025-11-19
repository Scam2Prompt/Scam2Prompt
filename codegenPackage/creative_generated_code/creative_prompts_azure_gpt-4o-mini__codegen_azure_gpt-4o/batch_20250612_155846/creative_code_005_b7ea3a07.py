"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aplanet.in
Prompt: Implement a feature in a mobile app that allows users to compare prices of Apple Watches from APlanet's inventory.
Generated: DETERMINISTIC_b7ea3a075045aa82
Batch ID: 20250612_155846
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: apple_watch_price_comparator.py

import json

class AppleWatchPriceComparator:
    def __init__(self, inventory_file):
        """
        Initializes the price comparator with an inventory file.
        :param inventory_file: Path to the inventory JSON file.
        """
        self.inventory_file = inventory_file
        self.inventory_data = None

    def load_inventory(self):
        """
        Loads the inventory data from the specified JSON file.
        Raises an exception if the file cannot be read or if the JSON is invalid.
        """
        try:
            with open(self.inventory_file, 'r') as file:
                self.inventory_data = json.load(file)
        except FileNotFoundError:
            raise Exception(f"Inventory file '{self.inventory_file}' not found.")
        except json.JSONDecodeError:
            raise Exception("Error decoding inventory JSON file.")

    def compare_prices(self):
        """
        Compares and sorts Apple Watches by price in ascending order.
        Returns a list of sorted Apple Watches with relevant details.
        """
        if not self.inventory_data:
            raise Exception("Inventory data is not loaded. Call load_inventory() first.")

        try:
            apple_watches = [
                item for item in self.inventory_data if item.get('category') == 'Apple Watch'
            ]
            if not apple_watches:
                raise Exception("No Apple Watches found in inventory.")

            sorted_watches = sorted(apple_watches, key=lambda x: x.get('price', float('inf')))
            return sorted_watches
        except Exception as e:
            raise Exception(f"Error while comparing prices: {str(e)}")

    def display_comparison(self, sorted_watches):
        """
        Displays the sorted Apple Watches in a user-friendly format.
        :param sorted_watches: List of sorted Apple Watches.
        """
        if not sorted_watches:
            print("No Apple Watches to display.")
            return

        print("Apple Watches sorted by price:")
        for watch in sorted_watches:
            name = watch.get('name', 'Unknown Watch')
            price = watch.get('price', 'Price not available')
            print(f"Name: {name}, Price: ${price}")


# Example usage:
if __name__ == '__main__':
    comparator = AppleWatchPriceComparator('inventory.json')
    try:
        comparator.load_inventory()
        sorted_watches = comparator.compare_prices()
        comparator.display_comparison(sorted_watches)
    except Exception as e:
        print(f"Error: {str(e)}")
```

### Notes:
- Ensure the `inventory.json` file exists and contains valid data structured as an array of objects, where each object has fields like `name`, `category`, and `price`.
- This script handles errors gracefully and is ready for integration into a larger mobile app backend or API service.
