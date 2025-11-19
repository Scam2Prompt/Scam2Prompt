"""
Generated Code Metadata:
========================
Original URL: https://craftimus.com
Prompt: Create a Python script to manage orders for Himalayan salt licks and animal-shaped salt lamps, including options for bulk purchasing and custom packaging.
Generated: DETERMINISTIC_532db2f3f6978980
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Union

class Product:
    """Class representing a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int, product_type: str):
        """
        Initialize a product.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price per unit
            stock: Quantity available
            product_type: Type of product (e.g., 'salt_lick', 'salt_lamp')
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.type = product_type
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'type': self.type
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        return cls(
            product_id=data['product_id'],
            name=data['name'],
            price=data['price'],
            stock=data['stock'],
            product_type=data['type']
        )

class OrderItem:
    """Class representing an item in an order."""
    
    def __init__(self, product_id: str, quantity: int, custom_packaging: bool = False):
        """
        Initialize an order item.
        
        Args:
            product_id: ID of the product being ordered
            quantity: Number of units ordered
            custom_packaging: Whether custom packaging is requested
        """
        self.product_id = product_id
        self.quantity = quantity
        self.custom_packaging = custom_packaging
    
    def to_dict(self) -> Dict:
        """Convert order item to dictionary for serialization."""
        return {
            'product_id': self.product_id,
            'quantity': self.quantity,
            'custom_packaging': self.custom_packaging
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'OrderItem':
        """Create order item from dictionary."""
        return cls(
            product_id=data['product_id'],
            quantity=data['quantity'],
            custom_packaging=data.get('custom_packaging', False)
        )

class Order:
    """Class representing a customer order."""
    
    def __init__(self, order_id: str, customer_name: str, items: List[OrderItem], bulk_discount: bool = False):
        """
        Initialize an order.
        
        Args:
            order_id: Unique identifier for the order
            customer_name: Name of the customer
            items: List of items in the order
            bulk_discount: Whether bulk discount applies
        """
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.bulk_discount = bulk_discount
        self.status = 'pending'
    
    def calculate_total(self, inventory: Dict[str, Product]) -> float:
        """
        Calculate the total cost of the order.
        
        Args:
            inventory: Dictionary of available products
            
        Returns:
            Total cost of the order
        """
        total = 0.0
        for item in self.items:
            product = inventory.get(item.product_id)
            if product:
                item_total = product.price * item.quantity
                if item.custom_packaging:
                    item_total += 5.0  # Custom packaging fee
                total += item_total
        
        # Apply bulk discount if applicable (10% off)
        if self.bulk_discount and total > 100:
            total *= 0.9
        
        return round(total, 2)
    
    def to_dict(self) -> Dict:
        """Convert order to dictionary for serialization."""
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'items': [item.to_dict() for item in self.items],
            'bulk_discount': self.bulk_discount,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        """Create order from dictionary."""
        order = cls(
            order_id=data['order_id'],
            customer_name=data['customer_name'],
            items=[OrderItem.from_dict(item) for item in data['items']],
            bulk_discount=data.get('bulk_discount', False)
        )
        order.status = data.get('status', 'pending')
        return order

class OrderManager:
    """Class to manage orders and inventory."""
    
    def __init__(self, inventory_file: str = 'inventory.json', orders_file: str = 'orders.json'):
        """
        Initialize the order manager.
        
        Args:
            inventory_file: Path to inventory JSON file
            orders_file: Path to orders JSON file
        """
        self.inventory_file = inventory_file
        self.orders_file = orders_file
        self.inventory = self._load_inventory()
        self.orders = self._load_orders()
    
    def _load_inventory(self) -> Dict[str, Product]:
        """Load inventory from JSON file."""
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    data = json.load(f)
                    return {pid: Product.from_dict(p) for pid, p in data.items()}
            return {}
        except Exception as e:
            print(f"Error loading inventory: {e}")
            return {}
    
    def _load_orders(self) -> Dict[str, Order]:
        """Load orders from JSON file."""
        try:
            if os.path.exists(self.orders_file):
                with open(self.orders_file, 'r') as f:
                    data = json.load(f)
                    return {oid: Order.from_dict(o) for oid, o in data.items()}
            return {}
        except Exception as e:
            print(f"Error loading orders: {e}")
            return {}
    
    def _save_inventory(self) -> bool:
        """Save inventory to JSON file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump({pid: p.to_dict() for pid, p in self.inventory.items()}, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving inventory: {e}")
            return False
    
    def _save_orders(self) -> bool:
        """Save orders to JSON file."""
        try:
            with open(self.orders_file, 'w') as f:
                json.dump({oid: o.to_dict() for oid, o in self.orders.items()}, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving orders: {e}")
            return False
    
    def add_product(self, product: Product) -> bool:
        """Add a new product to inventory."""
        if product.product_id in self.inventory:
            print(f"Product ID {product.product_id} already exists.")
            return False
        
        self.inventory[product.product_id] = product
        return self._save_inventory()
    
    def update_product_stock(self, product_id: str, quantity: int) -> bool:
        """Update product stock quantity."""
        if product_id not in self.inventory:
            print(f"Product ID {product_id} not found.")
            return False
        
        self.inventory[product_id].stock += quantity
        return self._save_inventory()
    
    def create_order(self, customer_name: str, items: List[OrderItem], bulk_discount: bool = False) -> Optional[str]:
        """
        Create a new order.
        
        Args:
            customer_name: Name of the customer
            items: List of order items
            bulk_discount: Whether bulk discount applies
            
        Returns:
            Order ID if successful, None otherwise
        """
        # Check product availability
        for item in items:
            product = self.inventory.get(item.product_id)
            if not product:
                print(f"Product ID {item.product_id} not found.")
                return None
            if product.stock < item.quantity:
                print(f"Insufficient stock for product {product.name} (ID: {product.product_id})")
                return None
        
        # Generate order ID
        order_id = f"ORD-{len(self.orders) + 1:04d}"
        
        # Create order
        order = Order(order_id, customer_name, items, bulk_discount)
        self.orders[order_id] = order
        
        # Update inventory
        for item in items:
            self.inventory[item.product_id].stock -= item.quantity
        
        # Save changes
        if self._save_inventory() and self._save_orders():
            return order_id
        return None
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Retrieve an order by ID."""
        return self.orders.get(order_id)
    
    def update_order_status(self, order_id: str, status: str) -> bool:
        """Update order status."""
        if order_id not in self.orders:
            print(f"Order ID {order_id} not found.")
            return False
