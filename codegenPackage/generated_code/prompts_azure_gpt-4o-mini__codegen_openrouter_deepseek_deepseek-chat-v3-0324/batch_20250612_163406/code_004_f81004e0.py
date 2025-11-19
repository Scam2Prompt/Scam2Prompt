"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Design a database schema for storing client information, appointment details, and service records for an art makeup salon, focusing on scalability and security.
Generated: DETERMINISTIC_f81004e042056219
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Art Makeup Salon

```python
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from passlib.hash import bcrypt

Base = declarative_base()

class Client(Base):
    """Stores client personal information and contact details"""
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    birth_date = Column(DateTime)
    registration_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="client")
    service_records = relationship("ServiceRecord", back_populates="client")
    
    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.first_name} {self.last_name}')>"

class Artist(Base):
    """Stores makeup artist information"""
    __tablename__ = 'artists'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    specialization = Column(String(100))
    hire_date = Column(DateTime, default=datetime.utcnow)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="artist")
    service_records = relationship("ServiceRecord", back_populates="artist")
    
    def __repr__(self):
        return f"<Artist(id={self.id}, name='{self.first_name} {self.last_name}')>"

class Service(Base):
    """Stores available makeup services"""
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration_minutes = Column(Integer, nullable=False)
    base_price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    appointments = relationship("Appointment", back_populates="service")
    service_records = relationship("ServiceRecord", back_populates="service")
    
    def __repr__(self):
        return f"<Service(id={self.id}, name='{self.name}')>"

class Appointment(Base):
    """Stores booking information for client appointments"""
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    notes = Column(Text)
    status = Column(String(20), default='scheduled')  # scheduled, completed, cancelled, no-show
    
    # Relationships
    client = relationship("Client", back_populates="appointments")
    artist = relationship("Artist", back_populates="appointments")
    service = relationship("Service", back_populates="appointments")
    
    def __repr__(self):
        return f"<Appointment(id={self.id}, client_id={self.client_id}, time={self.appointment_time})>"

class ServiceRecord(Base):
    """Stores completed service details and history"""
    __tablename__ = 'service_records'
    
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    appointment_id = Column(Integer, ForeignKey('appointments.id'))
    service_date = Column(DateTime, default=datetime.utcnow)
    actual_duration = Column(Integer)  # in minutes
    final_price = Column(Float, nullable=False)
    notes = Column(Text)
    feedback = Column(Text)
    rating = Column(Integer)  # 1-5 scale
    
    # Relationships
    client = relationship("Client", back_populates="service_records")
    artist = relationship("Artist", back_populates="service_records")
    service = relationship("Service", back_populates="service_records")
    
    def __repr__(self):
        return f"<ServiceRecord(id={self.id}, client_id={self.client_id}, service_id={self.service_id})>"

class User(Base):
    """Stores system user accounts for salon staff"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    last_login = Column(DateTime)
    
    def set_password(self, password):
        """Hashes and stores the password"""
        self.password_hash = bcrypt.hash(password)
    
    def check_password(self, password):
        """Verifies the password against the stored hash"""
        return bcrypt.verify(password, self.password_hash)
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

class AuditLog(Base):
    """Tracks important system events for security and accountability"""
    __tablename__ = 'audit_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    action = Column(String(50), nullable=False)
    table_name = Column(String(50))
    record_id = Column(Integer)
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(Text)
    
    def __repr__(self):
        return f"<AuditLog(id={self.id}, action='{self.action}', timestamp={self.timestamp})>"

def init_db(connection_string, echo=False):
    """Initialize the database connection and create tables"""
    engine = create_engine(connection_string, echo=echo)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage:
# DATABASE_URL = "postgresql://username:password@localhost/salon_db"
# Session = init_db(DATABASE_URL)
```
