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
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Base class for SQLAlchemy models
Base = declarative_base()

# Association table for many-to-many relationship between volunteers and areas of interest
volunteer_interest_association = Table(
    'volunteer_interest_association',
    Base.metadata,
    Column('volunteer_id', Integer, ForeignKey('volunteers.id'), primary_key=True),
    Column('interest_id', Integer, ForeignKey('interests.id'), primary_key=True)
)

class Volunteer(Base):
    """
    Represents a volunteer in the soccer academy.
    """
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=True)
    is_available = Column(Boolean, default=True)  # Indicates if the volunteer is currently available

    # Many-to-many relationship with areas of interest
    interests = relationship(
        'Interest',
        secondary=volunteer_interest_association,
        back_populates='volunteers'
    )

    def __repr__(self):
        return f"<Volunteer(id={self.id}, name={self.first_name} {self.last_name}, email={self.email})>"

class Interest(Base):
    """
    Represents an area of interest for volunteers.
    """
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    # Many-to-many relationship with volunteers
    volunteers = relationship(
        'Volunteer',
        secondary=volunteer_interest_association,
        back_populates='interests'
    )

    def __repr__(self):
        return f"<Interest(id={self.id}, name={self.name})>"

# Database setup
def setup_database():
    """
    Sets up the database and creates tables.
    """
    engine = create_engine('sqlite:///soccer_academy.db')  # Replace with your database URL
    Base.metadata.create_all(engine)
    return engine

# Example usage
if __name__ == "__main__":
    # Initialize the database
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Add sample data
        interest1 = Interest(name="Coaching")
        interest2 = Interest(name="Event Management")
        volunteer1 = Volunteer(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="123-456-7890",
            is_available=True,
            interests=[interest1, interest2]
        )
        session.add(volunteer1)
        session.commit()

        # Query and print data
        volunteers = session.query(Volunteer).all()
        for volunteer in volunteers:
            print(volunteer)
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()
```
