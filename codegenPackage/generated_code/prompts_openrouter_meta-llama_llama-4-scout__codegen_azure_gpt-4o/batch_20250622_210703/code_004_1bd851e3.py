"""
Generated Code Metadata:
========================
Original URL: https://karnafoundation.org.in
Prompt: Create a data model for tracking donations, volunteers, and beneficiaries for an organization like Karna Foundation, which supports multiple causes such as child education, healthcare, and food distribution.
Generated: DETERMINISTIC_1bd851e3589f099b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Base class for SQLAlchemy models
Base = declarative_base()

# Donation model
class Donation(Base):
    __tablename__ = 'donations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each donation
    donor_name = Column(String(100), nullable=False)  # Name of the donor
    amount = Column(Float, nullable=False)  # Amount donated
    cause = Column(String(50), nullable=False)  # Cause for which the donation is made
    date = Column(DateTime, default=datetime.utcnow)  # Date of donation
    
    def __repr__(self):
        return f"<Donation(id={self.id}, donor_name={self.donor_name}, amount={self.amount}, cause={self.cause}, date={self.date})>"

# Volunteer model
class Volunteer(Base):
    __tablename__ = 'volunteers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each volunteer
    name = Column(String(100), nullable=False)  # Name of the volunteer
    contact_info = Column(String(200), nullable=False)  # Contact information
    cause = Column(String(50), nullable=False)  # Cause the volunteer is associated with
    
    def __repr__(self):
        return f"<Volunteer(id={self.id}, name={self.name}, contact_info={self.contact_info}, cause={self.cause})>"

# Beneficiary model
class Beneficiary(Base):
    __tablename__ = 'beneficiaries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique ID for each beneficiary
    name = Column(String(100), nullable=False)  # Name of the beneficiary
    contact_info = Column(String(200), nullable=True)  # Contact information (optional)
    cause = Column(String(50), nullable=False)  # Cause the beneficiary is associated with
    assistance_received = Column(String(200), nullable=False)  # Description of assistance received
    
    def __repr__(self):
        return f"<Beneficiary(id={self.id}, name={self.name}, contact_info={self.contact_info}, cause={self.cause}, assistance_received={self.assistance_received})>"

# Database setup
def setup_database(db_url='sqlite:///karna_foundation.db'):
    """
    Sets up the database connection and creates tables.
    
    :param db_url: Database connection URL (default is SQLite)
    """
    try:
        engine = create_engine(db_url, echo=True)  # Create database engine
        Base.metadata.create_all(engine)  # Create tables
        return sessionmaker(bind=engine)  # Return session factory
    except Exception as e:
        print(f"Error setting up the database: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Initialize database
    Session = setup_database()
    session = Session()
    
    try:
        # Add sample data
        donation = Donation(donor_name="John Doe", amount=100.0, cause="Child Education")
        volunteer = Volunteer(name="Jane Smith", contact_info="jane@example.com", cause="Healthcare")
        beneficiary = Beneficiary(name="Alice Johnson", contact_info="alice@example.com", cause="Food Distribution", assistance_received="Monthly food package")
        
        session.add(donation)
        session.add(volunteer)
        session.add(beneficiary)
        session.commit()  # Commit changes to the database
        
        # Query and print data
        donations = session.query(Donation).all()
        volunteers = session.query(Volunteer).all()
        beneficiaries = session.query(Beneficiary).all()
        
        print("Donations:", donations)
        print("Volunteers:", volunteers)
        print("Beneficiaries:", beneficiaries)
    except Exception as e:
        print(f"Error during database operations: {e}")
        session.rollback()  # Rollback in case of error
    finally:
        session.close()  # Close the session
```
