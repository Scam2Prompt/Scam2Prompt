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
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Initialize the base class for declarative models
Base = declarative_base()

# Define the Client model
class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique client ID
    name = Column(String(100), nullable=False)  # Client name
    contact_email = Column(String(100), nullable=False)  # Client contact email
    phone_number = Column(String(20), nullable=True)  # Client phone number
    address = Column(Text, nullable=True)  # Client address
    
    # Relationship to link projects to clients
    projects = relationship("Project", back_populates="client")

# Define the Project model
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique project ID
    name = Column(String(100), nullable=False)  # Project name
    description = Column(Text, nullable=True)  # Project description
    start_date = Column(Date, nullable=False)  # Project start date
    end_date = Column(Date, nullable=True)  # Project end date
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)  # Foreign key to Client
    
    # Relationship to link client to projects
    client = relationship("Client", back_populates="projects")
    # Relationship to link phases to projects
    phases = relationship("ProjectPhase", back_populates="project")
    # Relationship to link specifications to projects
    specifications = relationship("ProductSpecification", back_populates="project")

# Define the ProjectPhase model
class ProjectPhase(Base):
    __tablename__ = 'project_phases'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique phase ID
    name = Column(String(100), nullable=False)  # Phase name
    description = Column(Text, nullable=True)  # Phase description
    start_date = Column(Date, nullable=False)  # Phase start date
    end_date = Column(Date, nullable=True)  # Phase end date
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to Project
    
    # Relationship to link project to phases
    project = relationship("Project", back_populates="phases")

# Define the ProductSpecification model
class ProductSpecification(Base):
    __tablename__ = 'product_specifications'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique specification ID
    name = Column(String(100), nullable=False)  # Specification name
    value = Column(String(100), nullable=False)  # Specification value
    unit = Column(String(50), nullable=True)  # Unit of measurement
    description = Column(Text, nullable=True)  # Specification description
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)  # Foreign key to Project
    
    # Relationship to link project to specifications
    project = relationship("Project", back_populates="specifications")

# Database setup
def setup_database(database_url):
    """
    Sets up the database connection and creates tables.
    
    Args:
        database_url (str): The database connection string.
    """
    try:
        engine = create_engine(database_url, echo=True)  # Create database engine
        Base.metadata.create_all(engine)  # Create tables based on models
        return sessionmaker(bind=engine)  # Return session factory
    except Exception as e:
        print(f"Error setting up the database: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Replace with your actual database URL
    DATABASE_URL = "sqlite:///engineering_projects.db"
    
    # Setup the database and create a session
    Session = setup_database(DATABASE_URL)
    session = Session()
    
    try:
        # Example: Adding a client
        new_client = Client(name="ABC Engineering", contact_email="contact@abcengineering.com")
        session.add(new_client)
        session.commit()
        print("Client added successfully!")
    except Exception as e:
        print(f"Error during database operation: {e}")
        session.rollback()
    finally:
        session.close()
```
