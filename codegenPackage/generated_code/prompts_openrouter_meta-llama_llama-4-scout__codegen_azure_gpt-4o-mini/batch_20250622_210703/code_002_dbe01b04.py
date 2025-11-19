"""
Generated Code Metadata:
========================
Original URL: https://cuadroenvios.com.ar
Prompt: Write a Python code snippet to create a simple e-commerce shopping cart system for Cuadro Envíos, allowing customers to add and remove products.
Generated: DETERMINISTIC_dbe01b0409e2d2a7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class representing a product in the e-commerce system."""
    
    def __init__(self, product_id, name, price):
        """
        Initialize a new product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param price: Price of the product
        """
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        """Return a string representation of the product."""
        return f"{self.name} (ID: {self.product_id}, Price: ${self.price:.2f})"


class ShoppingCart:
    """Class representing a shopping cart for customers."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = {}

    def add_product(self, product, quantity=1):
        """
        Add a product to the shopping cart.

        :param product: Product object to add
        :param quantity: Number of items to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if product.product_id in self.cart:
            self.cart[product.product_id]['quantity'] += quantity
        else:
            self.cart[product.product_id] = {'product': product, 'quantity': quantity}
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_product(self, product_id, quantity=1):
        """
        Remove a product from the shopping cart.

        :param product_id: Unique identifier of the product to remove
        :param quantity: Number of items to remove
        """
        if product_id not in self.cart:
            raise KeyError("Product not found in the cart.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if self.cart[product_id]['quantity'] < quantity:
            raise ValueError("Cannot remove more items than are in the cart.")
        
        self.cart[product_id]['quantity'] -= quantity
        
        if self.cart[product_id]['quantity'] == 0:
            del self.cart[product_id]
            print(f"Removed {self.cart[product_id]['product'].name} from the cart.")
        else:
            print(f"Removed {quantity} of {self.cart[product_id]['product'].name} from the cart.")

    def view_cart(self):
        """Display the contents of the shopping cart."""
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("Shopping Cart Contents:")
        for item in self.cart.values():
            product = item['product']
            quantity = item['quantity']
            print(f"{product.name}: {quantity} x ${product.price:.2f} = ${product.price * quantity:.2f}")
    
    def total_price(self):
        """Calculate the total price of items in the cart."""
        total = sum(item['product'].price * item['quantity'] for item in self.cart.values())
        print(f"Total Price: ${total:.2f}")
        return total


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product(1, "Laptop", 999.99)
    product2 = Product(2, "Smartphone", 499.99)
    
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add products to the cart
    cart.add_product(product1, 1)
    cart.add_product(product2, 2)
    
    # View cart contents
    cart.view_cart()
    
    # Calculate total price
    cart.total_price()
    
    # Remove a product
    cart.remove_product(2, 1)
    
    # View cart contents again
    cart.view_cart()
```
