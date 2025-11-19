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
# Import required libraries
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum
from datetime import datetime

# Define database connection URL
DATABASE_URL = 'sqlite:///soccer_academy_volunteers.db'

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define an Enum for areas of interest
class AreaOfInterest(PyEnum):
    COACHING = 'coaching'
    ADMINISTRATION = 'administration'
    FUNDRAISING = 'fundraising'
    OTHER = 'other'

# Define an Enum for volunteer availability
class Availability(PyEnum):
    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

# Define the Volunteer class
class Volunteer(Base):
    """
    Represents a soccer academy volunteer.

    Attributes:
        id (int): Unique identifier for the volunteer.
        name (str): Name of the volunteer.
        email (str): Email address of the volunteer.
        phone_number (str): Phone number of the volunteer.
        availability (list): List of days the volunteer is available.
        areas_of_interest (list): List of areas the volunteer is interested in.
    """
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False)

    # Define a many-to-many relationship for availability
    volunteer_availability = Column(String)

    # Define a many-to-many relationship for areas of interest
    volunteer_areas_of_interest = Column(String)

    def __repr__(self):
        return f"Volunteer(name='{self.name}', email='{self.email}')"

# Define the Availability class
class VolunteerAvailability(Base):
    """
    Represents a volunteer's availability.

    Attributes:
        id (int): Unique identifier for the volunteer availability.
        volunteer_id (int): Foreign key referencing the Volunteer class.
        day (str): Day of the week the volunteer is available.
    """
    __tablename__ = 'volunteer_availability'

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, Column(Integer, ForeignKey('volunteers.id')))
    day = Column(Enum(Availability))

    def __repr__(self):
        return f"VolunteerAvailability(volunteer_id={self.volunteer_id}, day='{self.day}')"

# Define the AreaOfInterest class
class VolunteerAreaOfInterest(Base):
    """
    Represents a volunteer's area of interest.

    Attributes:
        id (int): Unique identifier for the volunteer area of interest.
        volunteer_id (int): Foreign key referencing the Volunteer class.
        area (str): Area the volunteer is interested in.
    """
    __tablename__ = 'volunteer_areas_of_interest'

    id = Column(Integer, primary_key=True)
    volunteer_id = Column(Integer, Column(Integer, ForeignKey('volunteers.id')))
    area = Column(Enum(AreaOfInterest))

    def __repr__(self):
        return f"VolunteerAreaOfInterest(volunteer_id={self.volunteer_id}, area='{self.area}')"

# Create all tables in the engine
Base.metadata.create_all(engine)

def create_volunteer(session, name, email, phone_number):
    """
    Creates a new volunteer.

    Args:
        session: SQLAlchemy session.
        name (str): Name of the volunteer.
        email (str): Email address of the volunteer.
        phone_number (str): Phone number of the volunteer.

    Returns:
        Volunteer: The newly created volunteer.
    """
    volunteer = Volunteer(name=name, email=email, phone_number=phone_number)
    session.add(volunteer)
    session.commit()
    return volunteer

def add_volunteer_availability(session, volunteer_id, day):
    """
    Adds a volunteer's availability.

    Args:
        session: SQLAlchemy session.
        volunteer_id (int): ID of the volunteer.
        day (str): Day of the week the volunteer is available.

    Returns:
        VolunteerAvailability: The newly created volunteer availability.
    """
    volunteer_availability = VolunteerAvailability(volunteer_id=volunteer_id, day=day)
    session.add(volunteer_availability)
    session.commit()
    return volunteer_availability

def add_volunteer_area_of_interest(session, volunteer_id, area):
    """
    Adds a volunteer's area of interest.

    Args:
        session: SQLAlchemy session.
        volunteer_id (int): ID of the volunteer.
        area (str): Area the volunteer is interested in.

    Returns:
        VolunteerAreaOfInterest: The newly created volunteer area of interest.
    """
    volunteer_area_of_interest = VolunteerAreaOfInterest(volunteer_id=volunteer_id, area=area)
    session.add(volunteer_area_of_interest)
    session.commit()
    return volunteer_area_of_interest

def main():
    # Create a new session
    session = Session()

    try:
        # Create a new volunteer
        volunteer = create_volunteer(session, 'John Doe', 'john@example.com', '123-456-7890')

        # Add volunteer's availability
        add_volunteer_availability(session, volunteer.id, Availability.MONDAY)
        add_volunteer_availability(session, volunteer.id, Availability.TUESDAY)

        # Add volunteer's areas of interest
        add_volunteer_area_of_interest(session, volunteer.id, AreaOfInterest.COACHING)
        add_volunteer_area_of_interest(session, volunteer.id, AreaOfInterest.ADMINISTRATION)

        # Query volunteers
        volunteers = session.query(Volunteer).all()
        for v in volunteers:
            print(v)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the session
        session.close()

if __name__ == '__main__':
    main()
```
