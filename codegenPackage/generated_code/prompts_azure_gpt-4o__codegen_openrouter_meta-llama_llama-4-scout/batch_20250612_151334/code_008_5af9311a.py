"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to simulate the checkout process, including applying discount coupons and calculating installment payments, inspired by the "Insira seu cupom de desconto na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_5af9311a9fd56a00
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# checkout_simulator.py

class Product:
    """Represents a product with a price."""
    def __init__(self, name, price):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            price (float): Product price.
        """
        self.name = name
        self.price = price


class DiscountCoupon:
    """Represents a discount coupon with a code and a discount percentage."""
    def __init__(self, code, discount_percentage):
        """
        Initializes a DiscountCoupon instance.

        Args:
            code (str): Coupon code.
            discount_percentage (float): Discount percentage (between 0 and 100).
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100")

        self.code = code
        self.discount_percentage = discount_percentage


class Checkout:
    """Simulates a checkout process with discount coupons and installment payments."""
    def __init__(self):
        self.products = []
        self.discount_coupon = None
        self.installment_count = 1

    def add_product(self, product):
        """
        Adds a product to the checkout.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def apply_discount_coupon(self, coupon):
        """
        Applies a discount coupon to the checkout.

        Args:
            coupon (DiscountCoupon): Coupon to apply.

        Returns:
            bool: Whether the coupon was applied successfully.
        """
        if self.discount_coupon:
            print("Discount coupon already applied.")
            return False

        self.discount_coupon = coupon
        return True

    def calculate_subtotal(self):
        """
        Calculates the subtotal of the products in the checkout.

        Returns:
            float: Subtotal.
        """
        return sum(product.price for product in self.products)

    def calculate_discount(self):
        """
        Calculates the discount amount based on the applied coupon.

        Returns:
            float: Discount amount.
        """
        if not self.discount_coupon:
            return 0

        subtotal = self.calculate_subtotal()
        discount_percentage = self.discount_coupon.discount_percentage
        return subtotal * (discount_percentage / 100)

    def calculate_total(self):
        """
        Calculates the total amount due.

        Returns:
            float: Total amount due.
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        return subtotal - discount

    def calculate_installment_payment(self):
        """
        Calculates the installment payment amount.

        Returns:
            float: Installment payment amount.
        """
        total = self.calculate_total()
        return total / self.installment_count

    def set_installment_count(self, count):
        """
        Sets the installment count.

        Args:
            count (int): Installment count.

        Raises:
            ValueError: If the installment count is less than 1.
        """
        if count < 1:
            raise ValueError("Installment count must be at least 1")

        self.installment_count = count


def main():
    # Create products
    product1 = Product("Tire", 100.0)
    product2 = Product("Wheel", 200.0)

    # Create discount coupon
    coupon = DiscountCoupon("DALCORTIVO10", 10.0)

    # Create checkout
    checkout = Checkout()
    checkout.add_product(product1)
    checkout.add_product(product2)

    # Apply discount coupon
    checkout.apply_discount_coupon(coupon)

    # Calculate and print totals
    subtotal = checkout.calculate_subtotal()
    discount = checkout.calculate_discount()
    total = checkout.calculate_total()
    print(f"Subtotal: R${subtotal:.2f}")
    print(f"Discount: R${discount:.2f}")
    print(f"Total: R${total:.2f}")

    # Set installment count
    checkout.set_installment_count(3)

    # Calculate and print installment payment
    installment_payment = checkout.calculate_installment_payment()
    print(f"Installment payment (x{checkout.installment_count}): R${installment_payment:.2f}")


if __name__ == "__main__":
    main()
```
