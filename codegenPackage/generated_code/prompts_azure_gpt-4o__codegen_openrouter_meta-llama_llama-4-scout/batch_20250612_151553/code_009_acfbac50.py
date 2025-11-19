"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Create a Python script to simulate bulk order placement for products such as "کابل Ldnio LC631C دو سر تایپ سی" and calculate the total cost after applying discounts.
Generated: DETERMINISTIC_acfbac50e3d59423
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bulk_order_simulator.py

class Product:
    """Represents a product with a name, price, and discount rate."""

    def __init__(self, name: str, price: float, discount_rate: float = 0.0):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
            discount_rate (float, optional): The discount rate (0-100). Defaults to 0.0.
        """
        self.name = name
        self.price = price
        self.discount_rate = discount_rate

    def calculate_discounted_price(self) -> float:
        """
        Calculates the price after applying the discount.

        Returns:
            float: The discounted price.
        """
        return self.price * (1 - self.discount_rate / 100)


class Order:
    """Represents a bulk order with a list of products and quantities."""

    def __init__(self):
        """Initializes an empty Order instance."""
        self.products = {}

    def add_product(self, product: Product, quantity: int):
        """
        Adds a product to the order.

        Args:
            product (Product): The product to add.
            quantity (int): The product quantity.
        """
        self.products[product] = quantity

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the order after applying discounts.

        Returns:
            float: The total cost.
        """
        total_cost = 0.0
        for product, quantity in self.products.items():
            discounted_price = product.calculate_discounted_price()
            total_cost += discounted_price * quantity
        return total_cost


def main():
    try:
        # Create products
        product1 = Product("کابل Ldnio LC631C دو سر تایپ سی", 25.0, discount_rate=10.0)
        product2 = Product("Product B", 50.0)

        # Create an order
        order = Order()
        order.add_product(product1, 5)
        order.add_product(product2, 3)

        # Calculate and print the total cost
        total_cost = order.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
