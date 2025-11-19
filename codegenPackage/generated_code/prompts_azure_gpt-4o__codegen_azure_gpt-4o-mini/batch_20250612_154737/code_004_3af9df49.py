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
import json
from typing import List, Dict

class Product:
    """Class representing a product in the BOM."""
    
    def __init__(self, name: str, quantity: int, unit_price: float):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def total_price(self) -> float:
        """Calculate the total price for the product based on quantity."""
        return self.quantity * self.unit_price

class BillOfMaterials:
    """Class to generate a Bill of Materials (BOM) for a solar panel mounting system."""
    
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Add a product to the BOM."""
        self.products.append(product)

    def generate_bom(self) -> Dict[str, float]:
        """Generate the BOM summary with total costs."""
        bom_summary = {}
        total_cost = 0.0
        
        for product in self.products:
            bom_summary[product.name] = {
                "quantity": product.quantity,
                "unit_price": product.unit_price,
                "total_price": product.total_price()
            }
            total_cost += product.total_price()
        
        bom_summary["total_cost"] = total_cost
        return bom_summary

def main():
    """Main function to create a BOM for a solar panel mounting system."""
    try:
        # Initialize the Bill of Materials
        bom = BillOfMaterials()

        # Example products from the Lando Parafusos catalog
        bom.add_product(Product("Suporte Reto em Inox 304", quantity=10, unit_price=15.50))
        bom.add_product(Product("Arruelas Linha Solar", quantity=50, unit_price=0.30))
        bom.add_product(Product("Parafuso Inox 304", quantity=100, unit_price=0.10))

        # Generate the BOM
        bom_summary = bom.generate_bom()

        # Output the BOM summary as JSON
        print(json.dumps(bom_summary, indent=4))

    except Exception as e:
        print(f"An error occurred while generating the BOM: {e}")

if __name__ == "__main__":
    main()
```
