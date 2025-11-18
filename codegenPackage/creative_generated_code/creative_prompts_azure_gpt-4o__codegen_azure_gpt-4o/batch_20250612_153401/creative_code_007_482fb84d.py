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
# A simple shopping cart system for cycling gear

class Product:
    """
    A class to represent a product in the shop.
    """
    def __init__(self, product_id, name, price, stock):
        """
        Initialize the product with ID, name, price, and stock.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        :param stock: Quantity available in stock
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """
        String representation of the product.
        """
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    """
    A class to represent a shopping cart.
    """
    def __init__(self):
        """
        Initialize the shopping cart with an empty dictionary for items.
        """
        self.items = {}  # Format: {product_instance: quantity}

    def add_to_cart(self, product, quantity):
        """
        Add a product to the shopping cart.

        :param product: Product instance to add
        :param quantity: Quantity to add
        :raises ValueError: If requested quantity exceeds stock
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if product.stock < quantity:
            raise ValueError(f"Not enough stock available for {product.name}. Requested: {quantity}, Available: {product.stock}")
        
        # Add to cart
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
        
        # Reduce stock
        product.stock -= quantity

    def remove_from_cart(self, product, quantity):
        """
        Remove a product from the shopping cart.

        :param product: Product instance to remove
        :param quantity: Quantity to remove
        :raises ValueError: If the product is not in the cart or requested quantity exceeds cart quantity
        """
        if product not in self.items:
            raise ValueError(f"{product.name} is not in the cart.")
        if quantity <= 0 or self.items[product] < quantity:
            raise ValueError(f"Invalid quantity to remove. Quantity in cart: {self.items[product]}, Requested to remove: {quantity}")
        
        # Remove from cart
        self.items[product] -= quantity
        if self.items[product] == 0:
            del self.items[product]
        
        # Increase stock
        product.stock += quantity

    def view_cart(self):
        """
        View the contents of the shopping cart.

        :return: String representation of the shopping cart
        """
        if not self.items:
            return "Your cart is empty."
        cart_content = ["Shopping Cart:"]
        total_price = 0.0
        for product, quantity in self.items.items():
            cart_content.append(f"{product.name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}")
            total_price += product.price * quantity
        cart_content.append(f"Total Price: ${total_price:.2f}")
        return "\n".join(cart_content)

    def checkout(self):
        """
        Checkout the shopping cart. Clears all items from the cart.

        :return: Total price of the items purchased
        """
        total_price = sum(product.price * quantity for product, quantity in self.items.items())
        self.items.clear()
        return total_price


# Example Usage
if __name__ == "__main__":
    # Define products
    ignite_bike = Product(product_id=1, name="Ignite Bike", price=1500.00, stock=5)
    hunt_wheels = Product(product_id=2, name="Hunt Wheels", price=750.00, stock=10)
    ccn_kit = Product(product_id=3, name="CCN Kit", price=120.00, stock=20)
    nimbl_shoes = Product(product_id=4, name="Nimbl Shoes", price=320.00, stock=15)
    giro_helmets = Product(product_id=5, name="Giro Helmet", price=200.00, stock=8)

    # Create shopping cart
    cart = ShoppingCart()

    try:
        # Add products to the cart
        cart.add_to_cart(ignite_bike, 1)
        cart.add_to_cart(hunt_wheels, 2)
        cart.add_to_cart(ccn_kit, 1)
        print(cart.view_cart())

        # Remove a product from the cart
        cart.remove_from_cart(hunt_wheels, 1)
        print(cart.view_cart())

        # Checkout
        total = cart.checkout()
        print(f"Checkout successful! Total price: ${total:.2f}")
        print(cart.view_cart())
    except ValueError as e:
        print(f"Error: {e}")
```
