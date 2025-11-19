"""
Generated Code Metadata:
========================
Original URL: https://pulse.claims
Prompt: "Design a data model for storing and retrieving insurance claims information, including claimant details and claim status."
Generated: DETERMINISTIC_91c643aedb054342
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_claims_model.py

from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import enum

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Enum for claim status
class ClaimStatus(enum.Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    UNDER_REVIEW = "Under Review"

# Model for Claimant details
class Claimant(Base):
    __tablename__ = 'claimants'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the claimant
    first_name = Column(String(50), nullable=False)  # First name of the claimant
    last_name = Column(String(50), nullable=False)  # Last name of the claimant
    email = Column(String(100), unique=True, nullable=False)  # Email of the claimant
    phone_number = Column(String(15), nullable=True)  # Phone number of the claimant

    # Relationship to link claims to claimants
    claims = relationship("InsuranceClaim", back_populates="claimant")

# Model for Insurance Claims
class InsuranceClaim(Base):
    __tablename__ = 'insurance_claims'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the claim
    claimant_id = Column(Integer, ForeignKey('claimants.id'), nullable=False)  # Foreign key to Claimant
    claim_date = Column(Date, nullable=False)  # Date the claim was filed
    claim_amount = Column(Float, nullable=False)  # Amount being claimed
    status = Column(Enum(ClaimStatus), nullable=False, default=ClaimStatus.PENDING)  # Status of the claim
    description = Column(String(255), nullable=True)  # Description of the claim

    # Relationship to link claimants to claims
    claimant = relationship("Claimant", back_populates="claims")

# Database setup function
def setup_database(database_url):
    """
    Sets up the database connection and creates tables if they don't exist.
    :param database_url: URL for the database connection (e.g., 'sqlite:///insurance.db')
    """
    try:
        engine = create_engine(database_url, echo=True)  # Create database engine
        Base.metadata.create_all(engine)  # Create tables
        return sessionmaker(bind=engine)  # Return session factory
    except Exception as e:
        print(f"Error setting up the database: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Database URL (SQLite for demonstration purposes)
    DATABASE_URL = 'sqlite:///insurance.db'

    # Setup the database and create a session
    Session = setup_database(DATABASE_URL)
    session = Session()

    try:
        # Example: Adding a new claimant
        new_claimant = Claimant(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="123-456-7890"
        )
        session.add(new_claimant)
        session.commit()

        # Example: Adding a new insurance claim
        new_claim = InsuranceClaim(
            claimant_id=new_claimant.id,
            claim_date="2023-10-01",
            claim_amount=5000.00,
            status=ClaimStatus.PENDING,
            description="Car accident claim"
        )
        session.add(new_claim)
        session.commit()

        print("Data added successfully!")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error occurred: {e}")
    finally:
        session.close()  # Close the session
```
