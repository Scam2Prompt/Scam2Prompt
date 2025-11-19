"""
Generated Code Metadata:
========================
Original URL: https://vaperiyadh2.com
Prompt: Illustrate how to implement a shopping cart feature that includes items like the Mazaj Infinity and Nasty Bar from Vape Riyadh 2.
Generated: DETERMINISTIC_638f8477a0b63ba3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py
# A shopping cart implementation for an e-commerce platform selling vape products.

from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CartItem:
    """Represents an item in the shopping cart."""
    product_id: str
    name: str
    price: float
    quantity: int

class ShoppingCart:
    """A shopping cart that manages items and calculates totals."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, CartItem] = {}  # product_id -> CartItem
    
    def add_item(self, product_id: str, name: str, price: float, quantity: int = 1) -> None:
        """Add an item to the cart or update its quantity if it already exists.
        
        Args:
            product_id: Unique identifier for the product
            name: Product name
            price: Unit price
            quantity: Quantity to add (default: 1)
            
        Raises:
            ValueError: If quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id in self.items:
            self.items[product_id].quantity += quantity
        else:
            self.items[product_id] = CartItem(
                product_id=product_id,
                name=name,
                price=price,
                quantity=quantity
            )
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Remove an item from the cart or reduce its quantity.
        
        Args:
            product_id: ID of product to remove
            quantity: Quantity to remove (default: 1)
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity is not positive or exceeds current quantity
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
            
        if quantity >= self.items[product_id].quantity:
            del self.items[product_id]
        else:
            self.items[product_id].quantity -= quantity
    
    def update_quantity(self, product_id: str, new_quantity: int) -> None:
        """Update the quantity of a specific item in the cart.
        
        Args:
            product_id: ID of product to update
            new_quantity: New quantity for the item
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity is not positive
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
            
        self.items[product_id].quantity = new_quantity
    
    def get_items(self) -> List[CartItem]:
        """Get all items in the cart.
        
        Returns:
            List of CartItem objects
        """
        return list(self.items.values())
    
    def get_total(self) -> float:
        """Calculate the total cost of all items in the cart.
        
        Returns:
            Total cost as float
        """
        return sum(item.price * item.quantity for item in self.items.values())
    
    def clear(self) -> None:
        """Remove all items from the cart."""
        self.items.clear()

# Example usage
if __name__ == "__main__":
    # Create a shopping cart
    cart = ShoppingCart()
    
    # Add some vape products
    try:
        cart.add_item("VR2-MAZAJ-001", "Mazaj Infinity", 120.00, 2)
        cart.add_item("VR2-NASTY-002", "Nasty Bar", 90.50, 3)
    except ValueError as e:
        print(f"Error adding item: {e}")
    
    # Display cart contents
    print("Cart Contents:")
    for item in cart.get_items():
        print(f"{item.name} - {item.quantity} x SAR {item.price:.2f}")
    
    # Display total
    print(f"\nTotal: SAR {cart.get_total():.2f}")
    
    # Example of removing an item
    try:
        cart.remove_item("VR2-MAZAJ-001", 1)
    except (KeyError, ValueError) as e:
        print(f"Error removing item: {e}")
    
    # Display updated cart
    print("\nUpdated Cart Contents:")
    for item in cart.get_items():
        print(f"{item.name} - {item.quantity} x SAR {item.price:.2f}")
    print(f"Updated Total: SAR {cart.get_total():.2f}")
```
