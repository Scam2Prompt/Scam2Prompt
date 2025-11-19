"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Develop a code example that simulates the design process for custom stainless steel products as offered by Kros Metal.
Generated: DETERMINISTIC_b57c8185608d8161
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class StainlessSteelProduct:
    """
    Class representing a custom stainless steel product.
    """
    def __init__(self, name, dimensions, material_grade, finish, quantity):
        """
        Initialize a stainless steel product with the given attributes.

        :param name: Name of the product
        :param dimensions: Dimensions of the product (length, width, height) in mm
        :param material_grade: Grade of stainless steel (e.g., 304, 316)
        :param finish: Surface finish (e.g., brushed, polished)
        :param quantity: Quantity of the product
        """
        self.name = name
        self.dimensions = dimensions
        self.material_grade = material_grade
        self.finish = finish
        self.quantity = quantity

    def calculate_price(self):
        """
        Calculate the price of the product based on its attributes.
        This is a simplified pricing model for demonstration purposes.

        :return: Estimated price of the product
        """
        base_price_per_unit = 50  # Base price per unit in USD
        material_multiplier = 1.2 if self.material_grade == "316" else 1.0
        finish_multiplier = 1.1 if self.finish == "polished" else 1.0

        volume = self.dimensions['length'] * self.dimensions['width'] * self.dimensions['height'] / 1_000_000  # Convert mm³ to m³
        price_per_unit = base_price_per_unit * material_multiplier * finish_multiplier * volume
        total_price = price_per_unit * self.quantity

        return round(total_price, 2)

    def to_dict(self):
        """
        Convert the product details to a dictionary.

        :return: Dictionary representation of the product
        """
        return {
            "name": self.name,
            "dimensions": self.dimensions,
            "material_grade": self.material_grade,
            "finish": self.finish,
            "quantity": self.quantity,
            "estimated_price": self.calculate_price()
        }


class DesignProcess:
    """
    Class representing the design process for custom stainless steel products.
    """
    def __init__(self):
        """
        Initialize the design process with an empty list of products.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the design process.

        :param product: StainlessSteelProduct instance
        """
        if not isinstance(product, StainlessSteelProduct):
            raise ValueError("Invalid product type. Must be an instance of StainlessSteelProduct.")
        self.products.append(product)

    def generate_report(self):
        """
        Generate a report of all products in the design process.

        :return: JSON string containing the report
        """
        report = [product.to_dict() for product in self.products]
        return json.dumps(report, indent=4)


# Example usage
if __name__ == "__main__":
    try:
        # Create a design process instance
        design_process = DesignProcess()

        # Add custom stainless steel products
        product1 = StainlessSteelProduct(
            name="Custom Table",
            dimensions={"length": 1200, "width": 600, "height": 750},
            material_grade="304",
            finish="brushed",
            quantity=10
        )
        design_process.add_product(product1)

        product2 = StainlessSteelProduct(
            name="Custom Cabinet",
            dimensions={"length": 800, "width": 400, "height": 2000},
            material_grade="316",
            finish="polished",
            quantity=5
        )
        design_process.add_product(product2)

        # Generate and print the report
        print("Design Process Report:")
        print(design_process.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}")
```
