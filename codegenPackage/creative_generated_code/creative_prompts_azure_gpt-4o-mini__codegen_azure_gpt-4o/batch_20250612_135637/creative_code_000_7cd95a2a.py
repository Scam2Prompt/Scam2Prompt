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
"""
Shopping Cart Module for Baby Products
This script provides functionality for adding baby products to a shopping cart.
It is designed to be clean, efficient, and production-ready.
"""

class ShoppingCart:
    def __init__(self):
        """
        Initializes the shopping cart with an empty list of items and a total price.
        """
        self.items = []  # List to store cart items
        self.total_price = 0.0  # Total price of items in the cart

    def add_item(self, product_name, product_price, quantity=1):
        """
        Adds a baby product to the shopping cart.
        
        Args:
            product_name (str): Name of the product.
            product_price (float): Price of the product (per unit).
            quantity (int): Quantity of the product to add. Defaults to 1.
            
        Raises:
            ValueError: If product_price is negative or quantity is less than 1.
        """
        if product_price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        
        # Add product details to items list
        self.items.append({
            "product_name": product_name,
            "product_price": product_price,
            "quantity": quantity,
            "total_item_price": product_price * quantity
        })
        
        # Update the total price of the cart
        self.total_price += product_price * quantity

    def display_cart(self):
        """
        Displays the contents of the shopping cart in a user-friendly format.
        """
        if not self.items:
            print("Your shopping cart is empty.")
            return
        
        print("\nShopping Cart:")
        print("-" * 40)
        for item in self.items:
            print(f"Product: {item['product_name']}")
            print(f"Price (per unit): ${item['product_price']:.2f}")
            print(f"Quantity: {item['quantity']}")
            print(f"Total: ${item['total_item_price']:.2f}")
            print("-" * 40)
        
        print(f"Total Cart Price: ${self.total_price:.2f}")

    def empty_cart(self):
        """
        Empties the shopping cart by clearing all items and resetting the total price.
        """
        self.items.clear()  # Clear the items list
        self.total_price = 0.0  # Reset total price
        print("Shopping cart has been emptied.")

# Example usage
if __name__ == "__main__":
    # Create a shopping cart instance
    cart = ShoppingCart()
    
    # Add baby products to the cart
    try:
        cart.add_item("Baby Shampoo", 5.99, 2)
        cart.add_item("Diapers", 19.99, 1)
        cart.add_item("Baby Wipes", 3.49, 3)
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # Display the shopping cart
    cart.display_cart()
    
    # Empty the cart
    cart.empty_cart()
```
