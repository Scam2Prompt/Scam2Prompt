"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Generate code to model a database schema for tracking humanitarian aid projects, including categories like "mosquito fogging campaigns," "monthly financial assistance," and "water well drilling," as outlined on the Gulf and Aden website.
Generated: DETERMINISTIC_d8ba76552b55d1c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create a base class for declarative models
Base = declarative_base()

class ProjectCategory(Base):
    """Model for project categories."""
    __tablename__ = 'project_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Relationship to projects
    projects = relationship("Project", back_populates="category")

class Project(Base):
    """Model for humanitarian aid projects."""
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    budget = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    category_id = Column(Integer, ForeignKey('project_categories.id'), nullable=False)

    # Relationship to project category
    category = relationship("ProjectCategory", back_populates="projects")

# Database connection setup
DATABASE_URL = "sqlite:///humanitarian_aid_projects.db"  # Change to your database URL
engine = create_engine(DATABASE_URL)

# Create all tables in the database
try:
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")
except Exception as e:
    print(f"Error creating database tables: {e}")

# Session configuration
Session = sessionmaker(bind=engine)

def add_project_category(session, category_name):
    """Add a new project category to the database."""
    try:
        new_category = ProjectCategory(name=category_name)
        session.add(new_category)
        session.commit()
        print(f"Category '{category_name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding category '{category_name}': {e}")

def add_project(session, name, description, budget, start_date, end_date, category_id):
    """Add a new project to the database."""
    try:
        new_project = Project(
            name=name,
            description=description,
            budget=budget,
            start_date=start_date,
            end_date=end_date,
            category_id=category_id
        )
        session.add(new_project)
        session.commit()
        print(f"Project '{name}' added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error adding project '{name}': {e}")

# Example usage
if __name__ == "__main__":
    # Create a new session
    session = Session()

    # Add categories and projects (example data)
    add_project_category(session, "Mosquito Fogging Campaigns")
    add_project_category(session, "Monthly Financial Assistance")
    add_project_category(session, "Water Well Drilling")

    # Add a project (example data)
    add_project(session, "Mosquito Fogging in Region A", "Fogging to reduce mosquito population.", 5000.00, "2023-01-01", "2023-01-31", 1)

    # Close the session
    session.close()
```
