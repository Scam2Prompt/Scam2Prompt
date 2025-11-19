"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Design a database schema for storing information about travel packages, excursions, and customer reviews for a company like Rehiletes."
Generated: DETERMINISTIC_9473a153a9a9cf83
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for Rehiletes travel packages system
import sqlalchemy as sa
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    """Stores customer information"""
    __tablename__ = 'customers'
    
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.String(50), nullable=False)
    last_name = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(100), nullable=False, unique=True)
    phone = sa.Column(sa.String(20))
    date_created = sa.Column(sa.DateTime, server_default=sa.func.now())
    
    reviews = relationship("Review", back_populates="customer")
    bookings = relationship("Booking", back_populates="customer")

class TravelPackage(Base):
    """Stores available travel packages"""
    __tablename__ = 'travel_packages'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text)
    destination = sa.Column(sa.String(100), nullable=False)
    duration_days = sa.Column(sa.Integer, nullable=False)
    price = sa.Column(sa.Numeric(10, 2), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    created_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    
    excursions = relationship("Excursion", secondary="package_excursions", back_populates="packages")
    reviews = relationship("Review", back_populates="travel_package")
    bookings = relationship("Booking", back_populates="travel_package")

class Excursion(Base):
    """Stores individual excursions that can be part of packages"""
    __tablename__ = 'excursions'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text)
    location = sa.Column(sa.String(100), nullable=False)
    duration_hours = sa.Column(sa.Float, nullable=False)
    price = sa.Column(sa.Numeric(10, 2), nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)
    
    packages = relationship("TravelPackage", secondary="package_excursions", back_populates="excursions")

class PackageExcursion(Base):
    """Association table for many-to-many relationship between packages and excursions"""
    __tablename__ = 'package_excursions'
    
    package_id = sa.Column(sa.Integer, ForeignKey('travel_packages.id'), primary_key=True)
    excursion_id = sa.Column(sa.Integer, ForeignKey('excursions.id'), primary_key=True)
    is_included = sa.Column(sa.Boolean, default=True)  # Whether excursion is included in package price
    optional_price = sa.Column(sa.Numeric(10, 2))  # Price if not included
    
    __table_args__ = (
        UniqueConstraint('package_id', 'excursion_id', name='uq_package_excursion'),
    )

class Review(Base):
    """Stores customer reviews for travel packages"""
    __tablename__ = 'reviews'
    
    id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, ForeignKey('customers.id'), nullable=False)
    package_id = sa.Column(sa.Integer, ForeignKey('travel_packages.id'), nullable=False)
    rating = sa.Column(sa.Integer, nullable=False)  # 1-5 scale
    comment = sa.Column(sa.Text)
    review_date = sa.Column(sa.DateTime, server_default=sa.func.now())
    
    customer = relationship("Customer", back_populates="reviews")
    travel_package = relationship("TravelPackage", back_populates="reviews")
    
    __table_args__ = (
        sa.CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

class Booking(Base):
    """Stores customer bookings for travel packages"""
    __tablename__ = 'bookings'
    
    id = sa.Column(sa.Integer, primary_key=True)
    customer_id = sa.Column(sa.Integer, ForeignKey('customers.id'), nullable=False)
    package_id = sa.Column(sa.Integer, ForeignKey('travel_packages.id'), nullable=False)
    booking_date = sa.Column(sa.DateTime, server_default=sa.func.now())
    departure_date = sa.Column(sa.Date, nullable=False)
    travelers_count = sa.Column(sa.Integer, nullable=False)
    total_price = sa.Column(sa.Numeric(10, 2), nullable=False)
    status = sa.Column(sa.String(20), nullable=False, default='confirmed')  # confirmed, cancelled, completed
    
    customer = relationship("Customer", back_populates="bookings")
    travel_package = relationship("TravelPackage", back_populates="bookings")
    
    __table_args__ = (
        sa.CheckConstraint('travelers_count > 0', name='check_travelers_count'),
        sa.CheckConstraint("status IN ('confirmed', 'cancelled', 'completed')", name='check_booking_status'),
    )

def create_database(engine):
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
```
