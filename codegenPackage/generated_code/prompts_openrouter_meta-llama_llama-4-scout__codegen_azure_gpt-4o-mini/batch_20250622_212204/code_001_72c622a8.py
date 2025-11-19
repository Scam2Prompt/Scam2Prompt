"""
Generated Code Metadata:
========================
Original URL: https://pancakefarm.com
Prompt: Generate a product list for a farm that specializes in naturally reared meat, similar to Pancake Farm's offerings.
Generated: DETERMINISTIC_72c622a80e6dd055
Batch ID: 20250622_212204
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
    """Class representing a product in the farm's inventory."""
    
    def __init__(self, name: str, description: str, price: float, weight: float):
        """
        Initialize a new product.

        :param name: The name of the product.
        :param description: A brief description of the product.
        :param price: The price of the product.
        :param weight: The weight of the product in pounds.
        """
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    def to_dict(self) -> Dict:
        """Convert the product to a dictionary format for JSON serialization."""
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "weight": self.weight
        }

class FarmProductList:
    """Class to manage a list of farm products."""
    
    def __init__(self):
        """Initialize an empty product list."""
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """
        Add a product to the farm's inventory.

        :param product: An instance of Product to be added.
        """
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added.")
        self.products.append(product)

    def to_json(self) -> str:
        """Convert the product list to a JSON string."""
        return json.dumps([product.to_dict() for product in self.products], indent=4)

def main():
    """Main function to create a product list for the farm."""
    try:
        # Create an instance of FarmProductList
        farm_product_list = FarmProductList()

        # Define products
        products = [
            Product("Grass-Fed Beef", "Naturally reared beef from grass-fed cattle.", 8.99, 1.0),
            Product("Free-Range Chicken", "Organic free-range chicken, raised without antibiotics.", 5.49, 2.5),
            Product("Pasture-Raised Pork", "Pork from pigs raised on pasture, fed a natural diet.", 7.99, 1.5),
            Product("Heritage Turkey", "Heritage breed turkey, raised naturally for superior flavor.", 3.99, 10.0),
            Product("Grass-Fed Lamb", "Lamb from sheep raised on natural grass pastures.", 12.99, 1.2)
        ]

        # Add products to the farm's inventory
        for product in products:
            farm_product_list.add_product(product)

        # Output the product list in JSON format
        print(farm_product_list.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
