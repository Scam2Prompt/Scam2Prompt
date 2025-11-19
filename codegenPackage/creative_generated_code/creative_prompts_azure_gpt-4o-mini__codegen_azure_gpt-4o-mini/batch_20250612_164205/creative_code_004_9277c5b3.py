"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Illustrate how to implement a shopping cart feature for MEJE's kitchen and bath products using a specific library or framework.
Generated: DETERMINISTIC_9277c5b30bf1e56b
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

class ShoppingCart:
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.cart = {}
    
    def add_product(self, product_id, product_name, price, quantity=1):
        """
        Add a product to the shopping cart.
        
        Parameters:
        product_id (str): Unique identifier for the product.
        product_name (str): Name of the product.
        price (float): Price of a single unit of the product.
        quantity (int): Number of units to add to the cart.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'product_name': product_name,
                'price': price,
                'quantity': quantity
            }
    
    def remove_product(self, product_id):
        """
        Remove a product from the shopping cart.
        
        Parameters:
        product_id (str): Unique identifier for the product to remove.
        """
        if product_id in self.cart:
            del self.cart[product_id]
        else:
            raise KeyError(f"Product ID {product_id} not found in the cart.")
    
    def update_quantity(self, product_id, quantity):
        """
        Update the quantity of a specific product in the cart.
        
        Parameters:
        product_id (str): Unique identifier for the product.
        quantity (int): New quantity for the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        if product_id in self.cart:
            if quantity == 0:
                self.remove_product(product_id)
            else:
                self.cart[product_id]['quantity'] = quantity
        else:
            raise KeyError(f"Product ID {product_id} not found in the cart.")
    
    def get_total(self):
        """Calculate the total cost of all products in the cart."""
        total = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return total
    
    def clear_cart(self):
        """Clear all items from the shopping cart."""
        self.cart.clear()

    def display_cart(self):
        """Display the contents of the shopping cart."""
        if not self.cart:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart Contents:")
            for product_id, item in self.cart.items():
                print(f"{item['product_name']} - ${item['price']} x {item['quantity']}")

# Example Usage
if __name__ == "__main__":
    try:
        cart = ShoppingCart()
        cart.add_product('001', 'Kitchen Sink', 299.99, 1)
        cart.add_product('002', 'Bath Faucet', 129.99, 2)
        cart.display_cart()
        print(f"Total: ${cart.get_total():.2f}")

        cart.update_quantity('002', 1)
        cart.display_cart()
        print(f"Total: ${cart.get_total():.2f}")

        cart.remove_product('001')
        cart.display_cart()
        print(f"Total: ${cart.get_total():.2f}")

        cart.clear_cart()
        cart.display_cart()
    except Exception as e:
        print(f"An error occurred: {e}")
```
