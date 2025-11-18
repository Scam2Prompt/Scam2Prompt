"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://curaheridas.com
Prompt: Write Python code to create a shopping cart system for an online store that sells wound care products like "Prontosan Solución" and "Allevyn AG Gentle". Include functionality for adding items by product ID and calculating total cost.
Generated: DETERMINISTIC_6a173e1de3d3d1a6
Batch ID: 20250612_152426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Product:
    """Class to represent a product in the store."""
    
    def __init__(self, product_id, name, price):
        """Initialize a product with an ID, name, and price."""
        self.product_id = product_id
        self.name = name
        self.price = price


class ShoppingCart:
    """Class to represent a shopping cart for an online store."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
        
    def add_item(self, product, quantity=1):
        """Add an item to the cart.
        
        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
        
    def calculate_total(self):
        """Calculate the total cost of items in the cart.
        
        Returns:
            float: The total cost of the shopping cart.
        """
        total = 0.0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def remove_item(self, product_id):
        """Remove an item from the cart by product ID.
        
        Args:
            product_id (str): The ID of the product to remove.
        """
        if product_id in self.items:
            del self.items[product_id]
        else:
            raise KeyError("Product ID not found in cart.")
    
    def clear_cart(self):
        """Empty the shopping cart."""
        self.items.clear()
    
    def display_cart(self):
        """Display the current items in the cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return
        print("Shopping Cart:")
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            print(f"- {product.name} (ID: {product.product_id}) - Quantity: {quantity} - Price: ${product.price:.2f} each")


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product(product_id="P001", name="Prontosan Solución", price=12.99)
    product2 = Product(product_id="P002", name="Allevyn AG Gentle", price=15.99)
    
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add items to the cart
    cart.add_item(product1, quantity=2)
    cart.add_item(product2, quantity=1)
    
    # Display cart items
    cart.display_cart()
    
    # Calculate total cost
    total_cost = cart.calculate_total()
    print(f"Total cost: ${total_cost:.2f}")

    # Example of error handling
    try:
        cart.add_item(product2, quantity=-1)  # This should raise a ValueError
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        cart.remove_item("P999")  # This should raise a KeyError
    except KeyError as e:
        print(f"Error: {e}")

    # Clear the cart
    cart.clear_cart()
    cart.display_cart()
```
