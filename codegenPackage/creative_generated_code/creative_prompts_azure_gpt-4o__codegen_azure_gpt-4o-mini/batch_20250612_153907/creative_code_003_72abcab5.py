"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Provide code to create a searchable database of profiles with categories such as "Florist," "Government Official," and "Military," using SQLAlchemy in Python.
Generated: DETERMINISTIC_72abcab53a5cdcd0
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError

# Create a base class for declarative models
Base = declarative_base()

# Define the Profile class to represent user profiles in the database
class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    # Establish relationship with Category
    category = relationship('Category', back_populates='profiles')

    def __repr__(self):
        return f"<Profile(id={self.id}, name='{self.name}', category='{self.category.name}')>"

# Define the Category class to represent categories in the database
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Establish relationship with Profile
    profiles = relationship('Profile', back_populates='category')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

# Function to create a new SQLite database and tables
def setup_database(db_url='sqlite:///profiles.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

# Function to add a new profile
def add_profile(session, name, category_name):
    try:
        # Check if the category exists
        category = session.query(Category).filter_by(name=category_name).first()
        if not category:
            raise ValueError(f"Category '{category_name}' does not exist.")
        
        # Create a new profile
        new_profile = Profile(name=name, category=category)
        session.add(new_profile)
        session.commit()
        print(f"Profile added: {new_profile}")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding profile: {e}")
    except ValueError as ve:
        print(ve)

# Function to search profiles by category
def search_profiles_by_category(session, category_name):
    try:
        profiles = session.query(Profile).join(Category).filter(Category.name == category_name).all()
        return profiles
    except SQLAlchemyError as e:
        print(f"Error retrieving profiles: {e}")
        return []

# Main function to run the database setup and test the functionality
if __name__ == "__main__":
    # Setup the database
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example categories (this should be done separately or in a setup step)
    try:
        session.add_all([Category(name='Florist'), Category(name='Government Official'), Category(name='Military')])
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding categories: {e}")

    # Add sample profiles
    add_profile(session, 'Alice', 'Florist')
    add_profile(session, 'Bob', 'Government Official')
    add_profile(session, 'Charlie', 'Military')

    # Search for profiles in a specific category
    florists = search_profiles_by_category(session, 'Florist')
    print("Florists:", florists)

    # Close the session
    session.close()
```
