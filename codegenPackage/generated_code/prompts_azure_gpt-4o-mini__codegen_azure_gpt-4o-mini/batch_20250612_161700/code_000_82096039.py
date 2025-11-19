"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: Generate a Python script that automates the process of calculating laundry costs based on the pricing table from Lavandería Autoservicio Zaragoza.
Generated: DETERMINISTIC_82096039101ca5f6
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class LaundryCostCalculator:
    """
    A class to calculate laundry costs based on a predefined pricing table.
    """

    def __init__(self, pricing_table):
        """
        Initializes the LaundryCostCalculator with a pricing table.

        :param pricing_table: A dictionary containing the pricing for different laundry items.
        """
        self.pricing_table = pricing_table

    def calculate_cost(self, item, quantity):
        """
        Calculates the total cost for a given laundry item and quantity.

        :param item: The type of laundry item (e.g., 'shirt', 'pants').
        :param quantity: The number of items to be laundered.
        :return: The total cost for the laundry items.
        :raises ValueError: If the item is not found in the pricing table or quantity is not positive.
        """
        if item not in self.pricing_table:
            raise ValueError(f"Item '{item}' not found in pricing table.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        cost_per_item = self.pricing_table[item]
        total_cost = cost_per_item * quantity
        return total_cost

def load_pricing_table(file_path):
    """
    Loads the pricing table from a JSON file.

    :param file_path: The path to the JSON file containing the pricing table.
    :return: A dictionary containing the pricing table.
    :raises FileNotFoundError: If the file does not exist.
    :raises json.JSONDecodeError: If the file is not a valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            pricing_table = json.load(file)
            return pricing_table
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file '{file_path}' is not a valid JSON.")

def main():
    """
    Main function to execute the laundry cost calculation.
    """
    # Load the pricing table from a JSON file
    pricing_file = 'pricing_table.json'
    try:
        pricing_table = load_pricing_table(pricing_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error loading pricing table: {e}")
        return

    # Create an instance of the LaundryCostCalculator
    calculator = LaundryCostCalculator(pricing_table)

    # Example usage
    try:
        item = 'shirt'  # Example item
        quantity = 5    # Example quantity
        total_cost = calculator.calculate_cost(item, quantity)
        print(f"The total cost for {quantity} {item}(s) is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error calculating cost: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that you have a `pricing_table.json` file in the same directory as this script, containing the pricing data in JSON format, for example:
```json
{
    "shirt": 2.5,
    "pants": 3.0,
    "socks": 1.0
}
```
