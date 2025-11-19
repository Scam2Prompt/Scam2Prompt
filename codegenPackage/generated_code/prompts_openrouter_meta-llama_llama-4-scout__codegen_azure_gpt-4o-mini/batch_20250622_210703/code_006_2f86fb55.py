"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: "Design a data model for storing and managing information related to environmental impact assessments for electrical power projects, inspired by Marod Consultores' experience in EIA studies and reporting."
Generated: DETERMINISTIC_2f86fb5508bc61a8
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Create a base class for declarative models
Base = declarative_base()

class Project(Base):
    """Model representing an electrical power project."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    budget = Column(Float, nullable=False)

    # Relationship to Environmental Impact Assessment
    assessments = relationship("EnvironmentalImpactAssessment", back_populates="project")

class EnvironmentalImpactAssessment(Base):
    """Model representing an environmental impact assessment for a project."""
    __tablename__ = 'environmental_impact_assessments'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    assessment_date = Column(Date, nullable=False)
    summary = Column(String, nullable=False)
    findings = Column(String, nullable=False)

    # Relationship to Project
    project = relationship("Project", back_populates="assessments")

# Database connection setup
DATABASE_URL = "sqlite:///environmental_impact_assessments.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(engine)

# Session management
Session = sessionmaker(bind=engine)

def add_project(name, location, start_date, end_date, budget):
    """Add a new project to the database."""
    session = Session()
    try:
        new_project = Project(name=name, location=location, start_date=start_date, end_date=end_date, budget=budget)
        session.add(new_project)
        session.commit()
        return new_project
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding project: {e}")
    finally:
        session.close()

def add_assessment(project_id, assessment_date, summary, findings):
    """Add a new environmental impact assessment to the database."""
    session = Session()
    try:
        new_assessment = EnvironmentalImpactAssessment(project_id=project_id, assessment_date=assessment_date, summary=summary, findings=findings)
        session.add(new_assessment)
        session.commit()
        return new_assessment
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error adding assessment: {e}")
    finally:
        session.close()

# Example usage (uncomment to run)
# project = add_project("Solar Power Plant", "California", "2023-01-01", "2023-12-31", 5000000)
# assessment = add_assessment(project.id, "2023-06-01", "Initial assessment completed", "No significant impact found.")
```
