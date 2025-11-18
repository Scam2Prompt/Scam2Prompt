"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Generate code to model a database schema for tracking humanitarian aid projects, including categories like "mosquito fogging campaigns," "monthly financial assistance," and "water well drilling," as outlined on the Gulf and Aden website.
Generated: DETERMINISTIC_d8ba76552b55d1c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the base class for declarative models
Base = declarative_base()

class Category(Base):
    """Model to represent the category of humanitarian aid projects."""
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    
    # Relationship to link projects with their categories
    projects = relationship('Project', back_populates='category')

class Project(Base):
    """Model to represent a humanitarian aid project."""
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    budget = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    
    # Foreign key linking to the Category table
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    
    # Relationship to link projects with their categories
    category = relationship('Category', back_populates='projects')

class MonthlyFinancialAssistance(Base):
    """Model to represent monthly financial assistance records."""
    __tablename__ = 'monthly_financial_assistance'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    
    # Relationship to link financial assistance to a project
    project = relationship('Project')

class MosquitoFoggingCampaign(Base):
    """Model to represent mosquito fogging campaign records."""
    __tablename__ = 'mosquito_fogging_campaigns'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    location = Column(String, nullable=False)
    fogging_date = Column(Date, nullable=False)
    
    # Relationship to link campaigns to a project
    project = relationship('Project')

class WaterWellDrilling(Base):
    """Model to represent water well drilling records."""
    __tablename__ = 'water_well_drilling'
    
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    location = Column(String, nullable=False)
    drilling_date = Column(Date, nullable=False)
    
    # Relationship to link drilling records to a project
    project = relationship('Project')

# Database connection setup
DATABASE_URL = "sqlite:///humanitarian_aid.db"  # Change to your preferred database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except Exception as e:
    print(f"Error during table creation: {e}")

# Session configuration
Session = sessionmaker(bind=engine)

def create_project(session, project_data):
    """Creates a new project in the database."""
    try:
        new_project = Project(**project_data)
        session.add(new_project)
        session.commit()
        print("Project created successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error creating project: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new session
    session = Session()
    
    # Example project data
    project_data = {
        'name': 'Monthly Financial Assistance Program',
        'description': 'Providing financial assistance to families.',
        'budget': 10000.00,
        'start_date': '2023-01-01',
        'category_id': 1,  # Assume category with id 1 exists
    }
    
    # Create a new project
    create_project(session, project_data)

    # Close the session
    session.close()
```
