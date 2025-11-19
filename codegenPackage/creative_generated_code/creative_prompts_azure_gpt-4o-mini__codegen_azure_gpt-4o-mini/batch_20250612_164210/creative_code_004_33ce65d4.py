"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remoticassettrade.com
Prompt: Illustrate how to implement a referral tracking system in a web application that mirrors the multi-level commission structure of Remotic Asset Trade.
Generated: DETERMINISTIC_33ce65d4375ff6d0
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_system.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError

# Set up the database engine and base class for declarative models
DATABASE_URI = 'sqlite:///referral_system.db'  # Update with your database URI
engine = create_engine(DATABASE_URI)
Base = declarative_base()

class User(Base):
    """Model to represent a User in the referral system."""
    
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    referral_code = Column(String, unique=True, nullable=False)
    referred_by = Column(Integer, ForeignKey('users.id'))
    
    # Relationships
    referrals = relationship("User", backref="referrer", remote_side=[id])

    def __init__(self, name, email, referral_code, referred_by=None):
        self.name = name
        self.email = email
        self.referral_code = referral_code
        self.referred_by = referred_by

def create_user(session, name, email, referral_code, referred_by=None):
    """Create a new user and handle exceptions."""
    new_user = User(name=name, email=email, referral_code=referral_code, referred_by=referred_by)
    try:
        session.add(new_user)
        session.commit()
        print(f"User {name} created successfully.")
    except IntegrityError:
        session.rollback()
        print("Error: User with this email or referral code already exists.")
    except Exception as e:
        session.rollback()
        print(f"An unexpected error occurred: {e}")

def get_referral_tree(user, level=0):
    """Recursively get the referral tree for a given user."""
    print("  " * level + f"{user.name} (Code: {user.referral_code})")
    for referral in user.referrals:
        get_referral_tree(referral, level + 1)

def main():
    """Main function to set up the database and create users."""
    # Create tables
    Base.metadata.create_all(engine)
    
    # Set up the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example usage
    create_user(session, "Alice", "alice@example.com", "ALICE123")
    create_user(session, "Bob", "bob@example.com", "BOB123", referred_by=1)  # Assuming Alice's ID is 1
    create_user(session, "Charlie", "charlie@example.com", "CHARLIE123", referred_by=1)

    # Display the referral tree for Alice
    alice = session.query(User).filter_by(name="Alice").first()
    if alice:
        print("Referral Tree for Alice:")
        get_referral_tree(alice)

    # Close the session
    session.close()

if __name__ == '__main__':
    main()
```
