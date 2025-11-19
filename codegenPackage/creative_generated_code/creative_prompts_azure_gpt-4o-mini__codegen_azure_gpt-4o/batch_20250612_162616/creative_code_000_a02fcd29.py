"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zellerscanada.ca
Prompt: Generate a code snippet to create a shopping cart feature for an e-commerce site similar to Zellers Canada, incorporating product categories like furniture and jewelry.
Generated: DETERMINISTIC_a02fcd29202d8e0d
Batch ID: 20250612_162616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

from typing import List, Dict


class Product:
    """
    Represents a product in the e-commerce store.
    """

    def __init__(self, id: int, name: str, category: str, price: float):
        """
        Initializes a Product object.

        :param id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product (e.g., "Furniture", "Jewelry")
        :param price: Price of the product
        """
        self.id = id
        self.name = name
        self.category = category
        self.price = price


class ShoppingCart:
    """
    Represents a shopping cart containing multiple products.
    """

    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.items: List[Dict[str, any]] = []

    def add_product(self, product: Product, quantity: int = 1):
        """
        Adds a product to the shopping cart.

        :param product: Product object to be added
        :param quantity: Number of items to add (default is 1)
        :raises ValueError: If quantity is less than or equal to zero
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product_id: int):
        """
        Removes a product from the shopping cart by its ID.

        :param product_id: ID of the product to be removed
        :raises ValueError: If the product is not found in the cart
        """
        for item in self.items:
            if item["product"].id == product_id:
                self.items.remove(item)
                return
        raise ValueError("Product not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total cost of all items in the cart.

        :return: Total price of items in the cart
        """
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def list_items(self) -> None:
        """
        Lists all items in the shopping cart.

        :return: None
        """
        if not self.items:
            print("The shopping cart is empty.")
            return

        print("Items in your shopping cart:")
        for item in self.items:
            product = item["product"]
            print(
                f"Product ID: {product.id}, Name: {product.name}, "
                f"Category: {product.category}, Price: ${product.price:.2f}, "
                f"Quantity: {item['quantity']}"
            )


# Example usage
if __name__ == "__main__":
    # Create products
    furniture1 = Product(1, "Sofa", "Furniture", 499.99)
    jewelry1 = Product(2, "Gold Necklace", "Jewelry", 249.99)
    furniture2 = Product(3, "Dining Table", "Furniture", 799.99)

    # Create shopping cart
    cart = ShoppingCart()

    try:
        # Add products to cart
        cart.add_product(furniture1, 2)
        cart.add_product(jewelry1)
        cart.add_product(furniture2, 1)

        # List items in the cart
        cart.list_items()

        # Calculate total
        total = cart.calculate_total()
        print(f"Total price: ${total:.2f}")

        # Remove a product
        cart.remove_product(2)
        print("\nAfter removing Gold Necklace:")

        # List updated items in the cart
        cart.list_items()

        # Calculate updated total
        total = cart.calculate_total()
        print(f"Updated total price: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
