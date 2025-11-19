"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Generate a list of coffee tables with glass tops, similar to the "Веста" and "Изида" tables, including their prices and dimensions.
Generated: DETERMINISTIC_67512f4132330f5f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coffee_tables.py

# Import necessary modules
import json

# Define a CoffeeTable class to represent each coffee table
class CoffeeTable:
    def __init__(self, name, price, dimensions, material):
        """
        Initialize a CoffeeTable object.

        :param name: Name of the coffee table
        :param price: Price of the coffee table in USD
        :param dimensions: Dimensions of the coffee table (length x width x height) in cm
        :param material: Material of the coffee table
        """
        self.name = name
        self.price = price
        self.dimensions = dimensions
        self.material = material

    def to_dict(self):
        """
        Convert the CoffeeTable object to a dictionary.

        :return: Dictionary representation of the coffee table
        """
        return {
            "name": self.name,
            "price": self.price,
            "dimensions": self.dimensions,
            "material": self.material,
        }

# Function to generate a list of coffee tables
def generate_coffee_tables():
    """
    Generate a list of coffee tables with glass tops.

    :return: List of CoffeeTable objects
    """
    try:
        # Define coffee tables with glass tops
        coffee_tables = [
            CoffeeTable("Веста", 120.99, "100x60x45", "Glass and Metal"),
            CoffeeTable("Изида", 150.75, "110x70x50", "Glass and Wood"),
            CoffeeTable("Aurora", 135.50, "90x50x40", "Glass and Steel"),
            CoffeeTable("Luna", 145.00, "95x55x42", "Glass and Aluminum"),
        ]

        return coffee_tables
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating coffee tables: {e}")
        return []

# Function to save coffee tables to a JSON file
def save_to_json(coffee_tables, filename="coffee_tables.json"):
    """
    Save the list of coffee tables to a JSON file.

    :param coffee_tables: List of CoffeeTable objects
    :param filename: Name of the JSON file to save the data
    """
    try:
        # Convert coffee tables to a list of dictionaries
        coffee_table_dicts = [table.to_dict() for table in coffee_tables]

        # Write the data to a JSON file
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(coffee_table_dicts, file, ensure_ascii=False, indent=4)

        print(f"Coffee tables successfully saved to {filename}")
    except Exception as e:
        # Handle any file I/O errors
        print(f"An error occurred while saving coffee tables to JSON: {e}")

# Main function to execute the script
if __name__ == "__main__":
    # Generate the list of coffee tables
    tables = generate_coffee_tables()

    # Save the coffee tables to a JSON file
    save_to_json(tables)
```
