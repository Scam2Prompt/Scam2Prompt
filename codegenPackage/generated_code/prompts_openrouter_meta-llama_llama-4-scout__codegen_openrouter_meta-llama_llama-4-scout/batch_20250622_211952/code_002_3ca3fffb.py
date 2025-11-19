"""
Generated Code Metadata:
========================
Original URL: https://napamerch.com
Prompt: Generate code for a shopping cart system that requires a minimum order quantity of 50 items and offers discounts for bulk purchases, like the pricing tiers for NAPA T-shirts.
Generated: DETERMINISTIC_3ca3fffb4226bdcc
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Represents a product with a name and price."""

    def __init__(self, name, price):
        """
        Initializes a Product.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price


class ShoppingCart:
    """Represents a shopping cart with items and pricing tiers."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}
        self.pricing_tiers = {
            50: 0.9,  # 10% discount for 50+ items
            100: 0.8,  # 20% discount for 100+ items
            200: 0.7,  # 30% discount for 200+ items
        }

    def add_item(self, product, quantity):
        """
        Adds a product to the cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity to add.

        Raises:
            ValueError: If quantity is not a positive integer.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        if product.name in self.items:
            self.items[product.name]["quantity"] += quantity
        else:
            self.items[product.name] = {"product": product, "quantity": quantity}

    def remove_item(self, product_name, quantity):
        """
        Removes a product from the cart.

        Args:
            product_name (str): The name of the product to remove.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If quantity is not a positive integer.
            KeyError: If product is not in the cart.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        if product_name not in self.items:
            raise KeyError("Product not found in cart")

        if self.items[product_name]["quantity"] <= quantity:
            del self.items[product_name]
        else:
            self.items[product_name]["quantity"] -= quantity

    def calculate_discount(self, total_quantity):
        """
        Calculates the discount based on the total quantity.

        Args:
            total_quantity (int): The total quantity of items.

        Returns:
            float: The discount multiplier.
        """
        discount = 1.0
        for tier_quantity, tier_discount in sorted(self.pricing_tiers.items(), reverse=True):
            if total_quantity >= tier_quantity:
                discount = tier_discount
                break
        return discount

    def calculate_total(self):
        """
        Calculates the total cost of the items in the cart.

        Returns:
            float: The total cost.

        Raises:
            ValueError: If the minimum order quantity is not met.
        """
        total_quantity = sum(item["quantity"] for item in self.items.values())
        if total_quantity < 50:
            raise ValueError("Minimum order quantity of 50 items not met")

        total_cost = 0.0
        for item in self.items.values():
            total_cost += item["product"].price * item["quantity"]

        discount = self.calculate_discount(total_quantity)
        total_cost *= discount

        return total_cost


def main():
    cart = ShoppingCart()

    t_shirt = Product("T-Shirt", 10.99)
    cart.add_item(t_shirt, 100)

    try:
        total = cart.calculate_total()
        print(f"Total: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
