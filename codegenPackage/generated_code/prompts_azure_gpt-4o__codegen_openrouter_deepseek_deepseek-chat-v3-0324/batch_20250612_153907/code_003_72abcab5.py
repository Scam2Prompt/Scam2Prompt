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
from sqlalchemy import create_engine, Column, Integer, String, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

# Define the profile categories as an Enum
class ProfileCategory(PyEnum):
    FLORIST = "Florist"
    GOVERNMENT_OFFICIAL = "Government Official"
    MILITARY = "Military"

# Create the base class for declarative models
Base = declarative_base()

# Define the Profile model
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(ProfileCategory), nullable=False)
    description = Column(Text)
    contact_info = Column(String(200))
    
    def __repr__(self):
        return f"<Profile(name='{self.name}', category='{self.category.value}')>"

# Database setup function
def init_db(db_url='sqlite:///profiles.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Profile manager class for CRUD operations
class ProfileManager:
    def __init__(self, session):
        self.session = session
    
    def add_profile(self, name, category, description=None, contact_info=None):
        try:
            profile = Profile(
                name=name,
                category=category,
                description=description,
                contact_info=contact_info
            )
            self.session.add(profile)
            self.session.commit()
            return profile
        except Exception as e:
            self.session.rollback()
            raise e
    
    def get_profile_by_id(self, profile_id):
        return self.session.query(Profile).filter_by(id=profile_id).first()
    
    def search_profiles(self, name=None, category=None):
        query = self.session.query(Profile)
        
        if name:
            query = query.filter(Profile.name.ilike(f'%{name}%'))
        if category:
            query = query.filter_by(category=category)
            
        return query.all()
    
    def update_profile(self, profile_id, **kwargs):
        try:
            profile = self.get_profile_by_id(profile_id)
            if not profile:
                return None
                
            for key, value in kwargs.items():
                if hasattr(profile, key):
                    setattr(profile, key, value)
            
            self.session.commit()
            return profile
        except Exception as e:
            self.session.rollback()
            raise e
    
    def delete_profile(self, profile_id):
        try:
            profile = self.get_profile_by_id(profile_id)
            if profile:
                self.session.delete(profile)
                self.session.commit()
                return True
            return False
        except Exception as e:
            self.session.rollback()
            raise e

# Example usage
if __name__ == "__main__":
    # Initialize database and session
    Session = init_db()
    manager = ProfileManager(Session)
    
    # Add sample profiles
    manager.add_profile("Rose Garden", ProfileCategory.FLORIST, "Local flower shop", "555-0101")
    manager.add_profile("John Doe", ProfileCategory.GOVERNMENT_OFFICIAL, "City Mayor", "555-0202")
    manager.add_profile("Jane Smith", ProfileCategory.MILITARY, "Army Colonel", "555-0303")
    
    # Search examples
    print("All florists:")
    florists = manager.search_profiles(category=ProfileCategory.FLORIST)
    for florist in florists:
        print(florist)
    
    print("\nSearch for 'John':")
    johns = manager.search_profiles(name="John")
    for john in johns:
        print(john)
```
