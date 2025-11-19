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
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

# Base class for SQLAlchemy models
Base = declarative_base()

# Data model for luxury property developments
class Project(Base):
    __tablename__ = 'projects'

    # Primary key for the project
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # Name of the project
    location = Column(String(255), nullable=False)  # Location of the project
    start_date = Column(DateTime, nullable=False)  # Project start date
    end_date = Column(DateTime, nullable=True)  # Project end date
    budget = Column(Float, nullable=False)  # Budget for the project

    # Relationship to clients
    clients = relationship("Client", back_populates="project")

    # Relationship to quality control metrics
    quality_metrics = relationship("QualityControl", back_populates="project")

class Client(Base):
    __tablename__ = 'clients'

    # Primary key for the client
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)  # Name of the client
    email = Column(String(255), nullable=False, unique=True)  # Email of the client
    phone = Column(String(20), nullable=True)  # Phone number of the client
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to the project

    # Relationship to the project
    project = relationship("Project", back_populates="clients")

class QualityControl(Base):
    __tablename__ = 'quality_control'

    # Primary key for the quality control metric
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to the project
    metric_name = Column(String(255), nullable=False)  # Name of the quality control metric
    metric_value = Column(Float, nullable=False)  # Value of the metric
    passed = Column(Boolean, nullable=False)  # Whether the metric passed or failed
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)  # Timestamp of the metric evaluation

    # Relationship to the project
    project = relationship("Project", back_populates="quality_metrics")

# Database setup
def setup_database():
    """
    Sets up the database connection and creates tables if they don't exist.
    """
    engine = create_engine('sqlite:///luxury_properties.db')  # SQLite database connection
    Base.metadata.create_all(engine)  # Create tables based on the defined models
    return sessionmaker(bind=engine)  # Return a session factory

# Example usage
if __name__ == "__main__":
    # Initialize the database session
    Session = setup_database()
    session = Session()

    try:
        # Create a new project
        new_project = Project(
            name="Luxury Villas",
            location="Beverly Hills, CA",
            start_date=datetime.datetime(2023, 1, 1),
            budget=5000000.00
        )
        session.add(new_project)
        session.commit()

        # Add a client to the project
        client = Client(
            name="John Doe",
            email="john.doe@example.com",
            phone="123-456-7890",
            project_id=new_project.id
        )
        session.add(client)
        session.commit()

        # Add a quality control metric to the project
        qc_metric = QualityControl(
            project_id=new_project.id,
            metric_name="Foundation Inspection",
            metric_value=95.5,
            passed=True
        )
        session.add(qc_metric)
        session.commit()

        print("Data successfully added to the database.")
    except Exception as e:
        # Handle any errors that occur during database operations
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
