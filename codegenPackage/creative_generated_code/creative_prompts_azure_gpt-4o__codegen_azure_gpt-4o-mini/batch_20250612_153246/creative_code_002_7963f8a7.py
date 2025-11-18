"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Generate code to design a shopping cart system that supports adding products like "Gladiator Chef Safety Shoes 4020" and "Gladiator Clogs Shoes S085" with options for quantity and size selection.
Generated: DETERMINISTIC_7963f8a705c0b18a
Batch ID: 20250612_153246
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
    Represents a product in the shopping cart.
    """
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class CartItem:
    """
    Represents an item in the shopping cart.
    """
    def __init__(self, product: Product, quantity: int, size: str):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        self.product = product
        self.quantity = quantity
        self.size = size

    def total_price(self) -> float:
        """
        Calculates the total price for this cart item.
        """
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (Size: {self.size}, Quantity: {self.quantity}) - Total: ${self.total_price():.2f}"


class ShoppingCart:
    """
    Represents a shopping cart that can contain multiple products.
    """
    def __init__(self):
        self.items = []

    def add_item(self, product: Product, quantity: int, size: str):
        """
        Adds an item to the shopping cart.
        """
        try:
            cart_item = CartItem(product, quantity, size)
            self.items.append(cart_item)
        except ValueError as e:
            print(f"Error adding item to cart: {e}")

    def remove_item(self, product_name: str):
        """
        Removes an item from the shopping cart by product name.
        """
        self.items = [item for item in self.items if item.product.name != product_name]

    def total_amount(self) -> float:
        """
        Calculates the total amount for all items in the cart.
        """
        return sum(item.total_price() for item in self.items)

    def __str__(self):
        cart_contents = "\n".join(str(item) for item in self.items)
        total = self.total_amount()
        return f"Shopping Cart:\n{cart_contents}\nTotal Amount: ${total:.2f}"


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("Gladiator Chef Safety Shoes 4020", 89.99)
    product2 = Product("Gladiator Clogs Shoes S085", 49.99)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    cart.add_item(product1, 2, "10")
    cart.add_item(product2, 1, "9")

    # Print the shopping cart contents
    print(cart)

    # Remove an item from the cart
    cart.remove_item("Gladiator Clogs Shoes S085")

    # Print the shopping cart contents after removal
    print(cart)
```
