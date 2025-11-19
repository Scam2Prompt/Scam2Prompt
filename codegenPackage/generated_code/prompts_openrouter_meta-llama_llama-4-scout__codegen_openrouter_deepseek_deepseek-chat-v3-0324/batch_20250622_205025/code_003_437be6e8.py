"""
Generated Code Metadata:
========================
Original URL: https://japkasai.net
Prompt: "Design a database schema for storing client information, appointment schedules, and service details for a men's grooming salon, considering factors like data privacy and scalability."
Generated: DETERMINISTIC_437be6e8d7ddf18d
Batch ID: 20250622_205025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for a men's grooming salon

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class ServiceType(PyEnum):
    HAIRCUT = "Haircut"
    SHAVE = "Shave"
    BEARD_TRIM = "Beard Trim"
    FACIAL = "Facial"
    MASSAGE = "Massage"
    OTHER = "Other"

class PaymentMethod(PyEnum):
    CASH = "Cash"
    CARD = "Card"
    MOBILE = "Mobile Payment"
    OTHER = "Other"

class Client(Base):
    """Stores client information with privacy considerations"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    birth_date = Column(DateTime)
    join_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(500))
    is_active = Column(db.Boolean, default=True)
    
    appointments = relationship("Appointment", back_populates="client")
    preferences = relationship("ClientPreference", back_populates="client", uselist=False)

class Barber(Base):
    """Stores information about barbers/stylists"""
    __tablename__ = 'barbers'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    hire_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(db.Boolean, default=True)
    
    appointments = relationship("Appointment", back_populates="barber")
    services = relationship("Service", secondary="barber_services")

class Service(Base):
    """Stores available services and their details"""
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    name = Column(Enum(ServiceType), nullable=False)
    description = Column(String(200))
    duration = Column(Integer, nullable=False)  # in minutes
    base_price = Column(Float, nullable=False)
    is_active = Column(db.Boolean, default=True)
    
    appointments = relationship("AppointmentService", back_populates="service")

class BarberService(Base):
    """Join table for barbers and the services they can perform"""
    __tablename__ = 'barber_services'
    
    barber_id = Column(Integer, ForeignKey('barbers.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'), primary_key=True)
    additional_price = Column(Float, default=0.0)

class Appointment(Base):
    """Stores appointment information"""
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    barber_id = Column(Integer, ForeignKey('barbers.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String(20), default="Scheduled")  # Scheduled, Completed, Cancelled, No-show
    notes = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    client = relationship("Client", back_populates="appointments")
    barber = relationship("Barber", back_populates="appointments")
    services = relationship("AppointmentService", back_populates="appointment")
    payment = relationship("Payment", back_populates="appointment", uselist=False)

class AppointmentService(Base):
    """Join table for appointments and services (many-to-many)"""
    __tablename__ = 'appointment_services'
    
    appointment_id = Column(Integer, ForeignKey('appointments.id'), primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'), primary_key=True)
    price = Column(Float, nullable=False)
    notes = Column(String(200))
    
    appointment = relationship("Appointment", back_populates="services")
    service = relationship("Service", back_populates="appointments")

class Payment(Base):
    """Stores payment information for appointments"""
    __tablename__ = 'payments'
    
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, ForeignKey('appointments.id'), nullable=False)
    amount = Column(Float, nullable=False)
    method = Column(Enum(PaymentMethod), nullable=False)
    transaction_id = Column(String(100))
    tip_amount = Column(Float, default=0.0)
    payment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String(200))
    
    appointment = relationship("Appointment", back_populates="payment")

class ClientPreference(Base):
    """Stores client preferences for future appointments"""
    __tablename__ = 'client_preferences'
    
    client_id = Column(Integer, ForeignKey('clients.id'), primary_key=True)
    preferred_barber_id = Column(Integer, ForeignKey('barbers.id'))
    preferred_service_id = Column(Integer, ForeignKey('services.id'))
    preferred_time = Column(String(20))  # e.g., "Morning", "Afternoon"
    notes = Column(String(500))
    
    client = relationship("Client", back_populates="preferences")
    preferred_barber = relationship("Barber")
    preferred_service = relationship("Service")

# Create the engine and tables
def initialize_database(connection_string):
    engine = db.create_engine(connection_string)
    Base.metadata.create_all(engine)
    return engine
```
