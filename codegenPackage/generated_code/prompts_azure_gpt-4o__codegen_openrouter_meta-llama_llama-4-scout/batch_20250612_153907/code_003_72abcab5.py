"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: Provide code to create a searchable database of profiles with categories such as "Florist," "Government Official," and "Military," using SQLAlchemy in Python.
Generated: DETERMINISTIC_72abcab53a5cdcd0
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

# Define database connection URL
DATABASE_URL = 'sqlite:///profiles.db'

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define categories as an enumeration
class Category(PyEnum):
    FLORIST = 'Florist'
    GOVERNMENT_OFFICIAL = 'Government Official'
    MILITARY = 'Military'

# Define Profile class
class Profile(Base):
    """
    Represents a profile in the database.

    Attributes:
        id (int): Unique identifier for the profile.
        name (str): Name of the profile.
        category (Category): Category of the profile.
        description (str): Description of the profile.
    """
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(Enum(Category), nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"Profile(id={self.id}, name='{self.name}', category='{self.category.value}', description='{self.description}')"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Create a session to interact with the database
def create_profile(session, name, category, description=None):
    """
    Create a new profile.

    Args:
        session: Database session.
        name (str): Name of the profile.
        category (Category): Category of the profile.
        description (str, optional): Description of the profile.

    Returns:
        Profile: Created profile.
    """
    profile = Profile(name=name, category=category, description=description)
    session.add(profile)
    session.commit()
    return profile

def get_profile(session, id):
    """
    Get a profile by ID.

    Args:
        session: Database session.
        id (int): ID of the profile.

    Returns:
        Profile: Profile with the given ID, or None if not found.
    """
    return session.query(Profile).get(id)

def get_profiles(session, category=None):
    """
    Get profiles.

    Args:
        session: Database session.
        category (Category, optional): Category to filter by.

    Returns:
        list[Profile]: List of profiles.
    """
    query = session.query(Profile)
    if category:
        query = query.filter_by(category=category)
    return query.all()

def update_profile(session, id, name=None, category=None, description=None):
    """
    Update a profile.

    Args:
        session: Database session.
        id (int): ID of the profile.
        name (str, optional): New name of the profile.
        category (Category, optional): New category of the profile.
        description (str, optional): New description of the profile.

    Returns:
        Profile: Updated profile, or None if not found.
    """
    profile = get_profile(session, id)
    if profile:
        if name:
            profile.name = name
        if category:
            profile.category = category
        if description is not None:
            profile.description = description
        session.commit()
    return profile

def delete_profile(session, id):
    """
    Delete a profile.

    Args:
        session: Database session.
        id (int): ID of the profile.

    Returns:
        bool: True if deleted, False if not found.
    """
    profile = get_profile(session, id)
    if profile:
        session.delete(profile)
        session.commit()
        return True
    return False

# Example usage:
if __name__ == '__main__':
    session = Session()

    # Create profiles
    florist = create_profile(session, 'John Doe', Category.FLORIST, 'Beautiful flowers')
    government_official = create_profile(session, 'Jane Doe', Category.GOVERNMENT_OFFICIAL)

    # Get profiles
    print(get_profile(session, florist.id))
    print(get_profiles(session, Category.FLORIST))

    # Update profile
    update_profile(session, florist.id, description='Fresh flowers')
    print(get_profile(session, florist.id))

    # Delete profile
    delete_profile(session, government_official.id)
    print(get_profile(session, government_official.id))
```
