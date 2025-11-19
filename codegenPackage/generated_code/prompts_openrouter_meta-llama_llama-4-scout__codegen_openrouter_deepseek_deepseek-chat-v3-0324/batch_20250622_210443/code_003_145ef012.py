"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Design a database schema to store information about cargo shipments, clients, and transportation services, inspired by the operations of OPC."
Generated: DETERMINISTIC_145ef0126e17c50f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Cargo Shipment Management System

```python
import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class ShipmentStatus(PyEnum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    DELAYED = "delayed"

class PaymentStatus(PyEnum):
    UNPAID = "unpaid"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    REFUNDED = "refunded"

class Client(Base):
    """Represents a client/customer who ships cargo"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    tax_id = Column(String(50), unique=True)
    registration_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    shipments = relationship("Shipment", back_populates="client")

class TransportationService(Base):
    """Represents a transportation service provider"""
    __tablename__ = 'transportation_services'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    service_type = Column(String(50))
    rate_per_km = Column(Float)
    is_active = Column(Boolean, default=True)
    
    shipments = relationship("Shipment", back_populates="transport_service")

class Shipment(Base):
    """Represents a cargo shipment"""
    __tablename__ = 'shipments'
    
    id = Column(Integer, primary_key=True)
    tracking_number = Column(String(50), unique=True, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    transport_service_id = Column(Integer, ForeignKey('transportation_services.id'))
    origin = Column(String(200), nullable=False)
    destination = Column(String(200), nullable=False)
    weight = Column(Float, nullable=False)  # in kg
    volume = Column(Float)  # in cubic meters
    contents = Column(String(500))
    status = Column(Enum(ShipmentStatus), default=ShipmentStatus.PENDING)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.UNPAID)
    estimated_delivery = Column(DateTime)
    actual_delivery = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    client = relationship("Client", back_populates="shipments")
    transport_service = relationship("TransportationService", back_populates="shipments")
    documents = relationship("ShipmentDocument", back_populates="shipment")
    payments = relationship("Payment", back_populates="shipment")
    tracking_events = relationship("TrackingEvent", back_populates="shipment")

class ShipmentDocument(Base):
    """Represents documents associated with a shipment"""
    __tablename__ = 'shipment_documents'
    
    id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'), nullable=False)
    document_type = Column(String(50), nullable=False)
    file_path = Column(String(255), nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(200))
    
    shipment = relationship("Shipment", back_populates="documents")

class Payment(Base):
    """Represents payments made for shipments"""
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, default=datetime.utcnow)
    payment_method = Column(String(50))
    transaction_id = Column(String(100))
    notes = Column(String(200))
    
    shipment = relationship("Shipment", back_populates="payments")

class TrackingEvent(Base):
    """Represents tracking events for shipments"""
    __tablename__ = 'tracking_events'
    
    id = Column(Integer, primary_key=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'), nullable=False)
    event_type = Column(String(50), nullable=False)
    location = Column(String(200))
    timestamp = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(200))
    
    shipment = relationship("Shipment", back_populates="tracking_events")

def initialize_database(connection_string):
    """Initialize the database and create tables"""
    try:
        engine = db.create_engine(connection_string)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session
    except Exception as e:
        raise Exception(f"Failed to initialize database: {str(e)}")
```
