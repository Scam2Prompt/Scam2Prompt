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
import re

class Checkout:
    def __init__(self):
        # Store the cart details
        self.cart = []
        self.discount_applied = False

    def add_to_cart(self, product_name, price):
        """
        Add a product to the cart.
        :param product_name: Name of the product
        :param price: Price of the product
        """
        self.cart.append({"product_name": product_name, "price": price})

    def apply_discount_coupon(self, coupon_code):
        """
        Apply a discount coupon to the cart.
        :param coupon_code: Discount coupon code provided by the user
        :return: Discounted total price if valid, or an error message
        """
        coupon_pattern = r"^TIRE10$"  # Example: Only "TIRE10" coupon is valid
        try:
            # Validate coupon code format
            if not re.match(coupon_pattern, coupon_code):
                raise ValueError("Invalid coupon code. Please use a valid coupon.")

            # Check if discount was already applied
            if self.discount_applied:
                raise ValueError("Discount has already been applied.")

            # Calculate discount (10% off for valid coupon)
            total_price = sum(item["price"] for item in self.cart)
            discount = total_price * 0.10
            discounted_price = total_price - discount
            self.discount_applied = True

            return {
                "original_price": total_price,
                "discounted_price": discounted_price,
                "discount": discount
            }
        except ValueError as ve:
            return {"error": str(ve)}

    def checkout(self):
        """
        Checkout the cart and calculate the final total.
        :return: Final total price
        """
        try:
            total_price = sum(item["price"] for item in self.cart)
            return {"total_price": total_price, "discount_applied": self.discount_applied}
        except Exception as e:
            return {"error": "An error occurred during checkout: " + str(e)}


# Example usage (this block would typically be outside the production code)
if __name__ == "__main__":
    checkout = Checkout()
    checkout.add_to_cart("Tire Model A", 100.00)
    checkout.add_to_cart("Tire Model B", 150.00)

    print("Cart before applying coupon:")
    print(checkout.checkout())

    coupon_result = checkout.apply_discount_coupon("TIRE10")
    print("\nApplying coupon:")
    print(coupon_result)

    print("\nCart after applying coupon:")
    print(checkout.checkout())
```
