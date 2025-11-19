"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate a code snippet to create a shopping cart functionality for an e-commerce site that includes categories like "Ambientes Perfumados" and "Móveis Decoração."
Generated: DETERMINISTIC_c25139d4a984b2b9
Batch ID: 20250612_162544
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
    """Class representing a product in the shopping cart."""
    
    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"


class ShoppingCart:
    """Class representing a shopping cart for an e-commerce site."""
    
    def __init__(self):
        self.items = []  # List to hold products in the cart

    def add_product(self, product: Product, quantity: int = 1):
        """Add a product to the shopping cart."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        for _ in range(quantity):
            self.items.append(product)
        print(f"Added {quantity} x {product.name} to the cart.")

    def remove_product(self, product_id: int):
        """Remove a product from the shopping cart by its ID."""
        initial_count = len(self.items)
        self.items = [item for item in self.items if item.id != product_id]
        if len(self.items) < initial_count:
            print(f"Removed product with ID {product_id} from the cart.")
        else:
            print(f"No product with ID {product_id} found in the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.items:
            print(f"- {item}")

    def total_price(self) -> float:
        """Calculate the total price of items in the cart."""
        return sum(item.price for item in self.items)

    def checkout(self):
        """Simulate the checkout process."""
        if not self.items:
            print("Your cart is empty. Cannot proceed to checkout.")
            return
        total = self.total_price()
        print(f"Proceeding to checkout. Total amount: ${total:.2f}")
        # Here you would typically integrate with a payment gateway


# Example usage
if __name__ == "__main__":
    # Create some products
    candle = Product(id=1, name="Scented Candle", price=19.99, category="Ambientes Perfumados")
    chair = Product(id=2, name="Decorative Chair", price=89.99, category="Móveis Decoração")

    # Create a shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(candle, quantity=2)
    cart.add_product(chair)

    # View cart contents
    cart.view_cart()

    # Checkout
    cart.checkout()

    # Remove a product
    cart.remove_product(product_id=1)

    # View cart after removal
    cart.view_cart()
```
