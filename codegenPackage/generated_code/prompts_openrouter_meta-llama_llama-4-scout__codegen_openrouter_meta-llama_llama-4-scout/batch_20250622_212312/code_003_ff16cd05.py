"""
Generated Code Metadata:
========================
Original URL: https://pabshq.com
Prompt: "Design a data model for a platform like Pabs HQ, including entities for users, projects, news, and updates, and relationships between them."
Generated: DETERMINISTIC_ff16cd053a68bbed
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from datetime import datetime
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum

# Define database connection URL
DATABASE_URL = "sqlite:///pabs_hq.db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

class Role(PyEnum):
    """User role"""
    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"

class User(Base):
    """User entity"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(Role), default=Role.DEVELOPER)

    projects = relationship("Project", secondary="project_memberships")
    news = relationship("News", backref="author")

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', email='{self.email}')"

class Project(Base):
    """Project entity"""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    users = relationship("User", secondary="project_memberships", backref="projects")

    news = relationship("News", backref="project")

    def __repr__(self):
        return f"Project(id={self.id}, name='{self.name}')"

class News(Base):
    """News entity"""
    __tablename__ = "news"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    project_id = Column(Integer, ForeignKey("projects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"News(id={self.id}, title='{self.title}')"

class Update(Base):
    """Update entity"""
    __tablename__ = "updates"

    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    news_id = Column(Integer, ForeignKey("news.id"))

    def __repr__(self):
        return f"Update(id={self.id}, content='{self.content}')"

class ProjectMembership(Base):
    """Many-to-many relationship table between projects and users"""
    __tablename__ = "project_memberships"

    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    def __repr__(self):
        return f"ProjectMembership(project_id={self.project_id}, user_id={self.user_id})"

# Create all tables in the engine
Base.metadata.create_all(engine)

# Example usage
if __name__ == "__main__":
    session = Session()

    # Create a new user
    user = User(username="john_doe", email="john@example.com")
    session.add(user)
    session.commit()

    # Create a new project
    project = Project(name="My Project")
    session.add(project)
    session.commit()

    # Add user to project
    membership = ProjectMembership(project_id=project.id, user_id=user.id)
    session.add(membership)
    session.commit()

    # Create a new news
    news = News(title="My News", content="This is a news", project_id=project.id, user_id=user.id)
    session.add(news)
    session.commit()

    # Create a new update
    update = Update(content="This is an update", news_id=news.id)
    session.add(update)
    session.commit()

    # Query all news for a project
    news_for_project = session.query(News).filter_by(project_id=project.id).all()
    for n in news_for_project:
        print(n)

    session.close()
```
