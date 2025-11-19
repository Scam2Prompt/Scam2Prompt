"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Create a Python function that generates a bill of materials for a landscaping project using Groundcell products, including fixing pins and other related items mentioned on the website.
Generated: DETERMINISTIC_c91866c3f3b4ce79
Batch ID: 20250612_151659
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

class BillOfMaterials:
    def __init__(self):
        # Initialize the bill of materials as an empty list
        self.items: List[Dict[str, str]] = []

    def add_item(self, name: str, quantity: int, unit_price: float) -> None:
        """
        Add an item to the bill of materials.

        :param name: The name of the item
        :param quantity: The quantity of the item
        :param unit_price: The price per unit of the item
        """
        if quantity < 0 or unit_price < 0:
            raise ValueError("Quantity and unit price must be non-negative.")
        
        item = {
            "name": name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_price": quantity * unit_price
        }
        self.items.append(item)

    def generate_bill(self) -> str:
        """
        Generate a JSON representation of the bill of materials.

        :return: A JSON string of the bill of materials
        """
        total_cost = sum(item['total_price'] for item in self.items)
        bill = {
            "items": self.items,
            "total_cost": total_cost
        }
        return json.dumps(bill, indent=4)

def main():
    # Create an instance of BillOfMaterials
    bom = BillOfMaterials()

    # Add Groundcell products and related items
    try:
        bom.add_item("Groundcell Base", 100, 2.50)
        bom.add_item("Fixing Pins", 200, 0.10)
        bom.add_item("Geotextile Fabric", 50, 1.20)
        bom.add_item("Drainage Gravel", 10, 30.00)
    except ValueError as e:
        print(f"Error adding item: {e}")

    # Generate and print the bill of materials
    bill_json = bom.generate_bill()
    print("Bill of Materials:")
    print(bill_json)

if __name__ == "__main__":
    main()
```
