"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script to implement a discount system for an online store, including coupon code functionality, similar to the checkout system described on Cody Alt's website.
Generated: DETERMINISTIC_d22853f4162e53e8
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# discount_system.py

class Product:
    """Represents a product in the online store."""
    
    def __init__(self, product_id, name, price):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.price = price


class Coupon:
    """Represents a coupon code with its details."""
    
    def __init__(self, code, discount_type, discount_value, expiration_date):
        """
        Initializes a Coupon instance.

        Args:
            code (str): Unique coupon code.
            discount_type (str): Type of discount (percentage or fixed).
            discount_value (float): Discount value.
            expiration_date (str): Expiration date in YYYY-MM-DD format.
        """
        self.code = code
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.expiration_date = expiration_date


class Order:
    """Represents a customer's order with products and coupon applied."""
    
    def __init__(self):
        """Initializes an empty Order instance."""
        self.products = []
        self.coupon = None

    def add_product(self, product):
        """
        Adds a product to the order.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def apply_coupon(self, coupon):
        """
        Applies a coupon to the order.

        Args:
            coupon (Coupon): Coupon to apply.

        Raises:
            ValueError: If coupon has expired or is invalid.
        """
        from datetime import datetime

        expiration_date = datetime.strptime(coupon.expiration_date, "%Y-%m-%d")
        if expiration_date < datetime.now():
            raise ValueError("Coupon has expired")

        self.coupon = coupon

    def calculate_total(self):
        """
        Calculates the total cost of the order with coupon discount.

        Returns:
            float: Total cost.
        """
        subtotal = sum(product.price for product in self.products)

        if self.coupon:
            if self.coupon.discount_type == "percentage":
                discount = subtotal * (self.coupon.discount_value / 100)
            elif self.coupon.discount_type == "fixed":
                discount = self.coupon.discount_value
            else:
                raise ValueError("Invalid coupon discount type")

            subtotal -= discount

        return subtotal


def main():
    # Create products
    product1 = Product(1, "Product A", 19.99)
    product2 = Product(2, "Product B", 9.99)

    # Create coupon
    coupon = Coupon("DISCOUNT10", "percentage", 10, "2024-12-31")

    # Create order
    order = Order()
    order.add_product(product1)
    order.add_product(product2)

    try:
        order.apply_coupon(coupon)
    except ValueError as e:
        print(f"Error: {e}")

    total = order.calculate_total()
    print(f"Order Total: ${total:.2f}")


if __name__ == "__main__":
    main()
```
