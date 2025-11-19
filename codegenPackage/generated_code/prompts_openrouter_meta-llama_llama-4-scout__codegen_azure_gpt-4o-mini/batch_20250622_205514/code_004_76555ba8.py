"""
Generated Code Metadata:
========================
Original URL: https://cecd33.fr
Prompt: "Develop a data model or schema to store information about mechanical engineering projects, including project phases, client details, and product specifications, inspired by CECD 33's project management approach."
Generated: DETERMINISTIC_76555ba8ea950e65
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Create a base class for declarative models
Base = declarative_base()

class Client(Base):
    """Model to store client details."""
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(String(255), nullable=True)

    projects = relationship("Project", back_populates="client")

class Project(Base):
    """Model to store project information."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    client = relationship("Client", back_populates="projects")
    phases = relationship("ProjectPhase", back_populates="project")
    specifications = relationship("ProductSpecification", back_populates="project")

class ProjectPhase(Base):
    """Model to store project phases."""
    __tablename__ = 'project_phases'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    project = relationship("Project", back_populates="phases")

class ProductSpecification(Base):
    """Model to store product specifications."""
    __tablename__ = 'product_specifications'

    id = Column(Integer, primary_key=True)
    specification_detail = Column(Text, nullable=False)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)

    project = relationship("Project", back_populates="specifications")

# Database connection setup
DATABASE_URL = "sqlite:///mechanical_engineering_projects.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_client(name, contact_info=None):
    """Add a new client to the database."""
    session = Session()
    try:
        new_client = Client(name=name, contact_info=contact_info)
        session.add(new_client)
        session.commit()
        return new_client
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding client: {e}")
    finally:
        session.close()

def add_project(name, description, client_id):
    """Add a new project to the database."""
    session = Session()
    try:
        new_project = Project(name=name, description=description, client_id=client_id)
        session.add(new_project)
        session.commit()
        return new_project
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding project: {e}")
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    client = add_client("ABC Engineering", "contact@abcengineering.com")
    if client:
        project = add_project("Project X", "Description of Project X", client.id)
        print(f"Added project: {project.name} for client: {client.name}")
```
