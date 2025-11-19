"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a code snippet to implement a discount system for products in a Lojavirtualnuvem store, similar to the 20% OFF and 35% OFF promotions shown on the webpage.
Generated: DETERMINISTIC_36eec794b21eee82
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import List, Dict

# Define a Product class to represent individual products
class Product:
    def __init__(self, name: str, price: float):
        """
        Initialize a Product instance.

        :param name: Name of the product
        :param price: Original price of the product
        """
        self.name = name
        self.price = price

    def apply_discount(self, discount_percentage: float) -> float:
        """
        Apply a discount to the product price.

        :param discount_percentage: Discount percentage to apply (e.g., 20 for 20%)
        :return: Discounted price
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100.")
        return round(self.price * (1 - discount_percentage / 100), 2)

# Define a function to apply discounts to a list of products
def apply_discounts(products: List[Product], discounts: Dict[str, float]) -> List[Dict[str, float]]:
    """
    Apply discounts to a list of products.

    :param products: List of Product objects
    :param discounts: Dictionary mapping product names to discount percentages
    :return: List of dictionaries containing product details with discounted prices
    """
    discounted_products = []
    for product in products:
        try:
            # Check if the product has a discount
            discount_percentage = discounts.get(product.name, 0)
            discounted_price = product.apply_discount(discount_percentage)
            discounted_products.append({
                "name": product.name,
                "original_price": product.price,
                "discount_percentage": discount_percentage,
                "discounted_price": discounted_price
            })
        except ValueError as e:
            print(f"Error applying discount to {product.name}: {e}")
    return discounted_products

# Example usage
if __name__ == "__main__":
    # Create a list of products
    products = [
        Product("Product A", 100.0),
        Product("Product B", 200.0),
        Product("Product C", 300.0)
    ]

    # Define discounts for specific products
    discounts = {
        "Product A": 20,  # 20% OFF
        "Product B": 35   # 35% OFF
    }

    # Apply discounts and print the results
    discounted_products = apply_discounts(products, discounts)
    for product in discounted_products:
        print(product)
```
