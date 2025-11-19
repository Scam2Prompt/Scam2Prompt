"""
Generated Code Metadata:
========================
Original URL: https://aasteeldetailing.co.uk.steel-edge.co.uk
Prompt: "Design a data model for storing and managing steel detailing projects, including entities for take-off services, connection design, and supply chain solutions, and provide an example implementation in a programming language of your choice."
Generated: DETERMINISTIC_925cadc01d338be7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the Project entity
class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    take_off_services = relationship("TakeOffService", back_populates="project")
    connection_designs = relationship("ConnectionDesign", back_populates="project")
    supply_chain_solutions = relationship("SupplyChainSolution", back_populates="project")

# Define the TakeOffService entity
class TakeOffService(Base):
    __tablename__ = 'take_off_services'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    material_type = Column(String(255), nullable=False)
    quantity = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("Project", back_populates="take_off_services")

# Define the ConnectionDesign entity
class ConnectionDesign(Base):
    __tablename__ = 'connection_designs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    connection_type = Column(String(255), nullable=False)
    design_parameters = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("Project", back_populates="connection_designs")

# Define the SupplyChainSolution entity
class SupplyChainSolution(Base):
    __tablename__ = 'supply_chain_solutions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    supplier_name = Column(String(255), nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("Project", back_populates="supply_chain_solutions")

# Database setup
DATABASE_URL = "sqlite:///steel_detailing.db"  # Example using SQLite
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Example usage: Adding a new project with related entities
try:
    # Create a new project
    new_project = Project(name="Steel Detailing Project A", description="A sample project for steel detailing.")
    
    # Add take-off services
    new_project.take_off_services.append(TakeOffService(material_type="Steel Beam", quantity=100.5))
    new_project.take_off_services.append(TakeOffService(material_type="Steel Plate", quantity=50.0))
    
    # Add connection designs
    new_project.connection_designs.append(ConnectionDesign(connection_type="Bolted", design_parameters="Grade A bolts"))
    new_project.connection_designs.append(ConnectionDesign(connection_type="Welded", design_parameters="AWS D1.1 standards"))
    
    # Add supply chain solutions
    new_project.supply_chain_solutions.append(SupplyChainSolution(supplier_name="Supplier X", delivery_date=datetime(2023, 12, 15)))
    new_project.supply_chain_solutions.append(SupplyChainSolution(supplier_name="Supplier Y", delivery_date=datetime(2023, 12, 20)))
    
    # Commit the transaction
    session.add(new_project)
    session.commit()
    print("Project and related entities added successfully.")
except Exception as e:
    # Handle errors
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    # Close the session
    session.close()
```
