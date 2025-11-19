"""
Generated Code Metadata:
========================
Original URL: https://landoparafusos.blogspot.com
Prompt: Write code to generate a bill of materials (BOM) for a solar panel mounting system using the products listed in the Lando Parafusos catalog, such as "Suporte Reto em Inox 304" and "Arruelas Linha Solar".
Generated: DETERMINISTIC_3af9df494fc8300a
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bom_generator.py

class Product:
    """Represents a product in the Lando Parafusos catalog."""

    def __init__(self, name, description, quantity, unit_price):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            description (str): Product description.
            quantity (int): Product quantity.
            unit_price (float): Product unit price.
        """
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price

    def total_price(self):
        """Calculates the total price of the product."""
        return self.quantity * self.unit_price


class BillOfMaterials:
    """Represents a bill of materials (BOM) for a solar panel mounting system."""

    def __init__(self):
        """Initializes an empty BOM."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the BOM.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def calculate_subtotal(self):
        """Calculates the subtotal of the BOM."""
        return sum(product.total_price() for product in self.products)

    def calculate_tax(self, tax_rate):
        """
        Calculates the tax amount of the BOM.

        Args:
            tax_rate (float): Tax rate (e.g., 0.08 for 8%).

        Returns:
            float: Tax amount.
        """
        subtotal = self.calculate_subtotal()
        return subtotal * tax_rate

    def calculate_total(self, tax_rate):
        """
        Calculates the total cost of the BOM.

        Args:
            tax_rate (float): Tax rate (e.g., 0.08 for 8%).

        Returns:
            float: Total cost.
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        return subtotal + tax

    def generate_bom(self, tax_rate):
        """
        Generates the BOM report.

        Args:
            tax_rate (float): Tax rate (e.g., 0.08 for 8%).

        Returns:
            str: BOM report.
        """
        report = "Bill of Materials\n"
        report += "-----------------\n"
        for i, product in enumerate(self.products, start=1):
            report += f"{i}. {product.name} - {product.description}\n"
            report += f"  Quantity: {product.quantity}\n"
            report += f"  Unit Price: ${product.unit_price:.2f}\n"
            report += f"  Total Price: ${product.total_price():.2f}\n\n"
        report += f"Subtotal: ${self.calculate_subtotal():.2f}\n"
        report += f"Tax ({tax_rate*100}%): ${self.calculate_tax(tax_rate):.2f}\n"
        report += f"Total: ${self.calculate_total(tax_rate):.2f}\n"
        return report


def main():
    try:
        # Create products
        suporte_reto = Product("Suporte Reto em Inox 304", "Stainless steel support", 10, 50.0)
        arruelas_linha_solar = Product("Arruelas Linha Solar", "Solar line washers", 20, 10.0)
        parafusos = Product("Parafusos", "Screws", 50, 5.0)

        # Create BOM
        bom = BillOfMaterials()
        bom.add_product(suporte_reto)
        bom.add_product(arruelas_linha_solar)
        bom.add_product(parafusos)

        # Generate BOM report
        tax_rate = 0.08  # 8% tax rate
        report = bom.generate_bom(tax_rate)
        print(report)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
