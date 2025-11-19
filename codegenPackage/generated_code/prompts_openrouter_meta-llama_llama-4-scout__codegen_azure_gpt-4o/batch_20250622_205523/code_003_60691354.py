"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Design a data model for storing information on community development projects, including details on vacant buildings, project goals, and outcomes, based on the Starke Orte Netzwerk's approach to gemeinwohlorientierte Bestandsentwicklung."
Generated: DETERMINISTIC_60691354f752ffd9
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Define the base class for the data model
Base = declarative_base()

# Define the VacantBuilding model
class VacantBuilding(Base):
    """
    Represents a vacant building in the community development project.
    """
    __tablename__ = 'vacant_buildings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(255), nullable=False)  # Address of the building
    size_in_sq_meters = Column(Float, nullable=False)  # Size of the building in square meters
    condition = Column(String(50), nullable=False)  # Condition of the building (e.g., "Good", "Needs Repair")
    description = Column(Text, nullable=True)  # Additional details about the building

    # Relationship to link the building to projects
    projects = relationship("Project", back_populates="vacant_building")

# Define the Project model
class Project(Base):
    """
    Represents a community development project.
    """
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # Name of the project
    goal = Column(Text, nullable=False)  # Project goals
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)  # Start date of the project
    end_date = Column(DateTime, nullable=True)  # End date of the project
    vacant_building_id = Column(Integer, ForeignKey('vacant_buildings.id'), nullable=False)  # Foreign key to VacantBuilding

    # Relationship to link the project to a vacant building
    vacant_building = relationship("VacantBuilding", back_populates="projects")

    # Relationship to link the project to outcomes
    outcomes = relationship("Outcome", back_populates="project")

# Define the Outcome model
class Outcome(Base):
    """
    Represents the outcomes of a community development project.
    """
    __tablename__ = 'outcomes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)  # Description of the outcome
    impact_score = Column(Float, nullable=False)  # Impact score of the outcome (e.g., 0-10 scale)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to Project

    # Relationship to link the outcome to a project
    project = relationship("Project", back_populates="outcomes")

# Database setup
def setup_database(database_url):
    """
    Sets up the database connection and creates tables if they don't exist.
    :param database_url: URL for the database connection (e.g., 'sqlite:///community_projects.db')
    """
    try:
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)  # Create tables
        return sessionmaker(bind=engine)  # Return a session factory
    except Exception as e:
        print(f"Error setting up the database: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Set up the database
    DATABASE_URL = 'sqlite:///community_projects.db'
    Session = setup_database(DATABASE_URL)

    # Create a new session
    session = Session()

    try:
        # Example: Add a vacant building
        building = VacantBuilding(
            address="123 Main Street",
            size_in_sq_meters=250.5,
            condition="Needs Repair",
            description="Old warehouse with potential for community use."
        )
        session.add(building)
        session.commit()

        # Example: Add a project linked to the building
        project = Project(
            name="Community Art Center",
            goal="Transform the vacant building into a space for local artists.",
            vacant_building_id=building.id
        )
        session.add(project)
        session.commit()

        # Example: Add an outcome for the project
        outcome = Outcome(
            description="Increased community engagement through art workshops.",
            impact_score=8.5,
            project_id=project.id
        )
        session.add(outcome)
        session.commit()

        print("Data added successfully!")
    except Exception as e:
        session.rollback()  # Rollback in case of error
        print(f"Error during database operation: {e}")
    finally:
        session.close()  # Close the session
```
