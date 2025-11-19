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
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create a base class for declarative models
Base = declarative_base()

# Define the SteelDetailingProject entity
class SteelDetailingProject(Base):
    __tablename__ = 'steel_detailing_projects'

    id = Column(Integer, primary_key=True)
    project_name = Column(String, nullable=False)
    take_off_service_id = Column(Integer, ForeignKey('take_off_services.id'))
    connection_design_id = Column(Integer, ForeignKey('connection_designs.id'))
    supply_chain_solution_id = Column(Integer, ForeignKey('supply_chain_solutions.id'))

    # Relationships
    take_off_service = relationship("TakeOffService")
    connection_design = relationship("ConnectionDesign")
    supply_chain_solution = relationship("SupplyChainSolution")

    def __repr__(self):
        return f"<SteelDetailingProject(id={self.id}, project_name='{self.project_name}')>"

# Define the TakeOffService entity
class TakeOffService(Base):
    __tablename__ = 'take_off_services'

    id = Column(Integer, primary_key=True)
    service_description = Column(String, nullable=False)

    def __repr__(self):
        return f"<TakeOffService(id={self.id}, service_description='{self.service_description}')>"

# Define the ConnectionDesign entity
class ConnectionDesign(Base):
    __tablename__ = 'connection_designs'

    id = Column(Integer, primary_key=True)
    design_description = Column(String, nullable=False)

    def __repr__(self):
        return f"<ConnectionDesign(id={self.id}, design_description='{self.design_description}')>"

# Define the SupplyChainSolution entity
class SupplyChainSolution(Base):
    __tablename__ = 'supply_chain_solutions'

    id = Column(Integer, primary_key=True)
    solution_description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)

    def __repr__(self):
        return f"<SupplyChainSolution(id={self.id}, solution_description='{self.solution_description}', cost={self.cost})>"

# Database setup
def setup_database(db_url='sqlite:///steel_detailing.db'):
    """Sets up the database and creates tables."""
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    return engine

# Example usage
def main():
    # Setup the database
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Example data creation
    try:
        # Create instances of services
        take_off_service = TakeOffService(service_description="Detailed take-off for steel components")
        connection_design = ConnectionDesign(design_description="Connection design for beams and columns")
        supply_chain_solution = SupplyChainSolution(solution_description="Logistics and supply chain management", cost=15000.00)

        # Add services to the session
        session.add(take_off_service)
        session.add(connection_design)
        session.add(supply_chain_solution)
        session.commit()

        # Create a steel detailing project
        project = SteelDetailingProject(project_name="Project Alpha",
                                         take_off_service=take_off_service,
                                         connection_design=connection_design,
                                         supply_chain_solution=supply_chain_solution)

        # Add project to the session
        session.add(project)
        session.commit()

        print("Project created successfully:", project)

    except Exception as e:
        session.rollback()
        print("An error occurred:", e)
    finally:
        session.close()

if __name__ == "__main__":
    main()
```
