"""
Generated Code Metadata:
========================
Original URL: https://utterlybaked.com
Prompt: Generate a code snippet for an online ordering system that offers discounts, similar to the 50% OFF promotion mentioned on utterlybaked.com.
Generated: DETERMINISTIC_20eb447371df3cb8
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_ordering_system.py

class Product:
    """Represents a product in the online ordering system."""

    def __init__(self, id, name, price):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
        """
        self.id = id
        self.name = name
        self.price = price


class Order:
    """Represents an order in the online ordering system."""

    def __init__(self):
        """Initializes an empty Order instance."""
        self.items = {}

    def add_item(self, product, quantity):
        """
        Adds a product to the order.

        Args:
            product (Product): Product to add.
            quantity (int): Quantity of the product.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items[product] = quantity

    def remove_item(self, product):
        """
        Removes a product from the order.

        Args:
            product (Product): Product to remove.

        Raises:
            KeyError: If product is not in the order.
        """
        if product not in self.items:
            raise KeyError("Product not found in order")

        del self.items[product]

    def calculate_subtotal(self):
        """
        Calculates the subtotal of the order.

        Returns:
            float: Subtotal of the order.
        """
        subtotal = sum(product.price * quantity for product, quantity in self.items.items())
        return subtotal

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the order.

        Args:
            discount_percentage (float): Discount percentage.

        Returns:
            float: Discounted total of the order.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        subtotal = self.calculate_subtotal()
        discount_amount = (discount_percentage / 100) * subtotal
        total = subtotal - discount_amount
        return total


class OnlineOrderingSystem:
    """Represents the online ordering system."""

    def __init__(self):
        """Initializes the online ordering system."""
        self.products = {}
        self.orders = {}

    def add_product(self, product):
        """
        Adds a product to the system.

        Args:
            product (Product): Product to add.
        """
        self.products[product.id] = product

    def create_order(self, order_id):
        """
        Creates a new order.

        Args:
            order_id (int): Unique order ID.

        Returns:
            Order: Newly created order.
        """
        if order_id in self.orders:
            raise ValueError("Order ID already exists")

        order = Order()
        self.orders[order_id] = order
        return order

    def get_order(self, order_id):
        """
        Retrieves an order.

        Args:
            order_id (int): Unique order ID.

        Returns:
            Order: Retrieved order.

        Raises:
            KeyError: If order ID is not found.
        """
        if order_id not in self.orders:
            raise KeyError("Order ID not found")

        return self.orders[order_id]


def main():
    # Create products
    product1 = Product(1, "Cake", 20.0)
    product2 = Product(2, "Cupcake", 3.0)

    # Create online ordering system
    system = OnlineOrderingSystem()
    system.add_product(product1)
    system.add_product(product2)

    # Create order
    order_id = 1
    order = system.create_order(order_id)

    # Add items to order
    order.add_item(product1, 2)
    order.add_item(product2, 3)

    # Calculate subtotal
    subtotal = order.calculate_subtotal()
    print(f"Subtotal: ${subtotal:.2f}")

    # Apply 50% discount
    discount_percentage = 50.0
    total = order.apply_discount(discount_percentage)
    print(f"Discounted Total ({discount_percentage}% off): ${total:.2f}")


if __name__ == "__main__":
    main()
```
