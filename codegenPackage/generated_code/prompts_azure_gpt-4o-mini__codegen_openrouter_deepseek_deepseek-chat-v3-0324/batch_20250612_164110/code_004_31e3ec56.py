"""
Generated Code Metadata:
========================
Original URL: https://trattar.blogspot.com
Prompt: Illustrate how to implement a database schema for managing wood treatment projects, including fields for wood type, treatment method, and environmental compliance.
Generated: DETERMINISTIC_31e3ec569d60839e
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Database Schema for Wood Treatment Projects Management

```python
from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum as SQLEnum, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class WoodType(str, Enum):
    PINE = "pine"
    OAK = "oak"
    MAPLE = "maple"
    CEDAR = "cedar"
    REDWOOD = "redwood"
    WALNUT = "walnut"
    CHERRY = "cherry"
    MAHOGANY = "mahogany"

class TreatmentMethod(str, Enum):
    PRESSURE_TREATED = "pressure_treated"
    THERMALLY_MODIFIED = "thermally_modified"
    ACETYLATION = "acetylation"
    OIL_TREATMENT = "oil_treatment"
    BORATE_TREATMENT = "borate_treatment"
    CREOSOTE = "creosote"
    COPPER_NAPTHENATE = "copper_naphthenate"

class ComplianceStatus(str, Enum):
    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PENDING_REVIEW = "pending_review"
    EXEMPT = "exempt"

class Project(Base):
    """Database model for wood treatment projects."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    budget = Column(Float)
    
    # Relationships
    wood_entries = relationship("WoodEntry", back_populates="project", cascade="all, delete-orphan")
    treatments = relationship("TreatmentRecord", back_populates="project", cascade="all, delete-orphan")
    compliance_records = relationship("ComplianceRecord", back_populates="project", cascade="all, delete-orphan")

class WoodEntry(Base):
    """Database model for wood inventory entries."""
    __tablename__ = 'wood_entries'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    wood_type = Column(SQLEnum(WoodType), nullable=False)
    quantity = Column(Float, nullable=False)  # in board feet
    source = Column(String(100))
    acquisition_date = Column(DateTime, default=datetime.utcnow)
    quality_grade = Column(String(50))
    
    # Relationships
    project = relationship("Project", back_populates="wood_entries")

class TreatmentRecord(Base):
    """Database model for treatment process records."""
    __tablename__ = 'treatment_records'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    method = Column(SQLEnum(TreatmentMethod), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    temperature = Column(Float)  # in Celsius
    pressure = Column(Float)     # in PSI
    chemical_concentration = Column(Float)
    technician = Column(String(100))
    notes = Column(String(500))
    
    # Relationships
    project = relationship("Project", back_populates="treatments")

class ComplianceRecord(Base):
    """Database model for environmental compliance records."""
    __tablename__ = 'compliance_records'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    regulation_standard = Column(String(100), nullable=False)
    status = Column(SQLEnum(ComplianceStatus), default=ComplianceStatus.PENDING_REVIEW)
    inspection_date = Column(DateTime, default=datetime.utcnow)
    inspector = Column(String(100))
    report_reference = Column(String(100))
    notes = Column(String(500))
    
    # Relationships
    project = relationship("Project", back_populates="compliance_records")

class DatabaseManager:
    """Handles database connections and operations."""
    
    def __init__(self, db_url: str = "sqlite:///wood_treatment.db"):
        """Initialize database connection."""
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        
    def create_tables(self):
        """Create all database tables."""
        Base.metadata.create_all(self.engine)
        
    def drop_tables(self):
        """Drop all database tables."""
        Base.metadata.drop_all(self.engine)
        
    def get_session(self):
        """Return a new database session."""
        return self.Session()
        
    def add_project(self, name: str, description: Optional[str] = None, budget: Optional[float] = None) -> Project:
        """Add a new project to the database."""
        session = self.get_session()
        try:
            project = Project(name=name, description=description, budget=budget)
            session.add(project)
            session.commit()
            return project
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()

# Example usage
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.create_tables()
    
    # Create a sample project
    project = db_manager.add_project(
        name="Oak Decking Treatment",
        description="Pressure treatment of oak decking materials",
        budget=15000.00
    )
    print(f"Created project with ID: {project.id}")
```
