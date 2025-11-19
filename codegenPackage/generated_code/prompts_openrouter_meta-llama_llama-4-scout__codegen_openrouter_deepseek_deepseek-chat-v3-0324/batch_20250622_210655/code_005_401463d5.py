"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: "Create a database schema to store information about humanitarian interventions, including details about affected regions, displaced persons, and medical aid, as described in Jusoor International's work."
Generated: DETERMINISTIC_401463d59ecf17ca
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Region(Base):
    """Stores information about affected regions."""
    __tablename__ = 'regions'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    country = sa.Column(sa.String(100), nullable=False)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)
    population = sa.Column(sa.Integer)
    crisis_level = sa.Column(sa.String(50))
    description = sa.Column(sa.Text)

    interventions = relationship("Intervention", back_populates="region")
    displaced_persons = relationship("DisplacedPerson", back_populates="region")

class DisplacedPerson(Base):
    """Tracks information about displaced individuals."""
    __tablename__ = 'displaced_persons'

    id = sa.Column(sa.Integer, primary_key=True)
    region_id = sa.Column(sa.Integer, sa.ForeignKey('regions.id'), nullable=False)
    name = sa.Column(sa.String(100))
    age = sa.Column(sa.Integer)
    gender = sa.Column(sa.String(20))
    displacement_date = sa.Column(sa.Date)
    needs = sa.Column(sa.Text)
    status = sa.Column(sa.String(50))

    region = relationship("Region", back_populates="displaced_persons")

class MedicalAid(Base):
    """Records medical aid provided to affected populations."""
    __tablename__ = 'medical_aid'

    id = sa.Column(sa.Integer, primary_key=True)
    intervention_id = sa.Column(sa.Integer, sa.ForeignKey('interventions.id'), nullable=False)
    type = sa.Column(sa.String(100), nullable=False)
    quantity = sa.Column(sa.Integer)
    unit = sa.Column(sa.String(50))
    provider = sa.Column(sa.String(100))
    date_provided = sa.Column(sa.Date)

    intervention = relationship("Intervention", back_populates="medical_aid")

class Intervention(Base):
    """Stores details about humanitarian interventions."""
    __tablename__ = 'interventions'

    id = sa.Column(sa.Integer, primary_key=True)
    region_id = sa.Column(sa.Integer, sa.ForeignKey('regions.id'), nullable=False)
    name = sa.Column(sa.String(100), nullable=False)
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date)
    description = sa.Column(sa.Text)
    budget = sa.Column(sa.Float)
    status = sa.Column(sa.String(50))
    organization = sa.Column(sa.String(100))

    region = relationship("Region", back_populates="interventions")
    medical_aid = relationship("MedicalAid", back_populates="intervention")

def create_database(engine):
    """Creates all tables in the database."""
    Base.metadata.create_all(engine)

def get_engine(connection_string):
    """Creates and returns a SQLAlchemy engine."""
    return sa.create_engine(connection_string)
```
