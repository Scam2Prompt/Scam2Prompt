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
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a base class for declarative models
Base = declarative_base()

class Client(Base):
    """Model representing a client."""
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    projects = relationship("Project", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.id}, name={self.name}, email={self.email})>"

class Project(Base):
    """Model representing a project associated with a client."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    maintenance_records = relationship("MaintenanceRecord", back_populates="project")
    client = relationship("Client", back_populates="projects")

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, start_date={self.start_date}, end_date={self.end_date})>"

class MaintenanceRecord(Base):
    """Model representing maintenance records for a project."""
    __tablename__ = 'maintenance_records'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    maintenance_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    project = relationship("Project", back_populates="maintenance_records")

    def __repr__(self):
        return f"<MaintenanceRecord(id={self.id}, project_id={self.project_id}, maintenance_date={self.maintenance_date})>"

# Database setup
DATABASE_URL = "sqlite:///set_ingenieria.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_client(name, email):
    """Add a new client to the database."""
    session = Session()
    try:
        new_client = Client(name=name, email=email)
        session.add(new_client)
        session.commit()
        logger.info(f"Client added: {new_client}")
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding client: {e}")
    finally:
        session.close()

def add_project(client_id, name, start_date, end_date=None):
    """Add a new project for a specific client."""
    session = Session()
    try:
        new_project = Project(client_id=client_id, name=name, start_date=start_date, end_date=end_date)
        session.add(new_project)
        session.commit()
        logger.info(f"Project added: {new_project}")
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding project: {e}")
    finally:
        session.close()

def add_maintenance_record(project_id, maintenance_date, description):
    """Add a maintenance record for a specific project."""
    session = Session()
    try:
        new_record = MaintenanceRecord(project_id=project_id, maintenance_date=maintenance_date, description=description)
        session.add(new_record)
        session.commit()
        logger.info(f"Maintenance record added: {new_record}")
    except SQLAlchemyError as e:
        session.rollback()
        logger.error(f"Error adding maintenance record: {e}")
    finally:
        session.close()
```
