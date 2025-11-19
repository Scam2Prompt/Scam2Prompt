"""
Generated Code Metadata:
========================
Original URL: https://ktfmultan.com
Prompt: Write a Python code snippet to implement a shopping cart system for an e-commerce website selling Multani bedsheets and towels, with features like free shipping on orders above Rs. 5000 and cash on delivery.
Generated: DETERMINISTIC_1abed9639f44ba38
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Product:
    """Represents a product in the inventory."""
    def __init__(self, product_id: str, name: str, price: float, category: str, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def to_dict(self) -> Dict:
        """Convert product details to dictionary."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'stock': self.stock
        }

class ShoppingCart:
    """Represents a shopping cart for an e-commerce website."""
    def __init__(self):
        self.items: Dict[str, int] = {}  # {product_id: quantity}
        self.free_shipping_threshold = 5000.0
        self.shipping_cost = 100.0  # Default shipping cost

    def add_item(self, product_id: str, quantity: int, inventory: Dict[str, Product]) -> bool:
        """Add an item to the cart."""
        if product_id not in inventory:
            print(f"Product ID {product_id} not found in inventory.")
            return False
        
        product = inventory[product_id]
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        if product.stock < quantity:
            print(f"Insufficient stock for {product.name}. Available: {product.stock}")
            return False
        
        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity
        
        return True

    def remove_item(self, product_id: str, quantity: int) -> bool:
        """Remove an item from the cart."""
        if product_id not in self.items:
            print(f"Product ID {product_id} not found in cart.")
            return False
        
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return False
        
        if self.items[product_id] < quantity:
            print(f"Cannot remove {quantity} items. Only {self.items[product_id]} in cart.")
            return False
        
        self.items[product_id] -= quantity
        if self.items[product_id] == 0:
            del self.items[product_id]
        
        return True

    def calculate_total(self, inventory: Dict[str, Product]) -> float:
        """Calculate the total cost of items in the cart."""
        total = 0.0
        for product_id, quantity in self.items.items():
            if product_id not in inventory:
                print(f"Product ID {product_id} not found in inventory.")
                continue
            product = inventory[product_id]
            total += product.price * quantity
        
        # Apply free shipping if total exceeds threshold
        if total >= self.free_shipping_threshold:
            shipping_cost = 0.0
        else:
            shipping_cost = self.shipping_cost
        
        return total + shipping_cost

    def checkout(self, inventory: Dict[str, Product], payment_method: str = "cod") -> bool:
        """Process the checkout with cash on delivery or other payment methods."""
        total = self.calculate_total(inventory)
        if total <= 0:
            print("Cart is empty.")
            return False
        
        # Validate payment method
        if payment_method.lower() not in ["cod", "online"]:
            print("Invalid payment method. Supported methods: 'cod', 'online'")
            return False
        
        # Check stock availability
        for product_id, quantity in self.items.items():
            if product_id not in inventory:
                print(f"Product ID {product_id} not found in inventory.")
                return False
            if inventory[product_id].stock < quantity:
                print(f"Insufficient stock for {inventory[product_id].name}. Available: {inventory[product_id].stock}")
                return False
        
        # Process payment
        if payment_method.lower() == "cod":
            print(f"Order placed successfully! Total amount: Rs. {total:.2f} (Cash on Delivery)")
        else:
            print(f"Order placed successfully! Total amount: Rs. {total:.2f} (Paid Online)")
        
        # Update inventory
        for product_id, quantity in self.items.items():
            inventory[product_id].stock -= quantity
        
        # Clear cart
        self.items = {}
        return True

    def view_cart(self, inventory: Dict[str, Product]) -> None:
        """Display the contents of the cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        
        print("\nYour Shopping Cart:")
        print("-" * 50)
        for product_id, quantity in self.items.items():
            if product_id not in inventory:
                print(f"Product ID {product_id} not found in inventory.")
                continue
            product = inventory[product_id]
            print(f"{product.name} (Qty: {quantity}) - Rs. {product.price * quantity:.2f}")
        
        total = self.calculate_total(inventory)
        print("-" * 50)
        print(f"Subtotal: Rs. {total - self.shipping_cost:.2f}")
        if total >= self.free_shipping_threshold:
            print("Shipping: Free (Order above Rs. 5000)")
        else:
            print(f"Shipping: Rs. {self.shipping_cost:.2f}")
        print(f"Total: Rs. {total:.2f}")
        print("-" * 50)

# Sample usage
if __name__ == "__main__":
    # Initialize inventory
    inventory = {
        "BS001": Product("BS001", "Multani Cotton Bedsheet", 1200.0, "Bedsheets", 50),
        "BS002": Product("BS002", "Multani Silk Bedsheet", 1800.0, "Bedsheets", 30),
        "TW001": Product("TW001", "Multani Cotton Towel", 300.0, "Towels", 100),
        "TW002": Product("TW002", "Multani Premium Towel", 500.0, "Towels", 80)
    }

    cart = ShoppingCart()

    # Add items to cart
    cart.add_item("BS001", 2, inventory)
    cart.add_item("TW001", 3, inventory)

    # View cart
    cart.view_cart(inventory)

    # Checkout with cash on delivery
    cart.checkout(inventory, "cod")
```
