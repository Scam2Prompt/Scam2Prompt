"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Generate code to model a database schema for tracking humanitarian aid projects, including categories like "mosquito fogging campaigns," "monthly financial assistance," and "water well drilling," as outlined on the Gulf and Aden website.
Generated: DETERMINISTIC_d8ba76552b55d1c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum as PyEnum

# Define the database connection
DATABASE_URI = 'sqlite:///humanitarian_aid.db'  # Using SQLite for simplicity; replace with your DB URI in production
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define enums for project types and statuses
class ProjectType(PyEnum):
    MOSQUITO_FOGGING = "mosquito fogging campaigns"
    FINANCIAL_ASSISTANCE = "monthly financial assistance"
    WATER_WELL_DRILLING = "water well drilling"
    OTHER = "other"

class ProjectStatus(PyEnum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

# Define the Organization model
class Organization(Base):
    __tablename__ = 'organizations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    contact_email = Column(String(100))
    contact_phone = Column(String(20))
    
    projects = relationship("Project", back_populates="organization")

# Define the Project model
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    project_type = Column(Enum(ProjectType), nullable=False)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.PLANNED)
    start_date = Column(Date)
    end_date = Column(Date)
    budget = Column(Float)
    location = Column(String(100))
    
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    organization = relationship("Organization", back_populates="projects")
    
    beneficiaries = relationship("Beneficiary", back_populates="project")
    donations = relationship("Donation", back_populates="project")

# Define the Beneficiary model
class Beneficiary(Base):
    __tablename__ = 'beneficiaries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(String(100))
    beneficiary_type = Column(String(50))  # e.g., individual, family, community
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="beneficiaries")

# Define the Donation model
class Donation(Base):
    __tablename__ = 'donations'
    
    id = Column(Integer, primary_key=True)
    donor_name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    donation_date = Column(Date, nullable=False)
    donation_type = Column(String(50))  # e.g., cash, in-kind
    
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship("Project", back_populates="donations")

# Create all tables in the database
def initialize_database():
    Base.metadata.create_all(engine)

# Example usage
if __name__ == "__main__":
    initialize_database()
    print("Database tables created successfully.")
```
