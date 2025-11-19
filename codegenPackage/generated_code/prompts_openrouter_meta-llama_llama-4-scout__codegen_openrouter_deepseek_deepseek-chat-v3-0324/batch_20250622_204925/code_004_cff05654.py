"""
Generated Code Metadata:
========================
Original URL: https://myneel.com
Prompt: Design a database schema to store user data and progress tracking information for a weight loss app like Neel, ensuring data consistency and scalability.
Generated: DETERMINISTIC_cff056543dbb0495
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for a weight loss tracking app

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """Stores user account information"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)  # Store hashed passwords only
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(DateTime)
    height_cm = Column(Float, CheckConstraint('height_cm > 0'))
    gender = Column(String(1), CheckConstraint("gender IN ('M', 'F', 'O')"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    weight_entries = relationship("WeightEntry", back_populates="user")
    goals = relationship("Goal", back_populates="user")
    activities = relationship("ActivityLog", back_populates="user")

class WeightEntry(Base):
    """Tracks user weight over time"""
    __tablename__ = 'weight_entries'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    weight_kg = Column(Float, CheckConstraint('weight_kg > 0'), nullable=False)
    entry_date = Column(DateTime, nullable=False, server_default=func.now())
    notes = Column(String(255))
    
    # Relationships
    user = relationship("User", back_populates="weight_entries")

class Goal(Base):
    """Stores user weight loss goals"""
    __tablename__ = 'goals'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    target_weight_kg = Column(Float, CheckConstraint('target_weight_kg > 0'), nullable=False)
    start_weight_kg = Column(Float, CheckConstraint('start_weight_kg > 0'), nullable=False)
    start_date = Column(DateTime, nullable=False, server_default=func.now())
    target_date = Column(DateTime, nullable=False)
    is_active = Column(Integer, CheckConstraint('is_active IN (0, 1)'), default=1)
    created_at = Column(DateTime, server_default=func.now())
    
    # Relationships
    user = relationship("User", back_populates="goals")

class ActivityLog(Base):
    """Tracks user physical activities"""
    __tablename__ = 'activity_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_type = Column(String(50), nullable=False)
    duration_minutes = Column(Float, CheckConstraint('duration_minutes > 0'), nullable=False)
    calories_burned = Column(Float, CheckConstraint('calories_burned >= 0'))
    activity_date = Column(DateTime, nullable=False, server_default=func.now())
    notes = Column(String(255))
    
    # Relationships
    user = relationship("User", back_populates="activities")

class FoodLog(Base):
    """Tracks user food consumption"""
    __tablename__ = 'food_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    food_name = Column(String(100), nullable=False)
    calories = Column(Float, CheckConstraint('calories >= 0'), nullable=False)
    protein_g = Column(Float, CheckConstraint('protein_g >= 0'))
    carbs_g = Column(Float, CheckConstraint('carbs_g >= 0'))
    fats_g = Column(Float, CheckConstraint('fats_g >= 0'))
    serving_size = Column(String(50))
    log_date = Column(DateTime, nullable=False, server_default=func.now())
    notes = Column(String(255))
    
    # Relationships
    user = relationship("User")

# Database connection and session setup
def init_db(connection_string):
    """Initialize database connection and create tables"""
    engine = db.create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage:
# DATABASE_URL = "sqlite:///weight_loss_app.db"  # or your production DB URL
# Session = init_db(DATABASE_URL)
```
