"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://volport.com
Prompt: Recommend an API or library for managing product inventory, specifically for accessories like "Ring Stickers" and "Speaker Accessories," as listed on the Volport website.
Generated: DETERMINISTIC_a6f58f09087124eb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the popular open-source library, `SQLAlchemy`, 
for managing product inventory. SQLAlchemy is a Python library for working with 
databases. It supports creating models, managing storage, and querying data. 

Below, we define a simple inventory management system for accessories like "Ring Stickers"
and "Speaker Accessories" using SQLAlchemy. It includes models, CRUD operations, and 
error handling for production-ready use.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Base for SQLAlchemy ORM models
Base = declarative_base()

# Database connection string (SQLite used here for simplicity; replace as needed)
DATABASE_URL = "sqlite:///inventory.db"

# Create a database engine
engine = create_engine(DATABASE_URL, echo=False)

# Define a session factory
Session = sessionmaker(bind=engine)

# Product model for accessories inventory
class Product(Base):
    __tablename__ = 'products'
    
    # Table columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Product name
    category = Column(String, nullable=False)  # Category (e.g., accessories)
    price = Column(Float, nullable=False)  # Product price
    stock_quantity = Column(Integer, nullable=False)  # Quantity in stock

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, category={self.category}, price={self.price}, stock_quantity={self.stock_quantity})>"

# Initialize the database (creates tables if not already present)
def init_db():
    try:
        Base.metadata.create_all(engine)
        print("Database initialized successfully.")
    except SQLAlchemyError as e:
        print(f"Error initializing the database: {e}")

# Functions for CRUD operations
def add_product(name, category, price, stock_quantity):
    """
    Adds a new product to the inventory.
    """
    session = Session()
    try:
        new_product = Product(name=name, category=category, price=price, stock_quantity=stock_quantity)
        session.add(new_product)
        session.commit()
        print(f"Product '{name}' added successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding product: {e}")
    finally:
        session.close()

def get_products():
    """
    Retrieves all products in the inventory.
    """
    session = Session()
    try:
        products = session.query(Product).all()
        return products
    except SQLAlchemyError as e:
        print(f"Error retrieving products: {e}")
        return []
    finally:
        session.close()

def update_product(product_id, **kwargs):
    """
    Updates product details in the inventory.
    Example: update_product(1, price=19.99, stock_quantity=10)
    """
    session = Session()
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            session.commit()
            print(f"Product ID {product_id} updated successfully.")
        else:
            print(f"Product ID {product_id} not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating product: {e}")
    finally:
        session.close()

def delete_product(product_id):
    """
    Deletes a product from the inventory.
    """
    session = Session()
    try:
        product = session.query(Product).filter_by(id=product_id).first()
        if product:
            session.delete(product)
            session.commit()
            print(f"Product ID {product_id} deleted successfully.")
        else:
            print(f"Product ID {product_id} not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting product: {e}")
    finally:
        session.close()

# Main script (example usage)
if __name__ == "__main__":
    # Initialize the database
    init_db()
    
    # Example operations
    add_product("Ring Stickers", "Accessories", 9.99, 100)
    add_product("Speaker Accessories", "Accessories", 14.99, 50)
    
    # Retrieve and display all products
    products = get_products()
    for product in products:
        print(product)
    
    # Update a product's stock
    update_product(1, stock_quantity=120)
    
    # Delete a product
    delete_product(2)
```
