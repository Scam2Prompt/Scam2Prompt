"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Design a database schema to store shoe products with attributes like name, price, brand, category, and payment options (e.g., 3x, 5x, 7x installments), inspired by the content of https://magicenen-nfts.blogspot.com.
Generated: DETERMINISTIC_d628ab41dd0cb2ae
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for shoe products e-commerce platform
# Inspired by magicenen-nfts.blogspot.com content

import sqlalchemy as db
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between products and payment options
product_payment = Table(
    'product_payment',
    Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('payment_option_id', Integer, ForeignKey('payment_options.id'))
)

class Brand(Base):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500))
    logo_url = Column(String(255))
    
    products = relationship("Product", back_populates="brand")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(500))
    
    products = relationship("Product", back_populates="category")

class PaymentOption(Base):
    __tablename__ = 'payment_options'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)  # e.g., "3x installments"
    installment_count = Column(Integer, nullable=False)
    description = Column(String(255))
    
    products = relationship("Product", secondary=product_payment, back_populates="payment_options")

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(1000))
    price = Column(Float, nullable=False)
    discount_price = Column(Float)
    sku = Column(String(50), unique=True)
    stock_quantity = Column(Integer, default=0)
    image_url = Column(String(255))
    
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand = relationship("Brand", back_populates="products")
    
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", back_populates="products")
    
    payment_options = relationship("PaymentOption", secondary=product_payment, back_populates="products")

def initialize_database(connection_string):
    """Initialize the database and create tables"""
    try:
        engine = db.create_engine(connection_string)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        return Session()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise
```
