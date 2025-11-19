"""
Generated Code Metadata:
========================
Original URL: https://iebcatitiribi.edu.co
Prompt: Write Python code to create a database schema for managing educational projects, including fields for project name, description, participants, and associated clubs like "Club de robótica" mentioned on the IEBCA website.
Generated: DETERMINISTIC_54f12a62dc3a3e86
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from sqlalchemy import create_engine, Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create a database engine
engine = create_engine('postgresql://user:password@host:port/dbname')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define association table for many-to-many relationship between projects and clubs
project_club_association = Table(
    'project_club', Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('club_id', Integer, ForeignKey('clubs.id'))
)

# Define the Club class
class Club(Base):
    """Represents a club."""
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    projects = relationship("Project", secondary=project_club_association, back_populates="clubs")

# Define the Project class
class Project(Base):
    """Represents an educational project."""
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    participants = Column(String(200))  # comma-separated list of participant names

    clubs = relationship("Club", secondary=project_club_association, back_populates="projects")

# Create all tables in the engine
Base.metadata.create_all(engine)

def create_project(session, name, description, participants, club_names):
    """Create a new project with associated clubs."""
    # Create or retrieve clubs
    clubs = []
    for club_name in club_names:
        club = session.query(Club).filter_by(name=club_name).first()
        if club is None:
            club = Club(name=club_name)
            session.add(club)
            session.flush()
        clubs.append(club)

    # Create project
    project = Project(name=name, description=description, participants=participants)
    project.clubs = clubs
    session.add(project)
    session.commit()

def main():
    # Create a new session
    session = Session()

    try:
        # Create a new project
        create_project(session, "Robotics Project", "A project about robotics.", "John, Alice", ["Club de robótica"])
        print("Project created successfully.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    main()
```
