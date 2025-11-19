"""
Generated Code Metadata:
========================
Original URL: https://lalitarora.in
Prompt: Generate a code snippet for a simple e-commerce platform, similar to Dr. Lalit Arora's coaching shop, using a suitable programming language.
Generated: DETERMINISTIC_d32d00282a82e565
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# E-commerce Platform for Coaching Shop
# Features: Product Management, Cart Functionality, Checkout Process

from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
import datetime

@dataclass
class Product:
    id: str
    name: str
    description: str
    price: float
    stock: int
    category: str

@dataclass
class CartItem:
    product: Product
    quantity: int

@dataclass
class Order:
    id: str
    items: List[CartItem]
    total_amount: float
    customer_name: str
    customer_email: str
    order_date: str
    status: str = "Pending"

class ECommercePlatform:
    def __init__(self):
        self.products: List[Product] = []
        self.cart: List[CartItem] = []
        self.orders: List[Order] = []
        
    def add_product(self, name: str, description: str, price: float, stock: int, category: str) -> Product:
        """Add a new product to the inventory"""
        if price <= 0:
            raise ValueError("Price must be positive")
        if stock < 0:
            raise ValueError("Stock cannot be negative")
            
        product = Product(
            id=str(uuid.uuid4()),
            name=name,
            description=description,
            price=price,
            stock=stock,
            category=category
        )
        self.products.append(product)
        return product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Retrieve a product by ID"""
        for product in self.products:
            if product.id == product_id:
                return product
        return None
    
    def add_to_cart(self, product_id: str, quantity: int = 1) -> None:
        """Add product to shopping cart"""
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product.stock < quantity:
            raise ValueError("Insufficient stock")
            
        # Check if product already in cart
        for item in self.cart:
            if item.product.id == product_id:
                item.quantity += quantity
                return
                
        # Add new item to cart
        self.cart.append(CartItem(product=product, quantity=quantity))
    
    def remove_from_cart(self, product_id: str, quantity: int = 1) -> None:
        """Remove product from shopping cart"""
        for item in self.cart:
            if item.product.id == product_id:
                if quantity >= item.quantity:
                    self.cart.remove(item)
                else:
                    item.quantity -= quantity
                return
        raise ValueError("Product not found in cart")
    
    def get_cart_total(self) -> float:
        """Calculate total amount in cart"""
        return sum(item.product.price * item.quantity for item in self.cart)
    
    def checkout(self, customer_name: str, customer_email: str) -> Order:
        """Process order and create new order"""
        if not self.cart:
            raise ValueError("Cart is empty")
            
        # Verify stock availability
        for item in self.cart:
            product = self.get_product(item.product.id)
            if product.stock < item.quantity:
                raise ValueError(f"Insufficient stock for {product.name}")
                
        # Create order
        order = Order(
            id=str(uuid.uuid4()),
            items=self.cart.copy(),
            total_amount=self.get_cart_total(),
            customer_name=customer_name,
            customer_email=customer_email,
            order_date=datetime.datetime.now().isoformat()
        )
        
        # Update stock and clear cart
        for item in self.cart:
            product = self.get_product(item.product.id)
            product.stock -= item.quantity
            
        self.orders.append(order)
        self.cart.clear()
        
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve order by ID"""
        for order in self.orders:
            if order.id == order_id:
                return order
        return None
    
    def update_order_status(self, order_id: str, status: str) -> None:
        """Update order status"""
        order = self.get_order(order_id)
        if not order:
            raise ValueError("Order not found")
        order.status = status

# Example usage
if __name__ == "__main__":
    shop = ECommercePlatform()
    
    # Add products
    course1 = shop.add_product(
        name="Python Fundamentals",
        description="Learn Python from scratch",
        price=2999.00,
        stock=50,
        category="Online Course"
    )
    
    book1 = shop.add_product(
        name="Data Structures Handbook",
        description="Comprehensive guide to DS",
        price=499.00,
        stock=100,
        category="E-Book"
    )
    
    # Add to cart
    shop.add_to_cart(course1.id, 2)
    shop.add_to_cart(book1.id, 1)
    
    # Checkout
    try:
        order = shop.checkout(
            customer_name="John Doe",
            customer_email="john@example.com"
        )
        print(f"Order #{order.id} created successfully!")
    except ValueError as e:
        print(f"Checkout failed: {e}")
```
