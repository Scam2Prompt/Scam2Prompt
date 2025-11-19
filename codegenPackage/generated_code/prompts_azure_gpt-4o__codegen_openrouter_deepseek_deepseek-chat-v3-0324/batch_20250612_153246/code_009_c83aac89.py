"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write code to generate a customer management system for tracking orders from private companies, NGOs, government offices, and learning institutions, as described on Sanuri Supplies' site.
Generated: DETERMINISTIC_c83aac89292a086a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Customer Management System for Sanuri Supplies
This system tracks orders from various customer types including private companies,
NGOs, government offices, and learning institutions.
"""

from datetime import datetime
from enum import Enum
import json
import os
from typing import Dict, List, Optional, Union

class CustomerType(Enum):
    """Enum representing different customer types."""
    PRIVATE_COMPANY = "Private Company"
    NGO = "NGO"
    GOVERNMENT = "Government Office"
    LEARNING_INSTITUTION = "Learning Institution"

class OrderStatus(Enum):
    """Enum representing different order statuses."""
    PENDING = "Pending"
    PROCESSING = "Processing"
    SHIPPED = "Shipped"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

class Customer:
    """Class representing a customer."""
    
    def __init__(
        self,
        customer_id: str,
        name: str,
        customer_type: CustomerType,
        contact_person: str,
        email: str,
        phone: str,
        address: str,
        tax_id: Optional[str] = None
    ):
        """
        Initialize a customer.
        
        Args:
            customer_id: Unique identifier for the customer
            name: Name of the customer
            customer_type: Type of customer (from CustomerType enum)
            contact_person: Name of the contact person
            email: Email address
            phone: Phone number
            address: Physical address
            tax_id: Tax identification number (optional)
        """
        self.customer_id = customer_id
        self.name = name
        self.customer_type = customer_type
        self.contact_person = contact_person
        self.email = email
        self.phone = phone
        self.address = address
        self.tax_id = tax_id
        self.orders: List[Order] = []
    
    def add_order(self, order: 'Order') -> None:
        """Add an order to this customer."""
        self.orders.append(order)
    
    def to_dict(self) -> Dict:
        """Convert customer data to dictionary for serialization."""
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "customer_type": self.customer_type.value,
            "contact_person": self.contact_person,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "tax_id": self.tax_id,
            "orders": [order.to_dict() for order in self.orders]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Customer':
        """Create a Customer instance from dictionary data."""
        customer = cls(
            customer_id=data["customer_id"],
            name=data["name"],
            customer_type=CustomerType(data["customer_type"]),
            contact_person=data["contact_person"],
            email=data["email"],
            phone=data["phone"],
            address=data["address"],
            tax_id=data.get("tax_id")
        )
        customer.orders = [Order.from_dict(order_data) for order_data in data.get("orders", [])]
        return customer

class OrderItem:
    """Class representing an item in an order."""
    
    def __init__(self, product_id: str, name: str, quantity: int, unit_price: float):
        """
        Initialize an order item.
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            quantity: Quantity ordered
            unit_price: Price per unit
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price
    
    @property
    def total_price(self) -> float:
        """Calculate total price for this item."""
        return self.quantity * self.unit_price
    
    def to_dict(self) -> Dict:
        """Convert order item data to dictionary for serialization."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "quantity": self.quantity,
            "unit_price": self.unit_price
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'OrderItem':
        """Create an OrderItem instance from dictionary data."""
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            quantity=data["quantity"],
            unit_price=data["unit_price"]
        )

class Order:
    """Class representing an order."""
    
    def __init__(
        self,
        order_id: str,
        customer_id: str,
        items: List[OrderItem],
        order_date: Optional[datetime] = None,
        status: OrderStatus = OrderStatus.PENDING,
        notes: Optional[str] = None
    ):
        """
        Initialize an order.
        
        Args:
            order_id: Unique identifier for the order
            customer_id: ID of the customer who placed the order
            items: List of items in the order
            order_date: Date when order was placed (defaults to now)
            status: Current status of the order
            notes: Additional notes about the order
        """
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.order_date = order_date if order_date else datetime.now()
        self.status = status
        self.notes = notes
    
    @property
    def total_amount(self) -> float:
        """Calculate total amount for the order."""
        return sum(item.total_price for item in self.items)
    
    def update_status(self, new_status: OrderStatus) -> None:
        """Update the status of the order."""
        self.status = new_status
    
    def to_dict(self) -> Dict:
        """Convert order data to dictionary for serialization."""
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "items": [item.to_dict() for item in self.items],
            "order_date": self.order_date.isoformat(),
            "status": self.status.value,
            "notes": self.notes,
            "total_amount": self.total_amount
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Order':
        """Create an Order instance from dictionary data."""
        return cls(
            order_id=data["order_id"],
            customer_id=data["customer_id"],
            items=[OrderItem.from_dict(item_data) for item_data in data["items"]],
            order_date=datetime.fromisoformat(data["order_date"]),
            status=OrderStatus(data["status"]),
            notes=data.get("notes")
        )

class CustomerManager:
    """Class managing customer and order data."""
    
    def __init__(self, data_file: str = "customer_data.json"):
        """
        Initialize the customer manager.
        
        Args:
            data_file: Path to the JSON file for data persistence
        """
        self.data_file = data_file
        self.customers: Dict[str, Customer] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load customer data from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    data = json.load(file)
                    self.customers = {
                        cust_id: Customer.from_dict(cust_data)
                        for cust_id, cust_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Error loading customer data: {str(e)}")
    
    def _save_data(self) -> None:
        """Save customer data to the JSON file."""
        try:
            with open(self.data_file, "w") as file:
                json.dump(
                    {cust_id: cust.to_dict() for cust_id, cust in self.customers.items()},
                    file,
                    indent=2
                )
        except IOError as e:
            raise RuntimeError(f"Error saving customer data: {str(e)}")
    
    def add_customer(self, customer: Customer) -> None:
        """Add a new customer to the system."""
        if customer.customer_id in self.customers:
            raise ValueError(f"Customer with ID {customer.customer_id} already exists")
        self.customers[customer.customer_id] = customer
        self._save_data()
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Retrieve a customer by ID."""
        return self.customers.get(customer_id)
    
    def update_customer(self, customer_id: str, **kwargs) -> None:
        """Update customer information."""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError(f"Customer with ID {customer_id} not found")
        
        for key, value in kwargs.items():
            if hasattr(customer, key):
                setattr(customer, key, value)
        
        self._save_data()
    
    def delete_customer(self, customer_id: str) -> None:
        """Delete a customer from the system."""
        if customer_id not in self.customers:
            raise ValueError(f"Customer with ID {customer_id} not found")
        del self.customers[customer_id]
        self._save_data()
    
    def add_order(self, customer_id: str, order: Order) -> None:
        """Add an order to a customer
