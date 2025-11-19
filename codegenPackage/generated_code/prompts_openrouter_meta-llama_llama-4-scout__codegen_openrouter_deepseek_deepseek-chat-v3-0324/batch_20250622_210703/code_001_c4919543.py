"""
Generated Code Metadata:
========================
Original URL: https://elo.mk
Prompt: "Write a Python code snippet to manage an e-commerce shopping cart for baby products, including calculating discounts and totals."
Generated: DETERMINISTIC_c49195435735f883
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
from typing import List, Dict, Optional, Union

class Product:
    """Represents a baby product in the e-commerce store."""
    
    def __init__(self, product_id: str, name: str, price: float, category: str, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'category': self.category,
            'stock': self.stock
        }

class CartItem:
    """Represents an item in the shopping cart."""
    
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
    
    def update_quantity(self, new_quantity: int) -> None:
        """Update the quantity of the cart item."""
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.quantity = new_quantity
    
    def get_total_price(self) -> float:
        """Calculate total price for this cart item."""
        return self.product.price * self.quantity
    
    def to_dict(self) -> Dict:
        """Convert cart item to dictionary."""
        return {
            'product': self.product.to_dict(),
            'quantity': self.quantity,
            'total_price': self.get_total_price()
        }

class ShoppingCart:
    """Manages the shopping cart operations."""
    
    def __init__(self):
        self.items: Dict[str, CartItem] = {}
        self.discount_rules = {
            'DIAPERS10': {'type': 'percentage', 'value': 10},
            'BABY20': {'type': 'fixed', 'value': 20}
        }
        self.applied_discount_code: Optional[str] = None
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart or update its quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if product.product_id in self.items:
            self.items[product.product_id].update_quantity(
                self.items[product.product_id].quantity + quantity
            )
        else:
            self.items[product.product_id] = CartItem(product, quantity)
    
    def remove_item(self, product_id: str) -> None:
        """Remove an item from the cart."""
        if product_id not in self.items:
            raise ValueError("Product not found in cart")
        del self.items[product_id]
    
    def update_item_quantity(self, product_id: str, new_quantity: int) -> None:
        """Update the quantity of a specific item in the cart."""
        if product_id not in self.items:
            raise ValueError("Product not found in cart")
        self.items[product_id].update_quantity(new_quantity)
    
    def apply_discount(self, discount_code: str) -> bool:
        """Apply a discount code to the cart."""
        if discount_code not in self.discount_rules:
            return False
        self.applied_discount_code = discount_code
        return True
    
    def remove_discount(self) -> None:
        """Remove any applied discount from the cart."""
        self.applied_discount_code = None
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal before discounts."""
        return sum(item.get_total_price() for item in self.items.values())
    
    def calculate_discount(self) -> float:
        """Calculate discount amount based on applied discount."""
        if not self.applied_discount_code:
            return 0.0
        
        rule = self.discount_rules[self.applied_discount_code]
        subtotal = self.calculate_subtotal()
        
        if rule['type'] == 'percentage':
            return subtotal * (rule['value'] / 100)
        elif rule['type'] == 'fixed':
            return min(rule['value'], subtotal)
        return 0.0
    
    def calculate_total(self) -> float:
        """Calculate total after applying discounts."""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        return subtotal - discount
    
    def get_cart_summary(self) -> Dict:
        """Return a summary of the cart contents."""
        return {
            'items': [item.to_dict() for item in self.items.values()],
            'subtotal': self.calculate_subtotal(),
            'applied_discount': self.applied_discount_code,
            'discount_amount': self.calculate_discount(),
            'total': self.calculate_total()
        }
    
    def clear_cart(self) -> None:
        """Remove all items from the cart."""
        self.items = {}
        self.applied_discount_code = None

# Example usage
if __name__ == "__main__":
    # Create some sample products
    diaper = Product("P001", "Premium Diapers", 25.99, "diapers", 100)
    bottle = Product("P002", "Baby Bottle", 12.50, "feeding", 50)
    onesie = Product("P003", "Cotton Onesie", 15.75, "clothing", 30)
    
    # Initialize shopping cart
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item(diaper, 2)
    cart.add_item(bottle)
    cart.add_item(onesie, 3)
    
    # Apply discount
    cart.apply_discount("DIAPERS10")
    
    # Get cart summary
    summary = cart.get_cart_summary()
    print(json.dumps(summary, indent=2))
```
