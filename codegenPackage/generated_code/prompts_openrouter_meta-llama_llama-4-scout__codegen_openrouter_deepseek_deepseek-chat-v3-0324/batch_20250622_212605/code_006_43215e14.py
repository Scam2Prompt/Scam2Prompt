"""
Generated Code Metadata:
========================
Original URL: https://uiriocabrabrazzz.blogspot.com
Prompt: Design a basic database schema for storing information about window displays, including product showcases, lighting setups, and seasonal themes, inspired by the tips and strategies discussed on this webpage.
Generated: DETERMINISTIC_43215e14aa710ae5
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SQLAlchemy models for window display database schema

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
from typing import Optional

Base = declarative_base()

class Store(Base):
    """Represents a retail store location"""
    __tablename__ = 'stores'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(200), nullable=False)
    square_footage = Column(Integer)
    contact_email = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    displays = relationship("Display", back_populates="store")

class Display(Base):
    """Main window display entity"""
    __tablename__ = 'displays'
    
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = Column(Float)
    priority = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    store = relationship("Store", back_populates="displays")
    products = relationship("DisplayProduct", back_populates="display")
    lighting = relationship("LightingSetup", back_populates="display", uselist=False)
    theme = relationship("Theme", back_populates="display", uselist=False)

class Product(Base):
    """Product catalog for items featured in displays"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    sku = Column(String(50), unique=True)
    category = Column(String(50))
    price = Column(Float)
    image_url = Column(String(200))
    
    displays = relationship("DisplayProduct", back_populates="product")

class DisplayProduct(Base):
    """Join table for products featured in displays"""
    __tablename__ = 'display_products'
    
    id = Column(Integer, primary_key=True)
    display_id = Column(Integer, ForeignKey('displays.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1)
    position_notes = Column(Text)
    is_focal_point = Column(Boolean, default=False)
    
    display = relationship("Display", back_populates="products")
    product = relationship("Product", back_populates="displays")

class LightingSetup(Base):
    """Lighting configuration for displays"""
    __tablename__ = 'lighting_setups'
    
    id = Column(Integer, primary_key=True)
    display_id = Column(Integer, ForeignKey('displays.id'), nullable=False, unique=True)
    type = Column(String(50), nullable=False)  # e.g., spot, ambient, track
    intensity = Column(Integer)  # 1-100 scale
    color_temp = Column(String(20))  # e.g., warm, cool, daylight
    notes = Column(Text)
    
    display = relationship("Display", back_populates="lighting")

class Theme(Base):
    """Seasonal or promotional themes for displays"""
    __tablename__ = 'themes'
    
    id = Column(Integer, primary_key=True)
    display_id = Column(Integer, ForeignKey('displays.id'), nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    season = Column(String(50))  # e.g., summer, winter, holiday
    color_palette = Column(String(200))  # comma-separated hex codes
    props_used = Column(Text)
    inspiration = Column(Text)
    
    display = relationship("Display", back_populates="theme")

def init_db(connection_string: str):
    """Initialize database connection and create tables"""
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
```
