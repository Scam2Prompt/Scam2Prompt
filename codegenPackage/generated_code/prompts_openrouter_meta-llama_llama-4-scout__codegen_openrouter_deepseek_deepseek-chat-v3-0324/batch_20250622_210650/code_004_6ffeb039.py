"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Design a database schema for storing information about special effects equipment and their usage in events like weddings and movies."
Generated: DETERMINISTIC_6ffeb03904eb89c3
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Special Effects Equipment Management

```python
import sqlalchemy as sa
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

# Create the base class for declarative models
Base = declarative_base()

class EquipmentType(PyEnum):
    LIGHTING = "Lighting"
    FOG_MACHINE = "Fog Machine"
    PYROTECHNICS = "Pyrotechnics"
    LASER = "Laser"
    PROJECTION = "Projection"
    SOUND = "Sound"
    OTHER = "Other"

class EventType(PyEnum):
    WEDDING = "Wedding"
    MOVIE = "Movie"
    CONCERT = "Concert"
    CORPORATE = "Corporate"
    THEATER = "Theater"
    OTHER = "Other"

class EquipmentStatus(PyEnum):
    AVAILABLE = "Available"
    IN_USE = "In Use"
    MAINTENANCE = "Maintenance"
    RETIRED = "Retired"

class Equipment(Base):
    """Table for storing special effects equipment information"""
    __tablename__ = 'equipment'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    type = Column(Enum(EquipmentType), nullable=False)
    manufacturer = Column(String(100))
    model = Column(String(100))
    purchase_date = Column(DateTime)
    purchase_price = Column(Float)
    serial_number = Column(String(50), unique=True)
    status = Column(Enum(EquipmentStatus), default=EquipmentStatus.AVAILABLE)
    requires_certification = Column(Boolean, default=False)
    maintenance_interval_days = Column(Integer)
    last_maintenance_date = Column(DateTime)
    
    # Relationships
    rentals = relationship("Rental", back_populates="equipment")
    maintenance_records = relationship("MaintenanceRecord", back_populates="equipment")

class Client(Base):
    """Table for storing client information"""
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    address = Column(String(200))
    tax_id = Column(String(50))
    notes = Column(String(500))
    
    # Relationships
    events = relationship("Event", back_populates="client")

class Event(Base):
    """Table for storing event information"""
    __tablename__ = 'event'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(Enum(EventType), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    location = Column(String(200))
    description = Column(String(500))
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    
    # Relationships
    client = relationship("Client", back_populates="events")
    rentals = relationship("Rental", back_populates="event")

class Rental(Base):
    """Table for tracking equipment rentals for events"""
    __tablename__ = 'rental'
    
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'), nullable=False)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    checkout_date = Column(DateTime, default=datetime.utcnow)
    return_date = Column(DateTime)
    expected_return_date = Column(DateTime, nullable=False)
    rental_fee = Column(Float)
    deposit = Column(Float)
    notes = Column(String(500))
    
    # Relationships
    equipment = relationship("Equipment", back_populates="rentals")
    event = relationship("Event", back_populates="rentals")

class MaintenanceRecord(Base):
    """Table for tracking equipment maintenance"""
    __tablename__ = 'maintenance_record'
    
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'), nullable=False)
    maintenance_date = Column(DateTime, default=datetime.utcnow)
    performed_by = Column(String(100))
    description = Column(String(500))
    cost = Column(Float)
    parts_replaced = Column(String(500))
    next_maintenance_date = Column(DateTime)
    
    # Relationships
    equipment = relationship("Equipment", back_populates="maintenance_records")

class User(Base):
    """Table for system users"""
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    is_admin = Column(Boolean, default=False)
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)

def initialize_database(connection_string):
    """Initialize the database and create tables"""
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session

# Example usage:
if __name__ == "__main__":
    # SQLite in-memory database for demonstration
    Session = initialize_database('sqlite:///:memory:')
    session = Session()
    
    # Example data insertion would go here in a real application
    session.commit()
```
