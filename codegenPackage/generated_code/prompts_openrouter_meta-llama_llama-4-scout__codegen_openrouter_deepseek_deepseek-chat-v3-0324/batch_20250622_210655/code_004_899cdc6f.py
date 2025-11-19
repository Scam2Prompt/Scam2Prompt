"""
Generated Code Metadata:
========================
Original URL: https://jsa.academy
Prompt: "Design a database schema for storing information about soccer academy volunteers, including their contact details, availability, and areas of interest, using a library like SQLAlchemy."
Generated: DETERMINISTIC_899cdc6fc19ff9da
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import time
from enum import Enum
from sqlalchemy import (
    Column,
    DateTime,
    Enum as SQLAlchemyEnum,
    ForeignKey,
    Integer,
    String,
    Table,
    Time,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from typing import List, Optional

Base = declarative_base()

# Association table for many-to-many relationship between Volunteer and InterestArea
volunteer_interest_association = Table(
    'volunteer_interest_association',
    Base.metadata,
    Column('volunteer_id', Integer, ForeignKey('volunteers.id')),
    Column('interest_area_id', Integer, ForeignKey('interest_areas.id')),
)

class AvailabilityDay(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class Availability(Base):
    __tablename__ = 'availabilities'

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, ForeignKey('volunteers.id'))
    day = Column(SQLAlchemyEnum(AvailabilityDay), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    volunteer = relationship("Volunteer", back_populates="availabilities")

class InterestArea(Base):
    __tablename__ = 'interest_areas'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255))

    volunteers = relationship(
        "Volunteer",
        secondary=volunteer_interest_association,
        back_populates="interest_areas"
    )

class Volunteer(Base):
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    address = Column(String(200))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(50))
    registration_date = Column(DateTime, nullable=False)
    notes = Column(String(500))

    availabilities = relationship(
        "Availability",
        back_populates="volunteer",
        cascade="all, delete-orphan"
    )
    interest_areas = relationship(
        "InterestArea",
        secondary=volunteer_interest_association,
        back_populates="volunteers"
    )

def init_db(database_url: str = "sqlite:///soccer_academy.db"):
    """Initialize the database and create tables."""
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return engine

def create_session(engine):
    """Create a new database session."""
    Session = sessionmaker(bind=engine)
    return Session()

def add_sample_data(session):
    """Add sample data to the database for testing."""
    # Create interest areas
    coaching = InterestArea(name="Coaching", description="Helping with training sessions")
    admin = InterestArea(name="Administration", description="Office and paperwork tasks")
    events = InterestArea(name="Events", description="Organizing matches and tournaments")

    # Create volunteers
    volunteer1 = Volunteer(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        registration_date="2023-01-15 10:00:00",
        interest_areas=[coaching, events]
    )

    volunteer2 = Volunteer(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        phone="+1987654321",
        registration_date="2023-02-20 14:30:00",
        interest_areas=[admin]
    )

    # Add availabilities
    volunteer1.availabilities.extend([
        Availability(day=AvailabilityDay.MONDAY, start_time=time(9, 0), end_time=time(12, 0)),
        Availability(day=AvailabilityDay.WEDNESDAY, start_time=time(14, 0), end_time=time(17, 0))
    ])

    volunteer2.availabilities.extend([
        Availability(day=AvailabilityDay.TUESDAY, start_time=time(10, 0), end_time=time(15, 0)),
        Availability(day=AvailabilityDay.FRIDAY, start_time=time(9, 0), end_time=time(12, 0))
    ])

    session.add_all([coaching, admin, events, volunteer1, volunteer2])
    session.commit()

if __name__ == "__main__":
    engine = init_db()
    session = create_session(engine)
    add_sample_data(session)
```
