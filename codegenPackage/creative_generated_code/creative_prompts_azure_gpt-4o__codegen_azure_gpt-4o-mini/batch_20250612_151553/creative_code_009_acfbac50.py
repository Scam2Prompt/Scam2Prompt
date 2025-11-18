"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Create a Python script to simulate bulk order placement for products such as "کابل Ldnio LC631C دو سر تایپ سی" and calculate the total cost after applying discounts.
Generated: DETERMINISTIC_acfbac50e3d59423
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# bulk_order_simulator.py

class Product:
    """
    Class to represent a product with a name, price, and discount.
    """
    def __init__(self, name: str, price: float, discount: float = 0.0):
        self.name = name
        self.price = price
        self.discount = discount

    def get_final_price(self) -> float:
        """
        Calculate the final price after applying the discount.
        :return: Final price after discount
        """
        if self.discount < 0 or self.discount > 100:
            raise ValueError("Discount must be between 0 and 100")
        return self.price * (1 - self.discount / 100)


class Order:
    """
    Class to represent an order consisting of multiple products.
    """
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        """
        Add a product to the order.
        :param product: Instance of Product to add
        """
        self.products.append(product)

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of the order after discounts.
        :return: Total cost
        """
        total_cost = sum(product.get_final_price() for product in self.products)
        return total_cost


def main():
    """
    Simulates bulk order placement and calculates the total cost.
    """
    # Create a list of products with their names, prices, and discounts
    product_list = [
        Product("کابل Ldnio LC631C دو سر تایپ سی", 15.0, 10.0),
        Product("کابل Micro USB", 10.0, 5.0),
        Product("کابل HDMI", 25.0, 15.0),
    ]

    # Create an order instance
    order = Order()

    # Add products to the order
    for product in product_list:
        order.add_product(product)

    # Calculate total cost
    try:
        total_cost = order.calculate_total_cost()
        print(f"Total cost after discounts: {total_cost:.2f} units")
    except ValueError as e:
        print(f"Error calculating total cost: {e}")


if __name__ == "__main__":
    main()
```
