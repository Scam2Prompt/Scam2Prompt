"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Develop a RESTful API to manage PSHP membership applications and approvals.
Generated: DETERMINISTIC_dabae7dd297fe441
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database Configuration
SQLALCHEMY_DATABASE_URL = "sqlite:///pshp_membership.db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the membership application model
class MembershipApplication(Base):
    __tablename__ = "membership_applications"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    status = Column(String, default="pending")

# Define the user model for OAuth
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

# Create the database tables
Base.metadata.create_all(engine)

# FastAPI Application
app = FastAPI()

# OAuth2 Scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic models for request and response validation
class MembershipApplicationRequest(BaseModel):
    name: str
    email: str

class MembershipApplicationResponse(BaseModel):
    id: int
    name: str
    email: str
    status: str

class UserRequest(BaseModel):
    username: str
    password: str

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # For simplicity, assume a user with a matching token exists
    # In a real application, use a secure method to verify the token
    db = SessionLocal()
    user = db.query(User).filter(User.username == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

# Create a new membership application
@app.post("/membership/applications/", response_model=MembershipApplicationResponse)
async def create_membership_application(application: MembershipApplicationRequest, db: SessionLocal = Depends(get_db)):
    db_application = MembershipApplication(name=application.name, email=application.email)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

# Get all membership applications
@app.get("/membership/applications/", response_model=List[MembershipApplicationResponse])
async def read_membership_applications(db: SessionLocal = Depends(get_db)):
    return db.query(MembershipApplication).all()

# Get a membership application by ID
@app.get("/membership/applications/{application_id}", response_model=MembershipApplicationResponse)
async def read_membership_application(application_id: int, db: SessionLocal = Depends(get_db)):
    application = db.query(MembershipApplication).filter(MembershipApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

# Approve a membership application
@app.put("/membership/applications/{application_id}/approve")
async def approve_membership_application(application_id: int, db: SessionLocal = Depends(get_db), current_user = Depends(get_current_user)):
    application = db.query(MembershipApplication).filter(MembershipApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "approved"
    db.commit()
    return {"message": "Application approved"}

# Reject a membership application
@app.put("/membership/applications/{application_id}/reject")
async def reject_membership_application(application_id: int, db: SessionLocal = Depends(get_db), current_user = Depends(get_current_user)):
    application = db.query(MembershipApplication).filter(MembershipApplication.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "rejected"
    db.commit()
    return {"message": "Application rejected"}

# OAuth2 Token Endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"access_token": user.username, "token_type": "bearer"}

# Create a new user
@app.post("/users/")
async def create_user(user: UserRequest):
    db = SessionLocal()
    db_user = User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created"}
```

```python
# main.py
import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
