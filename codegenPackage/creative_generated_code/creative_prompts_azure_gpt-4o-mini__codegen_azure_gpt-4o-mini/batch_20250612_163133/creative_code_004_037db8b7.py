"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://radical-wear.cz
Prompt: Implement a shopping cart feature that displays product details and pricing, similar to the functionality provided by Radical Wear's cart system.
Generated: DETERMINISTIC_037db8b7452bda8b
Batch ID: 20250612_163133
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
    """Class representing a product in the shopping cart."""
    
    def __init__(self, product_id, name, price, quantity=1):
        """
        Initialize a new product.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product in the cart.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        """Calculate the total price for this product."""
        return self.price * self.quantity


class ShoppingCart:
    """Class representing a shopping cart that holds products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = {}

    def add_product(self, product):
        """
        Add a product to the cart or update its quantity.

        Args:
            product (Product): The product to add to the cart.
        """
        if product.product_id in self.cart:
            self.cart[product.product_id].quantity += product.quantity
        else:
            self.cart[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the cart.

        Args:
            product_id (str): The unique identifier for the product to remove.

        Raises:
            KeyError: If the product_id is not found in the cart.
        """
        if product_id in self.cart:
            del self.cart[product_id]
        else:
            raise KeyError(f"Product ID {product_id} not found in cart.")

    def clear_cart(self):
        """Clear all products from the cart."""
        self.cart.clear()

    def total_cost(self):
        """Calculate the total cost of all products in the cart."""
        return sum(product.total_price() for product in self.cart.values())

    def display_cart(self):
        """Display the details of all products in the cart."""
        if not self.cart:
            print("Your shopping cart is empty.")
            return
        
        print("Shopping Cart:")
        for product in self.cart.values():
            print(f"- {product.name}: {product.price:.2f} x {product.quantity} = {product.total_price():.2f}")
        print(f"Total Cost: {self.total_cost():.2f}")


# Example usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_product(Product("001", "T-Shirt", 19.99, 2))
        cart.add_product(Product("002", "Jeans", 49.99, 1))
        cart.display_cart()

        cart.remove_product("001")
        print("\nAfter removing T-Shirt:")
        cart.display_cart()

        cart.clear_cart()
        print("\nAfter clearing the cart:")
        cart.display_cart()
    except Exception as e:
        print(f"An error occurred: {e}")
```
