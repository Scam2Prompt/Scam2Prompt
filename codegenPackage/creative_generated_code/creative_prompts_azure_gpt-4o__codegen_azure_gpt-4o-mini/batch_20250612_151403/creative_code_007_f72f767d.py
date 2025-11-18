"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgiwindia.com
Prompt: Develop a Python script to calculate the total inventory of food grains like "Yellow Maize" and "Rice" using the product details from Jai Gurudev Industries.
Generated: DETERMINISTIC_f72f767d00516556
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from typing import Dict, List

class InventoryCalculator:
    """
    A class to calculate the total inventory of specific food grains from product details.
    """

    def __init__(self, filename: str):
        """
        Initializes the InventoryCalculator with the path to the CSV file.

        :param filename: The path to the CSV file containing product details.
        """
        self.filename = filename
        self.inventory: Dict[str, int] = {}

    def load_inventory(self) -> None:
        """
        Loads inventory data from a CSV file and populates the inventory dictionary.
        The expected CSV format is 'Product Name, Quantity'.
        """
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) != 2:
                        # Skip rows that do not contain exactly two columns
                        continue
                    product_name, quantity_str = row
                    try:
                        quantity = int(quantity_str)  # Convert quantity to integer
                    except ValueError:
                        # Log the error for invalid quantity format
                        print(f"Invalid quantity for product '{product_name}': '{quantity_str}'")
                        continue

                    # Accumulate quantities for each product
                    if product_name in self.inventory:
                        self.inventory[product_name] += quantity
                    else:
                        self.inventory[product_name] = quantity
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def calculate_total_inventory(self, products: List[str]) -> int:
        """
        Calculates the total inventory for the specified products.

        :param products: A list of product names to calculate the total for.
        :return: The total quantity of the specified products.
        """
        total_quantity = 0
        for product in products:
            total_quantity += self.inventory.get(product, 0)
        return total_quantity


if __name__ == "__main__":
    # Define the path to the CSV file
    csv_file_path = 'inventory.csv'
    
    # Create an instance of InventoryCalculator
    calculator = InventoryCalculator(csv_file_path)
    
    # Load the inventory data
    calculator.load_inventory()
    
    # Define the food grains to calculate total inventory for
    food_grains = ["Yellow Maize", "Rice"]
    
    # Calculate total inventory
    total_inventory = calculator.calculate_total_inventory(food_grains)
    
    # Output the result
    print(f"Total inventory for {', '.join(food_grains)}: {total_inventory}")
```

### CSV File Format Example (inventory.csv)
```
Yellow Maize, 100
Rice, 200
Wheat, 150
Yellow Maize, 50
Rice, not_a_number
```

This script will read the provided CSV file, calculate the total quantities for "Yellow Maize" and "Rice", and handle any errors that arise from invalid data or file access issues.
