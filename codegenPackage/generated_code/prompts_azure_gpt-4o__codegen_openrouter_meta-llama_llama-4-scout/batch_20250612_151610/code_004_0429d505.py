"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Write a program to generate a report comparing the resistance levels of different corrugated cardboard products, such as "Cartón Corrugado 1.64mts x 210gr" and "Cartón Corrugado 1.23mts x 110gr," based on their attributes from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_0429d505d0d0b25a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# corrugated_cardboard_report.py

class CorrugatedCardboard:
    """Represents a corrugated cardboard product."""

    def __init__(self, name, length, weight):
        """
        Initializes a CorrugatedCardboard object.

        Args:
            name (str): The name of the product.
            length (float): The length of the product in meters.
            weight (float): The weight of the product in grams per square meter.
        """
        self.name = name
        self.length = length
        self.weight = weight

    def calculate_resistance(self):
        """
        Calculates the resistance level of the product.

        The resistance level is calculated as the product of the length and weight.

        Returns:
            float: The resistance level of the product.
        """
        return self.length * self.weight


class CorrugatedCardboardReport:
    """Generates a report comparing the resistance levels of different corrugated cardboard products."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Adds a corrugated cardboard product to the report.

        Args:
            product (CorrugatedCardboard): The product to add.
        """
        self.products.append(product)

    def generate_report(self):
        """
        Generates the report comparing the resistance levels of the products.

        Returns:
            str: The report as a string.
        """
        if not self.products:
            return "No products added to the report."

        report = "Corrugated Cardboard Resistance Report\n"
        report += "----------------------------------------\n"

        for i, product in enumerate(self.products, start=1):
            resistance = product.calculate_resistance()
            report += f"{i}. {product.name}: {resistance:.2f} m*gr/m²\n"

        report += "\nComparison:\n"
        report += "-----------\n"

        max_resistance_product = max(self.products, key=lambda x: x.calculate_resistance())
        report += f"Highest resistance: {max_resistance_product.name} ({max_resistance_product.calculate_resistance():.2f} m*gr/m²)\n"

        min_resistance_product = min(self.products, key=lambda x: x.calculate_resistance())
        report += f"Lowest resistance: {min_resistance_product.name} ({min_resistance_product.calculate_resistance():.2f} m*gr/m²)\n"

        return report


def main():
    try:
        report = CorrugatedCardboardReport()

        product1 = CorrugatedCardboard("Cartón Corrugado 1.64mts x 210gr", 1.64, 210)
        product2 = CorrugatedCardboard("Cartón Corrugado 1.23mts x 110gr", 1.23, 110)

        report.add_product(product1)
        report.add_product(product2)

        print(report.generate_report())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
