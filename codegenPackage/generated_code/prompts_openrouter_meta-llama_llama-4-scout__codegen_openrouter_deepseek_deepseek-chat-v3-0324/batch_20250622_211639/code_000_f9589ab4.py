"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Write a Python code to manage wholesale orders for Elfworld Vape products, including PB45000 and AI22000 devices.
Generated: DETERMINISTIC_f9589ab465ff5a7d
Batch ID: 20250622_211639
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
from dataclasses import dataclass, asdict
import os


@dataclass
class Product:
    """Represents a vape product with its details."""
    product_id: str
    name: str
    description: str
    price: float
    quantity_in_stock: int


@dataclass
class OrderItem:
    """Represents an item in an order with product and quantity."""
    product_id: str
    quantity: int


@dataclass
class Order:
    """Represents a wholesale order with customer and items."""
    order_id: str
    customer_name: str
    items: List[OrderItem]
    total_price: float
    status: str = "pending"  # pending, fulfilled, cancelled


class ElfworldVapeWholesaleManager:
    """Manages wholesale orders for Elfworld Vape products."""
    
    def __init__(self, inventory_file: str = "inventory.json", orders_file: str = "orders.json"):
        """Initialize the wholesale manager with inventory and orders files."""
        self.inventory_file = inventory_file
        self.orders_file = orders_file
        self.products: Dict[str, Product] = {}
        self.orders: Dict[str, Order] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load inventory and orders data from files."""
        try:
            # Load inventory
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    inventory_data = json.load(f)
                    self.products = {
                        pid: Product(**data) for pid, data in inventory_data.items()
                    }
            else:
                # Initialize with default products if file doesn't exist
                self.products = {
                    "PB45000": Product(
                        product_id="PB45000",
                        name="Elfworld PB45000",
                        description="Premium vape device with 4500 puffs",
                        price=12.99,
                        quantity_in_stock=1000
                    ),
                    "AI22000": Product(
                        product_id="AI22000",
                        name="Elfworld AI22000",
                        description="Advanced AI-powered vape device with 22000 puffs",
                        price=24.99,
                        quantity_in_stock=500
                    )
                }
                self._save_inventory()
            
            # Load orders
            if os.path.exists(self.orders_file):
                with open(self.orders_file, 'r') as f:
                    orders_data = json.load(f)
                    self.orders = {
                        oid: Order(
                            order_id=oid,
                            customer_name=data['customer_name'],
                            items=[OrderItem(**item) for item in data['items']],
                            total_price=data['total_price'],
                            status=data['status']
                        ) for oid, data in orders_data.items()
                    }
        except Exception as e:
            raise RuntimeError(f"Failed to load data: {str(e)}")
    
    def _save_inventory(self) -> None:
        """Save inventory data to file."""
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(
                    {pid: asdict(product) for pid, product in self.products.items()},
                    f,
                    indent=2
                )
        except Exception as e:
            raise RuntimeError(f"Failed to save inventory: {str(e)}")
    
    def _save_orders(self) -> None:
        """Save orders data to file."""
        try:
            with open(self.orders_file, 'w') as f:
                json.dump(
                    {
                        oid: {
                            'order_id': oid,
                            'customer_name': order.customer_name,
                            'items': [asdict(item) for item in order.items],
                            'total_price': order.total_price,
                            'status': order.status
                        } for oid, order in self.orders.items()
                    },
                    f,
                    indent=2
                )
        except Exception as e:
            raise RuntimeError(f"Failed to save orders: {str(e)}")
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get a product by its ID."""
        return self.products.get(product_id)
    
    def get_order(self, order_id: str) -> Optional[Order]:
        """Get an order by its ID."""
        return self.orders.get(order_id)
    
    def add_product(self, product: Product) -> None:
        """Add a new product to inventory."""
        if product.product_id in self.products:
            raise ValueError(f"Product with ID {product.product_id} already exists")
        self.products[product.product_id] = product
        self._save_inventory()
    
    def update_product(self, product_id: str, **kwargs) -> None:
        """Update product details."""
        if product_id not in self.products:
            raise ValueError(f"Product with ID {product_id} not found")
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        
        self._save_inventory()
    
    def place_order(self, customer_name: str, items: List[OrderItem]) -> Order:
        """
        Place a new wholesale order.
        
        Args:
            customer_name: Name of the customer placing the order
            items: List of OrderItems representing products and quantities
            
        Returns:
            The created Order object
        """
        # Validate items and calculate total price
        total_price = 0.0
        for item in items:
            product = self.get_product(item.product_id)
            if not product:
                raise ValueError(f"Product {item.product_id} not found")
            if product.quantity_in_stock < item.quantity:
                raise ValueError(f"Insufficient stock for product {item.product_id}")
            total_price += product.price * item.quantity
        
        # Create order
        order_id = f"ORD-{len(self.orders) + 1:06d}"
        order = Order(
            order_id=order_id,
            customer_name=customer_name,
            items=items,
            total_price=total_price
        )
        
        # Update inventory and save order
        for item in items:
            self.products[item.product_id].quantity_in_stock -= item.quantity
        
        self.orders[order_id] = order
        self._save_inventory()
        self._save_orders()
        
        return order
    
    def update_order_status(self, order_id: str, status: str) -> Order:
        """
        Update the status of an order.
        
        Valid statuses: pending, fulfilled, cancelled
        """
        if order_id not in self.orders:
            raise ValueError(f"Order {order_id} not found")
        
        valid_statuses = {"pending", "fulfilled", "cancelled"}
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of {valid_statuses}")
        
        order = self.orders[order_id]
        order.status = status
        self._save_orders()
        
        return order
    
    def list_products(self) -> List[Product]:
        """List all available products."""
        return list(self.products.values())
    
    def list_orders(self, status_filter: Optional[str] = None) -> List[Order]:
        """List all orders, optionally filtered by status."""
        if status_filter:
            return [order for order in self.orders.values() if order.status == status_filter]
        return list(self.orders.values())


# Example usage
if __name__ == "__main__":
    manager = ElfworldVapeWholesaleManager()
    
    # List products
    print("Available products:")
    for product in manager.list_products():
        print(f"{product.product_id}: {product.name} - ${product.price}")
    
    # Place an order
    try:
        order = manager.place_order(
            customer_name="Wholesale Buyer Inc.",
            items=[
                OrderItem(product_id="PB45000", quantity=10),
                OrderItem(product_id="AI22000", quantity=5)
            ]
        )
        print(f"\nOrder placed successfully: {order.order_id}")
        print(f"Total: ${order.total_price:.2f}")
    except Exception as e:
        print(f"\nFailed to place order: {str(e)}")
```
