"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Write Python code to simulate a shopping cart system for an online store that sells gardening tools, irrigation accessories, and household items, referencing categories like "Motocoasa," "Pompa Apa," and "Drujbe."
Generated: DETERMINISTIC_92a5e1cd12fdc0b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """
    A class to represent a product in the shopping cart.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        category (str): The category of the product.
    """

    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class ShoppingCart:
    """
    A class to manage the shopping cart for an online store.

    Attributes:
        products (list): A list of products in the shopping cart.

    Methods:
        add_product(product): Adds a product to the cart.
        remove_product(product_name): Removes a product from the cart by name.
        calculate_total(): Calculates the total price of all products in the cart.
        display_cart(): Displays all products in the cart.
    """

    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        """Adds a product to the shopping cart."""
        self.products.append(product)

    def remove_product(self, product_name: str) -> None:
        """Removes a product from the shopping cart by name."""
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError(f"Product '{product_name}' not found in the cart.")

    def calculate_total(self) -> float:
        """Calculates the total price of products in the cart."""
        return sum(product.price for product in self.products)

    def display_cart(self) -> None:
        """Displays all products in the shopping cart."""
        if not self.products:
            print("Shopping cart is empty.")
            return
        
        print("Shopping Cart:")
        for product in self.products:
            print(product)
        print(f"Total: ${self.calculate_total():.2f}")


def main():
    """Main function to simulate the shopping cart system."""
    cart = ShoppingCart()

    # Sample products
    product1 = Product("Motocoasa", 299.99, "Gardening Tools")
    product2 = Product("Pompa Apa", 89.99, "Irrigation Accessories")
    product3 = Product("Drujbe", 199.99, "Gardening Tools")

    # Adding products to the cart
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Display the cart
    cart.display_cart()

    # Remove a product
    try:
        cart.remove_product("Pompa Apa")
        print("\nAfter removing 'Pompa Apa':")
        cart.display_cart()
    except ValueError as e:
        print(e)

    # Attempt to remove a non-existent product
    try:
        cart.remove_product("Non-existent Product")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
