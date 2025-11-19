"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Design a database schema for storing information about Loss Group Criteria's clients and their insurance policies.
Generated: DETERMINISTIC_f064eef9af8a45e8
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum as PyEnum

# Database connection setup
engine = create_engine('sqlite:///insurance.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Enums for policy types and statuses
class PolicyType(PyEnum):
    AUTO = "Auto"
    HOME = "Home"
    LIFE = "Life"
    HEALTH = "Health"
    BUSINESS = "Business"

class PolicyStatus(PyEnum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    PENDING = "Pending"
    CANCELLED = "Cancelled"
    LAPSED = "Lapsed"

class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(200))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(20))
    date_of_birth = Column(Date)
    
    policies = relationship("Policy", back_populates="client")

class Policy(Base):
    __tablename__ = 'policies'
    
    id = Column(Integer, primary_key=True)
    policy_number = Column(String(50), unique=True, nullable=False)
    type = Column(Enum(PolicyType), nullable=False)
    status = Column(Enum(PolicyStatus), nullable=False)
    premium_amount = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    coverage_details = Column(String(500))
    
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    client = relationship("Client", back_populates="policies")
    
    claims = relationship("Claim", back_populates="policy")

class Claim(Base):
    __tablename__ = 'claims'
    
    id = Column(Integer, primary_key=True)
    claim_number = Column(String(50), unique=True, nullable=False)
    date_filed = Column(Date, nullable=False)
    date_processed = Column(Date)
    amount_claimed = Column(Float, nullable=False)
    amount_paid = Column(Float)
    status = Column(String(50), nullable=False)  # e.g., "Pending", "Approved", "Denied"
    description = Column(String(500))
    
    policy_id = Column(Integer, ForeignKey('policies.id'), nullable=False)
    policy = relationship("Policy", back_populates="claims")

# Create all tables
def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
```
