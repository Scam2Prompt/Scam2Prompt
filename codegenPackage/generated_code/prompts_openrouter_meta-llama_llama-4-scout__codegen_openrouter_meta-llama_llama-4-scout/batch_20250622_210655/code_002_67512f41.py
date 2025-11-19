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
# Define a class for CoffeeTable
class CoffeeTable:
    def __init__(self, name, price, length, width, height):
        """
        Initialize a CoffeeTable object.

        Args:
            name (str): Name of the coffee table.
            price (float): Price of the coffee table.
            length (float): Length of the coffee table in cm.
            width (float): Width of the coffee table in cm.
            height (float): Height of the coffee table in cm.
        """
        self.name = name
        self.price = price
        self.dimensions = {
            "length": length,
            "width": width,
            "height": height
        }

    def __str__(self):
        return f"Coffee Table: {self.name}\nPrice: {self.price} RUB\nDimensions: {self.dimensions['length']} x {self.dimensions['width']} x {self.dimensions['height']} cm"


# Define a function to generate a list of coffee tables
def generate_coffee_tables():
    """
    Generate a list of coffee tables with glass tops.

    Returns:
        list: A list of CoffeeTable objects.
    """
    try:
        # Define coffee tables
        tables = [
            CoffeeTable("Веста", 12000.0, 80, 40, 45),
            CoffeeTable("Изида", 15000.0, 90, 50, 42),
            CoffeeTable("Астра", 18000.0, 100, 60, 40),
            CoffeeTable("Лига", 10000.0, 70, 35, 48)
        ]

        return tables

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Define a function to print coffee tables
def print_coffee_tables(tables):
    """
    Print a list of coffee tables.

    Args:
        tables (list): A list of CoffeeTable objects.
    """
    if not tables:
        print("No coffee tables available.")
        return

    for i, table in enumerate(tables, start=1):
        print(f"Table {i}:")
        print(table)
        print("------------------------")


# Main function
def main():
    coffee_tables = generate_coffee_tables()
    print_coffee_tables(coffee_tables)


if __name__ == "__main__":
    main()
```
