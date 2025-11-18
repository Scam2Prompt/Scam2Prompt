"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Recommend an API or library for implementing a shopping cart system that supports discount coupons and installment payments, as seen on the "Dal Cortivo Pneus" e-commerce platform.
Generated: DETERMINISTIC_1d6e78a2d7f99dbd
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class DiscountCoupon:
    """Class to handle discount coupons"""

    def __init__(self, code: str, discount_percentage: float):
        """Initialize the DiscountCoupon with a code and discount percentage"""
        self.code = code
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_amount: float) -> float:
        """Apply discount on the total amount and return the discounted amount"""
        if not (0 <= self.discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = (self.discount_percentage / 100) * total_amount
        return total_amount - discount_amount


class CartItem:
    """Class to represent an item in the shopping cart"""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize an item with a name, price, and quantity"""
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculate the total price for the item"""
        return self.price * self.quantity


class ShoppingCart:
    """Class to represent a shopping cart"""

    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = []

    def add_item(self, item: CartItem):
        """Add an item to the shopping cart"""
        self.items.append(item)

    def remove_item(self, item_name: str):
        """Remove an item from the shopping cart by name"""
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self) -> float:
        """Calculate the total cost of the shopping cart"""
        total = sum(item.total_price() for item in self.items)
        return total

    def apply_coupon(self, coupon: DiscountCoupon) -> float:
        """Apply a discount coupon and return the new total amount"""
        total = self.calculate_total()
        return coupon.apply_discount(total)

    def installment_payment(self, total_amount: float, installments: int) -> float:
        """Calculate the installment amount for a given total amount and number of installments"""
        if installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")
        return total_amount / installments


# Example usage
if __name__ == "__main__":
    try:
        # Create a shopping cart
        cart = ShoppingCart()

        # Add items to the cart
        cart.add_item(CartItem("Tire A", 150.00, 2))
        cart.add_item(CartItem("Tire B", 200.00, 1))

        # Calculate total cost
        total_before_discount = cart.calculate_total()
        print(f"Total before discount: ${total_before_discount:.2f}")

        # Create a discount coupon
        coupon = DiscountCoupon("SUMMER21", 10)  # 10% discount

        # Apply discount coupon
        total_after_discount = cart.apply_coupon(coupon)
        print(f"Total after applying coupon: ${total_after_discount:.2f}")

        # Calculate installment payment
        installments = 3
        installment_amount = cart.installment_payment(total_after_discount, installments)
        print(f"Installment amount for {installments} months: ${installment_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
