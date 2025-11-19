"""
Generated Code Metadata:
========================
Original URL: https://codestiers.com
Prompt: "Write a code example to implement a 'copy and paste' coupon code feature, like the one used on Codestiers, which allows users to easily apply discounts at checkout."
Generated: DETERMINISTIC_986055c384d8d92d
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# coupon_code_applier.py

class CouponCodeApplier:
    """
    A class to handle coupon code application at checkout.
    """

    def __init__(self, cart):
        """
        Initialize the CouponCodeApplier with a cart.

        Args:
            cart (Cart): The cart object containing items.
        """
        self.cart = cart
        self.coupon_codes = {}

    def add_coupon_code(self, code, discount_type, discount_value):
        """
        Add a coupon code to the system.

        Args:
            code (str): The coupon code.
            discount_type (str): The type of discount (e.g., percentage, fixed).
            discount_value (float): The discount value.
        """
        self.coupon_codes[code] = {
            'discount_type': discount_type,
            'discount_value': discount_value
        }

    def apply_coupon_code(self, code):
        """
        Apply a coupon code to the cart.

        Args:
            code (str): The coupon code to apply.

        Returns:
            bool: Whether the coupon code was applied successfully.
        """
        if code not in self.coupon_codes:
            raise ValueError("Invalid coupon code")

        discount_type = self.coupon_codes[code]['discount_type']
        discount_value = self.coupon_codes[code]['discount_value']

        if discount_type == 'percentage':
            self.cart.apply_percentage_discount(discount_value)
        elif discount_type == 'fixed':
            self.cart.apply_fixed_discount(discount_value)
        else:
            raise ValueError("Unsupported discount type")

        return True

    def remove_coupon_code(self, code):
        """
        Remove a coupon code from the cart.

        Args:
            code (str): The coupon code to remove.

        Returns:
            bool: Whether the coupon code was removed successfully.
        """
        if code not in self.coupon_codes:
            raise ValueError("Invalid coupon code")

        # Revert discount
        discount_type = self.coupon_codes[code]['discount_type']
        discount_value = self.coupon_codes[code]['discount_value']

        if discount_type == 'percentage':
            self.cart.revert_percentage_discount(discount_value)
        elif discount_type == 'fixed':
            self.cart.revert_fixed_discount(discount_value)

        return True


class Cart:
    """
    A simple cart class to demonstrate coupon code application.
    """

    def __init__(self):
        """
        Initialize the Cart.
        """
        self.items = []
        self.subtotal = 0.0
        self.discount = 0.0

    def add_item(self, price):
        """
        Add an item to the cart.

        Args:
            price (float): The price of the item.
        """
        self.items.append(price)
        self.subtotal += price

    def apply_percentage_discount(self, percentage):
        """
        Apply a percentage discount to the cart.

        Args:
            percentage (float): The percentage discount.
        """
        self.discount = self.subtotal * (percentage / 100)

    def apply_fixed_discount(self, amount):
        """
        Apply a fixed discount to the cart.

        Args:
            amount (float): The fixed discount amount.
        """
        self.discount = min(self.subtotal, amount)

    def revert_percentage_discount(self, percentage):
        """
        Revert a percentage discount.

        Args:
            percentage (float): The percentage discount.
        """
        self.discount = 0.0

    def revert_fixed_discount(self, amount):
        """
        Revert a fixed discount.

        Args:
            amount (float): The fixed discount amount.
        """
        self.discount = 0.0

    def get_total(self):
        """
        Get the total cost of the cart.

        Returns:
            float: The total cost.
        """
        return self.subtotal - self.discount


def main():
    cart = Cart()
    cart.add_item(100.0)
    cart.add_item(50.0)

    applier = CouponCodeApplier(cart)
    applier.add_coupon_code('CODES10', 'percentage', 10)

    print("Subtotal: $", cart.subtotal)

    try:
        applier.apply_coupon_code('CODES10')
        print("Discount: $", cart.discount)
        print("Total: $", cart.get_total())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
