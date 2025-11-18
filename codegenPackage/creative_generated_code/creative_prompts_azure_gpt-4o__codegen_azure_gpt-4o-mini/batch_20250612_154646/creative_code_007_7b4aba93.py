"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Generate a Python script to simulate a shopping cart system for Harman Kardon products, including adding items, calculating total costs, and applying discounts based on sale prices listed on Harman Kardon Philippines.
Generated: DETERMINISTIC_7b4aba933c17fab6
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class Product:
    """Represents a product in the shopping cart."""

    def __init__(self, name, price, sale_price=None):
        """
        Initializes a product.

        Args:
            name (str): The name of the product.
            price (float): The regular price of the product.
            sale_price (float, optional): The sale price of the product. Defaults to None.
        """
        self.name = name
        self.price = price
        self.sale_price = sale_price

    def get_price(self):
        """Returns the effective price of the product."""
        return self.sale_price if self.sale_price else self.price


class ShoppingCart:
    """Represents a shopping cart for Harman Kardon products."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add. Defaults to 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        for _ in range(quantity):
            self.items.append(product)

    def calculate_total(self):
        """Calculates the total cost of items in the cart."""
        total = sum(item.get_price() for item in self.items)
        return total

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the total cost.

        Args:
            discount_percentage (float): The discount percentage to apply.

        Returns:
            float: The total after applying the discount.
        """
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        total = self.calculate_total()
        discount_amount = (discount_percentage / 100) * total
        return total - discount_amount

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()
        
    def get_items(self):
        """Returns a list of items in the cart."""
        return [(item.name, item.get_price()) for item in self.items]


if __name__ == "__main__":
    # Example usage
    cart = ShoppingCart()

    # Creating some Harman Kardon products
    product1 = Product("Harman Kardon Onyx Studio 6", 299.99, 249.99)
    product2 = Product("Harman Kardon Go + Play", 399.99)

    # Adding products to the cart
    cart.add_item(product1, quantity=2)
    cart.add_item(product2)

    # Calculating total cost
    total_cost = cart.calculate_total()
    print(f"Total cost before discount: ${total_cost:.2f}")

    # Applying a discount
    discount_percentage = 10  # 10% discount
    discounted_total = cart.apply_discount(discount_percentage)
    print(f"Total cost after {discount_percentage}% discount: ${discounted_total:.2f}")

    # Displaying items in the cart
    print("Items in cart:")
    for item in cart.get_items():
        print(f"- {item[0]}: ${item[1]:.2f}")

    # Clearing the cart
    cart.clear_cart()
    print("Shopping cart cleared. Items in cart:", cart.get_items())
```
