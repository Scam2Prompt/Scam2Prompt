"""
Generated Code Metadata:
========================
Original URL: https://lavanderiacallezaragoza.com
Prompt: "Design a database schema for a laundry service business, incorporating customer, service, and payment information, as seen on lavanderiacallezaragoza.com."
Generated: DETERMINISTIC_a8438f5deb29f92c
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for a laundry service business
# Using SQLAlchemy ORM for Python

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class ServiceType(PyEnum):
    WASH_DRY_FOLD = "Wash, Dry & Fold"
    DRY_CLEANING = "Dry Cleaning"
    IRONING = "Ironing"
    SPECIAL = "Special Care"

class PaymentMethod(PyEnum):
    CASH = "Cash"
    CARD = "Credit/Debit Card"
    BANK_TRANSFER = "Bank Transfer"
    ONLINE = "Online Payment"

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    orders = relationship("Order", back_populates="customer")
    payments = relationship("Payment", back_populates="customer")

class Service(Base):
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    name = Column(Enum(ServiceType), nullable=False)
    description = Column(String(200))
    price_per_unit = Column(Float, nullable=False)
    unit = Column(String(20), default="kg")
    estimated_time = Column(Integer)  # in hours
    
    order_items = relationship("OrderItem", back_populates="service")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    pickup_date = Column(DateTime)
    delivery_date = Column(DateTime)
    status = Column(String(50), default="Pending")
    special_instructions = Column(String(300))
    
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
    payment = relationship("Payment", uselist=False, back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")
    service = relationship("Service", back_populates="order_items")

class Payment(Base):
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    amount = Column(Float, nullable=False)
    method = Column(Enum(PaymentMethod), nullable=False)
    transaction_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String(50), default="Pending")
    reference = Column(String(100))
    
    order = relationship("Order", back_populates="payment")
    customer = relationship("Customer", back_populates="payments")

def init_db(connection_string):
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage:
# db_session = init_db('sqlite:///laundry_service.db')
```
