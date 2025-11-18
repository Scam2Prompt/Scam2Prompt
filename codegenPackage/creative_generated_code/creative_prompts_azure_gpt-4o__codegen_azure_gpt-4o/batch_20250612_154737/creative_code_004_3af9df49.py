"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Write code to generate a bill of materials (BOM) for a solar panel mounting system using the products listed in the Lando Parafusos catalog, such as "Suporte Reto em Inox 304" and "Arruelas Linha Solar".
Generated: DETERMINISTIC_3af9df494fc8300a
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script: solar_panel_bom_generator.py
Description: Generate a Bill of Materials (BOM) for a solar panel mounting system using
             specific products from the Lando Parafusos catalog.
Author: [Your Name]
Date: [Today's Date]
"""

import csv


class SolarPanelBOMGenerator:
    """
    A class to generate a Bill of Materials (BOM) for a solar panel mounting system.
    """

    def __init__(self):
        """
        Initialize the BOM generator with predefined products from the catalog.
        """
        self.catalog_products = [
            {"name": "Suporte Reto em Inox 304", "unit_price": 12.50},
            {"name": "Arruelas Linha Solar", "unit_price": 0.35},
            {"name": "Parafuso Sextavado M8x60", "unit_price": 0.75},
            {"name": "Cantoneira Ajustável", "unit_price": 18.00},
            {"name": "Porca Sextavada M8", "unit_price": 0.25},
        ]
        self.bom_items = []

    def add_item(self, product_name, quantity):
        """
        Add an item to the BOM.
        :param product_name: Name of the product from the catalog.
        :param quantity: Quantity of the product required.
        """
        # Validate inputs
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        # Find the product in the catalog
        product = next(
            (item for item in self.catalog_products if item["name"] == product_name),
            None,
        )

        if not product:
            raise ValueError(f"Product '{product_name}' not found in the catalog.")

        # Calculate total cost for the item
        total_price = round(product["unit_price"] * quantity, 2)

        # Add the item to the BOM
        self.bom_items.append(
            {
                "product_name": product_name,
                "unit_price": product["unit_price"],
                "quantity": quantity,
                "total_price": total_price,
            }
        )

    def generate_bom_report(self, output_file):
        """
        Generate a BOM report as a CSV file.
        :param output_file: Name of the output CSV file.
        """
        if not self.bom_items:
            raise ValueError("No items in the BOM to generate the report.")

        # Define CSV headers
        headers = ["Product Name", "Unit Price", "Quantity", "Total Price"]

        try:
            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writeheader()

                for item in self.bom_items:
                    writer.writerow(
                        {
                            "Product Name": item["product_name"],
                            "Unit Price": f"${item['unit_price']:.2f}",
                            "Quantity": item["quantity"],
                            "Total Price": f"${item['total_price']:.2f}",
                        }
                    )
            print(f"BOM report successfully generated: {output_file}")
        except Exception as e:
            print(f"Error generating BOM report: {e}")


# Example usage
def main():
    """
    Main function to demonstrate the BOM generator functionality.
    """
    try:
        # Initialize the BOM generator
        bom_generator = SolarPanelBOMGenerator()

        # Add items to the BOM
        bom_generator.add_item("Suporte Reto em Inox 304", 10)
        bom_generator.add_item("Arruelas Linha Solar", 50)
        bom_generator.add_item("Parafuso Sextavado M8x60", 25)
        bom_generator.add_item("Cantoneira Ajustável", 5)
        bom_generator.add_item("Porca Sextavada M8", 25)

        # Generate BOM report
        bom_generator.generate_bom_report("solar_panel_bom.csv")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
