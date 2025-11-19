"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Design a data model for a mentorship platform that includes features such as mentor directories, opportunity databases, and scholarship listings.
Generated: DETERMINISTIC_336b36501600c83e
Batch ID: 20250622_212051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# models.py

from typing import List, Optional
from pydantic import BaseModel, validator
from datetime import date

class User(BaseModel):
    """Represents a user on the mentorship platform."""
    id: int
    name: str
    email: str
    role: str  # mentor, mentee, or admin

class Mentor(User):
    """Represents a mentor on the platform."""
    bio: Optional[str]
    expertise: List[str]
    availability: List[str]  # days of the week

class Mentee(User):
    """Represents a mentee on the platform."""
    interests: List[str]
    goals: List[str]

class Opportunity(BaseModel):
    """Represents a mentorship opportunity."""
    id: int
    title: str
    description: str
    mentor_id: int
    mentee_id: int
    start_date: date
    end_date: date

class Scholarship(BaseModel):
    """Represents a scholarship listing."""
    id: int
    title: str
    description: str
    eligibility: str
    deadline: date
    award_amount: float

class MentorDirectory(BaseModel):
    """Represents a mentor directory."""
    mentors: List[Mentor]

class OpportunityDatabase(BaseModel):
    """Represents an opportunity database."""
    opportunities: List[Opportunity]

class ScholarshipListing(BaseModel):
    """Represents a scholarship listing."""
    scholarships: List[Scholarship]

# Example usage:

if __name__ == "__main__":
    # Create users
    mentor = Mentor(
        id=1,
        name="John Doe",
        email="john@example.com",
        role="mentor",
        bio="Software engineer with 10 years of experience.",
        expertise=["Python", "Java"],
        availability=["Monday", "Wednesday"]
    )

    mentee = Mentee(
        id=2,
        name="Jane Doe",
        email="jane@example.com",
        role="mentee",
        interests=["Machine Learning", "Data Science"],
        goals=["Improve coding skills"]
    )

    # Create opportunity
    opportunity = Opportunity(
        id=1,
        title="Software Engineering Mentorship",
        description="Learn software engineering best practices.",
        mentor_id=mentor.id,
        mentee_id=mentee.id,
        start_date=date(2024, 9, 1),
        end_date=date(2024, 12, 31)
    )

    # Create scholarship
    scholarship = Scholarship(
        id=1,
        title="Coding Scholarship",
        description="Award for outstanding coding skills.",
        eligibility="Open to all students.",
        deadline=date(2024, 10, 31),
        award_amount=1000.0
    )

    # Create directories and listings
    mentor_directory = MentorDirectory(mentors=[mentor])
    opportunity_database = OpportunityDatabase(opportunities=[opportunity])
    scholarship_listing = ScholarshipListing(scholarships=[scholarship])

    # Print example data
    print(mentor)
    print(mentee)
    print(opportunity)
    print(scholarship)
    print(mentor_directory)
    print(opportunity_database)
    print(scholarship_listing)
```

```python
# database.py

from typing import List
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///mentorship.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    role = Column(String)

class Mentor(Base):
    __tablename__ = 'mentors'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    bio = Column(String)
    expertise = Column(String)
    availability = Column(String)
    user = relationship("User", backref="mentor")

class Mentee(Base):
    __tablename__ = 'mentees'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    interests = Column(String)
    goals = Column(String)
    user = relationship("User", backref="mentee")

class Opportunity(Base):
    __tablename__ = 'opportunities'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    mentor_id = Column(Integer, ForeignKey('mentors.id'))
    mentee_id = Column(Integer, ForeignKey('mentees.id'))
    start_date = Column(Date)
    end_date = Column(Date)
    mentor = relationship("Mentor", backref="opportunities")
    mentee = relationship("Mentee", backref="opportunities")

class Scholarship(Base):
    __tablename__ = 'scholarships'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    eligibility = Column(String)
    deadline = Column(Date)
    award_amount = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example usage:

if __name__ == "__main__":
    # Create users
    user = User(name="John Doe", email="john@example.com", role="mentor")
    session.add(user)
    session.commit()

    mentor = Mentor(id=user.id, bio="Software engineer with 10 years of experience.", expertise="Python, Java", availability="Monday, Wednesday")
    session.add(mentor)
    session.commit()

    # Query database
    mentors = session.query(Mentor).all()
    for mentor in mentors:
        print(mentor.user.name, mentor.bio)
```

```python
# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Mentor, Mentee, Opportunity, Scholarship
from database import session, Mentor as MentorModel, Mentee as MenteeModel, Opportunity as OpportunityModel, Scholarship as ScholarshipModel

app = FastAPI()

class MentorRequest(BaseModel):
    name: str
    email: str
    bio: str
    expertise: List[str]
    availability: List[str]

class MenteeRequest(BaseModel):
    name: str
    email: str
    interests: List[str]
    goals: List[str]

class OpportunityRequest(BaseModel):
    title: str
    description: str
    mentor_id: int
    mentee_id: int
    start_date: str
    end_date: str

class ScholarshipRequest(BaseModel):
    title: str
    description: str
    eligibility: str
    deadline: str
    award_amount: float

@app.post("/mentors/")
def create_mentor(mentor: MentorRequest):
    mentor_model = MentorModel(name=mentor.name, email=mentor.email, bio=mentor.bio, expertise=','.join(mentor.expertise), availability=','.join(mentor.availability))
    session.add(mentor_model)
    session.commit()
    return {"id": mentor_model.id, "name": mentor_model.name}

@app.post("/mentees/")
def create_mentee(mentee: MenteeRequest):
    mentee_model = MenteeModel(name=mentee.name, email=mentee.email, interests=','.join(mentee.interests), goals=','.join(mentee.goals))
    session.add(mentee_model)
    session.commit()
    return {"id": mentee_model.id, "name": mentee_model.name}

@app.post("/opportunities/")
def create_opportunity(opportunity: OpportunityRequest):
    opportunity_model = OpportunityModel(title=opportunity.title, description=opportunity.description, mentor_id=opportunity.mentor_id, mentee_id=opportunity.mentee_id, start_date=opportunity.start_date, end_date=opportunity.end_date)
    session.add(opportunity_model)
    session.commit()
    return {"id": opportunity_model.id, "title": opportunity_model.title}

@app.post("/scholarships/")
def create_scholarship(scholarship: ScholarshipRequest):
    scholarship_model = ScholarshipModel(title=scholarship.title, description=scholarship.description, eligibility=scholarship.eligibility, deadline=scholarship.deadline, award_amount=scholarship.award_amount)
    session.add(scholarship_model)
    session.commit()
    return {"id": scholarship_model.id, "title": scholarship_model.title}

@app.get("/mentors/")
def read_mentors():
    mentors = session.query(MentorModel).all()
    return [{"id": mentor.id, "name": mentor.user.name} for mentor in mentors]

@app.get("/mentees/")
def read_mentees():
    mentees = session.query(MenteeModel).all()
    return [{"id": mentee.id, "name": mentee.user.name} for mentee in mentees]

@app.get("/opportunities/")
def read_opportunities():
    opportunities = session.query(OpportunityModel).all()
    return [{"id": opportunity.id, "title": opportunity.title} for opportunity in opportunities]

@app.get("/scholarships/")
def read_scholarships():
    scholarships = session.query(ScholarshipModel).all()
    return [{"id": scholarship.id, "title": scholarship.title} for scholarship in scholarships]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
