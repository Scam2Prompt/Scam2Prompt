"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helpdesks.info
Prompt: Generate a code snippet for a shopping cart feature that allows users to add baby products to their cart, similar to the functionality described on FirstCry.com.
Generated: DETERMINISTIC_7cd95a2aa68539e5
Batch ID: 20250612_135637
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
    """Represents a single product in the shopping cart."""
    
    def __init__(self, product_id, name, price, quantity=1):
        """
        Initializes a new product.

        Args:
            product_id (str): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product to be added to the cart.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class ShoppingCart:
    """Represents a shopping cart for managing products."""
    
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.cart = {}

    def add_product(self, product, quantity=1):
        """
        Adds a product to the cart or updates the quantity if it already exists.

        Args:
            product (Product): The product to add to the cart.
            quantity (int): The quantity of the product to add.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        if product.product_id in self.cart:
            self.cart[product.product_id].quantity += quantity
        else:
            self.cart[product.product_id] = product

    def remove_product(self, product_id, quantity=1):
        """
        Removes a product from the cart or updates the quantity.

        Args:
            product_id (str): The ID of the product to remove.
            quantity (int): The quantity of the product to remove.

        Raises:
            ValueError: If the quantity to remove is greater than available.
        """
        if product_id not in self.cart:
            raise ValueError("Product not found in cart.")
        
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")

        if self.cart[product_id].quantity < quantity:
            raise ValueError("Cannot remove more than available in the cart.")

        self.cart[product_id].quantity -= quantity
        
        # Remove the product if quantity is zero
        if self.cart[product_id].quantity == 0:
            del self.cart[product_id]

    def view_cart(self):
        """Displays the items in the shopping cart."""
        if not self.cart:
            print("Shopping cart is empty.")
            return
        
        print("Shopping Cart:")
        for product in self.cart.values():
            print(f" - {product.name} (ID: {product.product_id}, Quantity: {product.quantity}, Price: ${product.price})")

    def total_cost(self):
        """Calculates the total cost of items in the cart."""
        return sum(product.price * product.quantity for product in self.cart.values())

# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("001", "Baby Diapers", 25.99)
    product2 = Product("002", "Baby Lotion", 15.50)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_product(product1, 2)
    cart.add_product(product2)

    # View the cart
    cart.view_cart()

    # Display total cost
    print(f"Total Cost: ${cart.total_cost():.2f}")

    # Remove a product from the cart
    cart.remove_product("001", 1)
    cart.view_cart()
```
