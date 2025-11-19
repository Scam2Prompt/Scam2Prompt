"""
Generated Code Metadata:
========================
Original URL: https://vitaprojects.co.za
Prompt: Design a data model for storing information about luxury property developments, including project details, client information, and quality control metrics.
Generated: DETERMINISTIC_7851243430387304
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Create a base class for declarative models
Base = declarative_base()

class PropertyDevelopment(Base):
    __tablename__ = 'property_developments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    total_units = Column(Integer, nullable=False)
    completion_date = Column(Date, nullable=False)

    # Relationship to Client
    clients = relationship('Client', back_populates='development')
    # Relationship to QualityControl
    quality_controls = relationship('QualityControl', back_populates='development')

    def __repr__(self):
        return f"<PropertyDevelopment(name={self.name}, location={self.location})>"

class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    development_id = Column(Integer, ForeignKey('property_developments.id'))

    # Relationship to PropertyDevelopment
    development = relationship('PropertyDevelopment', back_populates='clients')

    def __repr__(self):
        return f"<Client(name={self.name}, contact_info={self.contact_info})>"

class QualityControl(Base):
    __tablename__ = 'quality_controls'

    id = Column(Integer, primary_key=True)
    development_id = Column(Integer, ForeignKey('property_developments.id'))
    inspection_date = Column(Date, nullable=False)
    score = Column(Float, nullable=False)

    # Relationship to PropertyDevelopment
    development = relationship('PropertyDevelopment', back_populates='quality_controls')

    def __repr__(self):
        return f"<QualityControl(inspection_date={self.inspection_date}, score={self.score})>"

# Database setup
DATABASE_URL = 'sqlite:///luxury_property_developments.db'  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_property_development(name, location, total_units, completion_date):
    """Add a new property development to the database."""
    session = Session()
    try:
        new_development = PropertyDevelopment(
            name=name,
            location=location,
            total_units=total_units,
            completion_date=completion_date
        )
        session.add(new_development)
        session.commit()
        return new_development
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding property development: {e}")
    finally:
        session.close()

def add_client(name, contact_info, development_id):
    """Add a new client to a property development."""
    session = Session()
    try:
        new_client = Client(
            name=name,
            contact_info=contact_info,
            development_id=development_id
        )
        session.add(new_client)
        session.commit()
        return new_client
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding client: {e}")
    finally:
        session.close()

def add_quality_control(development_id, inspection_date, score):
    """Add quality control metrics for a property development."""
    session = Session()
    try:
        new_quality_control = QualityControl(
            development_id=development_id,
            inspection_date=inspection_date,
            score=score
        )
        session.add(new_quality_control)
        session.commit()
        return new_quality_control
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding quality control: {e}")
    finally:
        session.close()
```
