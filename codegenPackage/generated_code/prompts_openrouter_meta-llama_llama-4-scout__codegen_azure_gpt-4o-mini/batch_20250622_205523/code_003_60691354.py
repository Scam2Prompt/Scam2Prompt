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
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# Create a base class for declarative models
Base = declarative_base()

class CommunityProject(Base):
    __tablename__ = 'community_projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, default=datetime.utcnow)
    end_date = Column(Date, nullable=True)
    goals = relationship("ProjectGoal", back_populates="project")
    outcomes = relationship("ProjectOutcome", back_populates="project")

    def __repr__(self):
        return f"<CommunityProject(name={self.name}, start_date={self.start_date})>"

class ProjectGoal(Base):
    __tablename__ = 'project_goals'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('community_projects.id'), nullable=False)
    goal_description = Column(Text, nullable=False)
    project = relationship("CommunityProject", back_populates="goals")

    def __repr__(self):
        return f"<ProjectGoal(goal_description={self.goal_description})>"

class ProjectOutcome(Base):
    __tablename__ = 'project_outcomes'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('community_projects.id'), nullable=False)
    outcome_description = Column(Text, nullable=False)
    project = relationship("CommunityProject", back_populates="outcomes")

    def __repr__(self):
        return f"<ProjectOutcome(outcome_description={self.outcome_description})>"

class VacantBuilding(Base):
    __tablename__ = 'vacant_buildings'

    id = Column(Integer, primary_key=True)
    address = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)  # e.g., 'available', 'under renovation'
    project_id = Column(Integer, ForeignKey('community_projects.id'), nullable=True)
    project = relationship("CommunityProject", backref="vacant_buildings")

    def __repr__(self):
        return f"<VacantBuilding(address={self.address}, status={self.status})>"

# Database setup
DATABASE_URL = "sqlite:///community_development.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_project(name, description=None, start_date=None, end_date=None):
    """Add a new community project to the database."""
    session = Session()
    try:
        new_project = CommunityProject(name=name, description=description, start_date=start_date, end_date=end_date)
        session.add(new_project)
        session.commit()
        return new_project
    except Exception as e:
        session.rollback()
        print(f"Error adding project: {e}")
    finally:
        session.close()

def add_vacant_building(address, status, project_id=None):
    """Add a new vacant building to the database."""
    session = Session()
    try:
        new_building = VacantBuilding(address=address, status=status, project_id=project_id)
        session.add(new_building)
        session.commit()
        return new_building
    except Exception as e:
        session.rollback()
        print(f"Error adding vacant building: {e}")
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    project = add_project("Community Garden", "A project to create a community garden.", start_date=datetime(2023, 1, 1))
    building = add_vacant_building("123 Main St", "available", project_id=project.id)
    print(project)
    print(building)
```
