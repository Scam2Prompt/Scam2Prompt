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
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create a base class for declarative models
Base = declarative_base()

class Volunteer(Base):
    __tablename__ = 'volunteers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    availability = Column(String, nullable=False)  # e.g., "Weekends", "Weekdays"
    areas_of_interest = Column(String, nullable=True)  # e.g., "Coaching, Refereeing"

    def __repr__(self):
        return f"<Volunteer(name={self.name}, email={self.email})>"

# Database connection setup
DATABASE_URL = "sqlite:///soccer_academy_volunteers.db"  # Change to your preferred database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

def add_volunteer(name, email, phone, availability, areas_of_interest):
    """Add a new volunteer to the database."""
    session = Session()
    try:
        new_volunteer = Volunteer(
            name=name,
            email=email,
            phone=phone,
            availability=availability,
            areas_of_interest=areas_of_interest
        )
        session.add(new_volunteer)
        session.commit()
        print(f"Volunteer {name} added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding volunteer: {e}")
    finally:
        session.close()

def get_volunteers():
    """Retrieve all volunteers from the database."""
    session = Session()
    try:
        volunteers = session.query(Volunteer).all()
        return volunteers
    except Exception as e:
        print(f"Error retrieving volunteers: {e}")
        return []
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    # Uncomment the following line to add a volunteer
    # add_volunteer("John Doe", "john.doe@example.com", "123-456-7890", "Weekends", "Coaching")

    # Retrieve and print all volunteers
    volunteers = get_volunteers()
    for volunteer in volunteers:
        print(volunteer)
```
