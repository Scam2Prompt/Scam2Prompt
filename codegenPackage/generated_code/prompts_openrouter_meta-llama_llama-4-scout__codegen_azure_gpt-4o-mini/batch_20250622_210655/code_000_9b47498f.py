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
import random
from typing import List, Dict

class PromotionalProduct:
    """Class representing a promotional product."""
    
    def __init__(self, name: str, eco_friendly: bool, price: float):
        """
        Initialize a new promotional product.

        :param name: Name of the product
        :param eco_friendly: Indicates if the product is eco-friendly
        :param price: Price of the product
        """
        self.name = name
        self.eco_friendly = eco_friendly
        self.price = price

    def __repr__(self):
        """Return a string representation of the product."""
        eco_status = "Eco-Friendly" if self.eco_friendly else "Not Eco-Friendly"
        return f"{self.name} ({eco_status}) - ${self.price:.2f}"


class PromotionalProductGenerator:
    """Class to generate a list of promotional products."""
    
    def __init__(self):
        """Initialize the product generator with a predefined list of products."""
        self.products = [
            PromotionalProduct("Biodegradable Pen", True, 1.50),
            PromotionalProduct("Recycled Notebook", True, 3.00),
            PromotionalProduct("Stainless Steel Water Bottle", True, 15.00),
            PromotionalProduct("Plastic Pen", False, 0.50),
            PromotionalProduct("Standard Notebook", False, 2.00),
            PromotionalProduct("Glass Water Bottle", True, 20.00),
        ]

    def get_customized_products(self, eco_friendly: bool) -> List[PromotionalProduct]:
        """
        Get a list of customized promotional products based on eco-friendliness.

        :param eco_friendly: Filter for eco-friendly products
        :return: List of promotional products
        """
        try:
            filtered_products = [product for product in self.products if product.eco_friendly == eco_friendly]
            if not filtered_products:
                raise ValueError("No products found matching the criteria.")
            return filtered_products
        except Exception as e:
            print(f"Error occurred while fetching products: {e}")
            return []


def main():
    """Main function to execute the promotional product generation."""
    generator = PromotionalProductGenerator()
    
    # Fetch eco-friendly products
    eco_friendly_products = generator.get_customized_products(eco_friendly=True)
    
    # Display the eco-friendly products
    print("Eco-Friendly Promotional Products:")
    for product in eco_friendly_products:
        print(product)

if __name__ == "__main__":
    main()
```
