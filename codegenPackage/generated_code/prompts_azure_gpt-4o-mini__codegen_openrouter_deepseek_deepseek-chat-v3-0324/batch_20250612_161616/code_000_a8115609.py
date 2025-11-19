"""
Generated Code Metadata:
========================
Original URL: https://purebite.fi
Prompt: Generate a code snippet for a restaurant management system that includes features for online table reservations and takeout orders, inspired by the services offered by Purebite.
Generated: DETERMINISTIC_a81156092e0796ed
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_management_system.py
from datetime import datetime, timedelta
from typing import List, Optional, Dict
import json
import uuid
from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    PREPARING = "Preparing"
    READY = "Ready for Pickup"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class ReservationStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Table:
    def __init__(self, table_id: int, capacity: int, location: str):
        self.table_id = table_id
        self.capacity = capacity
        self.location = location
        self.is_available = True

    def to_dict(self) -> Dict:
        return {
            "table_id": self.table_id,
            "capacity": self.capacity,
            "location": self.location,
            "is_available": self.is_available
        }


class MenuItem:
    def __init__(self, item_id: int, name: str, description: str, price: float, category: str):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def to_dict(self) -> Dict:
        return {
            "item_id": self.item_id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category
        }


class Customer:
    def __init__(self, customer_id: str, name: str, phone: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self) -> Dict:
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int, special_instructions: str = ""):
        self.menu_item = menu_item
        self.quantity = quantity
        self.special_instructions = special_instructions

    def to_dict(self) -> Dict:
        return {
            "menu_item": self.menu_item.to_dict(),
            "quantity": self.quantity,
            "special_instructions": self.special_instructions
        }


class Order:
    def __init__(self, order_id: str, customer: Customer, items: List[OrderItem], 
                 order_type: str, status: OrderStatus = OrderStatus.PENDING):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.order_type = order_type  # "takeout" or "dine-in"
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    def calculate_total(self) -> float:
        return sum(item.menu_item.price * item.quantity for item in self.items)

    def to_dict(self) -> Dict:
        return {
            "order_id": self.order_id,
            "customer": self.customer.to_dict(),
            "items": [item.to_dict() for item in self.items],
            "order_type": self.order_type,
            "status": self.status.value,
            "total": self.calculate_total(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class Reservation:
    def __init__(self, reservation_id: str, customer: Customer, table: Table, 
                 party_size: int, reservation_time: datetime, 
                 status: ReservationStatus = ReservationStatus.PENDING):
        self.reservation_id = reservation_id
        self.customer = customer
        self.table = table
        self.party_size = party_size
        self.reservation_time = reservation_time
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_status(self, new_status: ReservationStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict:
        return {
            "reservation_id": self.reservation_id,
            "customer": self.customer.to_dict(),
            "table": self.table.to_dict(),
            "party_size": self.party_size,
            "reservation_time": self.reservation_time.isoformat(),
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }


class RestaurantManagementSystem:
    def __init__(self):
        self.tables: List[Table] = []
        self.menu_items: List[MenuItem] = []
        self.customers: List[Customer] = []
        self.orders: List[Order] = []
        self.reservations: List[Reservation] = []
        self.load_initial_data()

    def load_initial_data(self):
        # Sample initial data
        self.tables = [
            Table(1, 4, "Window"),
            Table(2, 2, "Bar"),
            Table(3, 6, "Patio"),
            Table(4, 8, "Private Room")
        ]
        
        self.menu_items = [
            MenuItem(1, "Burger", "Classic beef burger", 12.99, "Main"),
            MenuItem(2, "Salad", "Fresh garden salad", 8.99, "Starter"),
            MenuItem(3, "Pizza", "Margherita pizza", 14.99, "Main"),
            MenuItem(4, "Ice Cream", "Vanilla ice cream", 5.99, "Dessert")
        ]

    def add_customer(self, name: str, phone: str, email: str) -> Customer:
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, phone, email)
        self.customers.append(customer)
        return customer

    def find_customer_by_email(self, email: str) -> Optional[Customer]:
        for customer in self.customers:
            if customer.email.lower() == email.lower():
                return customer
        return None

    def get_available_tables(self, party_size: int, time: datetime) -> List[Table]:
        available_tables = []
        for table in self.tables:
            if table.capacity >= party_size and table.is_available:
                # Check if table is reserved at the requested time
                conflicting_reservations = [
                    r for r in self.reservations 
                    if r.table.table_id == table.table_id 
                    and abs((r.reservation_time - time).total_seconds()) < 7200  # 2-hour window
                    and r.status != ReservationStatus.CANCELLED
                ]
                if not conflicting_reservations:
                    available_tables.append(table)
        return available_tables

    def create_reservation(self, customer: Customer, party_size: int, 
                          reservation_time: datetime, table_preference: Optional[int] = None) -> Optional[Reservation]:
        available_tables = self.get_available_tables(party_size, reservation_time)
        
        if not available_tables:
            return None
            
        # Try to honor table preference if specified
        if table_preference:
            preferred_table = next((t for t in available_tables if t.table_id == table_preference), None)
            if preferred_table:
                selected_table = preferred_table
            else:
                selected_table = available_tables[0]
        else:
            selected_table = available_tables[0]
            
        reservation_id = str(uuid.uuid4())
        reservation = Reservation(reservation_id, customer, selected_table, 
                                 party_size, reservation_time)
        self.reservations.append(reservation)
        return reservation

    def cancel_reservation(self, reservation_id: str) -> bool:
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.update_status(ReservationStatus.CANCELLED)
                return True
        return False

    def create_order(self, customer: Customer, items: List[OrderItem], order_type: str) -> Order:
        order_id = str(uuid.uuid4())
        order = Order(order_id, customer, items, order_type)
        self.orders.append(order)
        return order

    def update_order_status(self, order_id: str, new_status: OrderStatus) -> bool:
        for order in self.orders:
            if order.order_id == order_id:
                order.update_status(new_status)
                return True
        return False

    def get_menu_items_by_category(self, category: str) -> List[MenuItem]:
        return [item for item in self.menu_items if item.category.lower() == category.lower()]

    def save_data_to_file(self, filename: str = "restaurant_data.json"):
        data = {
            "tables": [table.to_dict() for table in self.t
