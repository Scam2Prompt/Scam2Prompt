"""
Generated Code Metadata:
========================
Original URL: https://tiburonfishingreels.com
Prompt: How can I implement a shopping cart feature for a fishing reel website similar to Tiburon Fishing Reels, including international shipping options?
Generated: DETERMINISTIC_689f5e4a6c61fde9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from decimal import Decimal

class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, product_id, name, price, weight):
        """
        Initialize a product with an ID, name, price, and weight.
        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product (Decimal for precision)
        :param weight: Weight of the product in kilograms
        """
        self.product_id = product_id
        self.name = name
        self.price = Decimal(price)
        self.weight = weight

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price}, {self.weight}kg)"


class ShoppingCart:
    """
    Represents a shopping cart for the website.
    """
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.items = {}  # Dictionary to store product_id as key and quantity as value

    def add_item(self, product, quantity=1):
        """
        Add a product to the shopping cart.
        :param product: Product object to add
        :param quantity: Quantity of the product to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id, quantity=1):
        """
        Remove a product or reduce its quantity in the shopping cart.
        :param product_id: ID of the product to remove
        :param quantity: Quantity to remove
        """
        if product_id not in self.items:
            raise KeyError("Product not found in the cart.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if self.items[product_id]['quantity'] <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id]['quantity'] -= quantity

    def calculate_total(self):
        """
        Calculate the total price of items in the cart.
        :return: Total price as Decimal
        """
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def calculate_shipping(self, destination_country):
        """
        Calculate shipping cost based on destination and total weight.
        :param destination_country: Country to ship to
        :return: Shipping cost as Decimal
        """
        total_weight = sum(item['product'].weight * item['quantity'] for item in self.items.values())
        if destination_country.lower() == "us":
            return Decimal(total_weight * 5)  # $5 per kg for domestic shipping
        else:
            return Decimal(total_weight * 15)  # $15 per kg for international shipping

    def clear_cart(self):
        """
        Clear all items from the shopping cart.
        """
        self.items.clear()

    def __repr__(self):
        return f"ShoppingCart({self.items})"


# Example usage
if __name__ == "__main__":
    try:
        # Create some products
        reel1 = Product(product_id=1, name="Tiburon Reel A", price="199.99", weight=1.5)
        reel2 = Product(product_id=2, name="Tiburon Reel B", price="299.99", weight=2.0)

        # Initialize shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(reel1, quantity=2)
        cart.add_item(reel2, quantity=1)

        # Display cart contents
        print("Cart Contents:", cart)

        # Calculate total price
        print("Total Price: $", cart.calculate_total())

        # Calculate shipping cost
        print("Shipping Cost (US): $", cart.calculate_shipping("US"))
        print("Shipping Cost (International): $", cart.calculate_shipping("Canada"))

        # Remove an item
        cart.remove_item(product_id=1, quantity=1)
        print("Cart Contents after removal:", cart)

        # Clear the cart
        cart.clear_cart()
        print("Cart after clearing:", cart)

    except Exception as e:
        print("An error occurred:", e)
```
