"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code that simulates adding items like "XÍCARA DE CHÁ PEARL 180ML" to a shopping cart and calculates the total price, referencing the e-commerce structure of the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7e627e8db337fda2
Batch ID: 20250612_145249
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
    """
    Represents a product in the e-commerce system.
    """
    def __init__(self, name: str, price: float):
        """
        Initialize the product with a name and price.
        :param name: The name of the product (e.g., "XÍCARA DE CHÁ PEARL 180ML").
        :param price: The price of the product in float (e.g., 29.99).
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        String representation of the product.
        :return: A string containing the product name and price.
        """
        return f"{self.name} - ${self.price:.2f}"


class ShoppingCart:
    """
    Represents a shopping cart in the e-commerce system.
    """
    def __init__(self):
        """
        Initialize the shopping cart with an empty list of items.
        """
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        """
        Add a product to the shopping cart.
        :param product: The Product object to add.
        :param quantity: The number of units to add (default is 1).
        :raises ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self) -> float:
        """
        Calculate the total price of items in the cart.
        :return: The total price of the items in the cart.
        """
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def __str__(self):
        """
        String representation of the shopping cart.
        :return: A formatted string of all items in the cart and the total price.
        """
        if not self.items:
            return "Shopping cart is empty."
        
        cart_items = "\n".join(
            f"{item['quantity']}x {item['product']}" for item in self.items
        )
        total_price = self.calculate_total()
        return f"Shopping Cart:\n{cart_items}\nTotal: ${total_price:.2f}"


# Simulate usage
if __name__ == "__main__":
    # Create some sample products
    xicara_pearl = Product(name="XÍCARA DE CHÁ PEARL 180ML", price=29.99)
    prato_ceramica = Product(name="PRATO DE CERÂMICA 20CM", price=49.99)

    # Initialize a shopping cart
    cart = ShoppingCart()

    try:
        # Add items to the cart
        cart.add_item(xicara_pearl, quantity=2)
        cart.add_item(prato_ceramica, quantity=1)

        # Print the shopping cart contents and total
        print(cart)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
