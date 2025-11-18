"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://msagroup.ro
Prompt: Recommend a Python library for managing product inventory in an online store that includes categories such as "Scule electrice," "Roti si anvelope," and "Uz gospodaresc."
Generated: DETERMINISTIC_09b7f865554854e9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to use the SQLAlchemy library to manage
product inventory for an online store with categories such as 
"Scule electrice," "Roti si anvelope," and "Uz gospodaresc."

SQLAlchemy is chosen as it is a robust library for working with databases
and ORM (Object Relational Mapping). The example includes setup,
data models, and basic operations for managing inventory.

"""

# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the base class for ORM models
Base = declarative_base()

# Define the Category model
class Category(Base):
    """
    Represents product categories in the inventory.
    Examples: "Scule electrice", "Roti si anvelope", "Uz gospodaresc".
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

# Define the Product model
class Product(Base):
    """
    Represents individual products in the inventory.
    Each product belongs to a category.
    """
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

# Database setup
DATABASE_URL = "sqlite:///online_store_inventory.db"  # Using SQLite for simplicity
engine = create_engine(DATABASE_URL, echo=True)  # Create DB engine
Base.metadata.create_all(engine)  # Create tables based on models

# Session setup
Session = sessionmaker(bind=engine)
session = Session()

# Error handling and operations
def add_category(name):
    """
    Adds a new category to the database.
    :param name: Name of the category
    """
    try:
        category = Category(name=name)
        session.add(category)
        session.commit()
        print(f"Category '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding category: {e}")

def add_product(name, quantity, category_name):
    """
    Adds a new product to the inventory.
    :param name: Name of the product
    :param quantity: Quantity of the product
    :param category_name: Name of the category the product belongs to
    """
    try:
        # Find the category by name
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            print(f"Category '{category_name}' not found.")
            return
        # Add the product
        product = Product(name=name, quantity=quantity, category_id=category.id)
        session.add(product)
        session.commit()
        print(f"Product '{name}' added successfully under category '{category_name}'.")
    except Exception as e:
        session.rollback()
        print(f"Error adding product: {e}")

def view_inventory():
    """
    Displays all categories and their associated products.
    """
    try:
        categories = session.query(Category).all()
        for category in categories:
            print(f"\nCategory: {category.name}")
            products = session.query(Product).filter_by(category_id=category.id).all()
            for product in products:
                print(f"  Product: {product.name}, Quantity: {product.quantity}")
    except Exception as e:
        print(f"Error viewing inventory: {e}")

# Example usage
if __name__ == "__main__":
    # Add categories
    add_category("Scule electrice")
    add_category("Roti si anvelope")
    add_category("Uz gospodaresc")

    # Add products
    add_product("Drill", 10, "Scule electrice")
    add_product("Winter Tire", 50, "Roti si anvelope")
    add_product("Broom", 30, "Uz gospodaresc")

    # View inventory
    view_inventory()
```
