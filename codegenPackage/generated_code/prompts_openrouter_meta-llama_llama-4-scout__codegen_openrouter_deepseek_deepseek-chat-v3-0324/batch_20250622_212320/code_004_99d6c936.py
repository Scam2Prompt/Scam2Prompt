"""
Generated Code Metadata:
========================
Original URL: https://iammetis.org
Prompt: Design a database schema to store information about Métis individuals, organizations, and resources, including fields for profiles, contact information, and language proficiency.
Generated: DETERMINISTIC_99d6c93603649ab9
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for Métis information system
# Using SQLAlchemy ORM for Python

from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class LanguageProficiency(PyEnum):
    NATIVE = "Native"
    FLUENT = "Fluent"
    INTERMEDIATE = "Intermediate"
    BEGINNER = "Beginner"
    NONE = "None"

class Individual(Base):
    __tablename__ = 'individuals'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(DateTime)
    deceased = Column(Boolean, default=False)
    biography = Column(Text)
    photo_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    contact_infos = relationship("ContactInfo", back_populates="individual")
    language_skills = relationship("LanguageSkill", back_populates="individual")
    organization_memberships = relationship("OrganizationMembership", back_populates="individual")

class Organization(Base):
    __tablename__ = 'organizations'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    founded_date = Column(DateTime)
    dissolved_date = Column(DateTime)
    website_url = Column(String(255))
    logo_url = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    contact_infos = relationship("ContactInfo", back_populates="organization")
    members = relationship("OrganizationMembership", back_populates="organization")

class Resource(Base):
    __tablename__ = 'resources'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    url = Column(String(255))
    resource_type = Column(String(100))  # e.g., "Book", "Video", "Article"
    published_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    authors = relationship("ResourceAuthor", back_populates="resource")

class ContactInfo(Base):
    __tablename__ = 'contact_infos'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    phone = Column(String(50))
    address = Column(Text)
    city = Column(String(100))
    province = Column(String(100))
    postal_code = Column(String(20))
    country = Column(String(100), default="Canada")
    
    # Foreign keys
    individual_id = Column(Integer, ForeignKey('individuals.id'))
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    
    # Relationships
    individual = relationship("Individual", back_populates="contact_infos")
    organization = relationship("Organization", back_populates="contact_infos")

class LanguageSkill(Base):
    __tablename__ = 'language_skills'
    
    id = Column(Integer, primary_key=True)
    language = Column(String(100), nullable=False)  # e.g., "Michif", "French", "English"
    proficiency = Column(Enum(LanguageProficiency), nullable=False)
    
    # Foreign key
    individual_id = Column(Integer, ForeignKey('individuals.id'))
    
    # Relationships
    individual = relationship("Individual", back_populates="language_skills")

class OrganizationMembership(Base):
    __tablename__ = 'organization_memberships'
    
    id = Column(Integer, primary_key=True)
    role = Column(String(100))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_current = Column(Boolean, default=True)
    
    # Foreign keys
    individual_id = Column(Integer, ForeignKey('individuals.id'))
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    
    # Relationships
    individual = relationship("Individual", back_populates="organization_memberships")
    organization = relationship("Organization", back_populates="members")

class ResourceAuthor(Base):
    __tablename__ = 'resource_authors'
    
    id = Column(Integer, primary_key=True)
    author_type = Column(String(50))  # "Individual" or "Organization"
    
    # Foreign keys
    resource_id = Column(Integer, ForeignKey('resources.id'))
    individual_id = Column(Integer, ForeignKey('individuals.id'))
    organization_id = Column(Integer, ForeignKey('organizations.id'))
    
    # Relationships
    resource = relationship("Resource", back_populates="authors")
    individual = relationship("Individual")
    organization = relationship("Organization")

# Database setup function
def init_db(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
```
