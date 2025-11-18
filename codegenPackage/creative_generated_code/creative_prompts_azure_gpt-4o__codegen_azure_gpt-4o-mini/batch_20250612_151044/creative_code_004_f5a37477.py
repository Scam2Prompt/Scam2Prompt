"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Recommend a library or framework for building a multilingual directory website with categories like "Ωδεία" and "Ψυχίατροι," and provide an example of how to structure the database.
Generated: DETERMINISTIC_f5a374774dc57044
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database setup
DATABASE_URL = 'sqlite:///multilingual_directory.db'  # Change to your preferred database

# Base class for ORM models
Base = declarative_base()

class Category(Base):
    """Model for categories in the directory."""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    # Relationship to the directory items
    items = relationship('Item', back_populates='category')

class Item(Base):
    """Model for items in the directory."""
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    # Relationship back to the category
    category = relationship('Category', back_populates='items')

def initialize_database():
    """Create the database tables if they do not exist."""
    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        print("Database initialized successfully.")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {str(e)}")

def create_category(session, name, description=None):
    """Create a new category in the database."""
    try:
        category = Category(name=name, description=description)
        session.add(category)
        session.commit()
        print(f"Category '{name}' created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating category: {str(e)}")

def create_item(session, name, description, category_id):
    """Create a new item in the database."""
    try:
        item = Item(name=name, description=description, category_id=category_id)
        session.add(item)
        session.commit()
        print(f"Item '{name}' created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating item: {str(e)}")

if __name__ == "__main__":
    # Initialize database
    initialize_database()

    # Create a session for database operations
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example: Create categories
    create_category(session, "Ωδεία", "Music schools")
    create_category(session, "Ψυχίατροι", "Psychiatrists")

    # Example: Create items
    create_item(session, "Orchestra School", "A school for orchestra training", 1)
    create_item(session, "Child Psychiatrist", "Specialist in child psychology", 2)

    session.close()
```
