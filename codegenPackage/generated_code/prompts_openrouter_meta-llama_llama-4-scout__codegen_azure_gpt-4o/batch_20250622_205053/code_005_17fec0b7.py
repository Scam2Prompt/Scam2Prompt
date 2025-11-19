"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Create a simple checkout system with payment gateway integration (e.g., COD) and shipping cost calculation, inspired by the TikTok Shop VN checkout process.
Generated: DETERMINISTIC_17fec0b7c7ddec1f
Batch ID: 20250622_205053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class CheckoutSystem:
    """
    A simple checkout system with payment gateway integration (COD) and shipping cost calculation.
    """

    def __init__(self):
        # Initialize the cart and shipping cost
        self.cart = []
        self.shipping_cost = 0

    def add_to_cart(self, item_name, price, quantity=1):
        """
        Add an item to the cart.
        :param item_name: Name of the item
        :param price: Price of the item
        :param quantity: Quantity of the item
        """
        if price < 0 or quantity < 1:
            raise ValueError("Price must be non-negative and quantity must be at least 1.")
        self.cart.append({"item_name": item_name, "price": price, "quantity": quantity})

    def calculate_shipping_cost(self, distance_km):
        """
        Calculate shipping cost based on distance.
        :param distance_km: Distance in kilometers
        :return: Shipping cost
        """
        if distance_km < 0:
            raise ValueError("Distance must be non-negative.")
        # Example: $5 base cost + $0.5 per km
        self.shipping_cost = 5 + (0.5 * distance_km)
        return self.shipping_cost

    def calculate_total(self):
        """
        Calculate the total cost including shipping.
        :return: Total cost
        """
        cart_total = sum(item["price"] * item["quantity"] for item in self.cart)
        return cart_total + self.shipping_cost

    def checkout(self, payment_method="COD"):
        """
        Perform checkout process.
        :param payment_method: Payment method (default is "COD")
        :return: Confirmation message
        """
        if not self.cart:
            raise ValueError("Cart is empty. Add items before checkout.")
        if payment_method != "COD":
            raise ValueError("Currently, only 'COD' payment method is supported.")

        total_cost = self.calculate_total()
        return f"Checkout successful! Payment method: {payment_method}. Total cost: ${total_cost:.2f}"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the checkout system
        checkout_system = CheckoutSystem()

        # Add items to the cart
        checkout_system.add_to_cart("Item A", 10.0, 2)
        checkout_system.add_to_cart("Item B", 20.0, 1)

        # Calculate shipping cost
        distance = 10  # Example distance in km
        shipping_cost = checkout_system.calculate_shipping_cost(distance)
        print(f"Shipping cost: ${shipping_cost:.2f}")

        # Perform checkout
        confirmation = checkout_system.checkout(payment_method="COD")
        print(confirmation)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```
