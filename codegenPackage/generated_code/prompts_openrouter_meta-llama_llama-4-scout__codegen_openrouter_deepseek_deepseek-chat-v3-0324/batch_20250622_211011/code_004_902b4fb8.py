"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Design a database schema to store information about dietary supplements, including product details, ingredients, and scientific research backing their efficacy, using a company like Gematria as a reference.
Generated: DETERMINISTIC_902b4fb84fe3fbfd
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    website = Column(String(255))
    founded_date = Column(DateTime)
    is_certified = Column(Boolean, default=False)
    certification_details = Column(Text)
    
    products = relationship("Product", back_populates="manufacturer")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    category = Column(String(50))
    dosage_form = Column(String(50))  # e.g., capsule, powder, liquid
    serving_size = Column(String(50))
    price = Column(Float)
    is_vegan = Column(Boolean, default=False)
    is_gluten_free = Column(Boolean, default=False)
    is_organic = Column(Boolean, default=False)
    
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship("Manufacturer", back_populates="products")
    
    ingredients = relationship("ProductIngredient", back_populates="product")
    research = relationship("Research", back_populates="product")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    category = Column(String(50))  # e.g., vitamin, mineral, herb
    safety_rating = Column(String(20))  # e.g., 'Generally Recognized as Safe'
    
    products = relationship("ProductIngredient", back_populates="ingredient")
    research = relationship("Research", back_populates="ingredient")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class ProductIngredient(Base):
    __tablename__ = 'product_ingredients'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    amount = Column(String(50))  # e.g., '500mg', '10% DV'
    is_active = Column(Boolean, default=True)
    
    product = relationship("Product", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="products")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Research(Base):
    __tablename__ = 'research'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    study_type = Column(String(50))  # e.g., 'Clinical Trial', 'Meta-analysis'
    results = Column(Text)
    publication_date = Column(DateTime)
    source = Column(String(255))  # e.g., journal name or website
    source_url = Column(String(255))
    is_peer_reviewed = Column(Boolean, default=False)
    
    product_id = Column(Integer, ForeignKey('products.id'), nullable=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=True)
    
    product = relationship("Product", back_populates="research")
    ingredient = relationship("Ingredient", back_populates="research")
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

def init_db(connection_string):
    """Initialize the database and create tables"""
    try:
        engine = create_engine(connection_string)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise

# Example usage:
# DATABASE_URL = "sqlite:///supplements.db"
# Session = init_db(DATABASE_URL)
```
