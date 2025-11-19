"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Write Python code to create a database schema for storing healthcare professional profiles, including fields for qualifications, certifications (e.g., HCPC registration), experience, and job preferences.
Generated: DETERMINISTIC_007738027a0e72f0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from enum import Enum as PyEnum
from datetime import date

# Define database connection URL
DATABASE_URL = 'postgresql://user:password@host:port/dbname'

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define an Enum for job preferences
class JobType(PyEnum):
    FULL_TIME = 'full_time'
    PART_TIME = 'part_time'
    CONTRACT = 'contract'
    FREELANCE = 'freelance'

# Define an Enum for qualification levels
class QualificationLevel(PyEnum):
    BACHELORS = 'bachelors'
    MASTERS = 'masters'
    PHD = 'phd'
    DIPLOMA = 'diploma'
    CERTIFICATE = 'certificate'

# Define the ProfessionalProfile model
class ProfessionalProfile(Base):
    __tablename__ = 'professional_profiles'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20), nullable=False)
    created_at = Column(Date, default=date.today)
    updated_at = Column(Date, default=date.today, onupdate=date.today)

    qualifications = relationship('Qualification', backref='professional_profile')
    certifications = relationship('Certification', backref='professional_profile')
    experiences = relationship('Experience', backref='professional_profile')
    job_preference = Column(Enum(JobType), nullable=False)

# Define the Qualification model
class Qualification(Base):
    __tablename__ = 'qualifications'

    id = Column(Integer, primary_key=True)
    professional_profile_id = Column(Integer, ForeignKey('professional_profiles.id'), nullable=False)
    qualification_name = Column(String(100), nullable=False)
    qualification_level = Column(Enum(QualificationLevel), nullable=False)
    institution = Column(String(100), nullable=False)
    completion_date = Column(Date, nullable=False)

# Define the Certification model
class Certification(Base):
    __tablename__ = 'certifications'

    id = Column(Integer, primary_key=True)
    professional_profile_id = Column(Integer, ForeignKey('professional_profiles.id'), nullable=False)
    certification_name = Column(String(100), nullable=False)
    certification_number = Column(String(50), nullable=False)
    issuing_organisation = Column(String(100), nullable=False)
    issue_date = Column(Date, nullable=False)
    expiry_date = Column(Date)

# Define the Experience model
class Experience(Base):
    __tablename__ = 'experiences'

    id = Column(Integer, primary_key=True)
    professional_profile_id = Column(Integer, ForeignKey('professional_profiles.id'), nullable=False)
    employer = Column(String(100), nullable=False)
    job_title = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    is_current = Column(Boolean, default=False)

# Create all tables in the engine
Base.metadata.create_all(engine)

def create_professional_profile(session, 
                                first_name, 
                                last_name, 
                                email, 
                                phone_number, 
                                job_preference):
    try:
        profile = ProfessionalProfile(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            job_preference=job_preference
        )
        session.add(profile)
        session.commit()
        return profile
    except Exception as e:
        session.rollback()
        print(f"Error creating professional profile: {str(e)}")
        return None

def main():
    session = Session()
    profile = create_professional_profile(
        session,
        'John',
        'Doe',
        'john.doe@example.com',
        '1234567890',
        JobType.FULL_TIME
    )
    print(profile.id)

if __name__ == "__main__":
    main()
```
