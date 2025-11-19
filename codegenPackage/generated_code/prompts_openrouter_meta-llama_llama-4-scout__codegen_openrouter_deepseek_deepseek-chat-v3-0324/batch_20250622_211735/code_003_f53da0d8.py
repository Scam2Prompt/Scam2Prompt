"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Design a database schema for storing caregiver profiles, pet information, and reservation details for a pet sitting service like WUFIS.
Generated: DETERMINISTIC_f53da0d8d7279c9a
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for pet sitting service (WUFIS-like)
# Uses SQLAlchemy ORM for Python

from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserType(Enum):
    PET_OWNER = "pet_owner"
    CAREGIVER = "caregiver"
    ADMIN = "admin"

class PetType(Enum):
    DOG = "dog"
    CAT = "cat"
    BIRD = "bird"
    RABBIT = "rabbit"
    OTHER = "other"

class ReservationStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class User(Base):
    """User table for both pet owners and caregivers"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(200))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(20))
    profile_picture = Column(String(256))
    user_type = Column(SQLEnum(UserType), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    pets = relationship("Pet", back_populates="owner")
    caregiver_profile = relationship("CaregiverProfile", uselist=False, back_populates="user")
    reservations_as_owner = relationship("Reservation", foreign_keys="[Reservation.owner_id]", back_populates="owner")
    reservations_as_caregiver = relationship("Reservation", foreign_keys="[Reservation.caregiver_id]", back_populates="caregiver")

class CaregiverProfile(Base):
    """Additional profile information for caregivers"""
    __tablename__ = 'caregiver_profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False)
    bio = Column(String(500))
    experience_years = Column(Integer)
    hourly_rate = Column(Float)
    is_certified = Column(Boolean, default=False)
    certification_details = Column(String(200))
    availability = Column(String(500))  # Could be JSON or serialized data
    service_radius = Column(Integer)  # In miles/kilometers
    is_background_checked = Column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="caregiver_profile")
    services_offered = relationship("CaregiverService", back_populates="caregiver")
    reviews = relationship("Review", back_populates="caregiver")

class Pet(Base):
    """Pet information table"""
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    pet_type = Column(SQLEnum(PetType), nullable=False)
    breed = Column(String(50))
    age = Column(Integer)
    weight = Column(Float)
    medical_conditions = Column(String(500))
    special_instructions = Column(String(500))
    profile_picture = Column(String(256))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", back_populates="pets")
    reservations = relationship("Reservation", back_populates="pet")

class CaregiverService(Base):
    """Services offered by caregivers"""
    __tablename__ = 'caregiver_services'

    id = Column(Integer, primary_key=True)
    caregiver_id = Column(Integer, ForeignKey('caregiver_profiles.id'), nullable=False)
    service_name = Column(String(100), nullable=False)
    description = Column(String(300))
    rate = Column(Float, nullable=False)

    # Relationships
    caregiver = relationship("CaregiverProfile", back_populates="services_offered")

class Reservation(Base):
    """Pet sitting reservation details"""
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    caregiver_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    pet_id = Column(Integer, ForeignKey('pets.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(SQLEnum(ReservationStatus), default=ReservationStatus.PENDING)
    total_price = Column(Float)
    special_requests = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", foreign_keys=[owner_id], back_populates="reservations_as_owner")
    caregiver = relationship("User", foreign_keys=[caregiver_id], back_populates="reservations_as_caregiver")
    pet = relationship("Pet", back_populates="reservations")
    review = relationship("Review", uselist=False, back_populates="reservation")

class Review(Base):
    """Reviews for caregivers"""
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.id'), unique=True, nullable=False)
    caregiver_id = Column(Integer, ForeignKey('caregiver_profiles.id'), nullable=False)
    rating = Column(Integer, nullable=False)  # 1-5 scale
    comment = Column(String(500))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    reservation = relationship("Reservation", back_populates="review")
    caregiver = relationship("CaregiverProfile", back_populates="reviews")

# Database initialization function
def init_db(database_uri):
    """Initialize the database connection and create tables"""
    engine = create_engine(database_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session
```
