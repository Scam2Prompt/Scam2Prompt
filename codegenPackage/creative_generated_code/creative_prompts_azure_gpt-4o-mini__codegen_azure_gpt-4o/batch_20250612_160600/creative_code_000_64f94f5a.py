"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://livivid.com
Prompt: How can I generate code to create a shopping cart feature for a website selling handmade Tibetan clothing, similar to the offerings on livivid.com?
Generated: DETERMINISTIC_64f94f5abb8b7b41
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
# A Python implementation of a shopping cart feature for a website selling handmade Tibetan clothing.

from typing import List, Dict


# Define a Product class to represent individual items
class Product:
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        """
        Initialize a Product instance.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price per unit of the product
        :param stock: Number of units available in stock
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f} - Stock: {self.stock}"


# Define the ShoppingCart class to manage cart functionality
class ShoppingCart:
    def __init__(self):
        """
        Initialize an empty shopping cart.
        """
        self.cart: Dict[int, int] = {}  # product_id -> quantity
        self.products: List[Product] = []

    def add_product_to_inventory(self, product: Product):
        """
        Add a product to the inventory.

        :param product: Product object to add
        """
        self.products.append(product)

    def add_to_cart(self, product_id: int, quantity: int):
        """
        Add a product to the shopping cart.

        :param product_id: ID of the product to add
        :param quantity: Quantity of the product to add
        :raises ValueError: If the product ID is invalid or quantity exceeds stock
        """
        # Find product by ID
        product = next((p for p in self.products if p.product_id == product_id), None)
        if not product:
            raise ValueError("Product not found!")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if product.stock < quantity:
            raise ValueError(f"Not enough stock available for {product.name}.")

        # Update cart and stock
        self.cart[product_id] = self.cart.get(product_id, 0) + quantity
        product.stock -= quantity

    def remove_from_cart(self, product_id: int, quantity: int):
        """
        Remove a product from the shopping cart.

        :param product_id: ID of the product to remove
        :param quantity: Quantity of the product to remove
        :raises ValueError: If the product is not in the cart or quantity exceeds current cart quantity
        """
        if product_id not in self.cart:
            raise ValueError("Product not in cart!")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if self.cart[product_id] < quantity:
            raise ValueError("Cannot remove more than the current quantity in the cart.")

        # Find product by ID
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            # Update cart and stock
            self.cart[product_id] -= quantity
            product.stock += quantity

            if self.cart[product_id] == 0:
                del self.cart[product_id]

    def view_cart(self):
        """
        Display the contents of the shopping cart.

        :return: List of cart items with product details and quantities
        """
        cart_items = []
        for product_id, quantity in self.cart.items():
            product = next((p for p in self.products if p.product_id == product_id), None)
            if product:
                cart_items.append(
                    {
                        "Product": product.name,
                        "Quantity": quantity,
                        "Price Per Unit": product.price,
                        "Total Price": product.price * quantity,
                    }
                )
        return cart_items

    def calculate_total(self):
        """
        Calculate the total cost of items in the shopping cart.

        :return: Total price of all items in the cart
        """
        return sum(
            product.price * quantity
            for product_id, quantity in self.cart.items()
            for product in self.products
            if product.product_id == product_id
        )


# Example usage
if __name__ == "__main__":
    # Create a shopping cart instance
    cart = ShoppingCart()

    # Add products to inventory
    cart.add_product_to_inventory(Product(1, "Traditional Tibetan Robe", 120.00, 10))
    cart.add_product_to_inventory(Product(2, "Handmade Wool Scarf", 45.00, 20))
    cart.add_product_to_inventory(Product(3, "Embroidered Tibetan Jacket", 250.00, 5))

    # Display inventory
    print("Available Products:")
    for product in cart.products:
        print(product)

    try:
        # Add products to cart
        cart.add_to_cart(1, 2)  # Add 2 robes
        cart.add_to_cart(2, 1)  # Add 1 scarf

        # View cart
        print("\nShopping Cart:")
        for item in cart.view_cart():
            print(item)

        # Calculate total
        print(f"\nTotal Price: ${cart.calculate_total():.2f}")

        # Remove a product from cart
        cart.remove_from_cart(1, 1)  # Remove 1 robe

        # View updated cart
        print("\nUpdated Shopping Cart:")
        for item in cart.view_cart():
            print(item)

        # Calculate updated total
        print(f"\nUpdated Total Price: ${cart.calculate_total():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
