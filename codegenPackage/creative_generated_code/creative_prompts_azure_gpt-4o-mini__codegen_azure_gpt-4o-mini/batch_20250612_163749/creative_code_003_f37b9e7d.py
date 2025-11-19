"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Develop a code snippet that applies a discount coupon during the checkout process for tire purchases, as described on the dcpneus site.
Generated: DETERMINISTIC_f37b9e7d04f027bf
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0.0
        self.discount_coupons = {"SAVE10": 0.10, "SAVE20": 0.20}  # Discount coupons dictionary

    def add_item(self, item_name, item_price):
        """Adds an item to the shopping cart."""
        if item_price < 0:
            raise ValueError("Item price cannot be negative.")
        self.items.append((item_name, item_price))
        self.total_price += item_price
        print(f"Added {item_name} for ${item_price:.2f}. Total price: ${self.total_price:.2f}")

    def apply_discount(self, coupon_code):
        """Applies a discount to the total price based on the coupon code."""
        if coupon_code not in self.discount_coupons:
            raise ValueError("Invalid coupon code.")
        
        discount = self.discount_coupons[coupon_code]
        discount_amount = self.total_price * discount
        self.total_price -= discount_amount
        print(f"Coupon {coupon_code} applied. Discount: ${discount_amount:.2f}. New total: ${self.total_price:.2f}")

    def checkout(self):
        """Completes the checkout process."""
        if not self.items:
            raise ValueError("Cannot checkout: the shopping cart is empty.")
        
        print(f"Checking out with items: {self.items}")
        print(f"Total amount to pay: ${self.total_price:.2f}")
        # Simulate payment processing (could be integrated with a payment gateway)
        print("Payment processed successfully. Thank you for your purchase!")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    try:
        cart.add_item("Tire A", 100.00)
        cart.add_item("Tire B", 150.00)
        cart.apply_discount("SAVE10")  # Apply a discount coupon
        cart.checkout()  # Finalize the purchase
    except ValueError as e:
        print(f"Error: {e}")
```
