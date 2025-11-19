"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Design a database schema to store information about engraved products, including materials, designs, and customer orders.
Generated: DETERMINISTIC_5c3e3f4c9f611969
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for engraved products
CREATE DATABASE engraved_products;

-- Use the engraved_products database
USE engraved_products;

-- Create a table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (material_id)
);

-- Create a table for designs
CREATE TABLE designs (
  design_id INT AUTO_INCREMENT,
  design_name VARCHAR(255) NOT NULL,
  design_description TEXT,
  design_image BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (design_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  material_id INT,
  design_id INT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id),
  FOREIGN KEY (design_id) REFERENCES designs(design_id)
);

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create a table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_materials_material_id ON products (material_id);
CREATE INDEX idx_designs_design_id ON products (design_id);
CREATE INDEX idx_customers_customer_id ON orders (customer_id);
CREATE INDEX idx_orders_order_id ON order_items (order_id);
CREATE INDEX idx_products_product_id ON order_items (product_id);
```

```python
# models.py

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, DECIMAL, Enum, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

engine = create_engine('mysql+pymysql://user:password@localhost/engraved_products')
Base = declarative_base()

class Material(Base):
    __tablename__ = 'materials'
    material_id = Column(Integer, primary_key=True)
    material_name = Column(String(255), nullable=False)
    material_description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Design(Base):
    __tablename__ = 'designs'
    design_id = Column(Integer, primary_key=True)
    design_name = Column(String(255), nullable=False)
    design_description = Column(Text)
    design_image = Column(BLOB)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey('materials.material_id'))
    design_id = Column(Integer, ForeignKey('designs.design_id'))
    product_name = Column(String(255), nullable=False)
    product_description = Column(Text)
    product_price = Column(DECIMAL(10, 2), nullable=False)
    material = relationship('Material', backref='products')
    design = relationship('Design', backref='products')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20))
    address = Column(String(255))
    orders = relationship('Order', backref='customer')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    order_date = Column(DateTime, default=datetime.utcnow)
    total_cost = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum('pending', 'shipped', 'delivered', 'cancelled', name='status', create_constraint=True), default='pending')
    order_items = relationship('OrderItem', backref='order')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer, nullable=False)
    product = relationship('Product', backref='order_items')
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```
