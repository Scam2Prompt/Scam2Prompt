"""
Generated Code Metadata:
========================
Original URL: https://specialmetals.co.in
Prompt: Create a program to calculate the cost of bulk orders for products such as Alloy 20 Pipes and Stainless Steel 904L Pipes, using pricing data that could be extracted from the Dinkar Alloys website.
Generated: DETERMINISTIC_f6f68cb55d33d0d3
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bulk_order_calculator.py

class Product:
    """Represents a product with its name and price per unit."""

    def __init__(self, name, price_per_unit):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price_per_unit (float): The price per unit of the product.
        """
        self.name = name
        self.price_per_unit = price_per_unit


class BulkOrderCalculator:
    """Calculates the cost of bulk orders for products."""

    def __init__(self):
        """
        Initializes a BulkOrderCalculator instance with an empty product catalog.
        """
        self.product_catalog = {}

    def add_product(self, product):
        """
        Adds a product to the product catalog.

        Args:
            product (Product): The product to add.
        """
        self.product_catalog[product.name] = product

    def calculate_order_cost(self, product_name, quantity):
        """
        Calculates the cost of a bulk order.

        Args:
            product_name (str): The name of the product.
            quantity (int): The quantity of the product to order.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If the product is not found in the catalog or if the quantity is non-positive.
        """
        if product_name not in self.product_catalog:
            raise ValueError(f"Product '{product_name}' not found in catalog")

        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        product = self.product_catalog[product_name]
        return product.price_per_unit * quantity


def main():
    # Sample pricing data (replace with actual data from Dinkar Alloys website)
    alloy_20_pipe = Product("Alloy 20 Pipe", 100.0)
    stainless_steel_904l_pipe = Product("Stainless Steel 904L Pipe", 200.0)

    calculator = BulkOrderCalculator()
    calculator.add_product(alloy_20_pipe)
    calculator.add_product(stainless_steel_904l_pipe)

    try:
        product_name = input("Enter product name (e.g., Alloy 20 Pipe): ")
        quantity = int(input("Enter quantity: "))
        cost = calculator.calculate_order_cost(product_name, quantity)
        print(f"Total cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
