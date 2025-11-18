"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ysc.com.br
Prompt: Recommend libraries for creating a database of essential oil products, categorizing them by type (e.g., menthol crystallized, mint oil, melaleuca oil) as listed on YSC's website.
Generated: DETERMINISTIC_5cb2138cf0baff5b
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Essential Oil Database Manager

This script provides functionality to create and manage a database of essential oil products 
categorized by type. It leverages SQLite as the database and utilizes SQLAlchemy for ORM 
functionality.

Requirements:
- Install SQLAlchemy: `pip install sqlalchemy`
"""

from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model using SQLAlchemy ORM
Base = declarative_base()

class EssentialOil(Base):
    """
    EssentialOil Model

    Represents an essential oil product with attributes such as name, category, and price.
    """
    __tablename__ = 'essential_oils'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier
    name = Column(String, nullable=False)  # Name of the product
    category = Column(String, nullable=False)  # Type/category (e.g., mint oil, melaleuca oil)
    price = Column(Float, nullable=False)  # Price of the product

# Database setup - SQLite used for simplicity
DATABASE_URL = 'sqlite:///essential_oils.db'  # Path to SQLite database
engine = create_engine(DATABASE_URL, echo=False)

# Create the database and table(s) if they don't exist
Base.metadata.create_all(engine)

# Create a session factory to interact with the database
Session = sessionmaker(bind=engine)

# CRUD operations
def add_essential_oil(name, category, price):
    """
    Add a new essential oil product to the database.

    :param name: Name of the essential oil
    :param category: Category/type of the essential oil
    :param price: Price of the essential oil
    """
    session = Session()
    try:
        new_oil = EssentialOil(name=name, category=category, price=price)
        session.add(new_oil)
        session.commit()
        print(f"Added '{name}' to the database.")
    except Exception as e:
        session.rollback()
        print(f"Error adding essential oil: {e}")
    finally:
        session.close()

def list_essential_oils():
    """
    List all essential oil products in the database.
    """
    session = Session()
    try:
        oils = session.query(EssentialOil).all()
        for oil in oils:
            print(f"ID: {oil.id}, Name: {oil.name}, Category: {oil.category}, Price: ${oil.price:.2f}")
    except Exception as e:
        print(f"Error retrieving essential oils: {e}")
    finally:
        session.close()

def delete_essential_oil(oil_id):
    """
    Delete an essential oil product from the database by ID.

    :param oil_id: ID of the essential oil to delete
    """
    session = Session()
    try:
        oil = session.query(EssentialOil).get(oil_id)
        if oil:
            session.delete(oil)
            session.commit()
            print(f"Deleted essential oil with ID: {oil_id}")
        else:
            print(f"No essential oil found with ID: {oil_id}")
    except Exception as e:
        session.rollback()
        print(f"Error deleting essential oil: {e}")
    finally:
        session.close()

def update_essential_oil(oil_id, name=None, category=None, price=None):
    """
    Update an essential oil product in the database.

    :param oil_id: ID of the essential oil to update
    :param name: New name (optional)
    :param category: New category/type (optional)
    :param price: New price (optional)
    """
    session = Session()
    try:
        oil = session.query(EssentialOil).get(oil_id)
        if oil:
            if name:
                oil.name = name
            if category:
                oil.category = category
            if price:
                oil.price = price
            session.commit()
            print(f"Updated essential oil with ID: {oil_id}")
        else:
            print(f"No essential oil found with ID: {oil_id}")
    except Exception as e:
        session.rollback()
        print(f"Error updating essential oil: {e}")
    finally:
        session.close()

# Example usage (Uncomment these for testing)
# add_essential_oil("Menthol Crystallized", "Menthol", 12.50)
# add_essential_oil("Mint Oil", "Mint", 8.99)
# list_essential_oils()
# update_essential_oil(1, price=13.00)
# delete_essential_oil(2)
```

### Recommended Libraries
1. **SQLAlchemy**: For database interactions and ORM.
2. **SQLite**: Lightweight database for small-scale applications.

Install using:
```bash
pip install sqlalchemy
```
