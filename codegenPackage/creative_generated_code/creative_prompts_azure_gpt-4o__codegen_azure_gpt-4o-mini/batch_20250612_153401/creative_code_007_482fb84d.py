"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://race-ridefire.cc
Prompt: Write code to create a shopping cart system for cycling gear, optimized for products like the Ignite bike, Hunt wheels, CCN kit, Nimbl shoes, and Giro helmets, as featured on the Race Ride Fire shop page.
Generated: DETERMINISTIC_482fb84d1f9f9702
Batch ID: 20250612_153401
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
    Represents a product in the shopping cart.
    
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in the cart.
    """
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        """Calculates the total price for the product based on quantity."""
        return self.price * self.quantity

    def __str__(self) -> str:
        return f"{self.name} (x{self.quantity}): ${self.total_price():.2f}"


class ShoppingCart:
    """
    Represents a shopping cart for a cycling gear shop.
    
    Attributes:
        items (list): A list of Product instances in the cart.
    """
    def __init__(self):
        self.items = []

    def add_product(self, product: Product) -> None:
        """Adds a product to the cart, updating quantity if it already exists."""
        for item in self.items:
            if item.name == product.name:
                item.quantity += product.quantity
                return
        self.items.append(product)

    def remove_product(self, product_name: str) -> None:
        """Removes a product from the cart by name."""
        self.items = [item for item in self.items if item.name != product_name]

    def calculate_total(self) -> float:
        """Calculates the total price of all products in the cart."""
        return sum(item.total_price() for item in self.items)

    def display_cart(self) -> None:
        """Displays all products currently in the cart."""
        if not self.items:
            print("Shopping cart is empty.")
            return
            
        print("Shopping Cart Items:")
        for item in self.items:
            print(item)
        print(f"Total: ${self.calculate_total():.2f}")


# Example usage of the ShoppingCart system
if __name__ == "__main__":
    try:
        # Create a ShoppingCart instance
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(Product("Ignite Bike", 1200.00, 1))
        cart.add_product(Product("Hunt Wheels", 750.00, 1))
        cart.add_product(Product("CCN Kit", 150.00, 2))
        cart.add_product(Product("Nimbl Shoes", 100.00, 1))
        cart.add_product(Product("Giro Helmet", 75.00, 1))

        # Display the cart contents and total
        cart.display_cart()

        # Example of removing a product
        cart.remove_product("CCN Kit")
        print("\nAfter removing CCN Kit:")
        cart.display_cart()

    except Exception as e:
        print(f"An error occurred: {e}")
```
