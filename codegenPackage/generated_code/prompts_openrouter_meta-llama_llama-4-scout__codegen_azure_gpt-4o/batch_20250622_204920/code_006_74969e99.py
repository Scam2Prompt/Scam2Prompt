"""
Generated Code Metadata:
========================
Original URL: https://poweredproductions.com.au
Prompt: Design a data model for storing frequently asked questions and answers about armourer services, uniform hire, and prop rentals for a film production company website.
Generated: DETERMINISTIC_74969e99ee8cd624
Batch ID: 20250622_204920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for the ORM
Base = declarative_base()

# Define the Category model to categorize FAQs
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each category
    name = Column(String(100), nullable=False, unique=True)  # Name of the category (e.g., Armourer Services, Uniform Hire, Prop Rentals)
    description = Column(Text, nullable=True)  # Optional description of the category

    # Relationship to FAQs
    faqs = relationship('FAQ', back_populates='category', cascade='all, delete-orphan')

# Define the FAQ model to store questions and answers
class FAQ(Base):
    __tablename__ = 'faqs'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each FAQ
    question = Column(Text, nullable=False)  # The FAQ question
    answer = Column(Text, nullable=False)  # The FAQ answer
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)  # Foreign key to the Category table

    # Relationship to Category
    category = relationship('Category', back_populates='faqs')

# Function to initialize the database
def initialize_database(db_url='sqlite:///faqs.db'):
    """
    Initializes the database and creates tables if they don't exist.

    Args:
        db_url (str): The database URL. Defaults to a SQLite database named 'faqs.db'.
    """
    engine = create_engine(db_url, echo=True)  # Create the database engine
    Base.metadata.create_all(engine)  # Create tables based on the defined models
    return engine

# Example usage
if __name__ == '__main__':
    # Initialize the database
    engine = initialize_database()

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Add example categories
        armourer_services = Category(name='Armourer Services', description='FAQs about armourer services for film production.')
        uniform_hire = Category(name='Uniform Hire', description='FAQs about hiring uniforms for film production.')
        prop_rentals = Category(name='Prop Rentals', description='FAQs about renting props for film production.')

        session.add_all([armourer_services, uniform_hire, prop_rentals])
        session.commit()

        # Add example FAQs
        faq1 = FAQ(question='What types of weapons can the armourer provide?', 
                   answer='The armourer can provide a wide range of weapons, including swords, firearms, and custom props.',
                   category=armourer_services)
        faq2 = FAQ(question='Can I hire uniforms for a specific historical period?', 
                   answer='Yes, we offer uniforms from various historical periods, including World War I and II.',
                   category=uniform_hire)
        faq3 = FAQ(question='Are the props insured during rental?', 
                   answer='Yes, all props are insured during the rental period.',
                   category=prop_rentals)

        session.add_all([faq1, faq2, faq3])
        session.commit()

        print("Database initialized and sample data added successfully.")
    except Exception as e:
        # Handle any errors that occur during database operations
        session.rollback()
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()
```
