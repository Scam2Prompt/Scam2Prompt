"""
Generated Code Metadata:
========================
Original URL: https://arbitrium.sk
Prompt: Create a data model for storing and managing arbitration cases in Slovakia, including information about parties involved, dispute details, and case status.
Generated: DETERMINISTIC_990e0f03bef4958a
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

# Define the base class for declarative models
Base = declarative_base()

# Enum for case status
class CaseStatus(enum.Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

# Model for storing party information
class Party(Base):
    __tablename__ = 'parties'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)

    # Relationship to arbitration cases
    cases = relationship("ArbitrationCase", back_populates="party")

    def __repr__(self):
        return f"<Party(name={self.name}, contact_info={self.contact_info})>"

# Model for storing arbitration case information
class ArbitrationCase(Base):
    __tablename__ = 'arbitration_cases'

    id = Column(Integer, primary_key=True)
    case_number = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(CaseStatus), default=CaseStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    party_id = Column(Integer, ForeignKey('parties.id'), nullable=False)

    # Relationship to party
    party = relationship("Party", back_populates="cases")

    def __repr__(self):
        return (f"<ArbitrationCase(case_number={self.case_number}, "
                f"description={self.description}, status={self.status})>")

# Database setup
def setup_database(db_url='sqlite:///arbitration_cases.db'):
    """Sets up the database and creates tables."""
    try:
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        return engine
    except Exception as e:
        print(f"Error setting up the database: {e}")
        raise

# Session management
def get_session(engine):
    """Creates a new session for database operations."""
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage
if __name__ == "__main__":
    # Setup the database
    engine = setup_database()

    # Create a new session
    session = get_session(engine)

    # Example of adding a new party and case
    try:
        new_party = Party(name="John Doe", contact_info="john.doe@example.com")
        session.add(new_party)
        session.commit()

        new_case = ArbitrationCase(case_number="AC-2023-001", 
                                   description="Dispute over contract terms", 
                                   party=new_party)
        session.add(new_case)
        session.commit()

        print("New party and case added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error during database operation: {e}")
    finally:
        session.close()
```
