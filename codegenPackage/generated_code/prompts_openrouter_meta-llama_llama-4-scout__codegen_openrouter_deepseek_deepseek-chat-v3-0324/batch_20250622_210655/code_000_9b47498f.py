"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Generate a list of customized promotional products for a business event, including pens, notebooks, and bottles, with a focus on eco-friendly options."
Generated: DETERMINISTIC_9b47498f38ddf627
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PromotionalProduct:
    """Class representing a promotional product."""
    name: str
    description: str
    price: float
    is_eco_friendly: bool
    materials: List[str]
    minimum_order: int

class PromotionalProductGenerator:
    """Generates a list of customized promotional products."""
    
    def __init__(self):
        self.products = []
    
    def generate_products(self) -> List[PromotionalProduct]:
        """Generate a list of promotional products with eco-friendly options."""
        try:
            self.products = [
                PromotionalProduct(
                    name="Eco Pen",
                    description="Recycled plastic pen with plant-based ink",
                    price=0.99,
                    is_eco_friendly=True,
                    materials=["Recycled plastic", "Plant-based ink"],
                    minimum_order=100
                ),
                PromotionalProduct(
                    name="Bamboo Notebook",
                    description="Notebook made from sustainable bamboo paper",
                    price=4.50,
                    is_eco_friendly=True,
                    materials=["Bamboo paper", "Recycled cardboard cover"],
                    minimum_order=50
                ),
                PromotionalProduct(
                    name="Stainless Steel Bottle",
                    description="Reusable water bottle with company logo",
                    price=12.99,
                    is_eco_friendly=True,
                    materials=["Stainless steel", "Food-grade silicone"],
                    minimum_order=75
                ),
                PromotionalProduct(
                    name="Standard Pen",
                    description="Plastic pen with company branding",
                    price=0.50,
                    is_eco_friendly=False,
                    materials=["Plastic", "Petroleum-based ink"],
                    minimum_order=200
                ),
                PromotionalProduct(
                    name="Plastic Notebook",
                    description="Standard notebook with plastic cover",
                    price=3.25,
                    is_eco_friendly=False,
                    materials=["Paper", "Plastic"],
                    minimum_order=100
                ),
                PromotionalProduct(
                    name="Plastic Water Bottle",
                    description="Single-use plastic water bottle",
                    price=1.25,
                    is_eco_friendly=False,
                    materials=["PET plastic"],
                    minimum_order=150
                )
            ]
            return self.products
        except Exception as e:
            print(f"Error generating products: {e}")
            return []

    def filter_eco_friendly(self) -> List[PromotionalProduct]:
        """Filter and return only eco-friendly products."""
        return [product for product in self.products if product.is_eco_friendly]

    def get_product_summary(self) -> List[Dict]:
        """Return a summary of products with key details."""
        return [
            {
                "name": product.name,
                "price": product.price,
                "eco_friendly": product.is_eco_friendly,
                "minimum_order": product.minimum_order
            }
            for product in self.products
        ]

# Example usage
if __name__ == "__main__":
    generator = PromotionalProductGenerator()
    products = generator.generate_products()
    eco_friendly_products = generator.filter_eco_friendly()
    
    print("All Products:")
    for product in generator.get_product_summary():
        print(product)
    
    print("\nEco-Friendly Products:")
    for product in generator.filter_eco_friendly():
        print(f"{product.name} - {product.description}")
```
