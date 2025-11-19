"""
Generated Code Metadata:
========================
Original URL: https://krosmetal.com
Prompt: Create a program to calculate the cost of stainless steel raw materials, including profiles, rods, and sheets, based on the types of products sold by Kros Metal.
Generated: DETERMINISTIC_eb48d3284e99ec5a
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# stainless_steel_calculator.py

class StainlessSteelProduct:
    """Base class for stainless steel products."""

    def __init__(self, name, price_per_unit, unit):
        """
        Initialize a stainless steel product.

        Args:
        - name (str): Product name.
        - price_per_unit (float): Price per unit of the product.
        - unit (str): Unit of measurement for the product (e.g., kg, m, sheet).
        """
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit

    def calculate_cost(self, quantity):
        """
        Calculate the cost of the product.

        Args:
        - quantity (float): Quantity of the product.

        Returns:
        - float: Total cost of the product.
        """
        return self.price_per_unit * quantity


class Profile(StainlessSteelProduct):
    """Class for stainless steel profiles."""

    def __init__(self, name, price_per_kg):
        """
        Initialize a stainless steel profile.

        Args:
        - name (str): Profile name.
        - price_per_kg (float): Price per kilogram of the profile.
        """
        super().__init__(name, price_per_kg, "kg")


class Rod(StainlessSteelProduct):
    """Class for stainless steel rods."""

    def __init__(self, name, price_per_kg):
        """
        Initialize a stainless steel rod.

        Args:
        - name (str): Rod name.
        - price_per_kg (float): Price per kilogram of the rod.
        """
        super().__init__(name, price_per_kg, "kg")


class Sheet(StainlessSteelProduct):
    """Class for stainless steel sheets."""

    def __init__(self, name, price_per_sheet):
        """
        Initialize a stainless steel sheet.

        Args:
        - name (str): Sheet name.
        - price_per_sheet (float): Price per sheet.
        """
        super().__init__(name, price_per_sheet, "sheet")


class StainlessSteelCalculator:
    """Class for calculating the cost of stainless steel raw materials."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the calculator.

        Args:
        - product (StainlessSteelProduct): Product to add.
        """
        self.products.append(product)

    def calculate_total_cost(self, product_quantities):
        """
        Calculate the total cost of the products.

        Args:
        - product_quantities (dict): Dictionary of product names and quantities.

        Returns:
        - float: Total cost of the products.

        Raises:
        - ValueError: If a product is not found in the calculator.
        """
        total_cost = 0
        for product_name, quantity in product_quantities.items():
            product = next((p for p in self.products if p.name == product_name), None)
            if product is None:
                raise ValueError(f"Product '{product_name}' not found.")
            total_cost += product.calculate_cost(quantity)
        return total_cost


def main():
    calculator = StainlessSteelCalculator()

    # Add products
    profile = Profile("Profile 1", 10.0)
    rod = Rod("Rod 1", 5.0)
    sheet = Sheet("Sheet 1", 50.0)
    calculator.add_product(profile)
    calculator.add_product(rod)
    calculator.add_product(sheet)

    # Calculate total cost
    product_quantities = {
        "Profile 1": 100.0,  # 100 kg
        "Rod 1": 50.0,      # 50 kg
        "Sheet 1": 20.0     # 20 sheets
    }
    try:
        total_cost = calculator.calculate_total_cost(product_quantities)
        print(f"Total cost: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
