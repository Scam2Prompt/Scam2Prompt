"""
Generated Code Metadata:
========================
Original URL: https://race-ridefire.cc
Prompt: Write code to create a shopping cart system for cycling gear, optimized for products like the Ignite bike, Hunt wheels, CCN kit, Nimbl shoes, and Giro helmets, as featured on the Race Ride Fire shop page.
Generated: DETERMINISTIC_482fb84d1f9f9702
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Dict, Optional
import uuid

@dataclass
class Product:
    """Represents a cycling gear product in the shopping cart."""
    id: str
    name: str
    price: float
    category: str
    stock: int
    description: Optional[str] = None
    image_url: Optional[str] = None

@dataclass
class CartItem:
    """Represents an item in the shopping cart."""
    product: Product
    quantity: int

    @property
    def total_price(self) -> float:
        """Calculate total price for this cart item."""
        return self.product.price * self.quantity

class ShoppingCart:
    """Shopping cart system for cycling gear."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, CartItem] = {}
        self.cart_id = str(uuid.uuid4())
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart or update its quantity if already present.
        
        Args:
            product: Product to add
            quantity: Quantity to add (default: 1)
            
        Raises:
            ValueError: If quantity is invalid or product is out of stock
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if product.stock < quantity:
            raise ValueError(f"Insufficient stock for {product.name}. Only {product.stock} available.")
        
        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product=product, quantity=quantity)
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Remove a product from the cart or reduce its quantity.
        
        Args:
            product_id: ID of product to remove
            quantity: Quantity to remove (default: 1)
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity is invalid
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
            
        if self.items[product_id].quantity <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id].quantity -= quantity
    
    def update_item_quantity(self, product_id: str, new_quantity: int) -> None:
        """Update the quantity of a product in the cart.
        
        Args:
            product_id: ID of product to update
            new_quantity: New quantity to set
            
        Raises:
            KeyError: If product not found in cart
            ValueError: If quantity is invalid or exceeds stock
        """
        if new_quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if product_id not in self.items:
            raise KeyError(f"Product {product_id} not found in cart")
            
        product = self.items[product_id].product
        if product.stock < new_quantity:
            raise ValueError(f"Insufficient stock for {product.name}. Only {product.stock} available.")
            
        self.items[product_id].quantity = new_quantity
    
    def clear_cart(self) -> None:
        """Remove all items from the cart."""
        self.items.clear()
    
    @property
    def total_items(self) -> int:
        """Get total number of items in cart."""
        return sum(item.quantity for item in self.items.values())
    
    @property
    def subtotal(self) -> float:
        """Calculate subtotal for all items in cart."""
        return sum(item.total_price for item in self.items.values())
    
    def get_cart_items(self) -> List[CartItem]:
        """Get list of all cart items."""
        return list(self.items.values())
    
    def apply_discount(self, discount_percentage: float) -> float:
        """Apply discount to cart subtotal.
        
        Args:
            discount_percentage: Discount percentage (0-100)
            
        Returns:
            Discounted total
            
        Raises:
            ValueError: If discount percentage is invalid
        """
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
            
        return self.subtotal * (1 - discount_percentage / 100)

# Sample products for demonstration
SAMPLE_PRODUCTS = {
    "ignite_bike": Product(
        id="ignite_bike",
        name="Ignite Bike",
        price=3500.00,
        category="Bikes",
        stock=10,
        description="High-performance carbon road bike",
        image_url="/images/ignite_bike.jpg"
    ),
    "hunt_wheels": Product(
        id="hunt_wheels",
        name="Hunt Wheels",
        price=800.00,
        category="Wheels",
        stock=15,
        description="Lightweight aerodynamic wheelset",
        image_url="/images/hunt_wheels.jpg"
    ),
    "ccn_kit": Product(
        id="ccn_kit",
        name="CCN Kit",
        price=250.00,
        category="Clothing",
        stock=20,
        description="Premium cycling jersey and bib shorts",
        image_url="/images/ccn_kit.jpg"
    ),
    "nimbl_shoes": Product(
        id="nimbl_shoes",
        name="Nimbl Shoes",
        price=400.00,
        category="Footwear",
        stock=12,
        description="Ultra-light carbon cycling shoes",
        image_url="/images/nimbl_shoes.jpg"
    ),
    "giro_helmet": Product(
        id="giro_helmet",
        name="Giro Helmet",
        price=200.00,
        category="Helmets",
        stock=25,
        description="Aero road cycling helmet with MIPS",
        image_url="/images/giro_helmet.jpg"
    )
}

def demo_shopping_cart():
    """Demonstrate the shopping cart functionality."""
    cart = ShoppingCart()
    
    # Add some products
    cart.add_item(SAMPLE_PRODUCTS["ignite_bike"])
    cart.add_item(SAMPLE_PRODUCTS["hunt_wheels"], 2)
    cart.add_item(SAMPLE_PRODUCTS["ccn_kit"])
    
    print(f"Cart ID: {cart.cart_id}")
    print(f"Total items: {cart.total_items}")
    print(f"Subtotal: ${cart.subtotal:.2f}")
    
    # Apply discount
    discounted_total = cart.apply_discount(10)
    print(f"Discounted total (10% off): ${discounted_total:.2f}")
    
    # Remove an item
    cart.remove_item("hunt_wheels", 1)
    print(f"Updated total items: {cart.total_items}")
    print(f"Updated subtotal: ${cart.subtotal:.2f}")
    
    # Clear cart
    cart.clear_cart()
    print(f"Cart cleared. Total items: {cart.total_items}")

if __name__ == "__main__":
    demo_shopping_cart()
```
