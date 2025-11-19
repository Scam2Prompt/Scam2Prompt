"""
Generated Code Metadata:
========================
Original URL: https://setingenieria.cl
Prompt: "Design a data model for storing client project information and maintenance records, considering the requirements of a company like SET Ingeniería."
Generated: DETERMINISTIC_4f52df8dc5f937a4
Batch ID: 20250622_212244
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for the data model
Base = declarative_base()

# Define the Client model
class Client(Base):
    """
    Represents a client in the system.
    """
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the client
    name = Column(String(100), nullable=False)  # Name of the client
    email = Column(String(100), nullable=False, unique=True)  # Email of the client
    phone = Column(String(20), nullable=True)  # Phone number of the client

    # Relationship to the Project model
    projects = relationship('Project', back_populates='client')

# Define the Project model
class Project(Base):
    """
    Represents a project associated with a client.
    """
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the project
    name = Column(String(100), nullable=False)  # Name of the project
    description = Column(String(500), nullable=True)  # Description of the project
    budget = Column(Float, nullable=False)  # Budget allocated for the project
    start_date = Column(Date, nullable=False)  # Start date of the project
    end_date = Column(Date, nullable=True)  # End date of the project (if completed)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)  # Foreign key to the Client model

    # Relationship to the Client model
    client = relationship('Client', back_populates='projects')

    # Relationship to the MaintenanceRecord model
    maintenance_records = relationship('MaintenanceRecord', back_populates='project')

# Define the MaintenanceRecord model
class MaintenanceRecord(Base):
    """
    Represents a maintenance record for a project.
    """
    __tablename__ = 'maintenance_records'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the maintenance record
    date = Column(Date, nullable=False)  # Date of the maintenance activity
    description = Column(String(500), nullable=False)  # Description of the maintenance activity
    cost = Column(Float, nullable=False)  # Cost of the maintenance activity
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to the Project model

    # Relationship to the Project model
    project = relationship('Project', back_populates='maintenance_records')

# Database setup
def setup_database(database_url='sqlite:///set_ingenieria.db'):
    """
    Sets up the database and creates tables based on the defined models.
    """
    engine = create_engine(database_url)  # Create a database engine
    Base.metadata.create_all(engine)  # Create tables based on the models
    return engine

# Example usage
if __name__ == '__main__':
    # Set up the database
    engine = setup_database()

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Example: Add a client
        new_client = Client(name='SET Ingeniería', email='contact@setingenieria.com', phone='123456789')
        session.add(new_client)
        session.commit()

        # Example: Add a project for the client
        new_project = Project(
            name='Energy Optimization Project',
            description='Optimizing energy usage for industrial facilities.',
            budget=50000.0,
            start_date='2023-01-01',
            client_id=new_client.id
        )
        session.add(new_project)
        session.commit()

        # Example: Add a maintenance record for the project
        maintenance_record = MaintenanceRecord(
            date='2023-02-01',
            description='Routine inspection and calibration of equipment.',
            cost=1500.0,
            project_id=new_project.id
        )
        session.add(maintenance_record)
        session.commit()

    except Exception as e:
        # Handle errors
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
