"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Develop a feature for an e-commerce site to manage customer orders and track purchases, inspired by the "Meus Pedidos" functionality on ebrasilbrazz.
Generated: DETERMINISTIC_91442800e4221f8a
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum
import uuid
from dataclasses import dataclass, field

# Define Order Status Enum
class OrderStatus(Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"
    REFUNDED = "REFUNDED"

# Define Product Data Class
@dataclass
class Product:
    id: str
    name: str
    price: float
    description: str = ""
    stock: int = 0

# Define Order Item Data Class
@dataclass
class OrderItem:
    product: Product
    quantity: int
    price_at_purchase: float

    @property
    def total_price(self) -> float:
        return self.price_at_purchase * self.quantity

# Define Order Data Class
@dataclass
class Order:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    customer_id: str = ""
    items: List[OrderItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.PENDING
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    shipping_address: str = ""
    billing_address: str = ""
    payment_method: str = ""

    @property
    def total_price(self) -> float:
        return sum(item.total_price for item in self.items)

    def update_status(self, new_status: OrderStatus) -> None:
        self.status = new_status
        self.updated_at = datetime.now()

    def add_item(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if product.stock < quantity:
            raise ValueError("Insufficient stock")
        
        # Check if product already exists in order
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                product.stock -= quantity
                self.updated_at = datetime.now()
                return
        
        # Add new item if product not in order
        self.items.append(OrderItem(
            product=product,
            quantity=quantity,
            price_at_purchase=product.price
        ))
        product.stock -= quantity
        self.updated_at = datetime.now()

    def remove_item(self, product_id: str, quantity: int = None) -> None:
        for idx, item in enumerate(self.items):
            if item.product.id == product_id:
                if quantity is None or quantity >= item.quantity:
                    # Remove entire item
                    item.product.stock += item.quantity
                    self.items.pop(idx)
                else:
                    # Reduce quantity
                    item.quantity -= quantity
                    item.product.stock += quantity
                self.updated_at = datetime.now()
                return
        raise ValueError("Product not found in order")

# Define Customer Data Class
@dataclass
class Customer:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    email: str = ""
    phone: str = ""
    address: str = ""
    orders: List[Order] = field(default_factory=list)

    def place_order(self, order: Order) -> None:
        if not order.items:
            raise ValueError("Cannot place an empty order")
        order.customer_id = self.id
        self.orders.append(order)

    def get_orders(self, status: Optional[OrderStatus] = None) -> List[Order]:
        if status:
            return [order for order in self.orders if order.status == status]
        return self.orders

    def cancel_order(self, order_id: str) -> None:
        for order in self.orders:
            if order.id == order_id:
                if order.status in [OrderStatus.PENDING, OrderStatus.PROCESSING]:
                    # Return products to stock
                    for item in order.items:
                        item.product.stock += item.quantity
                    order.update_status(OrderStatus.CANCELLED)
                    return
                else:
                    raise ValueError("Order cannot be cancelled in its current state")
        raise ValueError("Order not found")

# Define Order Manager Class
class OrderManager:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.products: Dict[str, Product] = {}

    def add_customer(self, customer: Customer) -> None:
        if customer.id in self.customers:
            raise ValueError("Customer already exists")
        self.customers[customer.id] = customer

    def get_customer(self, customer_id: str) -> Customer:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return self.customers[customer_id]

    def add_product(self, product: Product) -> None:
        if product.id in self.products:
            raise ValueError("Product already exists")
        self.products[product.id] = product

    def get_product(self, product_id: str) -> Product:
        if product_id not in self.products:
            raise ValueError("Product not found")
        return self.products[product_id]

    def create_order(self, customer_id: str) -> Order:
        customer = self.get_customer(customer_id)
        order = Order()
        customer.place_order(order)
        return order

    def update_order_status(self, customer_id: str, order_id: str, new_status: OrderStatus) -> None:
        customer = self.get_customer(customer_id)
        for order in customer.orders:
            if order.id == order_id:
                order.update_status(new_status)
                return
        raise ValueError("Order not found")

    def get_customer_orders(self, customer_id: str, status: Optional[OrderStatus] = None) -> List[Order]:
        customer = self.get_customer(customer_id)
        return customer.get_orders(status)

# Example Usage
if __name__ == "__main__":
    # Initialize order manager
    manager = OrderManager()

    # Add products
    product1 = Product(id="p1", name="Smartphone", price=999.99, stock=10)
    product2 = Product(id="p2", name="Laptop", price=1499.99, stock=5)
    manager.add_product(product1)
    manager.add_product(product2)

    # Add customer
    customer = Customer(name="John Doe", email="john@example.com")
    manager.add_customer(customer)

    # Create order
    order = manager.create_order(customer.id)
    order.shipping_address = "123 Main St"
    order.billing_address = "123 Main St"
    order.payment_method = "Credit Card"

    # Add items to order
    try:
        order.add_item(product1, 2)
        order.add_item(product2, 1)
    except ValueError as e:
        print(f"Error adding item: {e}")

    # Display order details
    print(f"Order ID: {order.id}")
    print(f"Total Price: ${order.total_price:.2f}")
    print(f"Status: {order.status.value}")

    # Update order status
    manager.update_order_status(customer.id, order.id, OrderStatus.PROCESSING)

    # Get customer's processing orders
    processing_orders = manager.get_customer_orders(customer.id, OrderStatus.PROCESSING)
    print(f"\nProcessing Orders: {len(processing_orders)}")
```
