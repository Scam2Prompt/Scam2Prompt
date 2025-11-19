"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tiburonfishingreels.com
Prompt: How can I implement a shopping cart feature for a fishing reel website similar to Tiburon Fishing Reels, including international shipping options?
Generated: DETERMINISTIC_689f5e4a6c61fde9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script implements a shopping cart feature for a fishing reel website. 
It supports adding/removing items, calculating totals, and handling international shipping options.
"""

import json

class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, product_id, name, price, weight):
        self.product_id = product_id
        self.name = name
        self.price = price      # Price in USD
        self.weight = weight    # Weight in kilograms

    def __str__(self):
        return f"Product({self.name}, ${self.price})"


class ShoppingCart:
    """
    Represents a shopping cart where users can add, remove, and view items.
    """
    def __init__(self):
        self.items = []  # List of products in the cart

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.
        :param product: Product object to add
        :param quantity: Number of the product to add (default: 1)
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_id):
        """
        Removes a product from the shopping cart by product_id.
        :param product_id: ID of the product to remove
        """
        self.items = [
            item for item in self.items if item['product'].product_id != product_id
        ]

    def calculate_total(self):
        """
        Calculates the total cost of items in the shopping cart.
        :return: Total cost in USD
        """
        return sum(item['product'].price * item['quantity'] for item in self.items)

    def calculate_shipping_cost(self, country="USA"):
        """
        Calculates the shipping cost based on the destination country.
        :param country: Destination country for shipping
        :return: Shipping cost in USD
        """
        total_weight = sum(item['product'].weight * item['quantity'] for item in self.items)
        base_shipping_rate = 5.0  # Base rate in USD per kg

        # Apply international shipping multiplier
        country_shipping_multiplier = 1.0 if country == "USA" else 2.0

        return total_weight * base_shipping_rate * country_shipping_multiplier

    def checkout(self, country="USA"):
        """
        Finalizes the shopping cart and provides the total amount to pay.
        :param country: Destination country for shipping
        :return: Detailed receipt with total cost and shipping cost
        """
        try:
            total = self.calculate_total()
            shipping_cost = self.calculate_shipping_cost(country)
            grand_total = total + shipping_cost

            receipt = {
                "items": [
                    {
                        "product_id": item["product"].product_id,
                        "name": item["product"].name,
                        "quantity": item["quantity"],
                        "price_per_item": item["product"].price,
                        "total_price": item["product"].price * item["quantity"],
                    } for item in self.items
                ],
                "subtotal": total,
                "shipping_cost": shipping_cost,
                "grand_total": grand_total,
                "shipping_country": country
            }

            return json.dumps(receipt, indent=4)

        except Exception as e:
            return f"Error during checkout: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Create sample products
    reel1 = Product(product_id=1, name="Tiburon Reel X100", price=299.99, weight=1.2)
    reel2 = Product(product_id=2, name="Tiburon Reel X200", price=399.99, weight=1.5)

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(reel1, quantity=2)
    cart.add_item(reel2, quantity=1)

    # Remove an item
    cart.remove_item(product_id=1)

    # Checkout
    receipt = cart.checkout(country="UK")
    print(receipt)
```
