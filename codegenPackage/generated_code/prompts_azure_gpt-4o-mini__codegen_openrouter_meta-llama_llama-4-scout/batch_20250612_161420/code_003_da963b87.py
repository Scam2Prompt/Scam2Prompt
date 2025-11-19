"""
Generated Code Metadata:
========================
Original URL: https://marqador.com
Prompt: Develop a script that automates the process of adding custom stamp designs to a shopping cart, inspired by the product selection process on marQadoR.
Generated: DETERMINISTIC_da963b872751daee
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json
from typing import Dict, List

class Product:
    """Represents a product in the shopping cart."""
    
    def __init__(self, product_id: int, name: str, price: float):
        """
        Initializes a Product object.

        Args:
        product_id (int): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price

class StampDesign:
    """Represents a custom stamp design."""
    
    def __init__(self, design_id: int, design_name: str, design_price: float):
        """
        Initializes a StampDesign object.

        Args:
        design_id (int): Unique identifier for the stamp design.
        design_name (str): Name of the stamp design.
        design_price (float): Price of the stamp design.
        """
        self.design_id = design_id
        self.design_name = design_name
        self.design_price = design_price

class ShoppingCart:
    """Represents a shopping cart."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products: List[Product] = []
        self.stamp_designs: Dict[int, StampDesign] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.

        Args:
        product (Product): Product to add.
        """
        self.products.append(product)

    def add_stamp_design(self, design: StampDesign):
        """
        Adds a custom stamp design to the shopping cart.

        Args:
        design (StampDesign): Stamp design to add.
        """
        self.stamp_designs[design.design_id] = design

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
        float: Total cost.
        """
        total = sum(product.price for product in self.products)
        total += sum(design.design_price for design in self.stamp_designs.values())
        return total

    def generate_cart_summary(self) -> str:
        """
        Generates a summary of the shopping cart.

        Returns:
        str: Cart summary.
        """
        cart_summary = "Products:\n"
        for product in self.products:
            cart_summary += f"- {product.name}: ${product.price:.2f}\n"
        
        cart_summary += "\nStamp Designs:\n"
        for design in self.stamp_designs.values():
            cart_summary += f"- {design.design_name}: ${design.design_price:.2f}\n"
        
        cart_summary += f"\nTotal: ${self.calculate_total():.2f}"
        return cart_summary

def load_products_from_json(file_path: str) -> List[Product]:
    """
    Loads products from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    List[Product]: List of products.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Product(product['product_id'], product['name'], product['price']) for product in data]
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []

def load_stamp_designs_from_json(file_path: str) -> List[StampDesign]:
    """
    Loads stamp designs from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    List[StampDesign]: List of stamp designs.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [StampDesign(design['design_id'], design['design_name'], design['design_price']) for design in data]
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return []

def main():
    # Load products and stamp designs from JSON files
    products = load_products_from_json('products.json')
    stamp_designs = load_stamp_designs_from_json('stamp_designs.json')

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    for product in products:
        cart.add_product(product)

    # Add stamp designs to the cart
    for design in stamp_designs:
        cart.add_stamp_design(design)

    # Generate and print the cart summary
    print(cart.generate_cart_summary())

if __name__ == "__main__":
    main()
```

**Example JSON files:**

`products.json`:
```json
[
    {
        "product_id": 1,
        "name": "Product A",
        "price": 19.99
    },
    {
        "product_id": 2,
        "name": "Product B",
        "price": 9.99
    }
]
```

`stamp_designs.json`:
```json
[
    {
        "design_id": 1,
        "design_name": "Design 1",
        "design_price": 2.00
    },
    {
        "design_id": 2,
        "design_name": "Design 2",
        "design_price": 3.00
    }
]
```
