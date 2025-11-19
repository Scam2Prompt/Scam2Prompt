"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: "Design a database schema to store information about different types of concrete products, such as paving blocks, kanstin, and buis beton, similar to those offered by Komando Block Cirebon."
Generated: DETERMINISTIC_7265850d21ddb48f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlalchemy as sa
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class ProductCategory(Base):
    """Represents a category of concrete products"""
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    
    products = relationship("Product", back_populates="category")

class Product(Base):
    """Represents a concrete product with specifications"""
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey('product_categories.id'), nullable=False)
    description = Column(Text)
    dimensions = Column(String(100))  # e.g., "10x20x40 cm"
    weight = Column(Float)  # in kg
    price = Column(Float)  # in local currency
    stock = Column(Integer, default=0)
    image_url = Column(String(255))
    
    category = relationship("ProductCategory", back_populates="products")
    variants = relationship("ProductVariant", back_populates="product")

class ProductVariant(Base):
    """Represents different variants of a product (colors, finishes)"""
    __tablename__ = 'product_variants'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    name = Column(String(100), nullable=False)  # e.g., "Red", "Smooth Finish"
    color_code = Column(String(20))
    additional_price = Column(Float, default=0.0)
    stock = Column(Integer, default=0)
    
    product = relationship("Product", back_populates="variants")

class Customer(Base):
    """Stores customer information"""
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(Text)
    
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    """Records customer orders"""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(sa.DateTime, server_default=sa.func.now())
    status = Column(String(50), default='Pending')  # e.g., Pending, Processing, Shipped, Delivered
    total_amount = Column(Float)
    notes = Column(Text)
    
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    """Records individual items within an order"""
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    variant_id = Column(Integer, ForeignKey('product_variants.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
    variant = relationship("ProductVariant")

def create_database(db_url='sqlite:///concrete_products.db'):
    """Initialize the database and create tables"""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

def get_session(engine):
    """Create a new database session"""
    Session = sessionmaker(bind=engine)
    return Session()
```
