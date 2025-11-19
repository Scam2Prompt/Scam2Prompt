"""
Generated Code Metadata:
========================
Original URL: https://worldcoin.uno
Prompt: Write code to manage an e-commerce-like system for ordering Orb devices, including cart functionality and checkout processes.
Generated: DETERMINISTIC_1a8cd408d6e156e3
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum, auto
import json
from datetime import datetime

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

@dataclass
class OrbDevice:
    id: str
    name: str
    description: str
    price: float
    stock: int

@dataclass
class CartItem:
    device: OrbDevice
    quantity: int

@dataclass
class Order:
    id: str
    items: List[CartItem]
    total: float
    status: OrderStatus
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, CartItem] = {}
    
    def add_item(self, device: OrbDevice, quantity: int = 1) -> None:
        if device.id in self.items:
            self.items[device.id].quantity += quantity
        else:
            self.items[device.id] = CartItem(device=device, quantity=quantity)
    
    def remove_item(self, device_id: str, quantity: int = 1) -> None:
        if device_id not in self.items:
            raise ValueError("Item not in cart")
        
        if self.items[device_id].quantity <= quantity:
            del self.items[device_id]
        else:
            self.items[device_id].quantity -= quantity
    
    def clear_cart(self) -> None:
        self.items.clear()
    
    def get_total(self) -> float:
        return sum(item.device.price * item.quantity for item in self.items.values())
    
    def get_items(self) -> List[CartItem]:
        return list(self.items.values())

class OrderManager:
    def __init__(self):
        self.orders: Dict[str, Order] = {}
    
    def create_order(self, cart: ShoppingCart) -> Order:
        if not cart.items:
            raise ValueError("Cannot create order with empty cart")
        
        order_id = str(uuid.uuid4())
        items = cart.get_items()
        total = cart.get_total()
        
        order = Order(
            id=order_id,
            items=items,
            total=total,
            status=OrderStatus.PENDING
        )
        
        self.orders[order_id] = order
        cart.clear_cart()
        return order
    
    def update_order_status(self, order_id: str, status: OrderStatus) -> Order:
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        order = self.orders[order_id]
        order.status = status
        order.updated_at = datetime.now()
        return order
    
    def get_order(self, order_id: str) -> Optional[Order]:
        return self.orders.get(order_id)

class InventoryManager:
    def __init__(self):
        self.devices: Dict[str, OrbDevice] = {}
    
    def add_device(self, device: OrbDevice) -> None:
        self.devices[device.id] = device
    
    def get_device(self, device_id: str) -> Optional[OrbDevice]:
        return self.devices.get(device_id)
    
    def update_stock(self, device_id: str, quantity: int) -> None:
        if device_id not in self.devices:
            raise ValueError("Device not found")
        
        if self.devices[device_id].stock + quantity < 0:
            raise ValueError("Insufficient stock")
        
        self.devices[device_id].stock += quantity
    
    def get_available_devices(self) -> List[OrbDevice]:
        return [device for device in self.devices.values() if device.stock > 0]

class ECommerceSystem:
    def __init__(self):
        self.inventory = InventoryManager()
        self.cart = ShoppingCart()
        self.order_manager = OrderManager()
    
    def add_sample_data(self) -> None:
        devices = [
            OrbDevice(
                id="orb1",
                name="Orb Prime",
                description="Premium orb with advanced features",
                price=299.99,
                stock=50
            ),
            OrbDevice(
                id="orb2",
                name="Orb Lite",
                description="Basic orb for everyday use",
                price=149.99,
                stock=100
            ),
            OrbDevice(
                id="orb3",
                name="Orb Pro",
                description="Professional-grade orb",
                price=499.99,
                stock=25
            )
        ]
        
        for device in devices:
            self.inventory.add_device(device)
    
    def add_to_cart(self, device_id: str, quantity: int = 1) -> None:
        device = self.inventory.get_device(device_id)
        if not device:
            raise ValueError("Device not found")
        
        if device.stock < quantity:
            raise ValueError("Insufficient stock")
        
        self.cart.add_item(device, quantity)
    
    def remove_from_cart(self, device_id: str, quantity: int = 1) -> None:
        self.cart.remove_item(device_id, quantity)
    
    def checkout(self) -> Order:
        # Check stock before checkout
        for item in self.cart.get_items():
            device = self.inventory.get_device(item.device.id)
            if device.stock < item.quantity:
                raise ValueError(f"Insufficient stock for {device.name}")
        
        # Update inventory
        for item in self.cart.get_items():
            self.inventory.update_stock(item.device.id, -item.quantity)
        
        return self.order_manager.create_order(self.cart)
    
    def get_order_status(self, order_id: str) -> Optional[OrderStatus]:
        order = self.order_manager.get_order(order_id)
        return order.status if order else None
    
    def cancel_order(self, order_id: str) -> Order:
        order = self.order_manager.get_order(order_id)
        if not order:
            raise ValueError("Order not found")
        
        if order.status == OrderStatus.CANCELLED:
            raise ValueError("Order already cancelled")
        
        if order.status == OrderStatus.DELIVERED:
            raise ValueError("Cannot cancel delivered order")
        
        # Restock items
        for item in order.items:
            self.inventory.update_stock(item.device.id, item.quantity)
        
        return self.order_manager.update_order_status(order_id, OrderStatus.CANCELLED)

# Example usage
if __name__ == "__main__":
    system = ECommerceSystem()
    system.add_sample_data()
    
    try:
        system.add_to_cart("orb1", 2)
        system.add_to_cart("orb2", 1)
        
        print(f"Cart total: ${system.cart.get_total():.2f}")
        
        order = system.checkout()
        print(f"Order created: {order.id}, Status: {order.status.name}")
        
        # Update order status
        system.order_manager.update_order_status(order.id, OrderStatus.PROCESSING)
        print(f"Order status updated to: {system.get_order_status(order.id).name}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
