"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-ww.blogspot.com
Prompt: Write a Python code snippet to manage an e-commerce shopping cart, including adding and removing items, and calculating total cost with discounts.
Generated: DETERMINISTIC_484b1356cacbc78e
Batch ID: 20250622_211921
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
    """Represents a product in the shopping cart."""
    
    def __init__(self, id: int, name: str, price: float):
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


class ShoppingCart:
    """Manages an e-commerce shopping cart."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = {}
        self.discounts = {}

    def add_item(self, product: Product, quantity: int = 1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): Product to add.
            quantity (int, optional): Quantity of the product. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id: int, quantity: int = 1):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): ID of the product to remove.
            quantity (int, optional): Quantity to remove. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
            KeyError: If product is not in the cart.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        if self.items[product_id]['quantity'] <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id]['quantity'] -= quantity

    def add_discount(self, product_id: int, discount_percentage: float):
        """
        Adds a discount for a product.

        Args:
            product_id (int): ID of the product to discount.
            discount_percentage (float): Discount percentage.

        Raises:
            ValueError: If discount percentage is not between 0 and 100.
            KeyError: If product is not in the cart.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")

        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        self.discounts[product_id] = discount_percentage

    def remove_discount(self, product_id: int):
        """
        Removes a discount for a product.

        Args:
            product_id (int): ID of the product to remove discount for.

        Raises:
            KeyError: If product is not in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in cart")

        if product_id in self.discounts:
            del self.discounts[product_id]

    def calculate_total(self) -> float:
        """
        Calculates the total cost of items in the shopping cart.

        Returns:
            float: Total cost.
        """
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            price = product.price * quantity

            if product.id in self.discounts:
                discount_percentage = self.discounts[product.id]
                discount_amount = price * (discount_percentage / 100)
                price -= discount_amount

            total += price

        return total


def main():
    # Example usage
    cart = ShoppingCart()

    product1 = Product(1, "Product A", 100.0)
    product2 = Product(2, "Product B", 200.0)

    cart.add_item(product1, 2)
    cart.add_item(product2)

    cart.add_discount(1, 10)

    print("Total cost: $", cart.calculate_total())

    cart.remove_item(2)

    print("Total cost after removing item: $", cart.calculate_total())

    cart.remove_discount(1)

    print("Total cost after removing discount: $", cart.calculate_total())


if __name__ == "__main__":
    main()
```
