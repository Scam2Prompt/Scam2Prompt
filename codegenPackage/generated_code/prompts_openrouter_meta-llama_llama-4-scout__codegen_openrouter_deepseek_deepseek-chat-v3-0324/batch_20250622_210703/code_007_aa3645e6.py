"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Design a library for managing essential oil inventory, including functions for tracking stock levels, orders, and shipping information for an online store like Use Essential Oils Australia.
Generated: DETERMINISTIC_aa3645e6e47c9fdc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Essential Oil Inventory Management Library
This library provides functionality to manage inventory, orders, and shipping
for an online essential oils store.
"""

from typing import List, Dict, Optional
from datetime import datetime
import uuid
import json
import os

class EssentialOil:
    """Class representing an essential oil product."""
    
    def __init__(self, name: str, description: str, price: float, stock: int, 
                 category: str, batch_number: str, expiry_date: datetime):
        """
        Initialize an essential oil product.
        
        Args:
            name: Name of the oil
            description: Product description
            price: Price per unit
            stock: Current stock quantity
            category: Product category (e.g., 'Floral', 'Citrus')
            batch_number: Manufacturing batch number
            expiry_date: Expiry date of the product
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.category = category
        self.batch_number = batch_number
        self.expiry_date = expiry_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_stock(self, quantity: int) -> None:
        """Update the stock quantity of the product."""
        if self.stock + quantity < 0:
            raise ValueError("Stock cannot be negative")
        self.stock += quantity
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'stock': self.stock,
            'category': self.category,
            'batch_number': self.batch_number,
            'expiry_date': self.expiry_date.isoformat(),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Order:
    """Class representing a customer order."""
    
    def __init__(self, customer_id: str, items: Dict[str, int], shipping_address: str):
        """
        Initialize an order.
        
        Args:
            customer_id: ID of the customer placing the order
            items: Dictionary of product IDs and quantities
            shipping_address: Shipping address for the order
        """
        self.id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.items = items
        self.shipping_address = shipping_address
        self.status = "pending"
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def update_status(self, new_status: str) -> None:
        """Update the order status."""
        valid_statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert order to dictionary for serialization."""
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'items': self.items,
            'shipping_address': self.shipping_address,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Shipping:
    """Class representing shipping information for an order."""
    
    def __init__(self, order_id: str, carrier: str, tracking_number: str, 
                 estimated_delivery: datetime):
        """
        Initialize shipping information.
        
        Args:
            order_id: ID of the order being shipped
            carrier: Shipping carrier (e.g., 'Australia Post')
            tracking_number: Tracking number for the shipment
            estimated_delivery: Estimated delivery date
        """
        self.id = str(uuid.uuid4())
        self.order_id = order_id
        self.carrier = carrier
        self.tracking_number = tracking_number
        self.estimated_delivery = estimated_delivery
        self.actual_delivery = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def mark_delivered(self, delivery_date: datetime) -> None:
        """Mark the shipment as delivered."""
        if delivery_date < self.created_at:
            raise ValueError("Delivery date cannot be before shipping date")
        self.actual_delivery = delivery_date
        self.updated_at = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert shipping info to dictionary for serialization."""
        return {
            'id': self.id,
            'order_id': self.order_id,
            'carrier': self.carrier,
            'tracking_number': self.tracking_number,
            'estimated_delivery': self.estimated_delivery.isoformat(),
            'actual_delivery': self.actual_delivery.isoformat() if self.actual_delivery else None,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class InventoryManager:
    """Class for managing essential oil inventory."""
    
    def __init__(self, data_file: str = "inventory_data.json"):
        """
        Initialize the inventory manager.
        
        Args:
            data_file: Path to JSON file for data persistence
        """
        self.data_file = data_file
        self.products: Dict[str, EssentialOil] = {}
        self.orders: Dict[str, Order] = {}
        self.shipments: Dict[str, Shipping] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from the JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                for product_data in data.get('products', []):
                    product = EssentialOil(
                        name=product_data['name'],
                        description=product_data['description'],
                        price=product_data['price'],
                        stock=product_data['stock'],
                        category=product_data['category'],
                        batch_number=product_data['batch_number'],
                        expiry_date=datetime.fromisoformat(product_data['expiry_date'])
                    )
                    product.id = product_data['id']
                    product.created_at = datetime.fromisoformat(product_data['created_at'])
                    product.updated_at = datetime.fromisoformat(product_data['updated_at'])
                    self.products[product.id] = product
                
                for order_data in data.get('orders', []):
                    order = Order(
                        customer_id=order_data['customer_id'],
                        items=order_data['items'],
                        shipping_address=order_data['shipping_address']
                    )
                    order.id = order_data['id']
                    order.status = order_data['status']
                    order.created_at = datetime.fromisoformat(order_data['created_at'])
                    order.updated_at = datetime.fromisoformat(order_data['updated_at'])
                    self.orders[order.id] = order
                
                for shipping_data in data.get('shipments', []):
                    shipping = Shipping(
                        order_id=shipping_data['order_id'],
                        carrier=shipping_data['carrier'],
                        tracking_number=shipping_data['tracking_number'],
                        estimated_delivery=datetime.fromisoformat(shipping_data['estimated_delivery'])
                    )
                    shipping.id = shipping_data['id']
                    shipping.created_at = datetime.fromisoformat(shipping_data['created_at'])
                    shipping.updated_at = datetime.fromisoformat(shipping_data['updated_at'])
                    if shipping_data['actual_delivery']:
                        shipping.actual_delivery = datetime.fromisoformat(shipping_data['actual_delivery'])
                    self.shipments[shipping.id] = shipping
    
    def _save_data(self) -> None:
        """Save data to the JSON file."""
        data = {
            'products': [product.to_dict() for product in self.products.values()],
            'orders': [order.to_dict() for order in self.orders.values()],
            'shipments': [shipping.to_dict() for shipping in self.shipments.values()]
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def add_product(self, product: EssentialOil) -> None:
        """Add a new product to inventory."""
        if product.id in self.products:
            raise ValueError("Product with this ID already exists")
        self.products[product.id] = product
        self._save_data()
    
    def get_product(self, product_id: str) -> Optional[EssentialOil]:
        """Get a product by ID."""
        return self.products.get(product_id)
    
    def update_product_stock(self, product_id: str, quantity: int) -> None:
        """Update stock quantity for a product."""
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found")
        product.update_stock(quantity)
        self._save_data()
    
    def get_low_stock_products(self, threshold: int = 10) -> List[EssentialOil]:
        """
