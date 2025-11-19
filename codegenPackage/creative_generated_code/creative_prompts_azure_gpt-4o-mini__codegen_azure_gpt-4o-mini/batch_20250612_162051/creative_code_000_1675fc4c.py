"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wouo.com.br
Prompt: Generate code to create an e-commerce shopping cart for a website selling inhalers and nebulizers, similar to the features on Wouo.com.br.
Generated: DETERMINISTIC_1675fc4cdba274ce
Batch ID: 20250612_162051
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
    """Class to represent a product in the shopping cart."""
    
    def __init__(self, product_id, name, price, stock):
        """
        Initializes a new Product instance.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            stock (int): Quantity available in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f} - Stock: {self.stock}"


class ShoppingCart:
    """Class to represent a shopping cart for an e-commerce application."""

    def __init__(self):
        """Initializes a new empty shopping cart."""
        self.items = {}

    def add_product(self, product, quantity):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int): Quantity of the product to add.

        Raises:
            ValueError: If quantity is less than 1 or exceeds available stock.
        """
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        if quantity > product.stock:
            raise ValueError("Quantity exceeds stock available.")

        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        
        # Decrease stock in product
        product.stock -= quantity

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart.

        Args:
            product_id (int): Unique identifier of the product to remove.
        
        Raises:
            KeyError: If the product is not found in the cart.
        """
        if product_id not in self.items:
            raise KeyError("Product not found in the cart.")

        # Increase stock in product before removing
        product = self.items[product_id]['product']
        product.stock += self.items[product_id]['quantity']
        
        del self.items[product_id]

    def view_cart(self):
        """Returns a list of items in the shopping cart."""
        return {product['product'].name: product['quantity'] for product in self.items.values()}

    def total_price(self):
        """Calculates the total price of items in the cart."""
        total = sum(item['product'].price * item['quantity'] for item in self.items.values())
        return total

    def clear_cart(self):
        """Clears all items from the shopping cart."""
        self.items.clear()


# Example usage of the ShoppingCart class
if __name__ == "__main__":
    # Create sample products
    inhaler = Product(1, "Inhaler", 29.99, 10)
    nebulizer = Product(2, "Nebulizer", 199.99, 5)

    # Initialize shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    try:
        cart.add_product(inhaler, 2)
        cart.add_product(nebulizer, 1)
        print("Cart items:", cart.view_cart())
        print("Total price: $", cart.total_price())
        
        # Remove product from the cart
        cart.remove_product(1)
        print("Cart items after removal:", cart.view_cart())
        
        # Clear the cart
        cart.clear_cart()
        print("Cart items after clearing:", cart.view_cart())
        
    except (ValueError, KeyError) as e:
        print("Error:", e)
```
