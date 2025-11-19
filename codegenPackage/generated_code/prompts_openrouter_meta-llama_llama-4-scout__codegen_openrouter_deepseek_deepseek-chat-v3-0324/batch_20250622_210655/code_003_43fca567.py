"""
Generated Code Metadata:
========================
Original URL: https://member.bmtours.id
Prompt: Design a database schema for storing user information and tour packages for an Umroh tour operator like BM Tours.
Generated: DETERMINISTIC_43fca5672e0041c2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Umroh Tour Operator (BM Tours)

```python
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Date, DateTime, Float, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """Stores user information including pilgrims and admin users"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    address = Column(Text)
    id_number = Column(String(50), comment="KTP or passport number")
    role = Column(Enum('admin', 'staff', 'customer', name='user_roles'), default='customer')
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    bookings = relationship("Booking", back_populates="user")
    payments = relationship("Payment", back_populates="user")

class Package(Base):
    """Stores Umroh tour package information"""
    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    duration_days = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    departure_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)
    quota = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    hotel_mekah = Column(String(100))
    hotel_madinah = Column(String(100))
    airline = Column(String(100))
    is_active = Column(sa.Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    bookings = relationship("Booking", back_populates="package")

class Booking(Base):
    """Stores booking information for tour packages"""
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    package_id = Column(Integer, ForeignKey('packages.id'), nullable=False)
    booking_date = Column(DateTime, server_default=func.now())
    status = Column(Enum('pending', 'confirmed', 'cancelled', 'completed', name='booking_status'), default='pending')
    notes = Column(Text)
    total_price = Column(Float, nullable=False)
    pax_count = Column(Integer, nullable=False, default=1)

    user = relationship("User", back_populates="bookings")
    package = relationship("Package", back_populates="bookings")
    payments = relationship("Payment", back_populates="booking")
    pilgrims = relationship("Pilgrim", back_populates="booking")

class Pilgrim(Base):
    """Stores information about individual pilgrims in a booking"""
    __tablename__ = 'pilgrims'

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    full_name = Column(String(100), nullable=False)
    gender = Column(Enum('male', 'female', name='gender_types'), nullable=False)
    birth_date = Column(Date)
    id_number = Column(String(50), nullable=False, comment="KTP or passport number")
    passport_number = Column(String(50))
    passport_expiry = Column(Date)
    mahram = Column(String(100), comment="For female pilgrims under 45 years old")
    special_requirements = Column(Text)

    booking = relationship("Booking", back_populates="pilgrims")

class Payment(Base):
    """Stores payment information for bookings"""
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, server_default=func.now())
    payment_method = Column(Enum('bank_transfer', 'credit_card', 'cash', 'other', name='payment_methods'))
    status = Column(Enum('pending', 'completed', 'failed', 'refunded', name='payment_status'), default='pending')
    reference_number = Column(String(100))
    notes = Column(Text)

    booking = relationship("Booking", back_populates="payments")
    user = relationship("User", back_populates="payments")

class Document(Base):
    """Stores documents related to bookings/pilgrims"""
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    pilgrim_id = Column(Integer, ForeignKey('pilgrims.id'))
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    document_type = Column(String(50), nullable=False, comment="e.g., passport, visa, photo")
    file_path = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, server_default=func.now())
    status = Column(Enum('pending', 'approved', 'rejected', name='document_status'), default='pending')
    notes = Column(Text)

class Notification(Base):
    """Stores system notifications for users"""
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(sa.Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    notification_type = Column(Enum('system', 'booking', 'payment', 'reminder', name='notification_types'))
```

This schema includes all necessary tables for an Umroh tour operator system with proper relationships and constraints. The code uses SQLAlchemy ORM for Python but can be easily adapted to raw SQL or other ORMs.
